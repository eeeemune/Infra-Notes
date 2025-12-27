# 💚 Kubernetes Migration Common Mistakes & Tips

## 💛 Common Mistakes

### 🤍 Forgetting IAM Policies

> **Error Message:** "Instances failed to join the kubernetes cluster"
>
> **Fix:** Make sure you have ALL required policies:

- Cluster: `AmazonEKSClusterPolicy`
- Nodes: `AmazonEKSWorkerNodePolicy`, `AmazonEKS_CNI_Policy`, `AmazonEC2ContainerRegistryReadOnly`

### 🤍 Security Groups Blocking Traffic

> **Error:** Target groups show `unhealthy`, **timeouts**
> 
> **Fix:** Check that:

1. ALB SG can reach EKS nodes (all ports)
2. EKS nodes can reach RDS (port 5432)
3. EKS nodes can reach Redis (port 6379)

### 🤍 Wrong Target Type

> **Error:** ALB can't register targets
> 
> **Fix:** Use `target_type = "ip"` for EKS, not `instance`

### 🤍 Pods Can't Resolve DNS

> **Error Message:** "getaddrinfo ENOTFOUND"
> 
> **Fix:** Make sure CoreDNS addon is running:

```bash
kubectl get pods -n kube-system | grep coredns
```

### 🤍 Updating Immutable Fields

> **Error Message:** "TargetGroupBinding update may not change these fields"
> 
> **Fix:** Just delete and recreate. It’ll break nothing.

```bash
kubectl delete targetgroupbinding <name> -n <namespace>
terraform apply
```

### 🤍 Not Waiting for DNS Propagation

> **Error:** Works locally, fails from other services
> 
> **Fix:** Wait 5-10 minutes, or restart services to clear DNS cache

### 🤍 Secrets Not Taking Effect

> **Error:** Pods have old secret values
> 
> **Fix:** **Secrets are not auto-reload**! Roll out the deployments:

```bash
kubectl rollout restart deployment/chartmetric-api -n master
```

## 💛 Troubleshooting Guide

### 🤍 My Pod is ‘Weird’

```bash
# Check pod status
kubectl get pods -n master

# See why it's failing
kubectl describe pod <pod-name> -n master

# Check logs
kubectl logs <pod-name> -n master
```

**Common Causes:**

- Image pull error → Check ECR permissions
- CrashLoopBackOff → App is crashing, check logs
- Pending → Not enough resources, check nodes

### 🤍 I Can't Connect to Database

```bash
# Test from inside a pod
kubectl exec -it <pod-name> -n master -- bash
nc -zv <rds-endpoint> 5432
```

**If exec fails:** Mostly security group issue. Check the rules.

### 🤍 Health Check Takes Forever

→ Mostly ALB Health Checks Failing

```bash
# Check target group health in AWS Console
# Or use AWS CLI:
aws elbv2 describe-target-health --target-group-arn <arn>
```

**Common Causes:**

- Security group blocking traffic
- Health check path wrong
- App not listening on expected port

### 🤍 My Nodes are Not Scaled

```bash
# Check cluster autoscaler logs
kubectl logs -n kube-system -l app.kubernetes.io/name=cluster-autoscaler
```

**Common Causes:**

- Cluster autoscaler not installed
- IAM permissions missing
- Node group at max capacity

## 💛 Useful Commands Cheat Sheet

### 🤍 Cluster Access

```bash
# Configure kubectl
aws eks update-kubeconfig --name cm_cluster --region us-west-2

# Check connection
kubectl cluster-info
```

### 🤍 Getting Resources

```bash
# See everything in a namespace
kubectl get all -n master

# See pods
kubectl get pods -n master

# See pods with more details
kubectl get pods -n master -o wide

# See deployments
kubectl get deployments -n master

# See services
kubectl get svc -n master

# See ingresses
kubectl get ingress -A

# See secrets (names only)
kubectl get secrets -n master

```

### 🤍 Debugging

```bash
# Describe a resource (shows events, conditions)
kubectl describe pod <pod-name> -n master
kubectl describe deployment chartmetric-api -n master

# View logs
kubectl logs <pod-name> -n master
kubectl logs <pod-name> -n master -c <container-name>  # If multiple containers
kubectl logs -f <pod-name> -n master  # Follow (like tail -f)

# Execute command in pod
kubectl exec -it <pod-name> -n master -- bash
kubectl exec -it <pod-name> -n master -- env | grep REDIS
```

### 🤍 Deployments

```bash
# Restart pods (pick up new secrets, etc.)
kubectl rollout restart deployment/chartmetric-api -n master

# Check rollout status
kubectl rollout status deployment/chartmetric-api -n master

# Rollback if something went wrong
kubectl rollout undo deployment/chartmetric-api -n master

# Scale manually
kubectl scale deployment/chartmetric-api -n master --replicas=10

```

### 🤍 Get Secrets

```bash
# View secret value (base64 decoded)
kubectl get secret api-secrets -n master -o jsonpath='{.data.REDIS_HOST}' | base64 -d

# View all secret keys
kubectl get secret api-secrets -n master -o jsonpath='{.data}' | jq 'keys'
```

### 🤍 Troubleshooting Network

```bash
# Test connectivity from inside a pod
kubectl exec -it <pod-name> -n master -- nc -zv <hostname> <port>

# Check DNS resolution
kubectl exec -it <pod-name> -n master -- nslookup <hostname>
```
