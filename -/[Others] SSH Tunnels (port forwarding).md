# 💚 SSH Tunnels (port forwarding)

## 💛 What is it?
An **SSH tunnel** reuses an SSH connection to carry other traffic.
Plain version: "make a port on one machine actually reach a port on another machine, through SSH."
The classic use: reach a service that is not exposed to you directly (a database, an internal API, a cluster port) by borrowing a server that can reach it.
## 💛 Why do we need it?
- **Reach private services.** A database bound to `127.0.0.1` or an internal-only IP is not reachable from your laptop. If you can SSH to a box that can reach it, you can tunnel to it.
- **No new firewall holes.** You are not opening the database to the internet. Traffic rides the SSH port (22) you already allow.
- **Encryption for free.** Even a plaintext protocol becomes encrypted in transit, because it travels inside SSH.
- **Match certificates/hostnames.** As in the k3s case: a service whose cert is valid for `127.0.0.1` stays valid if you tunnel so it still looks like `127.0.0.1` to the client.
## 💛 The three kinds
There are three forwarding modes. The flag letter tells you the direction.
- `-L` **Local forwarding**: a port on YOUR machine forwards to a target reachable from the REMOTE. "Pull a remote service to me." Most common.
- `-R` **Remote forwarding**: a port on the REMOTE forwards back to a target reachable from YOUR machine. "Expose my local service on the server."
- `-D` **Dynamic forwarding**: turns SSH into a local SOCKS proxy. "Send lots of destinations through the remote," like a lightweight VPN for a browser.
### 🤍 -L Local forwarding (the common one)
```bash
# localhost:6443 on my Mac -> (via bastion) -> 127.0.0.1:6443 on the remote
ssh -N -L 6443:127.0.0.1:6443 llm_vpn
```
The address after the first colon is resolved FROM THE REMOTE's point of view. `127.0.0.1:6443` means "`localhost` on the server I SSH into," which is where the k3s API listens. `-N` means "do not run a remote shell, just forward."
```javascript
[ Mac ]                         [ bastion / llm host ]
localhost:6443  == SSH tunnel ==>  127.0.0.1:6443 (k3s API)
     ^ your kubectl connects here
```
Forward to a service on a THIRD host the remote can see (e.g. an internal RDS):
```bash
# my localhost:5432 -> (via bastion) -> db.internal:5432
ssh -N -L 5432:db.internal.example.com:5432 bastion
psql -h 127.0.0.1 -p 5432   # talks to the internal DB
```
### 🤍 -R Remote forwarding (expose local to the server)
```bash
# server's localhost:8080 -> back to my Mac's localhost:3000
ssh -N -R 8080:127.0.0.1:3000 remote
# now curl localhost:8080 ON the remote hits my local dev server
```
Use it to let a remote box reach a service running on your laptop (demo a local app, receive a webhook).
### 🤍 -D Dynamic forwarding (SOCKS proxy)
```bash
# open a SOCKS5 proxy on localhost:1080, routed through the remote
ssh -N -D 1080 bastion
# point a browser / tool at socks5://127.0.0.1:1080
```
Everything sent to the proxy exits from the remote host. Good for reaching many internal URLs without a tunnel per port.
## 💛 Handy flags
- `-N`: no remote command. Pure forwarding. Almost always used for tunnels.
- `-f`: go to the background after connecting (`ssh -fN -L ...`).
- `-L 0.0.0.0:PORT:...`: bind the local port on all interfaces, not just `localhost` (be careful, this exposes the tunnel to your LAN).
- `-o ExitOnForwardFailure=yes`: if the forward cannot be set up, kill the SSH instead of connecting anyway. Good for scripts.
- `-o BatchMode=yes`: never prompt (fail instead), so it does not hang in automation.
- `-J bastion` (ProxyJump): hop through a bastion to reach the real target in one command.
## 💛 Keeping it alive
A tunnel is just an SSH process. When it dies, the forward dies.
- It ends when the shell/session that started it ends. Reopen it before using the port again.
- For long-lived tunnels use **autossh**, which restarts a dropped tunnel automatically:
```bash
autossh -M 0 -fN -L 6443:127.0.0.1:6443 llm_vpn
```
- Or define reusable settings in `~/.ssh/config` (`LocalForward`, `ServerAliveInterval`) so `ssh llm_vpn` just works.
## 💛 Gotcha
- **The target is resolved from the remote side.** In `-L local:TARGET:port`, `TARGET` must be reachable FROM the server, not from you. `127.0.0.1` means the server's `localhost`, not yours. This trips people up constantly.
- **SSH aliases are local.** `llm_vpn` only means something on the machine whose `~/.ssh/config` defines it. It does not exist on remote hosts.
- **Port already in use.** If `localhost:6443` is taken, the forward fails. Pick another local port (`-L 7443:127.0.0.1:6443`) and point your client there.
- **A tunnel is not persistent.** No magic reconnect unless you use autossh or a supervisor. A laptop sleeping kills it.
- `-R` binds to the remote's `localhost` by default. To expose it beyond the remote box you also need `GatewayPorts` enabled on that server.
## 💛 References
- OpenSSH manual (`ssh`, see -L / -R / -D): https://man.openbsd.org/ssh
- SSH port forwarding guide (ssh.com): https://www.ssh.com/academy/ssh/tunneling/example
- autossh: https://www.harding.motd.ca/autossh/
