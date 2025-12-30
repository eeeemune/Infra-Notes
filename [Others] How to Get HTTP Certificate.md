# 💚 How to Get HTTP Certificate

## 💛 Install Nginx and Certbot

```bash
sudo apt-get update
sudo apt-get install -y nginx certbot python3-certbot-nginx
```

## 💛 Configure Nginx as reverse proxy

```bash
# /etc/nginx/sites-available/mcp
server {
   listen 80;
   server_name mcp.chartmetric.com;

   location / {
       proxy_pass http://localhost:8080;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
   }
}
```

## 💛 Enable the site

```bash
  sudo ln -sf /etc/nginx/sites-available/mcp /etc/nginx/sites-enabled/
  sudo rm -f /etc/nginx/sites-enabled/default
  sudo nginx -t
  sudo systemctl reload nginxv
```

## 💛 Obtain SSL certificate

```bash
sudo certbot --nginx -d mcp.chartmetric.com --non-interactive --agree-tos --email your-email@chartmetric.com --redirect
```

## 💛 Enable auto-renual

```bash
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

<aside>
🚨

**Why is this step needed?**

- Your certificate will expire in 3 months
- Your site will show SSL errors and become inaccessible via HTTPS
- You'd have to manually run certbot renew every 90 days
</aside>
