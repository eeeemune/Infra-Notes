# 💚 OCI (Open Container Images) and Registriesddd

## 💛 What is OCI?

- **`OCI`** stands for **Open Container Initiative**
- It defines **open standards for container image** formatsdf and runtimes.
- OCI ensures **interoperability** across different tools, platforms, and registries.

## 💛 OCI Images

- OCI images follow a **standardized format** (like Docker images).
- These images include:
    - A **manifest** (describes the image layers),
    - **Configuration** (runtime settings),
    - **Layers** (compressed filesystems),
    - **Signatures** (for trust/security).

## 💛 OCI Registries

- `Registries` store and serve OCI-compliant images.
- Common OCI-compatible registries:
    - **Docker Hub**
    - GitHub Container Registry (`ghcr.io`)
    - Amazon ECR
    - Google Artifact Registry
    - Azure Container Registry
- You can **push and pull Helm charts** and other artifacts (like WASM modules) as OCI objects.

## 💛 Helm + OCI

- Helm 3+ supports **storing charts in OCI registries**.
- Example:
    
    ```bash
    helm chart save ./mychart ghcr.io/myuser/mychart:v1
    helm chart push ghcr.io/myuser/mychart:v1
    helm chart pull ghcr.io/myuser/mychart:v1
    helm chart export ghcr.io/myuser/mychart:v1
    ```
    

### 🤍 Why Use OCI for Helm Charts?

- Versioned and immutable chart storage.
- Uniform tooling and access control across images & charts.
- **Aligns with existing CI/CD pipelines** using OCI tools.

## 💛 References

- [[Open Container Initiative (OCI)](https://opencontainers.org/)](https://opencontainers.org/)
- [[Helm - Working with OCI Registries](https://helm.sh/docs/topics/registries/)](https://helm.sh/docs/topics/registries/)
- [[Docker Distribution Spec](https://github.com/opencontainers/distribution-spec)](https://github.com/opencontainers/distribution-spec)
- [[OCI Image Layout Specification](https://github.com/opencontainers/image-spec/blob/main/image-layout.md)](https://github.com/opencontainers/image-spec/blob/main/image-layout.md)
