# 💚 GitHub Actions Runners & ARC Helm Chart

## 💛 What are GitHub Actions runners?

`GitHub Actions runners` are the machines that **run your CI/CD jobs** (like building, testing, or deploying code).

- **Hosted runners**: Provided by GitHub (like Ubuntu or Windows VMs).
- **Self-hosted runners**: You can run them on your own machines, cloud VMs, or Kubernetes.

## 💛 Why self-host runners?

- Faster builds (especially for large projects)
- Full control over environment (pre-installed tools)
- Lower cost at scale
- Needed for private code or air-gapped environments

## 💛 What is ARC (Actions Runner Controller)?

ARC = **Actions Runner Controller**, a Kubernetes controller that:

- **Deploys and manages self-hosted GitHub runners on Kubernetes**
- Automatically **scales runners up and down** based on the jobs
- Uses **custom Kubernetes resources** to manage runners per repo/org

## 💛 What is the ARC Helm chart?

Helm chart = a package of Kubernetes YAMLs

The ARC Helm chart:

- Installs the whole ARC system (controller + runners)
- Lets you configure scaling, GitHub access tokens, namespaces, etc.
- Makes setup easier with values.yaml

### 🤍 Example

```bash
# Add the Helm repo
helm repo add actions-runner-controller <https://actions-runner-controller.github.io/actions-runner-controller>

# Install ARC into Kubernetes
helm install arc actions-runner-controller/actions-runner-controller \\
  -n actions-runner-system --create-namespace \\
  -f values.yaml

```

You then create a custom resource like this to spin up runners:

```yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: my-runners
spec:
  replicas: 2
  template:
    spec:
      repository: your-org/your-repo

```

## 💛 Summary

- GitHub runners = machines that run Actions
- ARC = way to run GitHub runners inside Kubernetes
- ARC Helm chart = easy way to install ARC into your cluster

## 💛 References

- [[GitHub Actions - Runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
- [[Actions Runner Controller (ARC)](https://github.com/actions/actions-runner-controller)](https://github.com/actions/actions-runner-controller)
- [[ARC Helm Chart](https://github.com/actions/actions-runner-controller/tree/main/charts/actions-runner-controller)](https://github.com/actions/actions-runner-controller/tree/main/charts/actions-runner-controller)
