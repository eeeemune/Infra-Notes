# 💚 What is Helm?

## 💛 Short Answer

> **Helm** is the **package manager for Kubernetes**.


You can use it to:

- Install apps into your cluster
- Upgrade or delete them
- Reuse pre-made configurations

## 💛 Why Use Helm?

Without Helm, **installing apps** in Kubernetes means writing a LOT of YAML. 😵‍💫

**With Helm**:

- You just **run one command**
- It sets up everything for you
- You can **customize settings** easily

## 💛 What Is a Helm Chart?

A **`Helm Chart`** is like a recipe for an app.

It includes:

- All the YAML files you need
- Default values
- Options for customizing

### 🤍 Example:

Install **`nginx`** using Helm:

```bash
helm repo add bitnami <https://charts.bitnami.com/bitnami>
helm install my-nginx bitnami/nginx
```

Helm will:

- Create a Deployment
- Create a Service
- Set up configs — all in one go

## 💛 Helm Workflow

1. Add a chart repo (`helm repo add`)
2. Search for charts (`helm search`)
3. Install one (`helm install`)
4. Customize using `-values` file
5. Upgrade or rollback if needed

## 🤍 Summary

✅ `Helm` = **Easy app installation for Kubernetes**

✅ Use **charts** instead of hand-writing YAML

✅ Install, upgrade, and manage apps with **simple commands**

It’s like the **App Store for Kubernetes!** 🎉