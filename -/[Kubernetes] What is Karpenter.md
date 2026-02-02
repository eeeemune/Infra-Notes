# 💚 What is Karpenter?

## 💛 Karpenter

<aside>

Karpenter is a Kubernetes node autoscaler

</aside>

## 💛 Why Do We Need It?

In Kubernetes:

- Pods need CPU/RAM to run
- If there’s no space → Pods stay `Pending`

Without Karpenter:

- You manually add nodes
- Or use slow, static Auto Scaling Groups

With Karpenter:

- It **instantly launches the right EC2 instances automatically**

## 💛 How It Works

### 🤍 Flow

1. Pod is scheduled
2. Not enough resources → Pod becomes **Pending**
3. **Karpenter detects Pending Pod**
4. Karpenter:
    - calculates required CPU/memory
    - picks best EC2 instance type
    - launches new node
5. Pod runs 
6. When idle → node gets terminated automatically

## 💛 What Makes Karpenter Special?

Compared to the old Cluster Autoscaler:

### 🤍 Traditional Cluster Autoscaler

- Uses fixed Auto Scaling Groups
- Predefined instance types
- Slower
- Less flexible

### 🤍 Karpenter

- Chooses **any instance type dynamically**
- Faster scaling (seconds)
- Better bin-packing (lower cost)
- No ASG management needed
- Great for Spot instances

## 💛 Simple Config Example

```yaml
apiVersion: karpenter.sh/v1beta1
kind: Provisioner
metadata:
  name: default
spec:
  requirements:
    - key: node.kubernetes.io/instance-type
      operator: In
      values: ["t3.large", "t3.xlarge"]
  limits:
    resources:
      cpu: "1000"
```

This tells Karpenter:

- which instances are allowed
- max scaling limit

## 💛 References

- Karpenter Official Site: https://karpenter.sh/
- GitHub Repo: https://github.com/aws/karpenter
- AWS Blog: https://aws.amazon.com/blogs/containers/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/
