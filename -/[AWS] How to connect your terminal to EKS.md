# 💚 How to connect your terminal to EKS

## 💛 Prerequisites

### 🤍 Required tools

You need these installed **locally**:

1. **AWS CLI**
    
    ```bash
    aws --version
    ```
    
2. **kubectl**
    
    ```hcl
    kubectl version --client
    ```
    
3. **AWS credentials configured**
    
    ```bash
    aws configure
    ```
    

## 💛 Steps

### 🤍 1. Verify AWS access

Check who you are:

```bash
aws sts get-caller-identity
```

You should see:

- `Account`
- `Arn`
- `UserId`

### 🤍 2. Generate ‘kubeconfig’ for EKS

```bash
aws eks update-kubeconfig \
  --region <your-region> \
  --name <cluster-name>

# Real example
aws eks update-kubeconfig \
  --region us-west-2 \
  --name cm_cluster
```

This will:

- Fetch cluster endpoint + CA cert
- Write to `~/.kube/config`
- Add a new **context**

### 🤍 3. Select and check current context

```bash
kubectl config current-context
```

List all contexts:

```bash
kubectl config get-contexts
```

Switch if needed:

```bash
kubectl config use-context <context-name>
```

<aside>

**Q. What’s the ‘context’?**

Context = cluster + user + namespace

</aside>

### 🤍 4. Test

```bash
kubectl get nodes
```
