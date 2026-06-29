# 💚 AWS Savings Plans

# 💚 AWS Savings Plans
## 💛 What is it?
AWS **Savings Plans** is a flexible pricing model that helps you save money on AWS compute usage.
You commit to a certain **amount of usage ($/hour)** for **1 or 3 years**, and in return, AWS gives you lower prices (discounts up to ~72%) compared to On-Demand pricing.
## 💛 Types of Savings Plans
### 🤍 Compute Savings Plans
- Most flexible.
- Applies automatically to **any compute service**:
  - EC2 (any instance family, region, OS, tenancy)
  - Fargate
  - Lambda
- Example
  - If you commit to **$10/hour**, AWS gives you the discounted rate across all your compute usage.
  - Even if you switch from EC2 in `us-east-1` to Fargate in `us-west-2`, the plan still applies.
### 🤍 EC2 Instance Savings Plans
- More restrictive but **cheaper than Compute plan**.
- Discount applies to a specific **instance family in a specific region**.
- Example:
Commit to `m5` in `us-east-1`.
You can change size (`m5.large` → `m5.2xlarge`), OS, and tenancy — but not family or region.
## 💛 Example
### 🤍 Without Savings Plan
- 100 hours of `t3.medium` at $0.0416/hour = **$4.16**
### 🤍 With Savings Plan (say, 30% discount)
- Same usage = **$2.91**
- If you don’t use your full commitment (say, you only use $8/hour out of a $10/hour plan) → **you still pay $10/hour.**
## 💛 Benefits
- Save money (up to ~72%).
- Flexibility (especially with Compute Plans).
- Simple billing — discounts apply automatically.
## 💛 References
- AWS Savings Plans Overview
- Compute vs EC2 Instance Savings Plans
