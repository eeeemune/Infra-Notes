# 💚 Helm Chart and Release

## 💛 What is a **Helm Release**?

A **`Helm release`** is a **specific deployment of a Helm chart** into a Kubernetes cluster.

Think of it like this:

| Concept | Analogy | Description |
| --- | --- | --- |
| **Chart** | Template | The blueprint — it defines *what* to install (e.g. NGINX, Redis). |
| **Release** | Instance | The actual *running* deployment of that chart in your cluster. |

## 💛 Example

If you install the **`nginx`** Helm chart:

```bash
helm install my-nginx bitnami/nginx
```

- `bitnami/nginx` → is the **chart**
- `my-nginx` → is the **release name**
- The result → A **Helm release** named `my-nginx` deployed into your cluster.

## 💛 In Terraform

In Terraform, the `helm_release` **resource** represents that same concept:

```hcl
resource "helm_release" "nginx" {
  name       = "nginx"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "nginx"
}
```

Terraform will…

- Install the Helm chart
- Track it in state
- Let you upgrade, change, or destroy it later
