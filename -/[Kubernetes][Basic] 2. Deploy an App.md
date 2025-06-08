# 💚 Reference
[Kubernetes Document](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
# 💚 Objectives
1. Learn about **application Deployments**.

1. Deploy your first app on Kubernetes with `kubectl`.

# 💚 Deployments
## 💛 What is a Deployment?
**A Deployment in Kubernetes is a high-level API object that tells the cluster how to create and update instances of your application (i.e., Pods).**

Think of it as:
> 🧾 A declarative instruction manual for how many copies of your app should run, and how they should be managed over time.

## 💛 Why is it Useful?
- Makes sure the app is running — **always**

- Can **automatically update** your app with zero downtime

- If something crashes, it **heals itself** (no manual restart)

- Works across many computers (Nodes)

## 💛 What Happens If a Pod Dies?
`Kubernetes` says:
> “Oh no! One of the app copies is gone. I’ll make a new one — fast!” 🧑‍🔧
That’s what we mean by **self-healing**.
You don’t need to restart anything. Kubernetes does it for you.
### 🤍 Real-Life Example
Let’s say your app is a coffee machine ☕:
- You want **3 machines** working all the time.

- If 1 machine breaks, you want a **new one installed ****automatically**.

☕☕☕ → ❌☕☕ → ✅☕☕☕
That’s what Kubernetes Deployments do for your app.
## 💛 Summary
✅ You **define **_**what**_** you want**
✅ Kubernetes does the _how_
✅ If something breaks, it _heals itself_
It’s like hiring a smart robot assistant to manage your app!
