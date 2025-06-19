# 💚 What is NAT?

## 💛 NAT = Network Address Translation

NAT is a method used by routers or firewalls to **change IP addresses** in packets as they pass through a network boundary.

It helps devices on a **private network** (like `192.168.x.x` or `10.0.x.x`) talk to the **public internet**, even if they don’t have public IPs.

## 💛 Why do we need NAT?

- **IPv4 address shortage**
    
    We don’t have enough public IP addresses for every device.
    
- **Security**
    
    It hides private IPs from the outside world.
    
- **Multiple devices, one IP**
    
    Lets many devices (like your phone, laptop, TV) share a **single public IP**.
    

## 💛 How does it work?

### 🤍 Simple Example

```
Home network:
- PC1: 192.168.0.10
- PC2: 192.168.0.11
Router: Public IP = 203.0.113.5
```

When PC1 sends a request to Google:

1. PC1 → 192.168.0.10 sends packet to 8.8.8.8 (Google DNS)
2. Router replaces **source IP** `192.168.0.10` → `203.0.113.5`
3. Router keeps a table:`203.0.113.5:PORT12345 ←→ 192.168.0.10:PORT56789`
4. When reply comes back, router uses that table to send it back to PC1

---

## 💛 Types of NAT

| Type | What it does | Use Case |
| --- | --- | --- |
| SNAT (Source NAT) | Changes **source IP** | Devices going out to internet |
| DNAT (Destination NAT) | Changes **destination IP** | Port forwarding to internal servers |
| PAT (Port Address Translation) | Multiple devices share **one IP + port** | Home routers, cloud VPCs |

## 💛 Where is NAT used?

- Your home Wi-Fi router
- Cloud services (AWS, GCP: NAT Gateway)
- Kubernetes clusters (NodePort, egress IPs)
- VPN servers (like WireGuard)

## 💛 References

- [Wikipedia - NAT](https://en.wikipedia.org/wiki/Network_address_translation)
- [Cisco - NAT Basics](https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/network-address-translation/prod_white_paper09186a00800a3e2f.html)
- [Cloudflare - What is NAT](https://www.cloudflare.com/learning/network-layer/what-is-nat/)
