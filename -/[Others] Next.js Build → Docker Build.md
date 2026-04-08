# 💚 Next.js Build → Docker Build

## 💛 What You Deploy in Next.js?

After running:

```bash
next build
```

- You **DO NOT deploy source code**
- You deploy the **.next build output + minimal runtime**

## 💛 Option 1: Standard Deployment (Node Server)

<aside>

**We’re using this approach at Chartmetric!** 😭

</aside>

You run:

```bash
next start
```

This uses:

- `.next/server/` → backend logic (SSR, API routes)
- `.next/static/` → frontend assets
- `node_modules/` → dependencies

## 💛 Option 2: Standalone Mode (Best for Docker)

Enable in `next.config.js`:

```jsx
module.exports = {
  output: "standalone",
};
```

Then build:

```bash
next build
```

## 💛 What You Get

```
.next/
├── standalone/
├── static/
```

### 🤍 .next/standalone/

- Minimal Node.js server
- Includes only required dependencies
- Ready to run with `node server.js`

### 🤍 .next/static/

- Static assets (JS, CSS, chunks)

## 💛 Docker Deployment

### 🤍 Example Dockerfile

```docker
FROM node:20-alpine

WORKDIR /app

# Copy standalone server
COPY .next/standalone ./

# Copy static assets
COPY .next/static ./.next/static

# (optional) public folder
COPY public ./public

EXPOSE 3000

CMD ["node", "server.js"]
```

## 💛 Why Standalone is Awesome

Without standalone:

- Need full `node_modules`
- Bigger image

With standalone:

- Minimal dependencies
- Smaller image
- Faster startup

## 💛 Key Insight

👉 `.next` is NOT just static files

👉 It contains BOTH:

- frontend bundles
- backend (Node server logic)

## 💛 Production Best Practice

- Use **standalone mode**
- Use **multi-stage Docker build**
- Add **health check endpoint**
- Use **Horizontal Pod Autoscaling (HPA)**

## 💛 References

- Next.js Deployment Docs: https://nextjs.org/docs/app/building-your-application/deploying
- Next.js Standalone Output: https://nextjs.org/docs/app/api-reference/next-config-js/output
- Kubernetes Deployment Docs: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
