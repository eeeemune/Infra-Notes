# 💚 What Is Docker Mount?

In Docker, a **mount** lets you **connect files/folders from your host machine into a running container**.

This is useful for sharing configuration, data, or logs.

## 💛 Basic Syntax

```bash
-v /host/path:/container/path[:options]
```

- `/host/path`: path on your **local machine**
- `/container/path`: path **inside the container**
- `[:options]`: optional settings like `ro` (read-only)

## 💛 Example

```bash
/data/coolify/ssl/coolify-ca.crt:/etc/ssl/certs/coolify-ca.crt:ro
```

### 🤍 What It Means:

- **`/data/coolify/ssl/coolify-ca.crt`**: file on your host machine
- **`/etc/ssl/certs/coolify-ca.crt`**: path inside the container
- **`:ro`**: the file is **read-only** inside the container

## 💛 Why Use This?

In this case, you're mounting an **SSL certificate** into a container so it can use it for **secure communication**.

Making it `read-only` ensures the container cannot modify the original file.

## 💛 Other Mount Use Cases

- Share config files (`.env`, `.yaml`)
- Persist database data (`/var/lib/postgresql`)
- Expose log files
- Inject secrets or certs securely

## 💛 Reference

- [Docker Volumes - Official Docs](https://docs.docker.com/storage/volumes/)
- [Bind Mounts vs Volumes](https://docs.docker.com/storage/bind-mounts/)
