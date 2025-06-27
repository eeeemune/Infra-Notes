# 💚 How to Get My IP on Linux

## 💛 Public

### 🤍 IPv6

```bash
curl ifconfig.me
# 2603:3024:269:2200::bb22
```

### 🤍 IPv4

```bash
 curl -4 ifconfig.me
 # 67.188.200.55
```

## 💛 Private

```bash
hostname -I | awk '{print $1}'
# 10.1.10.198
```
