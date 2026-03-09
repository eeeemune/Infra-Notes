# Contents
## Docker
### [Docker Multi Stage Build](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20Docker%20Multi%20Stage%20Build.md)
- 💚 Docker Multi Stage Build
   - 💛 What is a Dockerfile Stage?
   - 💛 Basic Idea
   - 💛 Basic Syntax
- Builder Stage
- Runner Stage
   - 💛 How It Works
   - 💛 Example (Python)
   - 💛 Why Multi-Stage Builds Are Important
   - 💛 Target a Specific Stage
   - 💛 References


### [How to Run a Command on a Docker Image Stored in AWS ECR](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20How%20to%20Run%20a%20Command%20on%20a%20Docker%20Image%20Stored%20in%20AWS%20ECR.md)
- 💚 How to Run a Command on a Docker Image Stored in AWS ECR
   - 💛 Authenticate Docker with ECR
      - 🤍 Example
   - 💛 Pull the Image From ECR
   - 💛 Run the Image With a Command
   - 💛 Start an Interactive Shell


### [What is Docker Mount](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20What%20is%20Docker%20Mount.md)
- 💚 What Is Docker Mount?
   - 💛 Basic Syntax
   - 💛 Example
      - 🤍 What It Means:
   - 💛 Why Use This?
   - 💛 Other Mount Use Cases
   - 💛 Reference


### [How to Check Environment Variables in a Docker Container](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20How%20to%20Check%20Environment%20Variables%20in%20a%20Docker%20Container.md)
- 💚 How to Check Environment Variables in a Docker Container
   - 💛 1. While Running a Container
      - 🤍 Option A: Use ‘docker exec’
      - 🤍 Option B: Use a Shell
- or
- or
   - 💛 2. When Creating a Container
   - 💛 3. From ‘docker inspect’
   - 💛 References


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
### [How to Configure GitHub on Your Terminal](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHub]%20How%20to%20Configure%20GitHub%20on%20Your%20Terminal.md)
- 💚 How to Configure Git on Your Terminal
   - 💛 1. Set Your Identity (Required)
   - 💛 2. Check Your Config
   - 💛 3. Set Credential Helper (avoid typing password/PAT every time)
      - 🤍 macOS
      - 🤍 Linux (simple store)
   - 💛 4. Set Editor (Optional)
      - 🤍 Vim
   - 💛 5. Enable Colored Output (Pretty UI)
   - 💛 7. Setup SSH Instead of Password
- Hi eeeemune! You've successfully authenticated, but GitHub does not provide shell access.
   - 💛 Example Full Setup (Quick Copy)
   - 💛 References


### [How to set a team as Auto-Assigned Reviewers](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHub]%20How%20to%20set%20a%20team%20as%20Auto-Assigned%20Reviewers.md)
   - 💚 How to set a team as Auto-Assigned Reviewers
      - 💛 Make Sure You Have a GitHub Team
      - 💛 Create or Edit a  File
- All  files will be reviewed by the backend team
- All files in the frontend folder will be reviewed by the frontend team
      - 💛 Enable CODEOWNERS Auto-Assignment in Settings
      - 💛 Things to Note


### [How to Pull a Specific Branch from a Remote Git Repository](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Git]%20How%20to%20Pull%20a%20Specific%20Branch%20from%20a%20Remote%20Git%20Repository.md)
- 💚 How to Pull a Specific Branch from a Remote Git Repository
   - 💛 1. Check Remote Branches
   - 💛 2. Pull a Specific Branch (first time)
   - 💛 3. Pull Updates (branch already exists locally)
   - 💛 Bonus: Just Download Without Switching
   - 💛 References


