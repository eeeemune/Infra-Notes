#!/usr/bin/env python3
"""Publish Notion notes flagged 'Publish to GitHub' into this repo.

Flow: query the Chartmetric Notes database for pages whose 'Publish to GitHub'
checkbox is ticked, render each to markdown, refuse anything with internal markers
(public repo, fail-safe), write -/[Category] Title.md, rebuild the README index in
the same commit, push, then untick the box on each published page.

Self-contained on purpose: an Action push with the default GITHUB_TOKEN does not
trigger other workflows, so we rebuild README here instead of relying on it.

No-ops cleanly when NOTION_TOKEN is absent, so the schedule stays quiet until the
repo secret is added.
"""
import json, os, re, subprocess, sys, urllib.request

TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
DATABASE_ID = os.environ.get("NOTES_DATABASE_ID", "2503f66f52258047b727c219b03e4a1a")
NOTE_DIR = "-"
NVER = "2022-06-28"

if not TOKEN:
    print("NOTION_TOKEN not set; nothing to do (add the repo secret to enable).")
    sys.exit(0)

# Same fail-safe guard as publish-github.sh: refuse internal markers on a public repo.
SENSITIVE = re.compile(
    r"arn:aws:|897744604563|[0-9]{12}|ip-10-[0-9]|ip-172-[0-9]|ip-192-168|"
    r"10\.[0-9]+\.[0-9]+\.[0-9]+|172\.(1[6-9]|2[0-9]|3[01])\.|192\.168\.|"
    r"cm-ro|cm_cluster|eunhye-local-ro|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{20,}|"
    r"-----BEGIN|(password|secret|token|api[_-]?key)\s*[:=]",
    re.I,
)


def notion(method, path, body=None):
    req = urllib.request.Request(
        "https://api.notion.com/v1" + path, method=method,
        headers={"Authorization": "Bearer " + TOKEN, "Notion-Version": NVER,
                 "Content-Type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None,
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


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


def query_flagged():
    results, cursor = [], None
    while True:
        body = {"filter": {"property": "Publish to GitHub", "checkbox": {"equals": True}}, "page_size": 50}
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


def untick(page_id):
    notion("PATCH", f"/pages/{page_id}", {"properties": {"Publish to GitHub": {"checkbox": False}}})


def main():
    pages = query_flagged()
    if not pages:
        print("No notes flagged for publish.")
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
            untick(pg["id"])
            continue
        target = os.path.join(NOTE_DIR, f"[{category}] {title}.md")
        os.makedirs(NOTE_DIR, exist_ok=True)
        with open(target, "w") as f:
            f.write(content)
        subprocess.run(["git", "add", target], check=True)
        published.append((pg["id"], title, category))
        print(f"staged: {target}")

    if not published:
        print("Nothing to commit.")
        return

    # Rebuild the index in the same commit (the token push won't trigger the index workflow).
    subprocess.run(["bash", ".github/scripts/build-readme.sh"], check=True)
    subprocess.run(["git", "add", "README.md"], check=True)
    # Commit + push only if something actually changed (re-ticking an unchanged note is a no-op).
    if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
        msg = "note: publish from Notion (" + ", ".join(f"[{c}] {t}" for _, t, c in published) + ")"
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("committed and pushed.")
    else:
        print("no content change; nothing to commit.")

    for pid, title, _ in published:
        untick(pid)
        print(f"published & unticked: {title}")


if __name__ == "__main__":
    main()
