# 💚 How to Configure Git on Your Terminal

## 💛 1. Set Your Identity (Required)

Git needs your **name and email** for commits.

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

- `-global` → applies to all projects on your machine

## 💛 2. Check Your Config

```bash
git config --list
```

Or:

```bash
git config user.name
git config user.email
```

## 💛 3. Set Credential Helper (avoid typing password/PAT every time)

### 🤍 macOS

```bash
git config --global credential.helper osxkeychain
```

### 🤍 Linux (simple store)

```bash
git config --global credential.helper store
```

## 💛 4. Set Editor (Optional)

### 🤍 Vim

```bash
git config --global core.editor "vim"
```

---

## 💛 5. Enable Colored Output (Pretty UI)

```bash
git config --global color.ui auto
```

## 💛 7. Setup SSH Instead of Password

Generate key:

```bash
ssh-keygen -t ed25519
```

Add to GitHub:

```bash
cat ~/.ssh/id_ed25519.pub
```

Test:

```bash
ssh -T git@github.com

# Hi eeeemune! You've successfully authenticated, but GitHub does not provide shell access.
```

Clone with SSH:

```bash
git clone git@github.com:org/repo.git
```

## 💛 Example Full Setup (Quick Copy)

```bash
git config --global user.name "eemune"
git config --global user.email "eeeemune@gmail.com"
git config --global init.defaultBranch main
git config --global credential.helper store
git config --global color.ui auto
git config --global core.editor "code --wait"
```

## 💛 References

- Git Docs: https://git-scm.com/docs/git-config
- GitHub SSH Guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
