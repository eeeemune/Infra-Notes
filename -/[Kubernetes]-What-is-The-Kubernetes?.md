# 💚 Background
## 💛 Monoliths
**Monoliths**

> A **monolith** is a large single block of stone. In software architecture, it refers to a **large, single-tiered application** where all components are tightly coupled and interdependent.
### 🤍 Disadvantages of Monoliths
- **Tight Coupling**

    - **Too many interdependent** parts make the system fragile
    
- **Version Conflicts**

    - Difficult to manage **conflicting library versions**
    
- **Scalability Issues**

    - Cannot scale individual components independently
    
- **Deployment Complexity**

    - Changes require deploying the entire application
    
- **Technology Lock-in**

    - **Hard to adopt new technologies** for specific components
    
## 💛 Microservices
`Microservices` architecture **breaks down a monolithic application into smaller**, independent services that:
- Can be developed, deployed, and scaled independently

- Communicate through well-defined APIs

- Can use different technologies and frameworks

- Are organized around business capabilities

### 🤍 How to Run Microservices
1. **Single OS Deployment**

    - Simplest approach but limited isolation
    
    - Services share OS resources
    
    - **Potential for conflicts and resource contention**
    
1. **Virtual Machine Approach**

    - **Single VM**: All services in one VM
    
        - Better isolation than single OS
        
        - Still potential for conflicts
        
    - **Multiple VMs**: One VM per service
    
        - Complete isolation
        
        - Resource-intensive
        
        - **Higher operational overhead**
        
1. **Kubernetes Solution**

    - **`Containerization`**: Each service **runs in its own container**
    
    - **`Self-contained`**: **Libraries and dependencies are packaged with the service**
    
    - **Benefits**:
    
        - Lightweight compared to VMs
        
        - Consistent environment across development and production
        
        - Easy scaling and management
        
        - Built-in service discovery and load balancing
        
    - **Best Practice**: Each service should be:
    
        - Independently deployable
        
        - Loosely coupled
        
        - Focused on a single business capability
        
# 💚 Kubernetes
## 💛 What is the Kubernetes?
- Kubernetes is for **containerized application**

- It keep **track of micro services automatically**

## 💛 Key Goals
### 🤍 Maximize Capacity
Distribute containers in a logical and efficient way
### 🤍 Adapt to Demand
Scale up/down fast with the ops we have already
### 🤍 Don’t Go Dark
Keep processes continuously running and healthy
### 🤍 Abstraction
- Give us power over **what gets down**

    - without micro-manage ‘how’
    
## 💛 Notations
### 🤍 Pod and Container
**Pod sees container, Kubernetes sees Pods **


![image](https://github.com/user-attachments/assets/4fcd7c38-4342-4592-9184-a79bca2fc3d4)


- `Pods` are **smallest building block** in Kubernetes

    - Contains one or more containers
    
        - **Typically one container**, but it can contain two or more containers when they are highly inter-connencted
        
    - **Containers in a pod share network and storage**
    
    - `Pod` sees the `container` as running applications inside it
    
### 🤍 Node and Cluster
- `Node` means a physical or **virtual machine**

    
![image](https://github.com/user-attachments/assets/ed288e18-7fcf-4648-bee8-dc0420e257c8)


    
    - Runs multiple pods
    
    - **Managed by Kubernetes control plane**
    
- `Cluster` means collection of nodes

    
![image](https://github.com/user-attachments/assets/063d0656-29ca-474d-a227-20a55061f83e)

    
    
    - **Has control plane (master) and worker nodes**
    
    - Control plane manages the entire cluster
    
## 💛 Abstracted Infrastructure of Kubernetes
### 🤍 Why Abstracted Infra is Needed?
- **You don't need to worry about which server your app runs on**

- Same app works on different platforms

    - which can be  AWS, Google Cloud, or your laptop
    
- No need to manually install stuff on each machine

### 🤍 Immutable Template
- Imagine a **recipe** that creates identical copies

- Write YAML file once, use it many times

- Never change running app directly - always use template

### 🤍 Benefits
- **No "it works on my machine" problems**

- Easy to fix - just redeploy from template

- All environments look exactly the same

## 💛 Self-Healing in Kubernetes
Kubernetes ensures that your applications remain available and resilient by **automatically detecting and correcting issues**. Let's explore how this works.
### 🤍 Ideal State vs Actual State
- **`Ideal State`**: The desired configuration we define in `yaml` file (e.g., 3 replicas of a pod).

- **`Actual State`**: The current state of the cluster.

- **Controller Loop**: **Kubernetes continuously compares the actual state to the ideal state** and makes adjustments to reconcile any differences.

### 🤍 Update Mechanisms
- **`Pod Restarts`**

    - If a container crashes, Kubernetes restarts it based on the defined `restartPolicy`.
    
- **`Replica Management`**

    - Controllers like Deployments ensure the **specified number of pod replicas** are running.
    
- **`Node Failures`**

    - If a node goes down, **pods are rescheduled on healthy nodes**.
    
- **`Health Checks`**

    - **Liveness Probes**: Determine if a container is running. If it fails, the container is restarted.
    
    - **Readiness Probes**: Check if a container is ready to serve traffic. If it fails, the pod is removed from service endpoints.
    
    - **Startup Probes**: Verify if an application has started. Useful for applications with long startup times.
    
### 🤍 Labels
Labels are **key-value pairs** attached to Kubernetes resources.
- ✅ They help categorize and organize resources.

- ✅ They're essential for selectors (e.g. Services, Deployments).

_Example:_
```yaml
metadata:
  labels:
    app: my-app
    environment: production

```
This Pod is labeled with `app: my-app` and `environment: production`, making it easy to select and group for services or monitoring.
### 🤍 Services
A **Service** provides a stable IP and DNS name for accessing a group of Pods.
It uses **label selectors** to route traffic only to healthy Pods.
- Automatically load-balances traffic across matching Pods

- If a Pod fails, it is **automatically removed** from the service's endpoints

_Example:_
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376

```
This service routes traffic to any Pod with the label `app: my-app` on port 9376.
**With Labels + Services, Kubernetes can self-heal:**

> - It restarts failed Pods,
> 
> - Removes them from traffic routing,
> 
> - And reschedules them on healthy nodes — automatically!

# 💚 References

[Kubernetes](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

[Google Cloud Comic Book](https://cloud.google.com/kubernetes-engine/kubernetes-comic/)