# 💚 Objectives
1. Learn what a Kubernetes `cluster` is.

1. Learn what `Minikube` is.

1. Start a Kubernetes cluster on our computer.

# 💚 Control Plane

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7a75158-b9c4-4d57-84fa-9858bfaefc38/81bad1bb-faa6-436d-b589-2d511da84faf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2S4222C%2F20250605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250605T221045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIHUkOjpxuXIQnRw65MzSSTi1NWLZWazDgSBRoj1RiwWOAiBTa1DFAWkVENbBalhzhU8dxcEfJAXZwYeswyFkZBGECyr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMPFsCn1J7%2FGlzqvyBKtwDkA8e%2BmoGap0NbLZgc7ugmUGlXTXKpK66NmU2jswvslQVLgENOFfhGUZy73z83QmUrcD9SpnaoGGIM%2B0NPdz%2BCKYN2GpXptnSgwC8M5op8zhPi0b1dcN17jGUmE2oSoa9FmpNOmeMYGrklTLwPhgfmOr%2F8%2FiPUoclY7YFPBrjJTFQ01TldWP%2BCgoeiXnjzPHaGTGgTUQPu64zIOjDlYi0Ced%2BAa%2Fe4FuCH1EYKE5vV4R%2BqiT8%2Fpz6UgueOu7zJ17JKi5FUkG36lZkJl%2BjgkpH7JgjsPirFnTEdcd51X4ziVXmaN%2BrlkjMsVnQk1hv4BKvpTg%2Br9MGoF1VBSGgeF2mu7PUjdN64%2BFoiyIVDoo0OL8mPj0ipY6PLP41zN%2BetJbMxuQLRLWWem%2FeFJ1t13PMipQjxHvas8NXcK%2BKpHfIayNdkB1BZV54Bmt5%2FjIl3g31xASQyYSZUqLgjAhDhHYj4X%2FyVJzFW%2FLkemO4qZmywCD5Rw1%2FGUJCaKfS4JYDv5Vfe%2FYTYVU5JF3gYa1Pqzicl07oJzSRBZ%2BEetpVUJZxBQo%2FyAUoTq2EQIR2ehxeRyxQEipGuyJrxz1jhjIBmoVjSGCPbkd3eoyDydxw%2FcLYMZpFtucDCOUHKfCIPMgwndiHwgY6pgGMu%2BAE1anhK5cGohHSDJL2cxB9eGJNkCAf1rXqydSEkatEZmaRh2Frggdu0zAYyUdBylzHoWaqO%2FYzRzO29eooV%2B1UWqnKnkGPya0H6SJlCuo9mwCj%2FlRHIjVPV2ndlmDcijoyGawm1y9OLh5EYCNQu7n1yuB%2BD%2BR6IwB%2FIq71kxlAX9Tb4w0F%2BI4wsAT5fjErmEAF7qNGEgsUbCPdP48m9UiLX1ND&X-Amz-Signature=58d51fdc3bf64e0fefe627e78ed3e4d4a0dd4436ef615f0512a804a636ea000e&X-Amz-SignedHeaders=host&x-id=GetObject)

- Each cluster has its `control plane`.

- **Control Planes manage the cluster and the nodes** that are used to host the running applications.

# 💚 Kubelet
- Each node has a `kubelet`

    - A node is a VM or a physical computer
    
- **`Kubelet`**** manages the node and communicate with the kubernetes**

## 💛 Node-level Component

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7a75158-b9c4-4d57-84fa-9858bfaefc38/e04e62e1-8640-4733-ac68-d40576e2180c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2S4222C%2F20250605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250605T221045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIHUkOjpxuXIQnRw65MzSSTi1NWLZWazDgSBRoj1RiwWOAiBTa1DFAWkVENbBalhzhU8dxcEfJAXZwYeswyFkZBGECyr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMPFsCn1J7%2FGlzqvyBKtwDkA8e%2BmoGap0NbLZgc7ugmUGlXTXKpK66NmU2jswvslQVLgENOFfhGUZy73z83QmUrcD9SpnaoGGIM%2B0NPdz%2BCKYN2GpXptnSgwC8M5op8zhPi0b1dcN17jGUmE2oSoa9FmpNOmeMYGrklTLwPhgfmOr%2F8%2FiPUoclY7YFPBrjJTFQ01TldWP%2BCgoeiXnjzPHaGTGgTUQPu64zIOjDlYi0Ced%2BAa%2Fe4FuCH1EYKE5vV4R%2BqiT8%2Fpz6UgueOu7zJ17JKi5FUkG36lZkJl%2BjgkpH7JgjsPirFnTEdcd51X4ziVXmaN%2BrlkjMsVnQk1hv4BKvpTg%2Br9MGoF1VBSGgeF2mu7PUjdN64%2BFoiyIVDoo0OL8mPj0ipY6PLP41zN%2BetJbMxuQLRLWWem%2FeFJ1t13PMipQjxHvas8NXcK%2BKpHfIayNdkB1BZV54Bmt5%2FjIl3g31xASQyYSZUqLgjAhDhHYj4X%2FyVJzFW%2FLkemO4qZmywCD5Rw1%2FGUJCaKfS4JYDv5Vfe%2FYTYVU5JF3gYa1Pqzicl07oJzSRBZ%2BEetpVUJZxBQo%2FyAUoTq2EQIR2ehxeRyxQEipGuyJrxz1jhjIBmoVjSGCPbkd3eoyDydxw%2FcLYMZpFtucDCOUHKfCIPMgwndiHwgY6pgGMu%2BAE1anhK5cGohHSDJL2cxB9eGJNkCAf1rXqydSEkatEZmaRh2Frggdu0zAYyUdBylzHoWaqO%2FYzRzO29eooV%2B1UWqnKnkGPya0H6SJlCuo9mwCj%2FlRHIjVPV2ndlmDcijoyGawm1y9OLh5EYCNQu7n1yuB%2BD%2BR6IwB%2FIq71kxlAX9Tb4w0F%2BI4wsAT5fjErmEAF7qNGEgsUbCPdP48m9UiLX1ND&X-Amz-Signature=6983e15cae8f9c50b81f22ecedd112991562df33535b62c8b4de15a27f7956fd&X-Amz-SignedHeaders=host&x-id=GetObject)

- `Kubelet` is **Node-level Component**

- It **communicates with the control plane using the Kubernetes API**

    - A control plane exposes Kubernetes API
    
    - And each `kubelet` uses these APIs to communicate its with control plane
    
    - We can interact with other clusters by Kubernetes API, through control plane
# 💚 Reference
[Kubernetes Document](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)