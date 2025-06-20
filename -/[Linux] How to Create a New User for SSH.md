# 💚 How to Create a New User for SSH

## 💛 1. Add the User

Run this as `root` or with `sudo`:

```bash
sudo adduser <new_user>
```

## 💛 2. Add User to `sudo` Group (optional)

To allow the user to run `sudo` commands:

```bash
sudo usermod -aG sudo <new_user>
```

## 💛 3. Create `.ssh` Folder

```bash
sudo mkdir -p /home/<new_user>/.ssh
sudo chmod 700 /home/<new_user>/.ssh
```

## 💛 4. Add Public SSH Key

Paste your **public key** (usually from `~/.ssh/id_rsa.pub`) into a file:

```bash
sudo vim /home/<new_user>/.ssh/authorized_keys
```

Paste it in, then:

```bash
sudo chmod 600 /home/<new_user>/.ssh/authorized_keys
sudo chown -R <new_user>:<new_user> /home/<new_user>/.ssh
```

## 💛 5. Test the Login

From your local machine:

```bash
ssh <new_user>@your.server.ip
```

---

### 🤍 Example

If you have this key on your local machine:

```bash
cat ~/.ssh/id_ed25519.pub
```

Paste the output into `/home/<new_user>/.ssh/authorized_keys` on the server.

---

## 💛 References

- [DigitalOcean - Add a New User with SSH Access](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-root-privileges-on-ubuntu)
- [Ubuntu Docs - Users and Groups](https://help.ubuntu.com/community/AddUsersHowto)
