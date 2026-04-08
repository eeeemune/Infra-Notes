# 💚 What does ‘next build’ do?

## 💛 Short Answer

`next build` prepares your Next.js app for production.

→ It compiles, bundles, optimizes, and generates a `.next` directory.

## 💛 What Happens During Build?

### 🤍 1. Compile

- TypeScript → JavaScript
- JSX → JS
- Uses **SWC (fast Rust compiler)**

### 🤍 2. Bundle

- Splits code per page (code splitting)
- Creates optimized JS chunks

### 🤍 3. Pre-render

Depending on page type:

| Type | Behavior |
| --- | --- |
| SSG | HTML generated at build time |
| SSR | Prepared for runtime |
| ISR | Static + revalidation |

### 🤍 4. Optimize

- Minify JS/CSS
- Tree shaking
- Image optimization hooks
- Dead code removal

## 💛 Final Output: .next Directory

After build:

```
.next/
```

This is the **production-ready artifact**.

## 💛 .next Structure

### 🤍 1. Server Side Code

```
.next/server/
```

Contains:

- Compiled backend code
- API routes
- SSR logic

Example:

```
.next/server/app/
.next/server/pages/
```

→ Used by `next start` (Node.js server)

### 🤍 2. Static Files

```
.next/static/
```

Contains:

- JS bundles
- CSS
- chunks

Example:

```
.next/static/chunks/
.next/static/css/
.next/static/media/
```

→ Served directly to browser

### 🤍 3. Build Manifest

```
.next/build-manifest.json
```

- Maps pages → JS bundles
- Helps Next.js know what to load

### 🤍 4. Routes Manifest

```
.next/routes-manifest.json
```

- Defines routing rules
- Includes dynamic routes

### 🤍 5. Prerender Manifest

```
.next/prerender-manifest.json
```

- Lists pre-rendered pages (SSG)
- Contains ISR config (revalidate times)

### 🤍 6. Required Server Files

```
.next/required-server-files.json
```

- Lists files needed to run app in production
- Used for deployments (e.g. Docker, serverless)

### 🤍 7. Cache

```
.next/cache/
```

- Build cache for faster rebuilds
- Can be safely deleted

### 🤍 8. Standalone Output (Optional)

If using:

```jsx
output: "standalone"
```

Then:

```
.next/standalone/
```

Contains:

- Minimal Node.js server
- Only required dependencies

## 💛 Example Full Structure

```
.next/
├── cache/
├── server/
│   ├── app/
│   └── pages/
├── static/
│   ├── chunks/
│   ├── css/
│   └── media/
├── build-manifest.json
├── routes-manifest.json
├── prerender-manifest.json
├── required-server-files.json
```

## 💛 Runtime Flow Example

1. Browser requests `/about`
2. Server reads:
    - routing info
    - required JS bundle
3. Sends:
    - HTML (SSG/SSR)
    - JS from `.next/static`
4. React hydrates page

## 💛 References

- Next.js Docs: https://nextjs.org/docs/app/building-your-application/deploying
- Next.js Architecture: https://nextjs.org/docs/app/building-your-application/rendering
