# Contents

## AWS
### [AWS Lightsail](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20AWS%20Lightsail.md)
- 💚 AWS Lightsail
   - 💛 What is it?
   - 💛 Why do we need it?
      - 🤍 Real-world use cases
   - 💛 What you get
   - 💛 How does it work?
      - 🤍 Request Flow (typical web app)
      - 🤍 Example: launch via CLI
   - 💛 Lightsail vs EC2
   - 💛 Gotcha
   - 💛 References

### [AWS Savings Plans](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20AWS%20Savings%20Plans.md)
- 💚 AWS Savings Plans
- 💚 AWS Savings Plans
   - 💛 What is it?
   - 💛 Types of Savings Plans
      - 🤍 Compute Savings Plans
      - 🤍 EC2 Instance Savings Plans
   - 💛 Example
      - 🤍 Without Savings Plan
      - 🤍 With Savings Plan (say, 30% discount)
   - 💛 Benefits
   - 💛 References

### [AWS Spot Instance Data Feed](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20AWS%20Spot%20Instance%20Data%20Feed.md)
- 💚 AWS Spot Instance Data Feed
- 💚 AWS Spot Instance Data Feed
   - 💛 What it is
   - 💛 What's in each file
   - 💛 Why we(Chartmetric) need it
   - 💛 Good to know

### [Athena and CUR (AWS Cost and Usage Report)](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20Athena%20and%20CUR%20%28AWS%20Cost%20and%20Usage%20Report%29.md)
- 💚 Athena and CUR (AWS Cost and Usage Report)
   - 💛 What are they?
   - 💛 Why do we need them?
      - 🤍 Real-world use case
   - 💛 How does it work?
      - 🤍 Request Flow
      - 🤍 Example: set up CUR (CLI)
      - 🤍 Example: query costs with Athena (SQL)
   - 💛 Cost gotcha (Athena bills you too)
   - 💛 Gotcha
   - 💛 References

### [How to Block Specific IP Address by AWS WAF](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20How%20to%20Block%20Specific%20IP%20Address%20by%20AWS%20WAF.md)
- 💚 How to Block Specific IP Address by AWS WAF
- 💚 How to Block a Specific IP Address using AWS WAF
   - 💛 What is AWS WAF?
   - 💛 Steps to Block a Specific IP Address
      - 🤍 1. Create an IP Set
      - 🤍 2. Create a Web ACL
      - 🤍 3. Add a Rule to Block IPs
      - 🤍 4. Save and Deploy

### [How to Set Up AWS Resource Notification](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20How%20to%20Set%20Up%20AWS%20Resource%20Notification.md)
- 💚 How to Set Up AWS Resource Notification
- 💚 How to Set Up AWS Resource Notification
   - 💛 Configure AWS Chatbot with Slack
      - 🤍 Subscribe Topics
   - 💛 Create SNS Topic
   - 💛 Amazon EventBridge (Event Detection)

### [How to Test RDS Connection on Mac](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20How%20to%20Test%20RDS%20Connection%20on%20Mac.md)
- 💚 How to Test RDS Connection on Mac
- 💚 How to Test RDS Connection on Mac
   - 💛 Install PostgreSQL
   - 💛 Test
      - 🤍 basic connectivity
      - 🤍 Test with credentials

### [How to connect your terminal to EKS](https://github.com/eeeemune/Infra-Notes/blob/main/-/[AWS]%20How%20to%20connect%20your%20terminal%20to%20EKS.md)
- 💚 How to connect your terminal to EKS
- 💚 How to connect your terminal to EKS
   - 💛 Prerequisites
      - 🤍 Required tools
   - 💛 Steps
      - 🤍 1. Verify AWS access
      - 🤍 2. Generate ‘kubeconfig’ for EKS
      - 🤍 3. Select and check current context
      - 🤍 4. Test


## DB
### [OLTP and OLAP](https://github.com/eeeemune/Infra-Notes/blob/main/-/[DB]%20OLTP%20and%20OLAP.md)
- 💚 OLTP and OLAP
   - 💛 What are they?
   - 💛 Why do we need both?
      - 🤍 Real-world examples
   - 💛 How are they different under the hood?
      - 🤍 Row vs Column storage
      - 🤍 Side by side
   - 💛 How they connect (the pipeline)
      - 🤍 Data Flow
   - 💛 Gotcha
   - 💛 References


