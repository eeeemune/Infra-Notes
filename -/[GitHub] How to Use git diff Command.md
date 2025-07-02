# 💚 How to Use git diff Command

## 💛 What does it do?

`git diff` shows the **differences between two versions of your code**.

You can use it to:

- See what you changed before committing
- Compare branches
- Review staged vs. unstaged changes

## 💛 Common Usages

### 🤍 Show unstaged changes (what you've edited but not added)

```bash
git diff
```

### 🤍 Show staged changes (what you've added with `git add`)

```bash
git diff --cached
```

### 🤍 Show everything (staged + unstaged)

```bash
git diff HEAD
```

## 💛 Compare Between Branches

```bash
git diff main..feature-branch
```

This shows what’s different in `feature-branch` **compared to** `main`.

## 💛 Compare Between Commits

```bash
git diff abc123 def456
```

You can get commit hashes using:

```bash
git log --oneline
```

## 💛 See Only File Names (not full diff)

```bash
git diff --name-only
```

## 💛 Compare with Remote Branch

```bash
git diff origin/main
```

## 💛 References

- [Git SCM Docs - git diff](https://git-scm.com/docs/git-diff)
- [Atlassian Git Tutorial - Viewing Changes](https://www.atlassian.com/git/tutorials/saving-changes/git-diff)
