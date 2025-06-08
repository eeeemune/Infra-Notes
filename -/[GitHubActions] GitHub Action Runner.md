# 💚 What is the ‘**runner’**?

In this context, the **`runner`** is the **machine or container** that actually **runs your CI/CD jobs**, such as:

- Building Docker images
- Running tests
- Deploying code

## 💛 GitHub Actions Runner

The `runner` is such like a machine that runs the steps in your `.github/workflows/...` files.

## 💛 Where does the **runner** live?

In our infra setup, the runner is:

- A **self-hosted runner** running in your Kubernetes cluster (like `chartmetric-infra:runner` image),
    - We call this node as a `cyber`
- Or a **container** spun up to run a specific job (like in GitHub Actions, CircleCI, etc.),

## 💛 Example

Let’s say you have a `GitHub Action` like:

```yaml
- name: Build Docker image
  run: docker build -t my-app .

- name: Push to registry
  run: docker push registry.registry.svc.cluster.local:5000/my-app
```

All of this is happening **inside the runner**. So if that runner:

- Doesn’t have access to Harbor, or
- Is configured incorrectly,

→ Your push/pull will fail — like what you’re seeing with the `500 Internal Server Error`.
