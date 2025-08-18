# 💚 Terraform Tutorial

## 💛 What is Terraform?

<aside>

**Terraform**

Infrastructure as Code (IaC) tool

</aside>

- Lets you **define, change, and destroy infrastructure with code**.
- Works with many `providers`
    - AWS, GCP, Azure, Kubernetes, Helm, etc.

### 🤍 Example

Instead of clicking AWS Console, you can write code:

```hcl
resource "aws_s3_bucket" "example" {
  bucket = "my-terraform-bucket"
}
```

## 💛 Terraform Workflow

<aside>

1. **Write**
    - Create `.tf` files
        - resources, providers, variables
2. **Init**
    1. Run `terraform init` to download providers.
3. **Plan**
    1. Run `terraform plan` to preview changes.
4. **Apply**
    1. Run `terraform apply` to execute changes.
</aside>

## 💛 Core Concepts

- **Provider** → Plugin that talks to a service (e.g., `aws`, `azurerm`, `google`).
- **Resource** → Infrastructure object (VM, DB, S3 bucket).
- **Data Source** → Fetch existing infra info (e.g., existing VPC).
- **Variables** → Inputs (e.g., region, instance size).
- **Output** → Show values after apply (e.g., instance IP).
- **State** → Terraform keeps track of real resources in `terraform.tfstate`.
- **Module** → Reusable Terraform code.

## 💛 Variables & Outputs

### 🤍 variables.tf

```hcl
variable "region" {
  default = "us-west-2"
}
```

### 🤍 main.tf

```hcl
provider "aws" {
  region = var.region
}
```

### 🤍 outputs.tf

```hcl
output "bucket_name" {
  value = aws_s3_bucket.example.bucket
}
```

## 💛 State Management

- **`terraform.tfstate`** keeps record of resources.
- Stored **locally by default,** but teams use **remote state backends** (e.g., S3 + DynamoDB, Terraform Cloud).
- Allows collaboration & locking to avoid conflicts.

## 💛 Modules

- A `module` = group of `.tf` files (like a package).
- Helps reusability & organization.

### 🤍 Example

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
  name    = "my-vpc"
  cidr    = "10.0.0.0/16"
}
```

## 💛 Best Practices

- Use **.tfvars** files for environment values.
- Use **remote state backend** (e.g., S3 + DynamoDB for AWS).
- Split code into **modules** for reusability.
- Enable **locking** to prevent concurrent updates.
- Version-control your `.tf` files (e.g., Git).

## 💛 References

- Terraform Official Docs
- Terraform AWS Provider
- [Terraform Basics Tutorial](https://developer.hashicorp.com/terraform/tutorials)
