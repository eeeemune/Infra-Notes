# Contents
## Docker
### [OCI and Registries]([Docker]%20OCI%20and%20Registries.md)
- 💚 OCI (Open Container Images) and Registries
   - 💛 What is OCI?
   - 💛 OCI Images
   - 💛 OCI Registries
   - 💛 Helm + OCI
      - 🤍 Why Use OCI for Helm Charts?
   - 💛 References


### [How to Sign in Docker with AWS SSO]([Docker]%20How%20to%20Sign%20in%20Docker%20with%20AWS%20SSO.md)
- 💚 Command
- 💚 Explain
   - 💛 Sign in Docker with Terminal
   - 💛 Sign in Docker by AWS Profile
- 💚 Reference
## GitHubActions
### [GitHub Action Runner]([GitHubActions]%20GitHub%20Action%20Runner.md)
- 💚 What is the ‘**runner’**?
   - 💛 GitHub Actions Runner
   - 💛 Where does the **runner** live?
   - 💛 Example

## Kubernetes
### [How to Use Secrets in Kubernetes](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20How%20to%20Use%20Secrets%20in%20Kubernetes.md)
- 💚 How to Use Secrets in Kubernetes
   - 💛 Create a Secret
   - 💛 Check The Secret
      - 🤍 List Up Secrets
      - 🤍 See The Value for Secret
   - 💛 References

### [1. Kubernetes Clusters]([Kubernetes]%201.%20Kubernetes%20Clusters.md)
- 💚 Objectives
- 💚 Control Plane
- 💚 Kubelet
   - 💛 Node-level Component
- 💚 Reference


### [3. Kubernetes Services]([Kubernetes]%203.%20Kubernetes%20Services.md)
- 💚 Kubernetes Services
   - 💛 What is a Service?
   - 💛 Why Use a Service?
   - 💛 Types of Services
      - 🤍 ClusterIP
      - 🤍 NodePort
      - 🤍 LoadBalancer
      - 🤍 ExternalName
   - 💛 How Do Services Know Where to Send Traffic?
      - 🤍 Example: Service with Selector
   - 💛 What if There's No Selector?
   - 🤍 Summary
- Reference


### [2. Deploy an App]([Kubernetes]%202.%20Deploy%20an%20App.md)
- 💚 Reference
- 💚 Objectives
- 💚 Deployments
   - 💛 What is a Deployment?
   - 💛 Why is it Useful?
   - 💛 What Happens If a Pod Dies?
      - 🤍 Real-Life Example
   - 💛 Summary


### [What is The Kubernetes]([Kubernetes]%20What%20is%20The%20Kubernetes.md)
- 💚 Background
   - 💛 Monoliths
      - 🤍 Disadvantages of Monoliths
   - 💛 Microservices
      - 🤍 How to Run Microservices
- 💚 Kubernetes
   - 💛 What is the Kubernetes?
   - 💛 Key Goals
      - 🤍 Maximize Capacity
      - 🤍 Adapt to Demand
      - 🤍 Don’t Go Dark
      - 🤍 Abstraction
   - 💛 Notations
      - 🤍 Pod and Container
      - 🤍 Node and Cluster
   - 💛 Abstracted Infrastructure of Kubernetes
      - 🤍 Why Abstracted Infra is Needed?
      - 🤍 Immutable Template
      - 🤍 Benefits
   - 💛 Self-Healing in Kubernetes
      - 🤍 Ideal State vs Actual State
      - 🤍 Update Mechanisms
      - 🤍 Labels
      - 🤍 Services
- 💚 References


### [What is K3s]([Kubernetes]%20What%20is%20K3s.md)


### [What is Helm]([Kubernetes]%20What%20is%20Helm.md)
- 💚 What is Helm?
   - 💛 Short Answer
   - 💛 Why Use Helm?
   - 💛 What Is a Helm Chart?
      - 🤍 Example:
   - 💛 Helm Workflow
   - 🤍 Summary
## Harbor
### [What is Harbor]([Harbor]%20What%20is%20Harbor.md)
- 💚 Harbor
   - 💛 What is Harbor?
   - 💛 Key Features
      - 🤍 **Stores container images & Helm charts (OCI format)**
      - 🤍 **Controls who can see or change things (RBAC)**
      - 🤍 **Scans for security issues**
      - 🤍 **Signs and verifies images (trust)**
      - 🤍 **Replicates to other registries**
      - 🤍 **Login with your company account (LDAP/AD)**
      - 🤍 **Has a website and API**
   - 💛 How Harbor fits with Helm and OCI
   - 💛 Typical Use Cases
   - 💛 References
## Others
### [How VPN Works](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20VPN%20Works.md)
- 💚 How VPN Works?
   - 💛 What is a VPN?
   - 💛 Why use a VPN?
   - 💛 How VPN changes network behavior
      - 🤍 Networking Concepts Involved
   - 💛 Types of VPNs
   - 💛 What gets affected?
   - 💛 Common VPN Protocols
   - 💛 What does encrypted mean?
   - 💛 Common Use Cases
   - 💛 References
## Network
### [How to Set Up VPN with Wireguard](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Network]%20How%20to%20Set%20Up%20VPN%20with%20Wireguard.md)
- 💚 How to Set Up VPN with Wireguard
   - 💛 Install Wireguard
   - 💛 Generate keys on each machine
   - 💛 Set Up Server
- Client 1
- Client 2
   - 💛 Set Up Client


### [What is NAT](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Network]%20What%20is%20NAT.md)
- 💚 What is NAT?
   - 💛 NAT = Network Address Translation
   - 💛 Why do we need NAT?
   - 💛 How does it work?
      - 🤍 Simple Example
   - 💛 Types of NAT
   - 💛 Where is NAT used?
   - 💛 References
## Linux
### [How to Get My IP on Linux](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Linux]%20How%20to%20Get%20My%20IP%20on%20Linux.md)
- 💚 How to Get My IP on Linux
   - 💛 Public
      - 🤍 IPv6
- 2603:3024:269:2200::bb22
      - 🤍 IPv4
   - 💛 Private
- 10.1.10.198


### [How to Create a New User for SSH](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Linux]%20How%20to%20Create%20a%20New%20User%20for%20SSH.md)
- 💚 How to Create a New User for SSH
   - 💛 1. Add the User
   - 💛 2. Add User to  Group (optional)
   - 💛 3. Create  Folder
   - 💛 4. Add Public SSH Key
   - 💛 5. Test the Login
      - 🤍 Example
   - 💛 References
## GCP
### [How to Create OAuth Client](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GCP]%20How%20to%20Create%20OAuth%20Client.md)
- 💚 How to Create OAuth Client
   - 💛 Reference
   - 💛 Create OAuth Client
      - 🤍 Go to Google Auth Platform → Clients Tab
      - 🤍 Create Client
   - 💛 Save Auth Information
      - 🤍 Download Auth JSON
