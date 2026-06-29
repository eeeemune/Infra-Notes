#!/usr/bin/env python3
"""Publish / mirror Notion notes flagged in the Chartmetric Notes database.

Two independent checkbox triggers on a note:
  - 'Publish to GitHub'  -> render to markdown, run the sensitivity guard (public
    repo, fail-safe), write -/[Category] Title.md, rebuild README, push, untick.
  - 'Publish to Company' -> copy the note as a page in the chartmetric (company)
    Notion database, then untick. Private workspace, so no guard.

Notes are READ from the eemune workspace with NOTION_TOKEN. The company copy is
WRITTEN to chartmetric with NOTION_CHARTMETRIC_TOKEN. Each path no-ops when its
token(s) are absent, so the schedule stays quiet until secrets are added.
"""
import json, os, re, subprocess, sys, urllib.error, urllib.request

TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
CM_TOKEN = os.environ.get("NOTION_CHARTMETRIC_TOKEN", "").strip()
DATABASE_ID = os.environ.get("NOTES_DATABASE_ID", "2503f66f52258047b727c219b03e4a1a")
CM_DATABASE_ID = os.environ.get("CHARTMETRIC_DATABASE_ID", "251ad25273268088b7e1ffd4f913ce1c")
NOTE_DIR = "-"
NVER = "2022-06-28"

SENSITIVE = re.compile(
    r"arn:aws:|897744604563|[0-9]{12}|ip-10-[0-9]|ip-172-[0-9]|ip-192-168|"
    r"10\.[0-9]+\.[0-9]+\.[0-9]+|172\.(1[6-9]|2[0-9]|3[01])\.|192\.168\.|"
    r"cm-ro|cm_cluster|eunhye-local-ro|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{20,}|"
    r"-----BEGIN|(password|secret|token|api[_-]?key)\s*[:=]",
    re.I,
)


