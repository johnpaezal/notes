# Domain 1 – Design Secure Architectures

*IAM, S3, VPC, network security, secrets, KMS*

---

## IAM Deep Dive

*Identity policies, roles, boundaries*

**Identity-based policy** – Attached to a principal (user/group/role)  
**Resource-based policy** – Attached to a resource (S3, KMS, Lambda)  
**Permission boundary** – Max permissions an identity policy can grant  
**SCP (Service Control Policy)** – Org-level guardrail; limits all accounts in OU  
**Instance profile** – Container that passes an IAM role to EC2  

### Policy Evaluation Order

*Explicit deny wins always*

1. Explicit **Deny** → stop, denied
2. **SCP** allows? → continue
3. Resource-based policy allows? → allow (same account)
4. Identity-based policy allows? → allow
5. Permission boundary allows? → allow
6. Default → implicit deny

### Cross-Account Access via Roles

*Delegate access across AWS accounts*

```hcl
# Usage: Account A (trusting) creates role; Account B (trusted) assumes it

# Trust policy on Role in Account A:
{
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::ACCOUNT_B:root" },
  "Action": "sts:AssumeRole"
}

# Account B calls:
aws sts assume-role \
  --role-arn arn:aws:iam::ACCOUNT_A:id/MyRole \
  --role-session-name session1
```

**SCP vs IAM policy**: SCP restricts what *can* be allowed; IAM grants what *is* allowed. Both must permit an action.

---

## S3 Security

*Bucket policies, encryption, object lock*

**Bucket policy** – Resource-based JSON; controls cross-account or public access  
**ACL (legacy)** – Per-object/bucket; use bucket policies instead  
**Block Public Access** – Account/bucket level toggle; overrides ACLs and policies  
**Pre-signed URL** – Temporary URL granting access using creator's credentials  
**MFA Delete** – Requires MFA to delete object versions or disable versioning  

### S3 Encryption Options

| Option | Key managed by | Notes |
|--------|----------------|-------|
| SSE-S3 | AWS (S3 service) | AES-256; simplest |
| SSE-KMS | AWS KMS (CMK) | Audit via CloudTrail; costs per API call |
| DSSE-KMS | AWS KMS (dual layer) | Two independent layers of encryption |
| SSE-C | Customer | Customer provides key per request; AWS discards it |
| Client-side | Customer | Encrypted before upload |

### S3 Object Lock (WORM)

*Prevent deletion or overwrite*

**Governance mode** – Users with special permission can override  
**Compliance mode** – Nobody can delete/modify, including root  
**Retention period** – Fixed time window for lock  
**Legal hold** – No expiry; removed independently  

---

## VPC Security

*Security Groups, NACLs, endpoints*

**Security Group** – Stateful, instance-level firewall; return traffic auto-allowed  
**NACL** – Stateless, subnet-level; inbound AND outbound rules required  
**VPC Flow Logs** – Capture IP traffic metadata (not payload) to CloudWatch/S3  

### Security Group vs NACL

| Feature | Security Group | NACL |
|---------|---------------|------|
| Level | Instance (ENI) | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + Deny |
| Order | All rules evaluated | Rules evaluated in order (lowest # first) |
| Default | Deny all inbound | Allow all (default NACL) |

### VPC Endpoints

*Private access to AWS services*

**Gateway endpoint** – Routes to S3 or DynamoDB via route table; free  
**Interface endpoint (PrivateLink)** – ENI with private IP for most services; costs per hour  

```bash
# Usage: create Gateway endpoint for S3
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-123 \
  --service-name com.amazonaws.us-east-1.s3 \
  --route-table-ids rtb-456 \
  --vpc-endpoint-type Gateway
```

---

## Network Security

*WAF, Shield, Firewall Manager*

**AWS WAF** – Layer 7 firewall; rules for SQL injection, XSS, IP blocks, rate limiting  
**Shield Standard** – Free; automatic DDoS protection for all AWS customers  
**Shield Advanced** – Paid; near real-time DDoS visibility, 24/7 DRT, cost protection  
**Firewall Manager** – Centrally manage WAF, Shield, Security Groups across org  

### WAF Rule Types

*Filter malicious HTTP traffic*

- **Managed rule groups** – AWS or Marketplace; pre-built (e.g., AWSManagedRulesCommonRuleSet)
- **Custom rules** – IP sets, regex patterns, rate-based
- **Web ACL** – Collection of rules attached to CloudFront, ALB, API Gateway, AppSync

---

## Secrets Management

*Secrets Manager vs Parameter Store*

| Feature | Secrets Manager | SSM Parameter Store |
|---------|----------------|---------------------|
| Cost | ~$0.40/secret/month | Free (Standard tier) |
| Rotation | Native automatic rotation | Manual (Lambda required) |
| Cross-account | Yes | Via resource policy |
| Types | Credentials, API keys | Strings, SecureStrings |
| Integration | RDS, Redshift, DocumentDB | General purpose |

**SecureString in Parameter Store** – Encrypted with KMS; no native rotation  
**Secret rotation** – Secrets Manager calls a Lambda to update credentials automatically  

---

## KMS

*Key Management Service*

**AWS-managed CMK** – Created/managed by AWS for each service (e.g., `aws/s3`); no cost  
**Customer-managed CMK** – Created by customer; full key policy control; $1/month  
**Imported key material** – Customer provides raw key; customer responsible for backup  

### Envelope Encryption

*Encrypt large data efficiently*

1. KMS generates **Data Encryption Key (DEK)**
2. DEK encrypts the data (locally, fast)
3. KMS encrypts the DEK with CMK → **encrypted DEK** stored alongside data
4. Decryption: KMS decrypts DEK → DEK decrypts data

```bash
# Usage: generate a data key
aws kms generate-data-key \
  --key-id alias/my-key \
  --key-spec AES_256
# Returns: Plaintext DEK + CiphertextBlob (encrypted DEK)
```

**Key policy** – Resource-based policy on CMK; must explicitly allow principals  
**Key rotation** – Customer-managed CMKs: optional annual rotation; AWS-managed: automatic every year  
