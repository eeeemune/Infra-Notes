# 💚 Terraform Module

## 💛 What is a Module?

<aside>

A **module** is a **reusable Terraform configuration**.

</aside>

Instead of writing the same infrastructure code again and again, you group it into a module and reuse it.

Think of it like:

- Function/package/library in programming

## 💛 Basic Structure

A module is just a folder with `.tf` files:

```
my-module/
  main.tf
  variables.tf
  outputs.tf
```

## 💛 Example

Let’s say we’re creating a `storage` module that creates S3 bucket with given name…

### 🤍 Configure the Module

```hcl
# variables.tf (input)
variable "bucket_name" { # Variable. You will custom this
  type = string
}

# main.tf
resource "aws_s3_bucket" "storage" { # Implement
  bucket = var.bucket_name
}

# outputs.tf (output)
output "bucket_name" { # Printout the name of bucket
  value = aws_s3_bucket.this.bucket
}
```

### 🤍 Use the Module

```hcl
module "my_bucket" {
  source      = "./modules/s3"
  bucket_name = "my-terraform-bucket"
}
```

- `Terrraform apply` will print out the bucket name(my-terraform-bucket)

## 💛 Module Source Types

### 🤍 Local Module

```hcl
source = "./modules/s3"
```

### 🤍 GitHub Module

```hcl
source = "github.com/terraform-aws-modules/terraform-aws-vpc"
```

### 🤍 Terraform Registry

```hcl
source  = "terraform-aws-modules/vpc/aws"
version = "5.0.0"
```

## 💛 Best Practices

- One module = one responsibility (e.g. VPC, DB, EKS)
- Use variables instead of hardcoding
- Version modules (especially shared ones)
- Keep modules small and reusable

## 💛 References

- https://developer.hashicorp.com/terraform/language/modules
- https://registry.terraform.io/
