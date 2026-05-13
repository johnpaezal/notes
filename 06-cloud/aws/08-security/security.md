# AWS Security
*IAM, Secrets, KMS, and security services*

## IAM Best Practices
*Secure identity and access management*

**Principle of Least Privilege** – Grant only what is needed, nothing more  
**No Root Account for Daily Use** – Create IAM admin user, lock root credentials  
**Roles over Users for Services** – EC2, Lambda, ECS use IAM Roles, not access keys  
**MFA** – Enable MFA on all IAM users, especially root  

```bash
# Create role for EC2 to access S3
aws iam create-role \
  --role-name ec2-s3-read \
  --assume-role-policy-document file://ec2-trust-policy.json

# Attach policy
aws iam attach-role-policy \
  --role-name ec2-s3-read \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Attach role to instance profile
aws iam create-instance-profile --instance-profile-name ec2-s3-read
aws iam add-role-to-instance-profile \
  --instance-profile-name ec2-s3-read \
  --role-name ec2-s3-read
```

---

## Secrets Manager
*Store and rotate secrets securely*

**Secrets Manager** – Store DB passwords, API keys, tokens; automatic rotation  
**Parameter Store** – Simpler alternative; free tier; no automatic rotation  

```python
import boto3, json

client = boto3.client("secretsmanager")

# Get secret
response = client.get_secret_value(SecretId="prod/db/password")
secret = json.loads(response["SecretString"])
db_password = secret["password"]
```

```bash
# Create secret
aws secretsmanager create-secret \
  --name prod/db/password \
  --secret-string '{"username":"admin","password":"secret123"}'

# Get secret (CLI)
aws secretsmanager get-secret-value --secret-id prod/db/password
```

---

## KMS
*Key Management Service — encryption keys*

**KMS (Key Management Service)** – Create and manage encryption keys  
**CMK (Customer Master Key)** – Key you control; used to encrypt/decrypt  
**AWS-managed key** – Managed by AWS for specific services (free)  
**Customer-managed key** – You create and rotate; $1/month  

**Encryption at rest**: S3 (SSE-S3, SSE-KMS), RDS, EBS, DynamoDB  
**Encryption in transit**: TLS/HTTPS always  

```bash
# Encrypt a file
aws kms encrypt \
  --key-id alias/my-key \
  --plaintext fileb://secret.txt \
  --output text --query CiphertextBlob | base64 -d > secret.enc

# Decrypt
aws kms decrypt \
  --ciphertext-blob fileb://secret.enc \
  --output text --query Plaintext | base64 -d
```

---

## Security Services
*Monitoring and threat detection*

**CloudTrail** – Log all API calls in your account (who did what, when)  
**CloudWatch** – Metrics, logs, alarms for AWS resources  
**GuardDuty** – Threat detection using ML; detects anomalies in CloudTrail, VPC Flow Logs  
**Security Hub** – Aggregated security findings across services  
**WAF (Web Application Firewall)** – Block SQLi, XSS, bad bots at CloudFront/ALB layer  
**Shield** – DDoS protection (Standard: free, Advanced: $3000/month)  

---

## Security Checklist
*Before going to production*

- [ ] No access keys on EC2 — use IAM roles
- [ ] All S3 buckets have Block Public Access enabled
- [ ] RDS in private subnet, no public access
- [ ] Secrets in Secrets Manager, not in env vars or code
- [ ] CloudTrail enabled in all regions
- [ ] GuardDuty enabled
- [ ] MFA on all IAM users
- [ ] Security groups: principle of least privilege on ports
