# 💚 Terraform Provider for Helm
## 💛 What is the Terraform Provider for Helm?
The **`Terraform Helm provider`** lets you **manage Helm charts using Terraform**.
### 🤍 Helm Chart
Think of Helm charts like `apt` or `brew` packages
-  — but for Kubernetes.

### 🤍 What it does
- **Installs, upgrades, and deletes ****`Helm charts`**

- Works with any Kubernetes cluster 

    - EKS, GKE, **K3s**, etc.
    
- Integrates Helm into Terraform's lifecycle

### 🤍 Why use it?
- **Unified workflow:** Define your cluster and apps **in one Terraform config**

- **Automation**: Helm install happens automatically after the cluster is ready

- **Version control**: Helm releases are tracked in your `.tf` files

## 💛 Basic Example
```hcl
provider "helm" {
  kubernetes {
    host                   = data.aws_eks_cluster.cluster.endpoint
    cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      command     = "aws"
      args        = ["eks", "get-token", "--cluster-name", data.aws_eks_cluster.cluster.name]
    }
  }
}

resource "helm_release" "nginx" {
  name       = "nginx"
  repository = "<https://charts.bitnami.com/bitnami>"
  chart      = "nginx"
  values     = [file("${path.module}/nginx-values.yaml")]
}
```
> You define the app with helm_release, and Terraform installs it when you run terraform apply.