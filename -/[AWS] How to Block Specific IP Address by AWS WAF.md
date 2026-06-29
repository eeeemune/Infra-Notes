# 💚 How to Block Specific IP Address by AWS WAF

# 💚 How to Block a Specific IP Address using AWS WAF
## 💛 What is AWS WAF?
AWS WAF (Web Application Firewall) lets you filter HTTP(S) traffic to your applications (e.g., CloudFront, ALB, API Gateway).
You can **block, allow, or count** requests based on rules like IP addresses, headers, or SQL injection patterns.
## 💛 Steps to Block a Specific IP Address
### 🤍 1. Create an IP Set
- Go to **AWS WAF Console** → **IP addresses** → **Create IP set**.
- Give it a name (e.g., `BlockedIPs`).
- Add the IP address or CIDR range you want to block (e.g., `203.0.113.25/32` for a single IP).
### 🤍 2. Create a Web ACL
- Go to **Web ACLs** → **Create Web ACL**.
- **Choose resource type (CloudFront, ALB, API Gateway, AppSync).**
- Attach it to your resource (e.g., CloudFront distribution).
### 🤍 3. Add a Rule to Block IPs
- In your **Web ACL** → **Add rules** → **Add my own rules and rule groups**.
- Select **Rule builder**.
- Rule type: **IP match**.
- Use the IP set (`BlockedIPs`).
- Action: **Block**.
### 🤍 4. Save and Deploy
- Save the Web ACL and deploy.
- Requests from the blocked IP will now be denied.
