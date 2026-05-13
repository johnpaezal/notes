# AWS Core
*Foundational concepts for all AWS services*

## What is AWS
*Cloud computing platform by Amazon*

**AWS (Amazon Web Services)** – Leading cloud platform; 200+ services  
**Region** – Geographic area with multiple data centers (e.g., `us-east-1`)  
**Availability Zone (AZ)** – Isolated data center within a region  
**Edge Location** – CDN node for caching (used by CloudFront)  

**Rule** – Always deploy across at least 2 AZs for high availability.

---

## Global Infrastructure
*How AWS is organized geographically*

```
World
└── Region (us-east-1, eu-west-1, ap-southeast-1...)
    ├── AZ-a  (data center cluster)
    ├── AZ-b
    └── AZ-c
        └── Data Center
```

**~35 regions, ~100+ AZs** worldwide (2024).  
**Region choice**: data residency, latency to users, service availability, cost.

---

## IAM
*Identity and Access Management*

**IAM User** – Long-term credential for a person or app  
**IAM Role** – Temporary credential assumed by services (EC2, Lambda)  
**IAM Group** – Collection of users sharing the same policies  
**Policy** – JSON document defining Allow/Deny actions on resources  
**Principal** – Entity that can make API requests (user, role, service)  

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:PutObject"],
    "Resource": "arn:aws:s3:::my-bucket/*"
  }]
}
```

**Least Privilege** – Grant only the permissions needed, nothing more.

---

## ARN
*Amazon Resource Name — unique identifier*

```
arn:partition:service:region:account-id:resource

arn:aws:s3:::my-bucket
arn:aws:iam::123456789:user/alice
arn:aws:ec2:us-east-1:123456789:instance/i-1234abcd
```

---

## AWS CLI
*Command-line access to all services*

```bash
# Install
pip install awscli
aws configure          # set key, secret, region, output

# Common commands
aws sts get-caller-identity       # who am I?
aws s3 ls                         # list buckets
aws ec2 describe-instances        # list EC2 instances
aws logs tail /aws/lambda/my-fn   # stream Lambda logs

# Use profile
aws s3 ls --profile prod
```

---

## Shared Responsibility Model
*Who is responsible for what*

| AWS Responsible | Customer Responsible |
|-----------------|----------------------|
| Physical hardware | OS patching (EC2) |
| Hypervisor | App code and config |
| Global network | IAM policies and users |
| Managed service internals | Data encryption (at rest/in transit) |
| Availability zones | Security groups and NACLs |
