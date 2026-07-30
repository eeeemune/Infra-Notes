# 💚 Setting up a Claude Cloud Environment

## 💛 What is it?
A **Claude cloud environment** is the managed sandbox where Claude Code cloud sessions and routines run on Anthropic's infrastructure, not your laptop. It defines three things: the VM's base setup and network access, the environment variables Claude gets, and a **setup script** that runs before Claude starts.
Every cloud session boots its own fresh, isolated VM snapshot from that config. Sessions do not share filesystem state.
It is used by: Claude Code on the web (`claude.ai/code`), `claude --cloud` from the CLI, the desktop and mobile apps, and **routines**.
> Cloud environments are in research preview, so limits and details can change.
## 💛 Why do we need it?
A cloud session starts on a clean VM that has **no access to your local files** and none of your `~/.claude` config. So if your project needs a specific toolchain, some env vars, or network access to a private host, you set that up once in an environment and every cloud session or routine reuses it.
Without a configured environment, the agent boots a generic box that may be missing your dependencies or blocked from the hosts it needs to reach.
## 💛 What comes preinstalled
The base image is **Ubuntu 24.04** with a broad default toolchain, so most projects need little setup:
- **Python** (pip, poetry, uv, ruff, pytest, black, mypy)
- **Node** 20 to 22 (npm, yarn, pnpm, bun, eslint, prettier)
- **Go**, **Rust** (cargo), **Java 21** (Maven, Gradle), **Ruby**, **PHP 8.4**
- **Docker** and compose, **PostgreSQL 16**, **Redis 7**
- git, jq, yq, ripgrep, tmux, vim
You customize on top with a setup script. There is no Dockerfile or base-image swap.
## 💛 Where you set it up
- **Web**: at `claude.ai/code`, click the cloud icon above the message box, then **Add cloud environment** (or the gear to edit). The dialog has: Name, Network access, Allowed domains, Environment variables, Setup script.
- **CLI**: `/remote-env` picks the default cloud environment used by `claude --cloud` (saved to `remote.defaultEnvironmentId` in user settings).
- **Org-shared** (Team / Enterprise): admins manage shared environments at `claude.ai/admin-settings` under Cloud environments. Members then see them in the selector.
- **Not in the repo**: environments live in your claude.ai account, not a committed `devcontainer.json`. Project-level setup goes in `.claude/settings.json` instead (see below).
## 💛 The setup script
Bash that runs **as root, once per environment, before Claude launches**. Use it to install toolchains, pull Docker images, or configure tools.
```bash
#!/bin/bash
apt update && apt install -y gh
```
- It must **exit zero** (append `|| true` to non-critical commands) and finish within about **5 minutes**, or the environment fails to build.
- The result is cached as a filesystem snapshot for about **7 days**. New sessions reuse it and skip the script, so startup is fast.
- Changing the script or the allowed domains **invalidates the cache** and the next session rebuilds it.
- The cache stores **files, not running processes**. Start databases and services per-session, not in the script.
### 🤍 Setup script vs SessionStart hook
Two different tools, easy to confuse:
- **Setup script**: VM-level provisioning, cloud sessions only, runs once, benefits from caching.
- **SessionStart hook** (in `.claude/settings.json`): project-level, runs on **every** session (local and cloud), no caching. Gate cloud-only work with a check on the `CLAUDE_CODE_REMOTE=true` variable.
## 💛 Environment variables (not a secrets store)
Provided in `.env` format, one `KEY=value` per line, copied into the VM at startup.
```javascript
NODE_ENV=development
LOG_LEVEL=debug
DATABASE_URL=postgres://localhost:5432/myapp
```
- Changing them affects **new sessions only**, not running ones.
- **Security**: these are ordinary env vars, readable by any command Claude runs, and visible to everyone who uses the environment. This is **not** a secrets store. Do not put API keys or credentials here.
- For GitHub, prefer the built-in proxy: the repo is cloned and pushes work without the real token ever entering the VM. Only set `GH_TOKEN` / `GITHUB_TOKEN` if a script needs it directly.
## 💛 Repositories
- The repo is **cloned from GitHub at session start** (its default branch), not copied from your machine.
- By default Claude can only push to `claude/*`-prefixed branches. Enable unrestricted branch pushes per repo to remove that guard.
- Committed files are available (`CLAUDE.md`, `.claude/settings.json`, `.mcp.json`, `.claude/skills/`, `.claude/agents/`). Local-only files and your user-level `~/.claude/` are **not**. Commit anything the cloud agent needs.
- Project-scope MCP servers (from `.mcp.json`) work. Local-scope MCP servers do not.
## 💛 Network access (four levels)
Outbound traffic is restricted by default. You pick a level per environment.
- For **Custom**, also set `allow_package_managers: true` if you want npm, PyPI, RubyGems, crates.io, and friends reachable.
- **MCP connector** traffic is routed through Anthropic's servers, so connector hosts do **not** need to be in your allowlist.
- **GitHub** goes through its own proxy, independent of the network level.
## 💛 Compute
Roughly **4 vCPUs, 16 GB RAM, 30 GB disk** per session, not tunable. Very large builds or memory-heavy tests may be stopped. For those, use Remote Control to run Claude Code locally instead.
## 💛 Lifecycle
- **Create**: set name, network access, variables, and setup script once. The environment gets an ID.
- **Attach**: when starting a cloud session or routine, pick the environment (or pass its `environment_id` via the API).
- **First run**: setup script runs, snapshot is cached, Claude launches, then SessionStart hooks run.
- **Later runs**: reuse the cached snapshot (script skipped), each on its own isolated VM.
- **Edit**: changing the script or domains rebuilds the cache; changing only variables reuses the cache with new values.
- **Archive / delete**: archive hides it from the selector (running sessions continue); delete is only allowed when nothing references it.
## 💛 Gotcha
- **The cloud VM cannot see your machine.** No local files, no `~/.claude`. Commit `CLAUDE.md`, `.claude/settings.json`, `.mcp.json`, skills, and agents into the repo, or the cloud agent will not have them.
- **Env vars are not secret.** Anyone using the environment can read them. Use the GitHub proxy for tokens and keep real credentials out.
- **Setup script is strict.** It must exit zero and stay under about 5 minutes, or the build fails.
- **Cache holds files, not processes.** Start Postgres, Redis, or your app per-session, not in the setup script.
- **Local-scope MCP will not appear.** Only project-scope (`.mcp.json`) servers load in the cloud.
## 💛 References
- Cloud environments configuration: https://code.claude.com/docs/en/cloud-environments.md
- Claude Code on the web overview: https://code.claude.com/docs/en/claude-code-on-the-web.md
- Routines (environments and network access): https://code.claude.com/docs/en/routines.md
- Managed Agents environments (API): https://platform.claude.com/docs/en/managed-agents/environments.md
