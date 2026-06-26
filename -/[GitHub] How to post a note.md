# 💚 How to post a note

## 💛 What is it?
- A note-generator flow: write a note once, and it publishes itself to several places. No more manual copy-paste.
## 💛 Why do we need it?
- A note is only useful where you actually look: your personal Notion, your team's Notion, and a public repo for the shareable ones.
- Doing that by hand for every note is the bottleneck. Automating the publish step removes it.
## 💛 How does it work?
One canonical markdown note is generated in a fixed style, then fanned out. Each destination has its own rule:
- Personal Notion: always. It is tagged so it lands in the Notes view. A Notion view is a saved filter, so the Category property (not a folder) decides where the page shows up.
- Team Notion: when that workspace is connected. Each workspace needs its own connection; one integration cannot span two workspaces.
- Public GitHub repo: only when the note is general and educational, never when it holds internal detail.
### 🤍 Sensitivity gate
- A public repo is not the same as private Notion. Before any push, a guard scans the note for leak markers (cloud account ids, cluster names, access keys) and refuses if it finds any.
- It is fail-safe: when unsure, it skips the public push instead of risking a leak.
### 🤍 Example
```bash
# write the note once; it routes itself to Notion and (if safe) GitHub
/note-generator "How to post a note"
```
## 💛 References
- Notion API — create pages in a database
- GitHub REST API — create or update file contents
