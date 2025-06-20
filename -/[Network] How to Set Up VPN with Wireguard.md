# 💚 How to Set Up VPN with Wireguard

## 💛 Install Wireguard

```bash
sudo apt install wireguard
```

## 💛 Generate keys on each machine

On **every server and client**, run:

```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

This creates:

- `privatekey`: for `[Interface]`
- `publickey`: to share with peers

## 💛 Set Up Server

- `/etc/wireguard/wg0.conf`

```
[Interface]
PrivateKey = SERVER_PRIVATE_KEY
Address = <server_vpn_ip>/24
ListenPort = <port>

# Client 1
[Peer]
PublicKey = CLIENT1_PUBLIC_KEY
AllowedIPs = <client_vpn_ip>/32

# Client 2
[Peer]
PublicKey = CLIENT2_PUBLIC_KEY
AllowedIPs = 10.0.0.3/32
```

Enable IP forwarding:

```bash
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

Start server:

```bash
sudo wg-quick up wg0
```

---

## 💛 Set Up Client

- `/etc/wireguard/wg0.conf`

```
[Interface]
PrivateKey = CLIENT1_PRIVATE_KEY
Address = <client_vpn_ip>/24

[Peer]
PublicKey = SERVER_PUBLIC_KEY
Endpoint = <server_ip>:<port>
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

Start client:

```bash
sudo wg-quick up wg0
```