### [How to Use git diff Command](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHub]%20How%20to%20Use%20git%20diff%20Command.md)
- 💚 How to Use git diff Command
   - 💛 What does it do?
   - 💛 Common Usages
      - 🤍 Show unstaged changes (what you've edited but not added)
      - 🤍 Show staged changes (what you've added with )
      - 🤍 Show everything (staged + unstaged)
   - 💛 Compare Between Branches
   - 💛 Compare Between Commits
   - 💛 See Only File Names (not full diff)
   - 💛 Compare with Remote Branch
   - 💛 References


### [GitHub Action Runner]([GitHubActions]%20GitHub%20Action%20Runner.md)
- 💚 What is the ‘**runner’**?
   - 💛 GitHub Actions Runner
   - 💛 Where does the **runner** live?
   - 💛 Example

## Kubernetes
### [What is Karpenter](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20What%20is%20Karpenter.md)
- 💚 What is Karpenter?
   - 💛 Karpenter
   - 💛 Why Do We Need It?
   - 💛 How It Works
      - 🤍 Flow
   - 💛 What Makes Karpenter Special?
      - 🤍 Traditional Cluster Autoscaler
      - 🤍 Karpenter
   - 💛 Simple Config Example
   - 💛 References


### [Helm Chart and Release](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20Helm%20Chart%20and%20Release.md)
- 💚 Helm Chart and Release
   - 💛 What is a **Helm Release**?
   - 💛 Example
   - 💛 In Terraform


### [ECS to EKS Migration Guide](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20ECS%20to%20EKS%20Migration%20Guide.md)
- 💚 ECS to EKS Migration Guide
   - 💛 Before You Start…
      - 🤍 Essential Concept
      - 🤍 The Big Picture
      - 🤍 Overal Structure
   - 💛 IAM Setup
      - 🤍 Why Do We Need IAM Roles?
      - 🤍 Cluster Role
- iam.tf
- Create the role
- Attach the required policy
      - 🤍 Node Role
- Create the role
- Nodes need THREE policies:
      - 🤍 User Access
- Import your IAM user
- Add yourself to the cluster's access list
- Give yourself admin permissions
   - 💛 Creating the EKS Cluster
      - 🤍 The Cluster Itself
- cluster.tf
      - 🤍 Node Groups
      - 🤍 Essential Add-ons
- DNS for service discovery (pods find each other by name - like a dns server in K8s)
- Networking (assigns IPs to pods)
- Network routing
- Metrics (needed for auto-scaling)
   - 💛 Networking & Security Groups
      - 🤍 Why This Matters?
      - 🤍 EKS → RDS
      - 🤍 EKS → Redis(ElastiCache)
      - 🤍 ALB → EKS Pods
- First, create a security group for the ALB
- Then allow ALB to reach EKS nodes
   - 💛 Load Balancer
      - 🤍 Create the ALB
      - 🤍 Create HTTPS Listener
      - 🤍 Create Target Groups
      - 🤍 Create Listener Rules
      - 🤍 Connect ALB to EKS (TargetGroupBinding)
   - 💛 Managing Secrets
      - 🤍 Background - The Problem
      - 🤍 Variable Flows
      - 🤍 Fetch Secrets from SSM by Terraform
- Get all parameters under /chartmetric/shared/
- Get environment-specific parameters
      - 🤍 Create Kubernetes Secrets
      - 🤍 Use Secrets in Deployments
- In your deployment spec:
- This value will WIN over anything in api-secrets
- This loads from secrets (but env above takes precedence)
   - 💛 Deploying Applications
      - 🤍 Basic Deployment
      - 🤍 Creating a Service
      - 🤍 Horizontal Pod Autoscaler (HPA)
   - 💛 Redis Configuration
      - 🤍 The Setup
      - 🤍 Define Redis in Environment Config
- environments.tf
      - 🤍 Create Redis Clusters
- redis.tf
      - 🤍 Connect Pods with Redis
- In deployment spec:
   - 💛 DNS & Traffic Migration
      - 🤍 How Can We Migrate with Zero-Downtime?
      - 🤍 Create DNS Records
      - 🤍 Update CloudFront
      - 🤍 Attach WAF


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
### [How to Check Harbor Connection](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Harbor]%20How%20to%20Check%20Harbor%20Connection.md)
- 💚 How to Check Harbor Connection
   - 💛 Background
   - 💛 How to check
      - 🤍 Command
      - 🤍 Succeed
      - 🤍 Failure


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
### [Data Driven Design Pattern](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20Data%20Driven%20Design%20Pattern.md)
- 💚 Data-Driven Design Pattern
   - 💛 What is Data-Driven Design Pattern?
   - 💛 Why Use It?
   - 💛 Example
      - 🤍 Traditional (Hard-coded)
      - 🤍 Data-Driven
   - 💛 Summary


### [How to Connect a Slack App](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20to%20Connect%20a%20Slack%20App.md)
- 💚 How to Connect a Slack App
   - 💛 Create a Slack Incoming Webhook
   - 💛 Enable Socket Mode
   - 💛 Add a Coolify Webhook Trigger
      - 🤍 Configure a Webhook
      - 🤍 Set the Webhook to Your Application


### [How to Get HTTP Certificate](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20to%20Get%20HTTP%20Certificate.md)
- 💚 How to Get HTTP Certificate
   - 💛 Install Nginx and Certbot
   - 💛 Configure Nginx as reverse proxy
- /etc/nginx/sites-available/mcp
   - 💛 Enable the site
   - 💛 Obtain SSL certificate
   - 💛 Enable auto-renual


### [How to Connect a Slack App](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20to%20Connect%20a%20Slack%20App.md)
- 💚 How to Connect a Slack App
   - 💛 Create a Slack Incoming Webhook
   - 💛 Enable Socket Mode
   - 💛 Add a Coolify Webhook Trigger
      - 🤍 Configure a Webhook
      - 🤍 Set the Webhook to Your Application

- 💚 How to Connect a Slack App
- 💚 How to Connect a Slack App
   - 💛 Create a Slack Incoming Webhook
   - 💛 Enable Socket Mode
   - 💛 Add a Coolify Webhook Trigger
      - 🤍 Configure a Webhook
      - 🤍 Set the Webhook to Your Application

   - 💛 Create a Slack Incoming Webhook
   - 💛 Enable Socket Mode
   - 💛 Add a Coolify Webhook Trigger
      - 🤍 Configure a Webhook
      - 🤍 Set the Webhook to Your Application


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
### [Setting the Root Password for the First Time](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Linux]%20Setting%20the%20Root%20Password%20for%20the%20First%20Time.md)
- 💚 Setting the Root Password for the First Time
   - 💛 Step-by-Step


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
## Python
### [How to Use Poetry](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Python]%20How%20to%20Use%20Poetry.md)
- 💚 How to Use Poetry
   - 💛 What is Poetry?
   - 💛 Quick Start
      - 🤍 1. Install Poetry
      - 🤍 2. Create a New Project
      - 🤍 3. Add Dependencies
      - 🤍 4. Install Everything (existing project)
      - 🤍 5. Run Commands Inside Environment
      - 🤍 6. Update Dependencies
      - 🤍 7. Check Dependency Graph
      - 🤍 8. Publish Your Package
   - 💛 Useful Extras
   - 💛 Workflow Example


### [How to Use requirements in Python](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Python]%20How%20to%20Use%20requirements%20in%20Python.md)
- 💚 How to Use requirements.txt in Python
   - 💛 What is requirements.txt?
   - 💛 Install Packages from requirements.txt
   - 💛 Create Your Own requirements.txt
   - 💛 4. Use with Virtual Environments
   - 💛 Best Practices
- Web framework
   - 💛 References
## DNS
### [What does 'Your connection is not private' mean](https://github.com/eeeemune/Infra-Notes/blob/main/-/[DNS]%20What%20does%20'Your%20connection%20is%20not%20private'%20mean.md)
- 💚 What Does Your Connection is Not Private Mean?
   - 💛 What Is SSL?
   - 💛 Why This Error Happens
      - 🤍 1. Expired or invalid SSL certificate
      - 🤍 2. Your computer’s date/time is wrong
      - 🤍 3. Man-in-the-middle (MITM) attack
      - 🤍 4. Untrusted certificate authority (CA)
   - 💛 What You See
   - 💛 Developer Tips
   - 💛 References
## Terraform
### [Add a New GitHub Member with Terraform](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Terraform]%20Add%20a%20New%20GitHub%20Member%20with%20Terraform.md)
- 💚 Add a New GitHub Member with Terraform
   - 💛 Go to the Files
- teams.terraform → defines GitHub teams
- membership.terraform → defines who’s in each team
   - 💛 Add a New Member
- membership.tf  
   - 💛 Apply Terraform
   - 💛 Commit the Change & Create a PR
## TroubleShootings
### [docker-entrypoint.sh: exec format error](https://github.com/eeeemune/Infra-Notes/blob/main/-/%5BTroubleShootings%5D%20docker-entrypoint.sh%3A%20exec%20format%20error.md)

### [Terraform Tutorial](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Terraform]%20Terraform%20Tutorial.md)
- 💚 Terraform Tutorial
   - 💛 What is Terraform?
      - 🤍 Example
   - 💛 Terraform Workflow
   - 💛 Core Concepts
   - 💛 Variables & Outputs
      - 🤍 variables.tf
      - 🤍 main.tf
      - 🤍 outputs.tf
   - 💛 State Management
   - 💛 Modules
      - 🤍 Example
   - 💛 Best Practices
   - 💛 References
## AWS
### [How to connect your terminal to EKS](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20How%20to%20connect%20your%20terminal%20to%20EKS.md)
- 💚 How to connect your terminal to EKS
   - 💛 Prerequisites
      - 🤍 Required tools
   - 💛 Steps
      - 🤍 1. Verify AWS access
      - 🤍 2. Generate ‘kubeconfig’ for EKS
- Real example
      - 🤍 3. Select and check current context
      - 🤍 4. Test
## Terrraform
### [Terraform Module](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Terrraform]%20Terraform%20Module.md)
- 💚 Terraform Module
   - 💛 What is a Module?
   - 💛 Basic Structure
   - 💛 Example
      - 🤍 Configure the Module
- variables.tf (input)
- main.tf
- outputs.tf (output)
      - 🤍 Use the Module
   - 💛 Module Source Types
      - 🤍 Local Module
      - 🤍 GitHub Module
      - 🤍 Terraform Registry
   - 💛 Best Practices
   - 💛 References
