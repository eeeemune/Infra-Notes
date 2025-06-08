# 💚 Harbor

## 💛 What is Harbor?

`Harbor` is an **open-source OCI-compliant container registry** that stores, signs, and scans container images for vulnerabilities. It **extends the Docker Distribution** (registry) by adding essential features for enterprise use.

## 💛 Key Features

### 🤍 **Stores container images & Helm charts (OCI format)**

**You can push your app's Docker image** or Helm chart into Harbor, just like uploading a file to Google Drive.

*Example: `docker push harbor.mycompany.com/my-app:1.0`*

### 🤍 **Controls who can see or change things (RBAC)**

<aside>

**Role Based Access Control**

A.K.A RBAC, Controls who can see or change things 

</aside>

Only people with the right permission can access certain projects.

### 🤍 **Scans for security issues**

Harbor checks your image for known vulnerabilities using tools like `Trivy`.

*Example: You upload `backend-app:2.1`, and **Harbor warns** **you** that it contains an old library with a security hole.*

### 🤍 **Signs and verifies images (trust)**

Harbor can **sign** images, so others know they are safe and haven’t been tampered with.

*Example: Only images signed by your DevOps team can be used in production.*

### 🤍 **Replicates to other registries**

**Harbor can copy images to or from other places** like AWS ECR or another Harbor.

*Example: Automatically send new images to a backup registry in another region.*

### 🤍 **Login with your company account (LDAP/AD)**

You can log into Harbor using your company email and password — no need to make a new account.

### 🤍 **Has a website and API**

You can see everything in a web UI, or automate stuff using code (API).

## 💛 How Harbor fits with Helm and OCI

- You can **store and pull Helm charts** in OCI format from Harbor.
- Helm 3.7+ supports `helm push` and `helm pull` for charts in OCI-compliant registries, including Harbor.
- Useful for **private chart distribution** and **secure internal deployments**.

## 💛 Typical Use Cases

- Secure **internal registry for Kubernetes** applications
- Air-gapped environments
- Managing container images and Helm charts at scale
- Enterprise-grade access control and auditing

## 💛 References

- [[Harbor - Official Site](https://goharbor.io/)](https://goharbor.io/)
- [[Harbor Documentation](https://goharbor.io/docs)](https://goharbor.io/docs)
- [[Harbor GitHub Repo](https://github.com/goharbor/harbor)](https://github.com/goharbor/harbor)
