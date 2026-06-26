#!/usr/bin/env bash
# build-readme.sh — regenerate README.md as an index of every note in -/.
#
# Idempotent FULL REBUILD: it reads all `-/[Category] Title.md` files and writes
# README.md from scratch, sorted by category then title. Re-running produces the
# same output, so it can never duplicate entries. The previous workflow appended to
# the existing README without de-duping, which is why entries piled up.
#
# Used by .github/workflows/index-readme.yaml; also runnable locally from anywhere.
set -euo pipefail
cd "$(dirname "$0")/../.."   # repo root

NOTE_DIR="-"
OUT="README.md"
BASE="https://github.com/eeeemune/Infra-Notes/blob/main/-/"

# URL-encode the characters that break a markdown link or URL. Brackets stay literal
# (GitHub accepts them and the repo's link style uses them).
urlenc() { printf '%s' "$1" | sed 's/ /%20/g; s/(/%28/g; s/)/%29/g'; }

# Build rows "Category<TAB>Title<TAB>filename", one per note, sorted by category then title.
TMP=$(mktemp)
for f in "$NOTE_DIR"/*.md; do
  [ -e "$f" ] || continue
  fn=${f#"$NOTE_DIR"/}                      # [Category] Title.md
  case "$fn" in \[*\]*) : ;; *) continue ;; esac
  category=${fn#\[}; category=${category%%\]*}
  title=${fn#"[$category] "}; title=${title%.md}
  printf '%s\t%s\t%s\n' "$category" "$title" "$fn"
done | LC_ALL=C sort -t$'\t' -k1,1 -k2,2 > "$TMP"

{
  printf '# Contents\n'
  prev=""
  while IFS=$'\t' read -r category title fn; do
    if [ "$category" != "$prev" ]; then
      printf '\n## %s\n' "$category"
      prev="$category"
    fi
    printf '### [%s](%s%s)\n' "$title" "$BASE" "$(urlenc "$fn")"
    # Outline: each heading becomes a nested bullet (# -> top, ## -> 3sp, ### -> 6sp).
    # Skip lines inside fenced code blocks so code comments don't leak into the index.
    in_code=0
    while IFS= read -r line || [ -n "$line" ]; do
      case "$line" in '```'*) in_code=$((1 - in_code)); continue ;; esac
      [ "$in_code" = 1 ] && continue
      case "$line" in
        '### '*) printf '%s\n' "      - ${line#'### '}" ;;
        '## '*)  printf '%s\n' "   - ${line#'## '}"     ;;
        '# '*)   printf '%s\n' "- ${line#'# '}"         ;;
      esac
    done < "$NOTE_DIR/$fn"
    printf '\n'
  done < "$TMP"
} > "$OUT"
rm -f "$TMP"

echo "Rebuilt $OUT: $(grep -c '^### ' "$OUT") notes, $(grep -c '^## ' "$OUT") categories."
