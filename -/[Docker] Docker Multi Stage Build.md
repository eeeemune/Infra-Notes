# 💚 Docker Multi Stage Build

## 💛 What is a Dockerfile Stage?

A **Dockerfile stage** (also called **multi-stage build**) allows you to use **multiple build environments in one Dockerfile**.

This helps you:

- Build artifacts in one stage
- ***Copy only the final result*** to a smaller runtime image

## 💛 Basic Idea

Example workflow: Separate runner stage from builder stage

1. Use a builder image to compile the app
2. Copy only the compiled files to a lightweight runtime image

## 💛 Basic Syntax

Use multiple `FROM` statements.

```docker
# Builder Stage
FROM node:20 AS builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# Runner Stage
FROM node:20-slim
WORKDIR /app
COPY --from=builder /app/dist ./dist
CMD ["node", "dist/index.js"]
```

## 💛 How It Works

Stage 1 (`builder`)

- Install dependencies
- Compile the application

Stage 2 (`runtime`)

- Copy compiled output only
- Does **not include build tools**

Final image is much smaller.

## 💛 Example (Python)

```
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD ["python", "app.py"]
```

Final image only contains:

- binary
- tiny Alpine base image

## 💛 Why Multi-Stage Builds Are Important

Benefits:

- **Smaller image size**
- **Better security**
- **No build tools in production**
- **Cleaner images**

Example size difference:

| Build Method | Image Size |
| --- | --- |
| Single-stage | ~1.2GB |
| Multi-stage | ~120MB |

## 💛 Target a Specific Stage

You can build only one stage:

```
docker build --target builder -t myapp-builder .
```

Useful for debugging builds.

## 💛 References

- Docker Docs: [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
