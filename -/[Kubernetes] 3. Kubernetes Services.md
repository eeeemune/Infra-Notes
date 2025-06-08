# 💚 Kubernetes Services
## 💛 What is a Service?

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7a75158-b9c4-4d57-84fa-9858bfaefc38/ec9eb857-b11a-41e8-8109-368a37c901f3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKZSSET6%2F20250606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250606T014332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIB0QMb%2B9f7hqZsq%2BdmeT9FVAFHskrWooScOtEO94uEEyAiB5KUfeYf9c1%2FU3siOuHQbw6w%2BhStq9DPr5ZRMEtF22qir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM1SFLVwRxri1rfDKUKtwDl9ik636zIbE7qLLBvEXWgT7f4wLTOj%2FwAl1AkXa3KqnORzqhtghQ7P2bpT8OTA68dZ4TWdVKVDqsPoE9mRZTc5AL7tYSUeqJwmZWkUI7zpvfnK9DcCV%2B6%2Bxi%2FtjhLOFV50Ey0xFMkmrqixOhpJiyLt4u%2F01mX8Fvj8aW4UZ1eUw8a0pQKH2e06amf1PDu%2Fql7YVGs1%2FrA%2FC%2FnvGVD6FFnMyVSzAE078t%2Fn0gLNqy0LjM6Y686HX7HlpxgtvCG9C6txba%2Bs%2BcJAuBiELJM3qfe%2FSI6ymB2blkLcxRP%2FNfF%2BL6Ahhdq590EVse5dEofMRsjpL3%2BZ1oreizCwxfVyxal4NmJl83xAYV0mNAmHHw%2Fvg8DMkGh%2FM78sfGhl4PKXZuieDEQGyw%2FMCo7HyBbjiau%2FdUVZ%2FgZ5HCqJGX93%2FQqOHlOUXGXXdIe%2BorFEl6vFfH5GnMGcAjxXgl39yrzzCiQoKY1NdnbEJ7uvqIE%2BEsCvM00vjApqc369A%2F7tb25YtXkpx%2FlAQaTBLSz25oz%2BJ3u%2FAxSjV63LCvCNv1RZPyNDx6WeVFii1B%2BINmUjySQidIk6GEgSP%2F9cUcpEfoCwJaVd3CBIBGFHUGVOUcX07tMwHcR3NTBRXPyO0E%2BJYwwP2IwgY6pgH4LFdGFiOFoeqBzduvJzTIkEm3dIQjRmbKXR7U5NgbaYvuDq4%2FuRbVj6UqmXUwKh8odulDTP%2FEsg7jKUGYSHbSp6w6BQf3RedGyuSepcMFEAO3R%2FuWwZmci6UIKoerDGKGlrDR3WAU%2B%2BqJ6TkW%2BN7rtG4MSZofkd3YXXZVUNsbj0QzMofeF6%2FqYsmnyekh1GPtLmZ0eCzADdycmu29Jx%2FiJW1PiaRq&X-Amz-Signature=a796bf4907ad9d0bf30bcdf852c33c5bc5669404bf77a9f2b1440253210ac5c2&X-Amz-SignedHeaders=host&x-id=GetObject)

`Pod`s in Kubernetes are **temporary** — they can be created and destroyed at any time. For example:
- If a Node crashes, the Pods on it disappear.

- The cluster might create **new Pods** elsewhere to keep things running.

But here’s the problem:
👉 Every Pod has a **different IP address**, so how can other apps or users keep track?
💡 **That’s why we need a Service!**
A **`Service`** is like a **stable doorway** to a group of Pods.
Even if the Pods come and go, the Service stays the same.
## 💛 Why Use a Service?
**A Service is how people or apps find and talk to your app — even if it moves around!**

1.  Service **routes traffic** to the right Pods

    - even if they restart or move
    
1. It **discovers** and tracks healthy Pods

1. It **exposes** your app to the world!

## 💛 Types of Services
You can **expose your app in different ways** using the `type` field in the Service definition:
### 🤍 ClusterIP
- **Default**

- Only reachable **inside the cluster**

- Great for internal services (e.g. backend)

### 🤍 NodePort
- Exposes your app to the **outside world** using `NodeIP:NodePort`

- Adds a public port to each Node

### 🤍 LoadBalancer
- Works in cloud environments (like GCP, AWS)

