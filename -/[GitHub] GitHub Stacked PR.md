# 💚 GitHub Stacked PR

## 💛 What is it?
A **stacked PR** (a "stack") is an ordered chain of branches where each branch builds on the one below it, and **each branch is its own pull request**. `gh stack` is the GitHub CLI extension that manages the chain for you.
Plain version: instead of one huge PR, you split a feature into layers (auth, then api, then frontend), each a small PR a reviewer can read on its own. `gh stack` keeps them wired together: each PR's base is the branch directly below it.
```javascript
main (trunk)
 └── auth          -> PR #1 (base: main)      bottom, closest to trunk
     └── api       -> PR #2 (base: auth)
         └── frontend -> PR #3 (base: api)    top, furthest from trunk
```
## 💛 Why do we need it?
One giant PR is painful: slow to review, easy to miss bugs, and it blocks you until it merges. Stacking fixes that:
- **Small, reviewable PRs** instead of one 2000-line monster.
- **Keep working while lower layers are in review.** You do not wait for PR #1 to merge before building PR #2 on top of it.
- **Each PR shows only its own layer's diff**, not everything beneath it. Reviewers see one concern at a time.
- **The history tells one story** in dependency order.
### 🤍 Real-world use case
A feature needs a new auth middleware, then API routes that use it, then a dashboard that calls the API. As three stacked PRs, the auth PR can be reviewed and approved while you are still writing the dashboard, and each reviewer sees only their layer.
## 💛 How it works (the mental model)
- **Trunk** is the default branch (usually `main`). The stack roots on it.
- **Bottom** is closest to trunk, **top** is furthest. Navigation follows this: `up` and `top` move away from trunk, `down` and `bottom` move toward it.
- **One branch equals one PR**, whose base is the branch below it.
- **Linear only**: each branch has exactly one parent and at most one child. Parallel workstreams use separate stacks.
Order branches by dependency: foundational changes (models, shared APIs) go low, dependents (UI, tests) go high. Plan the layers before writing code.
### 🤍 Change a lower layer (the key skill)
You are on `frontend` but realize you need an API change that belongs on `api-routes`. Commit it where it belongs, then replay everything above it.
```bash
gh stack down                      # go to the layer the change belongs on
git add users_api.go && git commit -m "Add get-user endpoint"
gh stack rebase --upstack          # replay every branch above onto the change
gh stack top                       # back to where you were
gh stack push
```
Committing on the wrong layer mixes unrelated diffs into that PR. Always commit where the change logically belongs.
### 🤍 Sync and merge
```bash
gh stack sync --prune              # fetch, rebase onto moved parents, push, drop merged branches
gh stack merge --yes               # land the whole stack, bottom to top
gh stack merge 42 --yes            # land only up to PR #42
gh stack merge --yes --squash      # land with a specific merge method
```
## 💛 Gotcha
- **Every command is non-interactive or it hangs.** A command that would prompt hangs forever, which matters for scripts and agents. Pass the prompt-avoiding flags: `submit --auto`, `view --json`, `merge --yes`. Note `gh pr merge` does not work on a stack; use `gh stack merge`.
- **submit and merge act outward, so confirm first.** `submit` opens or updates PRs (drafts by default, `--open` for ready-for-review). `merge` lands the whole stack bottom-to-top and can trigger deploys. It is all-or-nothing and hard to undo, so check the branch list before running either.
- **Linear only.** No branching stacks. A separate feature or unrelated fix starts its own stack with `gh stack init` or switches with `gh stack checkout`.
- **No custom PR title or body at submit.** They are auto-generated from your commit messages, so write good commit messages. Edit afterward with `gh pr edit`.
- **Restructure before any PR merges.** To reorder, rename, or drop layers, run `gh stack unstack` (this drops the grouping but does NOT delete the PRs), make the change, then rebuild with `gh stack init`. Clean only while the whole stack is still open.
- **Rebase conflicts exit with code 3.** Resolve the `<<<<<<<` markers, `git add` the files, then `gh stack rebase --continue` (or `--abort` to bail out and restore every branch).
- **Multiple remotes need a default.** Set `git config remote.pushDefault origin`, or several commands will error.
## 💛 References
- Managing stacked pull requests: https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/managing-stacked-pull-requests
- gh stack CLI reference: https://github.github.com/gh-stack/reference/cli/
- gh stack FAQ (merge queues, branch protection, CI): https://github.github.com/gh-stack/faq/
- GitHub CLI: https://cli.github.com/
