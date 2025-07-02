# 💚 How to Check Environment Variables in a Docker Container

## 💛 1. While Running a Container

### 🤍 Option A: Use ‘docker exec’

If the container is already running:

```bash
docker exec -it <container_name> printenv
```

Or to check a specific variable:

```bash
docker exec -it <container_name> printenv VAR_NAME
```

*Example*:

```bash
docker exec -it my-app printenv NODE_ENV
```

### 🤍 Option B: Use a Shell

If the container has `/bin/bash` or `/bin/sh`:

```bash
docker exec -it <container_name> bash
# or
docker exec -it <container_name> sh
```

Then inside the container:

```bash
env
# or
echo $VAR_NAME
```

## 💛 2. When Creating a Container

You can **see what’s passed in** via `-e`:

```bash
docker run -e MY_KEY=1234 my-image
```

## 💛 3. From ‘docker inspect’

To check env vars without running a command inside:

```bash
docker inspect <container_name>
```

Look for the section:

```json
"Env": [
  "MY_KEY=1234",
  "NODE_ENV=production"
]
```

Or use a cleaner version:

```bash
docker inspect --format='{{range .Config.Env}}{{println .}}{{end}}' <container_name>
```

## 💛 References

- [Docker Docs - Environment Variables](https://docs.docker.com/compose/environment-variables/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/exec/)
