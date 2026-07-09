# 💚 How Playwright Works

## 💛 What is it?
**Playwright** is a browser automation tool from Microsoft. You write a script (JS/TS, Python, Java, .NET) and it drives a real browser: click, type, navigate, screenshot, assert.
## 💛 Why do we need it?
Manually clicking through your app before every release does not scale. Playwright automates the browser so you can:
- **E2E test** the real user flow (login, checkout) against a real browser, not a fake DOM.
- **Test across engines.** One script runs on Chromium, Firefox, and WebKit (the Safari engine), so you catch browser-specific bugs.
- **Automate anything browser-based.** Scraping, PDF generation, screenshots, filling forms.
The reason it won over older tools (like Selenium) is **reliability**: it waits for elements automatically, so tests stop being flaky.
### 🤍 Real-world use case
Your CI pipeline runs a Playwright suite on every pull request. It spins up headless browsers, logs into a test build, walks the checkout flow, and fails the PR if a button broke. No human clicking required.
## 💛 How does it work (the architecture)?
This is the interesting part. There are three layers.
- **Your script (the client).** Calls like `page.click()` are not run inside the browser. They are commands sent to a separate process.
- **The Playwright driver (server).** A Node.js process that receives your commands and translates them into low-level browser instructions. Your client talks to it over a single persistent connection (a pipe / WebSocket) using a JSON protocol.
- **The browser.** The driver launches a browser it ships itself (a known-good build) and controls it through that browser's **remote debugging protocol** (CDP for Chromium; patched protocols for Firefox and WebKit).
### 🤍 Request Flow
```javascript
Your test code (Python / JS)
  |
  | one command: page.click("#buy")
  v
Playwright driver process (Node.js)
  |
  | debugging protocol (CDP / patched) over a pipe
  v
Browser (Chromium / Firefox / WebKit)
  |
  | performs the real action, sends events + results back
  v
driver -> your test (command resolves)
```
Key idea: your code and the browser are **separate processes** talking over one connection. That is why Playwright can control multiple pages and browsers at once, and why the same protocol works from any language.
## 💛 The two ideas that make it reliable
### 🤍 Browser contexts
A **BrowserContext** is an isolated session inside one browser process, like a fresh incognito window (its own cookies, storage, cache). They are cheap to create.
- One launched browser can hold many contexts.
- Each test gets its own context, so tests do not leak state into each other.
- This is how Playwright runs tests in parallel fast: many contexts, one browser, instead of many full browser launches.
```javascript
const browser = await chromium.launch();
const context = await browser.newContext();   // isolated session
const page = await context.newPage();
await page.goto("https://example.com");
```
### 🤍 Auto-waiting (actionability)
Before every action, Playwright automatically checks the target is **actionable**: attached to the DOM, visible, stable (not animating), enabled, and not covered by another element. It retries until the checks pass or it times out.
- You almost never write manual `sleep()` calls.
- This is the main reason Playwright tests are not flaky: it does not click a button that is not ready yet.
```python
# No manual wait needed. Playwright waits until #buy is clickable.
page.click("#buy")
expect(page.locator(".cart-count")).to_have_text("1")
```
## 💛 Locators vs selectors
- A **selector** is the string that finds an element (CSS, text, role).
- A **Locator** is a lazy, re-findable handle to that element. It does not grab the element once. It re-locates it every time you use it, which survives the page re-rendering.
```javascript
const buy = page.getByRole("button", { name: "Buy" });  // locator
await buy.click();   // finds it fresh, waits until actionable, clicks
```
## 💛 Gotcha
- **Bundled browsers, not your installed ones.** `playwright install` downloads its own browser builds so results are consistent. They are separate from the Chrome on your machine, and they take disk space.
- **Headless vs headed.** CI runs headless (no visible window) for speed. Run headed (`--headed`) or the Inspector when debugging so you can watch it.
- **WebKit is not Safari.** It is the same engine, but not the full Safari app. Close, not identical.
- **Auto-wait is not infinite.** It waits up to a timeout (default 30s). A truly missing element still fails, just after the wait, so a slow test can mean a real bug.
- **Every action is a command round-trip.** Calls like `page.click` cross the process boundary. Usually fine, but thousands of tiny calls in a tight loop are slower than doing the work in one `page.evaluate()` inside the browser.
## 💛 References
- Playwright docs: https://playwright.dev/docs/intro
- Playwright: browser contexts / isolation: https://playwright.dev/docs/browser-contexts
- Playwright: auto-waiting and actionability: https://playwright.dev/docs/actionability