## DNS
### [How to Set Certificate with Let’s Encrypt (Via Certbot)](https://github.com/eeeemune/Infra-Notes/blob/main/-/[DNS]%20How%20to%20Set%20Certificate%20with%20Let’s%20Encrypt%20%28Via%20Certbot%29.md)
- 💚 How to Set Certificate with Let’s Encrypt (Via Certbot)
   - 💛 Install Certbot
   - 💛 Get Certificate
   - 💛 Add a Record to the Cloudflare
      - 🤍 Copy the Content
      - 🤍 Go to Cloudflare Dashboard
      - 🤍 Add The Record
   - 💛 (Optional) Configure Traefik to Use the Certificate
      - 🤍 Set the Certificate Key to Proper Path
      - 🤍 (Optional) Check the content looks correct
      - 🤍 Configure Traefik to Use the Certificate

### [What does 'Your connection is not private' mean](https://github.com/eeeemune/Infra-Notes/blob/main/-/[DNS]%20What%20does%20'Your%20connection%20is%20not%20private'%20mean.md)
- 💚 What Does "Your Connection is Not Private" Mean?
   - 💛 What Is SSL?
   - 💛 Why This Error Happens
      - 🤍 1. Expired or invalid SSL certificate
      - 🤍 2. Your computer’s date/time is wrong
      - 🤍 3. Man-in-the-middle (MITM) attack
      - 🤍 4. Untrusted certificate authority (CA)
   - 💛 What You See
   - 💛 Developer Tips
   - 💛 References


## Docker
### [Docker Multi Stage Build](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20Docker%20Multi%20Stage%20Build.md)
- 💚 Docker Multi Stage Build
   - 💛 What is a Dockerfile Stage?
   - 💛 Basic Idea
   - 💛 Basic Syntax
   - 💛 How It Works
   - 💛 Example (Python)
   - 💛 Why Multi-Stage Builds Are Important
   - 💛 Target a Specific Stage
   - 💛 References

### [How to Check Environment Variables in a Docker Container](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20How%20to%20Check%20Environment%20Variables%20in%20a%20Docker%20Container.md)
- 💚 How to Check Environment Variables in a Docker Container
   - 💛 1. While Running a Container
      - 🤍 Option A: Use ‘docker exec’
      - 🤍 Option B: Use a Shell
   - 💛 2. When Creating a Container
   - 💛 3. From ‘docker inspect’
   - 💛 References

### [How to Run a Command on a Docker Image Stored in AWS ECR](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20How%20to%20Run%20a%20Command%20on%20a%20Docker%20Image%20Stored%20in%20AWS%20ECR.md)
- 💚 How to Run a Command on a Docker Image Stored in AWS ECR
   - 💛 Authenticate Docker with ECR
      - 🤍 Example
   - 💛 Pull the Image From ECR
   - 💛 Run the Image With a Command
   - 💛 Start an Interactive Shell

### [How to Sign in Docker with AWS SSO](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20How%20to%20Sign%20in%20Docker%20with%20AWS%20SSO.md)
- 💚 How to Sign in Docker with AWS SSO
- 💚 Command
- 💚 Explain
   - 💛 Sign in Docker with Terminal
   - 💛 Sign in Docker by AWS Profile
- 💚 Reference

### [OCI and Registries](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20OCI%20and%20Registries.md)
- 💚 OCI (Open Container Images) and Registries
   - 💛 What is OCI?
   - 💛 OCI Images
   - 💛 OCI Registries
   - 💛 Helm + OCI
      - 🤍 Why Use OCI for Helm Charts?
   - 💛 References

### [What is Docker Mount](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Docker]%20What%20is%20Docker%20Mount.md)
- 💚 What Is Docker Mount?
   - 💛 Basic Syntax
   - 💛 Example
      - 🤍 What It Means:
   - 💛 Why Use This?
   - 💛 Other Mount Use Cases
   - 💛 Reference


