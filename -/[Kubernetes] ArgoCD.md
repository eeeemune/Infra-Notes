# 💚 ArgoCD

## 💛 What is it?
**ArgoCD** is a **GitOps tool for Kubernetes**.
It keeps your cluster in sync with what's described in a Git repo.
### 🤍 The idea
Your Git repo is the **single source of truth**. You write your Kubernetes manifests (YAML, Helm, Kustomize) in Git, and ArgoCD makes sure the cluster **always matches** what's in Git.
Think of it like a robot that constantly checks: "Does the live cluster look exactly like the Git repo? If not, fix it."
## 💛 Why do we need it?
The old way of deploying to Kubernetes is running `kubectl apply` by hand or from a CI pipeline. That has problems:
- No clear record of what's actually running in the cluster
- Cluster can **drift** (someone runs `kubectl edit` manually and now it doesn't match Git)
- Your CI system needs **cluster admin credentials**, which is a security risk
- Rollback is awkward
ArgoCD fixes these:
- **Git is the record.** Want to know what's deployed? Read the repo.
- **Auto-heal drift.** A manual change in the cluster gets reverted back to Git's version.
- **No cluster creds in CI.** ArgoCD runs inside the cluster and pulls from Git, so CI never touches the cluster.
- **Rollback = git revert.** Roll back a deploy by reverting a commit.
### 🤍 Real-world use case
Your team commits a new image tag to the `prod` config repo. ArgoCD sees the change, syncs it, and the new version rolls out. No one runs `kubectl` against prod. The audit trail is just the Git history.
## 💛 How does it work?
ArgoCD runs as a controller inside your cluster. It watches a Git repo and a target cluster, then compares the two.
Two key states it tracks for every app:
- **Sync status**: does the live cluster match Git? (`Synced` vs `OutOfSync`)
- **Health status**: are the resources actually healthy? (`Healthy`, `Progressing`, `Degraded`)
### 🤍 Reconcile Flow
```javascript
Git repo (desired state)
        |
        v
   ArgoCD controller   (polls Git, compares)
        |
   diff: Git vs live cluster?
        |
   OutOfSync ----> sync (kubectl apply under the hood)
        |
        v
Kubernetes cluster (actual state)  ---> Healthy / Degraded
```
The loop never stops. If the live state drifts from Git, ArgoCD flags it `OutOfSync` (and can auto-correct if you turn that on).
### 🤍 Example: an Application
ArgoCD's main object is the `Application`. It points at a Git repo path and a destination cluster/namespace.
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/my-org/my-app-config.git
    targetRevision: main
    path: k8s/overlays/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: my-app
  syncPolicy:
    automated:
      prune: true       # delete resources removed from Git
      selfHeal: true    # revert manual cluster changes back to Git
```
### 🤍 Example: CLI
```bash
# Log in to the ArgoCD server
argocd login argocd.mycompany.com

# List apps and their sync/health status
argocd app list

# Manually trigger a sync
argocd app sync my-app

# See the diff between Git and the live cluster
argocd app diff my-app
```
## 💛 Push vs Pull (why GitOps matters)
- **Push model (old CI/CD)**: CI builds, then pushes to the cluster using stored cluster credentials.
- **Pull model (ArgoCD)**: ArgoCD lives in the cluster and pulls from Git. Credentials stay inside the cluster, not in CI.
This is the core security win of GitOps. Your CI pipeline only needs write access to Git, not to the cluster.
## 💛 Gotcha
- ArgoCD deploys **config**, it does not build images.
  - Chartmetric’s CI still builds and pushes the image, then updates the image tag in the Git config repo. ArgoCD takes over from there.
- A common setup is **two repos**: app source code in one, Kubernetes manifests in another (the "config repo"). ArgoCD watches the config repo.
- `selfHeal: true` means a manual `kubectl edit` on a synced app gets reverted fast. Good for prod safety, surprising the first time it happens to you.
## 💛 References
- Argo CD Docs (official): https://argo-cd.readthedocs.io/
- Argo CD Getting Started: https://argo-cd.readthedocs.io/en/stable/getting_started/
- Argo project (GitOps): https://argoproj.github.io/cd/
