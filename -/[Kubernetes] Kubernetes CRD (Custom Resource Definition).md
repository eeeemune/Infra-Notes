# 💚 Kubernetes CRD (Custom Resource Definition)

# 💚 Kubernetes CRD (Custom Resource Definition)
## 💛 What is a CRD?
### 🤍 Simple definition
**A Custom Resource Definition (CRD)** lets you extend the Kubernetes API by creating your own resource types.
This means you can create new objects like:
```
kind: MyDatabase
kind: ExternalSecret
kind: KafkaCluster
```
Even though Kubernetes **did not originally support them**.
Basis:
- Kubernetes API is **extensible**
- CRDs allow **custom resources** to behave like native objects (`Pod`, `Service`, `Deployment`)
📎 References
https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
## 💛 Why CRDs exist
### 🤍 The problem they solve
Before CRDs, extending Kubernetes required:
- Writing a **full API server**
- Maintaining it separately
CRDs allow developers to:
✅ Add new resource types
✅ Use `kubectl` with them
✅ Store them in Kubernetes etcd
✅ Manage them like native resources
Example:
```
kubectlget externalsecrets
kubectl describe kafkacluster
```
## 💛 Example CRD in the wild
### 🤍 External Secrets Operator
This project adds a new resource:
```
kind: ExternalSecret
```
Example usage:
```
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secret
spec:
  secretStoreRef:
    name: aws-ssm
  target:
    name: app-secret
```
📌 Basis:
- Kubernetes itself **doesn't know AWS SSM**
- The CRD + controller makes it possible
📎 Ref
https://external-secrets.io/
## 💛 How CRDs actually work
### 🤍 Two main parts
A full extension usually contains:
Example flow:
```
User creates Custom Resource
        ↓
Stored in Kubernetes etcd
        ↓
Controller watches it
        ↓
Controller performs actions
```
📌 Basis:
- CRDs only define **data structure**
- Controllers implement **behavior**
📎 Ref
https://kubernetes.io/docs/concepts/architecture/controller/
## 💛 Example CRD definition
### 🤍 The CRD itself
```
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.example.com
spec:
  group: example.com
  names:
    kind: Database
    plural: databases
  scope: Namespaced
  versions:
    - name: v1
      served: true
      storage: true
```
After installing it:
```
kubectlget databases
```
Now Kubernetes understands the new resource.
📎 Ref
https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
## 💛 Example Custom Resource
### 🤍 A resource created using the CRD
```
apiVersion: example.com/v1
kind: Database
metadata:
  name: prod-db
spec:
  engine: postgres
  size: large
```
📌 Basis:
- This object is stored in etcd
- Controller decides what to do with it
Example actions:
- create RDS
- create StatefulSet
- configure storage
## 💛 Popular Kubernetes tools built on CRDs
### 🤍 Many major projects rely on CRDs
📎 Refs
https://argo-cd.readthedocs.io/
https://cert-manager.io/docs/
https://istio.io/latest/docs/
## 💛 How to see CRDs in your cluster
### 🤍 List all CRDs
```
kubectlget crds
```
Example output:
```
applications.argoproj.io
certificates.cert-manager.io
externalsecrets.external-secrets.io
```
### 🤍 Inspect a CRD
```
kubectl describe crd externalsecrets.external-secrets.io
```
### 🤍 List custom resources
```
kubectlget externalsecrets
```
## 💛 CRD vs Built-in Kubernetes objects
### 🤍 Comparison
## 💛 Mental model (easy 🌱)
### 🤍 Think of CRDs as
Kubernetes **plugin APIs**.
```
Pod
Service
Deployment
      +
CustomResource
```
They allow Kubernetes to become a **platform for building platforms**.
## 💛 Real-world example architecture
### 🤍 AWS Secrets → Kubernetes
```
AWS SSM
   ↓
External Secrets Operator
   ↓
CRD: ExternalSecret
   ↓
Kubernetes Secret
   ↓
Deployment env vars
```
This is why **CRDs are everywhere in modern Kubernetes clusters**.
