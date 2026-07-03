# 💚 IAM Roles for Service Accounts

## 💛 What is it?
**IRSA (IAM Roles for Service Accounts)** lets a **pod in EKS assume an AWS IAM role** using its Kubernetes **service account**, instead of borrowing the EC2 node's credentials.
Plain version: you attach an IAM role to a service account. Any pod using that service account automatically gets **temporary AWS credentials** for that role. No access keys in the pod, no secrets to rotate.
It is the EKS answer to "how does my pod talk to S3 / SQS / DynamoDB securely?"
## 💛 Why do we need it?
Before IRSA, pods used the **node's IAM role**. That is bad because:
- **Every pod on that node shared the same permissions.** A tiny logging pod had the same AWS access as your main app. No isolation.
- **You over-grant.** The node role becomes a union of everything any pod might need. That is the opposite of least privilege.
- **Static keys are worse.** The other option was baking AWS access keys into a Secret, which leaks and never rotates.
IRSA fixes it: **per-workload permissions**, **no static keys**, **auto-rotating temporary credentials**.
### 🤍 Real-world use case
Your `image-uploader` pod needs write access to one S3 bucket. With IRSA you give only that service account a role scoped to only that bucket. The database pod next to it gets nothing. Blast radius stays tiny.
## 💛 How does it work?
IRSA is built on an **OIDC** trust between your EKS cluster and IAM, plus a token that gets projected into the pod.
- EKS exposes an **OIDC provider** (an identity endpoint for the cluster).
- You register that provider in IAM as trusted.
- The IAM role's **trust policy** says "trust tokens from this cluster's OIDC, but only for this specific service account."
- The pod gets a signed **service-account token** mounted in. The AWS SDK swaps it for role credentials via STS `AssumeRoleWithWebIdentity`.
### 🤍 Request Flow
```javascript
Pod (uses service account "uploader")
  |
  | projected service-account JWT token is mounted in
  v
AWS SDK calls STS: AssumeRoleWithWebIdentity(token)
  |
  | STS checks the role's trust policy against the
  | cluster OIDC provider + namespace + SA name
  v
Temporary AWS credentials (expire, auto-refresh)
  |
  v
Pod calls S3 / SQS / DynamoDB with just-enough permissions
```
Key idea: the pod never holds a long-lived secret. It holds a short-lived token that STS trades for role credentials, and the SDK refreshes it automatically.
## 💛 How to use it smartly
This is the part that matters. IRSA is easy to set up badly.
- **One role per service account, per app.** Do not make a shared "app-role" that everything uses. That recreates the node-role problem. Narrow role = small blast radius.
- **Scope the trust policy to the exact service account.** Use a `StringEquals` condition on `sub` for `system:serviceaccount:<namespace>:<sa-name>`. Without it, any SA in the cluster could assume the role.
- **Least privilege on the permissions policy.** Grant the specific actions on the specific ARNs. Not `s3:*` on `*`. Start narrow, widen only when something breaks.
- **Match the audience** to `sts.amazonaws.com`. This is the standard `aud` condition; keep it so only STS web-identity calls are accepted.
- **Separate roles per environment.** dev, staging, prod service accounts should map to separate roles, so a dev workload can never touch prod data.
- **Let a module wire it.** eksctl (`--service-account`) or Terraform modules generate the trust policy correctly. Hand-writing OIDC conditions is where people make mistakes.
### 🤍 Example: the trust policy (scoped to one SA)
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Federated": "<arn>"
    },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {
        "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539:aud": "sts.amazonaws.com",
        "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539:sub": "system:serviceaccount:media:uploader"
      }
    }
  }]
}
```
The `sub` line is the important one. It locks the role to the `uploader` service account in the `media` namespace only.
### 🤍 Example: annotate the service account
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: uploader
  namespace: media
  annotations:
    eks.amazonaws.com/role-arn: <arn>/media-uploader
```
Any pod that sets `serviceAccountName: uploader` now gets those role credentials, no keys needed.
### 🤍 Example: one command with eksctl
```bash
eksctl create iamserviceaccount \
  --cluster my-cluster \
  --namespace media \
  --name uploader \
  --attach-policy-arn "<arn>:iam::aws:policy/AmazonS3ReadOnlyAccess \
  --approve
```
This creates the SA, the role, and the correctly-scoped trust policy in one shot.
## 💛 Gotcha
- **The pod must use the annotated service account.** If you forget `serviceAccountName`, the pod falls back to `default` and IRSA silently does nothing (it uses the node role instead).
- **Old SDKs do not support it.** IRSA needs a reasonably recent AWS SDK to pick up the web-identity token. Ancient SDK versions ignore it.
- **One OIDC provider per cluster.** Rebuilding a cluster gives a new OIDC URL, which breaks every trust policy pointing at the old one. Automate it so it regenerates.
- **IRSA vs EKS Pod Identity.** AWS now also offers **EKS Pod Identity**, a newer mechanism that avoids per-cluster OIDC setup and is easier to manage at scale. For new clusters it is worth comparing; IRSA is still the widely-used default.
## 💛 References
- AWS Docs: IAM roles for service accounts: https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html
- AWS Docs: Configure the OIDC provider: https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html
- AWS Docs: EKS Pod Identity (the newer alternative): https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html