- **Creates an external load balancer** with a real public IP

### 🤍 ExternalName
- Doesn’t route traffic — instead, maps the Service to a DNS name (like `my-db.company.com`)

- Useful for connecting to things **outside** the cluster

## 💛 How Do Services Know Where to Send Traffic?
They use **`Labels`**! 🏷️
- Each Pod has labels like `app: my-app`, `tier: backend`

- The Service has a **selector** that says:
“Send traffic to Pods with label `app: my-app`”

### 🤍 Example: Service with Selector
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080

```
This sends traffic from `my-service:80` to all Pods labeled `app: my-app` on port `8080`.
## 💛 What if There's No Selector?
If you don’t include a selector, you can:
- Manually define endpoints (for advanced setups)

- Or use `type: ExternalName` to connect to something outside the cluster

## 🤍 Summary
✅ Services give your app a **stable connection point**
✅ They **balance traffic** between Pods
✅ They **keep things running** even when Pods change

# Reference
<details>
<summary>https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/#overview-of-kubernetes-services</summary>

Kubernetes [[Pods](https://kubernetes.io/docs/concepts/workloads/pods/)](https://kubernetes.io/docs/concepts/workloads/pods/) are mortal. Pods have a [[lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/). **When a worker node dies, the Pods running on the Node are also lost.** A [[Replicaset](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) might then dynamically drive the cluster back to the desired state via the creation of new Pods to keep your application running. As another example, consider an image-processing backend **with 3 replicas**. Those replicas are exchangeable; the front-end system should not care about backend replicas or even if a Pod is lost and recreated. That said, **each Pod in a Kubernetes cluster has a unique IP address**, even Pods on the same Node, so there needs to be a way of automatically reconciling changes among Pods so that your applications continue to function.

***A*** `Kubernetes Service` ***is an abstraction layer which defines a logical set of Pods and enables external traffic exposure, load balancing and service discovery for those Pods.***

A [`[Service](https://kubernetes.io/docs/concepts/services-networking/service/)`](https://kubernetes.io/docs/concepts/services-networking/service/) in Kubernetes is an abstraction which defines a **logical set of Pods and a policy** by which to access them. Services enable a loose coupling between dependent Pods. **A Service is defined using YAML or JSON**, like all Kubernetes object manifests. The set of Pods targeted by a Service is **usually determined by a *label selector*** (see below for why you might want a Service without including a `selector` in the spec).

Although each Pod has a unique IP address, those **IPs are not exposed outside the cluster without a Service**. **Services allow your applications to receive traffic**. **Services can be exposed in different ways** by specifying a `type` in the `spec` of the Service:

- `*ClusterIP*` (default) - Exposes the Service on an internal IP in the cluster. This type makes the Service **only reachable from within the cluster**.
- `*NodePort*` - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using `NodeIP:NodePort`. Superset of ClusterIP.
- `*LoadBalancer*` - Creates an **external load balancer** in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.
- `*ExternalName*` - Maps the Service to the contents of the `externalName` field (e.g. `foo.bar.example.com`), by returning a `CNAME` record with its value. No proxying of any kind is set up. This type requires v1.7 or higher of `kube-dns`, or CoreDNS version 0.0.8 or higher.

More information about the different types of Services can be found in the [[Using Source IP](https://kubernetes.io/docs/tutorials/services/source-ip/)](https://kubernetes.io/docs/tutorials/services/source-ip/) tutorial. Also see [[Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)](https://kubernetes.io/docs/tutorials/services/connect-applications-service/).

Additionally, note that there are some use cases with Services that involve not defining a `selector` in the spec. A Service created without `selector` will also not create the corresponding Endpoints object. This allows users to manually map a Service to specific endpoints. Another possibility why there may be no selector is you are strictly using `type: ExternalName`.

</details>

<details>

<summary>https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/#services-and-labels</summary>

A **Service routes traffic across a set of Pods**. Services are the abstraction that allows pods to die and replicate in Kubernetes without impacting your application. Discovery and **routing among dependent Pods** (such as the frontend and backend components in an application) are handled by Kubernetes Services.

`Services` **match a set of Pods using [[labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)**, a grouping primitive that allows logical operation on objects in Kubernetes. Labels are key/value pairs attached to objects and can be used in any number of ways:

- **Designate objects** for development, test, and production
- Embed **version tags**
- **Classify an object** using tags

</details>
