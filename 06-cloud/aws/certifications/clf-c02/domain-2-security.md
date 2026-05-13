# AWS CLF-C02 Domain 2: Security and Compliance

## Shared Responsibility Model
*Who owns what in cloud*

| Responsible | Area |
|-------------|------|
| **AWS** (Security OF the cloud) | Hardware, physical facilities, global infra, hypervisor, managed service patching (RDS OS, Lambda runtime) |
| **Customer** (Security IN the cloud) | OS patches (EC2), app code, IAM users/roles/policies, data encryption, network config (SG, NACLs), data in transit |

**Key edge cases**:  
- RDS → AWS patches DB engine; you manage DB users and data encryption  
- Lambda → AWS manages runtime; you manage function code and IAM execution role  
- S3 → AWS secures infrastructure; you manage bucket policies and object encryption  

---

## IAM
*Identity and Access Management*

**IAM User** – Permanent identity for a person or application  
**IAM Group** – Collection of users sharing the same policies  
**IAM Role** – Temporary identity assumed by services, apps, or users  
**IAM Policy** – JSON document defining allowed/denied actions on resources  
**Identity-based policy** – Attached to users, groups, or roles  
**Resource-based policy** – Attached to resources (e.g., S3 bucket policy)  
**MFA** – Multi-Factor Authentication; second factor beyond password  
**Principle of Least Privilege** – Grant only minimum permissions required  

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::my-bucket/*"
  }]
}

// Usage: attach to IAM user/group/role to grant S3 read access
```

---

## IAM Best Practices
*Securing AWS account identity*

- Never use the root account for daily operations  
- Enable MFA on the root account immediately  
- Create individual IAM users — never share credentials  
- Use IAM roles for AWS services (EC2, Lambda) — never embed keys in code  
- Rotate access keys regularly  
- Use IAM Access Analyzer to review permissions  
- Apply policies to groups, not individual users  

---

## AWS Security Services
*Quick reference per service*

| Service | What it does |
|---------|-------------|
| **GuardDuty** | Threat detection using ML on VPC Flow Logs, CloudTrail, DNS logs |
| **Inspector** | Automated vulnerability assessment for EC2 and container images |
| **Macie** | Discovers and protects sensitive data (PII) in S3 using ML |
| **Shield Standard** | Free DDoS protection for all AWS customers (L3/L4) |
| **Shield Advanced** | Paid DDoS protection with 24/7 DRT support and cost protection |
| **WAF** | Web Application Firewall; filters HTTP/S traffic with rules |
| **Security Hub** | Central dashboard aggregating findings from GuardDuty, Inspector, Macie |
| **CloudTrail** | Logs all API calls made in the account (who, what, when, where) |
| **Config** | Tracks resource configuration changes and evaluates compliance rules |

---

## Encryption
*Data protection at rest and in transit*

**At-rest encryption** – Data encrypted while stored on disk  
**In-transit encryption** – Data encrypted while traveling over network (TLS/HTTPS)  
**KMS** – AWS Key Management Service; creates and manages encryption keys  
**SSE-S3** – S3 Server-Side Encryption with AWS-managed keys  
**SSE-KMS** – S3 Server-Side Encryption with customer-managed KMS keys  
**SSE-C** – S3 Server-Side Encryption with customer-provided keys  
**TLS/HTTPS** – Standard protocol for in-transit encryption  

---

## Compliance
*AWS compliance programs and tools*

**AWS Artifact** – Self-service portal for compliance reports and agreements  
**Compliance reports** – SOC 1/2/3, PCI DSS, ISO 27001 reports downloadable via Artifact  
**BAA (Business Associate Agreement)** – HIPAA agreement available through Artifact  

**Key compliance programs**:  
**SOC** – Service Organization Control; auditing reports for security controls  
**PCI DSS** – Payment Card Industry; required for cardholder data processing  
**HIPAA** – Health Insurance Portability; required for protected health information  
**ISO 27001** – International information security management standard  
**FedRAMP** – US federal government cloud security authorization  