## GCP
### [How to Create OAuth Client](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GCP]%20How%20to%20Create%20OAuth%20Client.md)
- 💚 How to Create OAuth Client
   - 💛 Reference
   - 💛 Create OAuth Client
      - 🤍 Go to Google Auth Platform → Clients Tab
      - 🤍 Create Client
   - 💛 Save Auth Information
      - 🤍 Download Auth JSON


## Git
### [How to Pull a Specific Branch from a Remote Git Repository](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Git]%20How%20to%20Pull%20a%20Specific%20Branch%20from%20a%20Remote%20Git%20Repository.md)
- 💚 How to Pull a Specific Branch from a Remote Git Repository
   - 💛 1. Check Remote Branches
   - 💛 2. Pull a Specific Branch (first time)
   - 💛 3. Pull Updates (branch already exists locally)
   - 💛 Bonus: Just Download Without Switching
   - 💛 References


## GitHub
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
   - 💛 Example Full Setup (Quick Copy)
   - 💛 References

### [How to Use git diff Command](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHub]%20How%20to%20Use%20git%20diff%20Command.md)
- 💚 How to Use git diff Command
   - 💛 What does it do?
   - 💛 Common Usages
      - 🤍 Show unstaged changes (what you've edited but not added)
      - 🤍 Show staged changes (what you've added with `git add`)
      - 🤍 Show everything (staged + unstaged)
   - 💛 Compare Between Branches
   - 💛 Compare Between Commits
   - 💛 See Only File Names (not full diff)
   - 💛 Compare with Remote Branch
   - 💛 References

### [How to post a note](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHub]%20How%20to%20post%20a%20note.md)
- 💚 How to post a note
   - 💛 What is it?
   - 💛 Why do we need it?
   - 💛 How does it work?
      - 🤍 Sensitivity gate
      - 🤍 Example
   - 💛 References

### [How to set a team as Auto-Assigned Reviewers](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHub]%20How%20to%20set%20a%20team%20as%20Auto-Assigned%20Reviewers.md)
   - 💚 How to set a team as Auto-Assigned Reviewers
      - 💛 Make Sure You Have a GitHub Team
      - 💛 Create or Edit a `CODEOWNERS` File
      - 💛 Enable CODEOWNERS Auto-Assignment in Settings
      - 💛 Things to Note


## GitHubActions
### [GitHub Action Runner](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHubActions]%20GitHub%20Action%20Runner.md)
- 💚 What is the ‘**runner’**?
   - 💛 GitHub Actions Runner
   - 💛 Where does the **runner** live?
   - 💛 Example

### [GitHub Actions Runners & ARC Helm Chart](https://github.com/eeeemune/Infra-Notes/blob/main/-/[GitHubActions]%20GitHub%20Actions%20Runners%20&%20ARC%20Helm%20Chart.md)
- 💚 GitHub Actions Runners & ARC Helm Chart
   - 💛 What are GitHub Actions runners?
   - 💛 Why self-host runners?
   - 💛 What is ARC (Actions Runner Controller)?
   - 💛 What is the ARC Helm chart?
      - 🤍 Example
   - 💛 Summary
   - 💛 References


## Harbor
### [How to Check Harbor Connection](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Harbor]%20How%20to%20Check%20Harbor%20Connection.md)
- 💚 How to Check Harbor Connection
   - 💛 Background
   - 💛 How to check
      - 🤍 Command
      - 🤍 Succeed
      - 🤍 Failure

### [What is Harbor](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Harbor]%20What%20is%20Harbor.md)
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


## Kubernetes
### [1. Kubernetes Clusters](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%201.%20Kubernetes%20Clusters.md)
- 💚 Objectives
- 💚 Control Plane
- 💚 Kubelet
   - 💛 Node-level Component
- 💚 Reference

### [2. Deploy an App](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%202.%20Deploy%20an%20App.md)
- 💚 Reference
- 💚 Objectives
- 💚 Deployments
   - 💛 What is a Deployment?
   - 💛 Why is it Useful?
   - 💛 What Happens If a Pod Dies?
      - 🤍 Real-Life Example
   - 💛 Summary

### [3. Kubernetes Services](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%203.%20Kubernetes%20Services.md)
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

### [ArgoCD](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20ArgoCD.md)
- 💚 ArgoCD
   - 💛 What is it?
      - 🤍 The idea
   - 💛 Why do we need it?
      - 🤍 Real-world use case
   - 💛 How does it work?
      - 🤍 Reconcile Flow
      - 🤍 Example: an Application
      - 🤍 Example: CLI
   - 💛 Push vs Pull (why GitOps matters)
   - 💛 Gotcha
   - 💛 References

### [ECS to EKS Migration Guide](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20ECS%20to%20EKS%20Migration%20Guide.md)
- 💚 ECS to EKS Migration Guide
   - 💛 Before You Start…
      - 🤍 Essential Concept
      - 🤍 The Big Picture
      - 🤍 Overal Structure
   - 💛 IAM Setup
      - 🤍 Why Do We Need IAM Roles?
      - 🤍 Cluster Role
      - 🤍 Node Role
      - 🤍 User Access
   - 💛 Creating the EKS Cluster
      - 🤍 The Cluster Itself
      - 🤍 Node Groups
      - 🤍 Essential Add-ons
   - 💛 Networking & Security Groups
      - 🤍 Why This Matters?
      - 🤍 EKS → RDS
      - 🤍 EKS → Redis(ElastiCache)
      - 🤍 ALB → EKS Pods
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
      - 🤍 Create Kubernetes Secrets
      - 🤍 Use Secrets in Deployments
   - 💛 Deploying Applications
      - 🤍 Basic Deployment
      - 🤍 Creating a Service
      - 🤍 Horizontal Pod Autoscaler (HPA)
   - 💛 Redis Configuration
      - 🤍 The Setup
      - 🤍 Define Redis in Environment Config
      - 🤍 Create Redis Clusters
      - 🤍 Connect Pods with Redis
   - 💛 DNS & Traffic Migration
      - 🤍 How Can We Migrate with Zero-Downtime?
      - 🤍 Create DNS Records
      - 🤍 Update CloudFront
      - 🤍 Attach WAF

### [Helm Chart and Release](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20Helm%20Chart%20and%20Release.md)
- 💚 Helm Chart and Release
   - 💛 What is a **Helm Release**?
   - 💛 Example
   - 💛 In Terraform

### [How to Use Secrets in Kubernetes](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20How%20to%20Use%20Secrets%20in%20Kubernetes.md)
- 💚 How to Use Secrets in Kubernetes
   - 💛 Create a Secret
   - 💛 Check The Secret
      - 🤍 List Up Secrets
      - 🤍 See The Value for Secret
   - 💛 References

### [Kubernetes CRD (Custom Resource Definition)](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20Kubernetes%20CRD%20%28Custom%20Resource%20Definition%29.md)
- 💚 Kubernetes CRD (Custom Resource Definition)
- 💚 Kubernetes CRD (Custom Resource Definition)
   - 💛 What is a CRD?
      - 🤍 Simple definition
   - 💛 Why CRDs exist
      - 🤍 The problem they solve
   - 💛 Example CRD in the wild
      - 🤍 External Secrets Operator
   - 💛 How CRDs actually work
      - 🤍 Two main parts
   - 💛 Example CRD definition
      - 🤍 The CRD itself
   - 💛 Example Custom Resource
      - 🤍 A resource created using the CRD
   - 💛 Popular Kubernetes tools built on CRDs
      - 🤍 Many major projects rely on CRDs
   - 💛 How to see CRDs in your cluster
      - 🤍 List all CRDs
      - 🤍 Inspect a CRD
      - 🤍 List custom resources
   - 💛 CRD vs Built-in Kubernetes objects
      - 🤍 Comparison
   - 💛 Mental model (easy 🌱)
      - 🤍 Think of CRDs as
   - 💛 Real-world example architecture
      - 🤍 AWS Secrets → Kubernetes

### [Kubernetes Migration Common Mistakes & Tips](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20Kubernetes%20Migration%20Common%20Mistakes%20&%20Tips.md)
- 💚 Kubernetes Migration Common Mistakes & Tips
   - 💛 Common Mistakes
      - 🤍 Forgetting IAM Policies
      - 🤍 Security Groups Blocking Traffic
      - 🤍 Wrong Target Type
      - 🤍 Pods Can't Resolve DNS
      - 🤍 Updating Immutable Fields
      - 🤍 Not Waiting for DNS Propagation
      - 🤍 Secrets Not Taking Effect
   - 💛 Troubleshooting Guide
      - 🤍 My Pod is ‘Weird’
      - 🤍 I Can't Connect to Database
      - 🤍 Health Check Takes Forever
      - 🤍 My Nodes are Not Scaled
   - 💛 Useful Commands Cheat Sheet
      - 🤍 Cluster Access
      - 🤍 Getting Resources
      - 🤍 Debugging
      - 🤍 Deployments
      - 🤍 Get Secrets
      - 🤍 Troubleshooting Network

### [What is Helm](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20What%20is%20Helm.md)
- 💚 What is Helm?
   - 💛 Short Answer
   - 💛 Why Use Helm?
   - 💛 What Is a Helm Chart?
      - 🤍 Example:
   - 💛 Helm Workflow
   - 🤍 Summary

### [What is K3s](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20What%20is%20K3s.md)

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

### [What is The Kubernetes](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Kubernetes]%20What%20is%20The%20Kubernetes.md)
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


## Linux
### [How to Create a New User for SSH](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Linux]%20How%20to%20Create%20a%20New%20User%20for%20SSH.md)
- 💚 How to Create a New User for SSH
   - 💛 1. Add the User
   - 💛 2. Add User to `sudo` Group (optional)
   - 💛 3. Create `.ssh` Folder
   - 💛 4. Add Public SSH Key
   - 💛 5. Test the Login
      - 🤍 Example
   - 💛 References

### [How to Get My IP on Linux](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Linux]%20How%20to%20Get%20My%20IP%20on%20Linux.md)
- 💚 How to Get My IP on Linux
   - 💛 Public
      - 🤍 IPv6
      - 🤍 IPv4
   - 💛 Private

### [Setting the Root Password for the First Time](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Linux]%20Setting%20the%20Root%20Password%20for%20the%20First%20Time.md)
- 💚 Setting the Root Password for the First Time
   - 💛 Step-by-Step


## Network
### [How to Set Up VPN with Wireguard](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Network]%20How%20to%20Set%20Up%20VPN%20with%20Wireguard.md)
- 💚 How to Set Up VPN with Wireguard
   - 💛 Install Wireguard
   - 💛 Generate keys on each machine
   - 💛 Set Up Server
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


## Others
### [Data Driven Design Pattern](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20Data%20Driven%20Design%20Pattern.md)
- 💚 Data-Driven Design Pattern
   - 💛 What is Data-Driven Design Pattern?
   - 💛 Why Use It?
   - 💛 Example
      - 🤍 Traditional (Hard-coded)
      - 🤍 Data-Driven
   - 💛 Summary

### [How VPN Works](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20VPN%20Works.md)
- 💚 How VPN Works?
   - 💛 What is a VPN?
   - 💛 Why use a VPN?
   - 💛 How VPN changes network behavior
      - 🤍 Networking Concepts Involved
   - 💛 Types of VPNs
   - 💛 What gets affected?
   - 💛 Common VPN Protocols
   - 💛 What does "encrypted" mean?
   - 💛 Common Use Cases
   - 💛 References

### [How to Connect Your EKS Cluster with ClickHouse Cloud](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20to%20Connect%20Your%20EKS%20Cluster%20with%20ClickHouse%20Cloud.md)
- 💚 How to Connect Your Cluster with ClickHouse Cloud
   - 💛 Get Credentials
      - 🤍 Go to ‘Connect’ Tab
      - 🤍 Get Credentials
   - 💛 Allow EKS IP Access
      - 🤍 Go to Settings → IP Access List
      - 🤍 Add Your Node IP Address

### [How to Connect a Slack App](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20to%20Connect%20a%20Slack%20App.md)
- 💚 How to Connect a Slack App
   - 💛 Create a Slack Incoming Webhook
   - 💛 Enable Socket Mode
   - 💛 Add a Coolify Webhook Trigger
      - 🤍 Configure a Webhook
      - 🤍 Set the Webhook to Your Application

### [How to Forward Router Port](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20to%20Forward%20Router%20Port.md)
- 💚 How to Forward Router Port
   - 💛 Access Router Admin Console
   - 💛 Port Forwarding
      - 🤍 Go to the Port Forwarding Tab
      - 🤍 Add Service

### [How to Get HTTP Certificate](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20How%20to%20Get%20HTTP%20Certificate.md)
- 💚 How to Get HTTP Certificate
   - 💛 Install Nginx and Certbot
   - 💛 Configure Nginx as reverse proxy
   - 💛 Enable the site
   - 💛 Obtain SSL certificate
   - 💛 Enable auto-renual

### [Next.js Build → Docker Build](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20Next.js%20Build%20→%20Docker%20Build.md)
- 💚 Next.js Build → Docker Build
   - 💛 What You Deploy in Next.js?
   - 💛 Option 1: Standard Deployment (Node Server)
   - 💛 Option 2: Standalone Mode (Best for Docker)
   - 💛 What You Get
      - 🤍 .next/standalone/
      - 🤍 .next/static/
   - 💛 Docker Deployment
      - 🤍 Example Dockerfile
   - 💛 Why Standalone is Awesome
   - 💛 Key Insight
   - 💛 Production Best Practice
   - 💛 References

### [What does ‘next build’ do](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Others]%20What%20does%20‘next%20build’%20do.md)
- 💚 What does ‘next build’ do?
   - 💛 Short Answer
   - 💛 What Happens During Build?
      - 🤍 1. Compile
      - 🤍 2. Bundle
      - 🤍 3. Pre-render
      - 🤍 4. Optimize
   - 💛 Final Output: .next Directory
   - 💛 .next Structure
      - 🤍 1. Server Side Code
      - 🤍 2. Static Files
      - 🤍 3. Build Manifest
      - 🤍 4. Routes Manifest
      - 🤍 5. Prerender Manifest
      - 🤍 6. Required Server Files
      - 🤍 7. Cache
      - 🤍 8. Standalone Output (Optional)
   - 💛 Example Full Structure
   - 💛 Runtime Flow Example
   - 💛 References


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
   - 💛 References


## Terraform
### [Add a New GitHub Member with Terraform](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Terraform]%20Add%20a%20New%20GitHub%20Member%20with%20Terraform.md)
- 💚 Add a New GitHub Member with Terraform
   - 💛 Go to the Files
   - 💛 Add a New Member
   - 💛 Apply Terraform
   - 💛 Commit the Change & Create a PR

### [Terraform Provider for Helm](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Terraform]%20Terraform%20Provider%20for%20Helm.md)
- 💚 Terraform Provider for Helm
   - 💛 What is the Terraform Provider for Helm?
      - 🤍 Helm Chart
      - 🤍 What it does
      - 🤍 Why use it?
   - 💛 Basic Example

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


## Terrraform
### [Terraform Module](https://github.com/eeeemune/Infra-Notes/blob/main/-/[Terrraform]%20Terraform%20Module.md)
- 💚 Terraform Module
   - 💛 What is a Module?
   - 💛 Basic Structure
   - 💛 Example
      - 🤍 Configure the Module
      - 🤍 Use the Module
   - 💛 Module Source Types
      - 🤍 Local Module
      - 🤍 GitHub Module
      - 🤍 Terraform Registry
   - 💛 Best Practices
   - 💛 References


## TroubleShootings
### [docker-entrypoint.sh: exec format error](https://github.com/eeeemune/Infra-Notes/blob/main/-/[TroubleShootings]%20docker-entrypoint.sh:%20exec%20format%20error.md)
- 😵 Error Situation
   - Error Message
- 🤔 Why was it Happened?
   - Reason
      - The problematic code
- 😋 Solution

