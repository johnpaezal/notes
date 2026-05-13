# Terraform Basics
*Infrastructure as Code with HashiCorp Terraform*

## What is Terraform
*Declarative IaC tool for any cloud*

**Terraform** – Open-source IaC tool; describe infrastructure in HCL, apply to cloud  
**HCL (HashiCorp Configuration Language)** – Terraform's declarative config language  
**Provider** – Plugin that connects Terraform to an API (AWS, GCP, Azure, Kubernetes)  
**Resource** – Infrastructure object to manage (EC2 instance, S3 bucket, VPC)  
**State** – JSON file tracking what Terraform manages and current real-world values  

---

## Core Workflow
*Plan → Apply → Destroy*

```bash
terraform init        # download providers, init backend
terraform plan        # preview changes (dry run)
terraform apply       # apply changes (creates/updates/destroys)
terraform destroy     # tear down all managed resources

terraform fmt         # format .tf files
terraform validate    # check syntax
terraform show        # show current state
terraform output      # print output values
```

---

## File Structure
*Recommended layout*

```
infra/
├── main.tf          ← resources
├── variables.tf     ← input variables
├── outputs.tf       ← output values
├── providers.tf     ← provider config
├── terraform.tfvars ← variable values (not committed)
└── backend.tf       ← remote state config
```

---

## Provider and Resource
*Basic AWS example*

```hcl
# providers.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# main.tf
resource "aws_s3_bucket" "app_bucket" {
  bucket = "my-app-bucket-${var.env}"

  tags = {
    Environment = var.env
    Project     = "my-app"
  }
}

resource "aws_s3_bucket_versioning" "app_bucket" {
  bucket = aws_s3_bucket.app_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

---

## Variables and Outputs
*Parameterize and expose values*

```hcl
# variables.tf
variable "env" {
  type        = string
  description = "Deployment environment"
  default     = "dev"
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

# outputs.tf
output "bucket_name" {
  value = aws_s3_bucket.app_bucket.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.app_bucket.arn
}
```

```bash
# Pass variable at runtime
terraform apply -var="env=prod"

# Or via file (terraform.tfvars)
env           = "prod"
instance_type = "m5.large"
```

---

## State and Backend
*Where Terraform stores state*

**Local state** – `terraform.tfstate` on disk (default; avoid for teams)  
**Remote state** – Stored in S3 + DynamoDB lock (recommended for teams)  

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-tf-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-state-lock"
    encrypt        = true
  }
}
```
