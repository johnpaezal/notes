# Terraform Advanced
*Modules, loops, conditions, and patterns*

## Data Sources
*Read existing infrastructure*

```hcl
# Look up existing VPC
data "aws_vpc" "main" {
  filter {
    name   = "tag:Name"
    values = ["main-vpc"]
  }
}

# Look up latest Ubuntu AMI
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]   # Canonical
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-22.04-amd64-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  subnet_id     = data.aws_vpc.main.id
}
```

---

## Loops
*Create multiple resources*

```hcl
# count — simple repetition
resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

# for_each — iterate over map or set
variable "buckets" {
  default = {
    assets  = "us-east-1"
    backups = "us-west-2"
  }
}

resource "aws_s3_bucket" "buckets" {
  for_each = var.buckets
  bucket   = "myapp-${each.key}"
  # each.key   = "assets" / "backups"
  # each.value = "us-east-1" / "us-west-2"
}
```

---

## Conditionals
*Optional resources and values*

```hcl
variable "create_bucket" {
  type    = bool
  default = false
}

resource "aws_s3_bucket" "optional" {
  count  = var.create_bucket ? 1 : 0
  bucket = "my-optional-bucket"
}

# Conditional value
locals {
  instance_type = var.env == "prod" ? "m5.large" : "t3.micro"
}
```

---

## Locals
*Computed intermediate values*

```hcl
locals {
  common_tags = {
    Project     = "my-app"
    Environment = var.env
    ManagedBy   = "terraform"
  }
  name_prefix = "${var.app_name}-${var.env}"
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = local.instance_type
  tags          = merge(local.common_tags, { Name = "${local.name_prefix}-web" })
}
```

---

## Modules
*Reusable infrastructure components*

```hcl
# modules/ec2/main.tf
variable "instance_type" { default = "t3.micro" }
variable "subnet_id"     {}
variable "tags"          { default = {} }

resource "aws_instance" "this" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  tags          = var.tags
}

output "instance_id" { value = aws_instance.this.id }
```

```hcl
# root main.tf — use the module
module "web_server" {
  source        = "./modules/ec2"
  instance_type = "m5.large"
  subnet_id     = module.vpc.public_subnet_ids[0]
  tags          = local.common_tags
}

# Access module output
output "web_ip" {
  value = module.web_server.instance_id
}
```

---

## Best Practices
*Production-ready Terraform*

**Use remote state** – S3 + DynamoDB lock; never commit `.tfstate`  
**Use modules** – Reuse patterns; one module per logical component  
**`terraform plan` in CI** – Review before `apply`; never `apply` without plan  
**Tag everything** – `Environment`, `Project`, `ManagedBy = terraform`  
**Version-lock providers** – `~> 5.0` not `latest`; avoid breaking changes  
**Separate environments** – `envs/dev/`, `envs/prod/` with separate state files  