def notion(method, path, body=None, token=None, ver=None):
    req = urllib.request.Request(
        "https://api.notion.com/v1" + path, method=method,
        headers={"Authorization": "Bearer " + (token or TOKEN), "Notion-Version": ver or NVER,
                 "Content-Type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None,
    )
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print(f"Notion API error: {method} {path} -> HTTP {e.code}", file=sys.stderr)
        print(e.read().decode("utf-8", "replace"), file=sys.stderr)
        raise


def rich(texts):
    out = []
    for t in texts or []:
        s = t.get("plain_text", "")
        a = t.get("annotations", {})
        if a.get("code"):
            s = "`" + s + "`"
        elif a.get("bold"):
            s = "**" + s + "**"
        out.append(s)
    return "".join(out)


def query_flagged(prop):
    results, cursor = [], None
    while True:
        body = {"filter": {"property": prop, "checkbox": {"equals": True}}, "page_size": 50}
        if cursor:
            body["start_cursor"] = cursor
        data = notion("POST", f"/databases/{DATABASE_ID}/query", body)
        results += data["results"]
        if not data.get("has_more"):
            return results
        cursor = data["next_cursor"]


def children(block_id):
    out, cursor = [], None
    while True:
        q = f"/blocks/{block_id}/children?page_size=100" + (f"&start_cursor={cursor}" if cursor else "")
        data = notion("GET", q)
        out += data["results"]
        if not data.get("has_more"):
            return out
        cursor = data["next_cursor"]


def render(blocks, depth=0):
    lines, pad = [], "  " * depth
    for b in blocks:
        t = b["type"]
        d = b.get(t, {})
        txt = rich(d.get("rich_text")) if isinstance(d, dict) else ""
        if t == "heading_1":
            lines.append("# " + txt)
        elif t == "heading_2":
            lines.append("## " + txt)
        elif t == "heading_3":
            lines.append("### " + txt)
        elif t == "bulleted_list_item":
            lines.append(pad + "- " + txt)
        elif t == "numbered_list_item":
            lines.append(pad + "1. " + txt)
        elif t == "quote":
            lines.append("> " + txt)
        elif t == "code":
            lang = d.get("language", "")
            lines.append("```" + (lang if lang and lang != "plain text" else ""))
            lines.append(rich(d.get("rich_text")))
            lines.append("```")
        elif t == "divider":
            continue
        elif t == "paragraph":
            lines.append(pad + txt if txt else "")
        elif txt:
            lines.append(pad + txt)
        if b.get("has_children") and t in ("bulleted_list_item", "numbered_list_item"):
            lines += render(children(b["id"]), depth + 1)
    return lines


def prop_text(props, name):
    p = props.get(name, {})
    if p.get("type") == "rich_text":
        return rich(p["rich_text"]).strip()
    if p.get("type") == "title":
        return rich(p["title"]).strip()
    return ""


def first_tag(props):
    ms = props.get("Tags", {}).get("multi_select", [])
    return ms[0]["name"] if ms else ""


def untick(page_id, prop):
    notion("PATCH", f"/pages/{page_id}", {"properties": {prop: {"checkbox": False}}})


# --- GitHub publish (public repo) -------------------------------------------------
def publish_github():
    if not TOKEN:
        print("NOTION_TOKEN not set; skipping GitHub publish.")
        return
    pages = query_flagged("Publish to GitHub")
    if not pages:
        print("No notes flagged for GitHub.")
        return
    subprocess.run(["git", "config", "user.name", "eeeemune"], check=True)
    subprocess.run(["git", "config", "user.email", "eeeemune@gmail.com"], check=True)

    published = []
    for pg in pages:
        props = pg["properties"]
        title = prop_text(props, "Name")
        if not title or "/" in title:
            print(f"skip: bad title {title!r}")
            continue
        category = (prop_text(props, "GH Category") or first_tag(props) or "Others").replace("/", "-")
        body = "\n".join(render(children(pg["id"]))).strip()
        content = f"# \U0001f49a {title}\n\n{body}\n"
        hit = SENSITIVE.search(content)
        if hit:
            print(f"REFUSED (sensitive): '{title}' matched {hit.group()!r}; unticking, not publishing.")
            untick(pg["id"], "Publish to GitHub")
            continue
        target = os.path.join(NOTE_DIR, f"[{category}] {title}.md")
        os.makedirs(NOTE_DIR, exist_ok=True)
        with open(target, "w") as f:
            f.write(content)
        subprocess.run(["git", "add", "--", target], check=True)
        published.append((pg["id"], title, category))
        print(f"staged: {target}")

    if published:
        subprocess.run(["bash", ".github/scripts/build-readme.sh"], check=True)
        subprocess.run(["git", "add", "--", "README.md"], check=True)
        if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
            msg = "note: publish from Notion (" + ", ".join(f"[{c}] {t}" for _, t, c in published) + ")"
            subprocess.run(["git", "commit", "-m", msg], check=True)
            subprocess.run(["git", "push"], check=True)
            print("committed and pushed.")
        else:
            print("no content change; nothing to commit.")
        for pid, title, _ in published:
            untick(pid, "Publish to GitHub")
            print(f"published & unticked: {title}")


# --- Company Notion mirror (private workspace, no guard) --------------------------
def to_richtext(read_list):
    out = []
    for rt in read_list or []:
        txt = rt.get("plain_text", "")
        if not txt:
            continue
        obj = {"type": "text", "text": {"content": txt[:2000]}}
        if rt.get("href"):
            obj["text"]["link"] = {"url": rt["href"]}
        ann = rt.get("annotations") or {}
        keep = {k: True for k in ("bold", "italic", "strikethrough", "underline", "code") if ann.get(k)}
        if ann.get("color") and ann["color"] != "default":
            keep["color"] = ann["color"]
        if keep:
            obj["annotations"] = keep
        out.append(obj)
    return out


TEXTY = ("heading_1", "heading_2", "heading_3", "paragraph",
         "bulleted_list_item", "numbered_list_item", "quote")


def to_block(b):
    t = b["type"]
    d = b.get(t, {})
    if t == "divider":
        return {"object": "block", "type": "divider", "divider": {}}
    if t == "code":
        return {"object": "block", "type": "code", "code": {
            "rich_text": to_richtext(d.get("rich_text")),
            "language": d.get("language") or "plain text"}}
    if t in TEXTY:
        nb = {"object": "block", "type": t, t: {"rich_text": to_richtext(d.get("rich_text"))}}
        if b.get("has_children") and t in ("bulleted_list_item", "numbered_list_item"):
            kids = [k for k in (to_block(c) for c in children(b["id"])) if k]
            if kids:
                nb[t]["children"] = kids[:100]
        return nb
    return None


def build_blocks(page_id):
    return [k for k in (to_block(b) for b in children(page_id)) if k][:100]


CM_VER = "2025-09-03"  # data-source API (the chartmetric DB uses the newer model)


# The chartmetric "Infra Notes" data source (data-source ids are stable). Override
# with CHARTMETRIC_DATA_SOURCE_ID; set it to "" to auto-discover via search instead.
CM_DATA_SOURCE_ID = os.environ.get("CHARTMETRIC_DATA_SOURCE_ID", "251ad2527326812b89b2000b85f59cde")


def cm_data_source():
    if CM_DATA_SOURCE_ID:
        return CM_DATA_SOURCE_ID
    for r in notion("POST", "/search", {"page_size": 25}, token=CM_TOKEN, ver=CM_VER).get("results", []):
        if r.get("object") == "data_source":
            return r["id"]
        kids = [d.get("id") for d in (r.get("data_sources") or [])]
        if kids:
            return kids[0]
    raise SystemExit("This integration can access no usable data source in chartmetric.")


def cm_schema(ds_id):
    props = notion("GET", f"/data_sources/{ds_id}", token=CM_TOKEN, ver=CM_VER).get("properties", {})
    print("chartmetric data source properties: "
          + ", ".join(f"{n}({p.get('type')})" for n, p in props.items()), file=sys.stderr)
    return props


def title_prop_of(schema):
    for name, p in schema.items():
        if p.get("type") == "title":
            return name
    raise SystemExit("chartmetric data source has no title property")


def set_prop(out, schema, name, value):
    """Set property `name` to `value` (a string) per its declared type, if it exists."""
    p = schema.get(name)
    if not p or not value:
        return
    t = p.get("type")
    if t == "select":
        out[name] = {"select": {"name": value}}
    elif t == "multi_select":
        out[name] = {"multi_select": [{"name": value}]}
    elif t == "status":
        out[name] = {"status": {"name": value}}
    elif t == "rich_text":
        out[name] = {"rich_text": [{"type": "text", "text": {"content": value}}]}


def cm_exists(ds_id, title_prop, title):
    body = {"filter": {"property": title_prop, "title": {"equals": title}}, "page_size": 1}
    res = notion("POST", f"/data_sources/{ds_id}/query", body, token=CM_TOKEN, ver=CM_VER)
    return bool(res["results"])


def mirror_company():
    if not (TOKEN and CM_TOKEN):
        print("NOTION_CHARTMETRIC_TOKEN (or NOTION_TOKEN) not set; skipping company mirror.")
        return
    pages = query_flagged("Publish to Company")
    if not pages:
        print("No notes flagged for company mirror.")
        return
    ds_id = cm_data_source()
    schema = cm_schema(ds_id)
    title_prop = title_prop_of(schema)
    for pg in pages:
        props_in = pg["properties"]
        title = prop_text(props_in, "Name")
        if not title:
            print("skip: empty Name")
            continue
        if cm_exists(ds_id, title_prop, title):
            print(f"company: '{title}' already exists; skipping (delete it there to re-mirror).")
            untick(pg["id"], "Publish to Company")
            continue
        gh_tag = prop_text(props_in, "GH Category") or first_tag(props_in)
        out_props = {title_prop: {"title": [{"type": "text", "text": {"content": title}}]}}
        set_prop(out_props, schema, "Category", "Infra")  # company copies are always Category = Infra
        set_prop(out_props, schema, "Tags", gh_tag)        # Tags = the note's GitHub tag (GH Category)
        body = {
            "parent": {"type": "data_source_id", "data_source_id": ds_id},
            "icon": {"type": "emoji", "emoji": "\U0001f49a"},
            "properties": out_props,
            "children": build_blocks(pg["id"]),
        }
        res = notion("POST", "/pages", body, token=CM_TOKEN, ver=CM_VER)
        untick(pg["id"], "Publish to Company")
        print(f"company mirrored: {title} (Category=Infra, Tags={gh_tag}) -> {res.get('url')}")


def main():
    publish_github()
    mirror_company()


if __name__ == "__main__":
    main()
