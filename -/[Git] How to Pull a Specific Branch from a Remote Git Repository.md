# 💚 How to Pull a Specific Branch from a Remote Git Repository

## 💛 1. Check Remote Branches

First, list all branches available on the remote:

```bash
git fetch
git branch -r
```

You’ll see something like:

```
origin/main
origin/feature/login
origin/dev
```

## 💛 2. Pull a Specific Branch (first time)

If the branch doesn’t exist locally yet:

```bash
git checkout -b my-branch origin/my-branch
```

This:

- Creates a new local branch called `my-branch`
- Tracks the remote branch `origin/my-branch`

## 💛 3. Pull Updates (branch already exists locally)

If you’ve already checked it out:

```bash
git checkout my-branch
git pull origin my-branch
```

## 💛 Bonus: Just Download Without Switching

To fetch but **not switch** to that branch:

```bash
git fetch origin my-branch
```

The branch data will be downloaded and available as `origin/my-branch`.

## 💛 References

- [Git Docs - git fetch](https://git-scm.com/docs/git-fetch)
- [Git Docs - git checkout](https://git-scm.com/docs/git-checkout)
- [Atlassian Git Guide - Pulling Branches](https://www.atlassian.com/git/tutorials/syncing/git-pull)
