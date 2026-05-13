# AWS DEA-C01 Domain 4: Data Security and Governance

## Encryption at Rest
*Protecting stored data*

**S3 encryption options**:
- `SSE-S3` – AWS-managed keys (AES-256); default; no extra config
- `SSE-KMS` – Customer-managed CMK in KMS; audit trail via CloudTrail; extra cost
- `SSE-C` – Customer-provided key; AWS does not store the key; client manages rotation

**Redshift** – AES-256; choose KMS (AWS-managed or CMK) or CloudHSM for hardware isolation  
**DynamoDB encryption options**:
- AWS-owned key – Default, no cost, no visibility
- AWS-managed key – KMS key in your account, audit via CloudTrail
- Customer-managed key (CMK) – Full control, rotation managed by you

**Glue** – Encrypt job data (S3 and connection passwords) via Glue security configurations  

---

## Encryption in Transit
*Protecting data in motion*

**TLS** – All AWS API calls use HTTPS/TLS by default  
**Redshift SSL** – Enforce with `require_ssl` parameter in parameter group  
**Kinesis** – HTTPS endpoints only  

**Enforce SSL on S3 bucket policy**:
```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": ["arn:aws:s3:::my-bucket/*"],
  "Condition": {
    "Bool": {"aws:SecureTransport": "false"}
  }
}
```

---

## Lake Formation Permissions
*Fine-grained data lake access*

**Permission levels**: Database → Table → Column  
**Row-level security** – Row filters restrict which rows a principal can query  
**Cell-level security** – Column masks or column exclusions per principal  
**LF-Tags (ABAC)** – Tag columns/tables with business labels (e.g., `sensitivity=PII`); grant on tags, not individual resources  

```
# Permission hierarchy
Lake Formation Grant:
  Principal: arn:aws:iam::123456:role/AnalystRole
  Resource: db=sales_db, table=orders, columns=[order_id, amount]
  Permission: SELECT
```

Lake Formation **adds** to IAM — IAM must allow `lakeformation:GetDataAccess`; LF restricts further.

---

## IAM for Data Services
*Service roles and policies*

**Glue job role** – Needs: `s3:GetObject` + `s3:PutObject`, `glue:*` (Catalog), `logs:CreateLogGroup`  
**EMR instance profile** – EC2 role for core/task nodes; needs S3 access for data  
**Athena workgroup policy** – IAM policy restricts which workgroups and S3 locations a user can query  
**Redshift IAM role** – Attached to cluster for COPY (read S3) and UNLOAD (write S3)  

```json
// Usage: Redshift IAM role trust policy
{
  "Effect": "Allow",
  "Principal": {"Service": "redshift.amazonaws.com"},
  "Action": "sts:AssumeRole"
}
```

---

## Data Masking and PII
*Discovering and protecting sensitive data*

**Amazon Macie** – ML-based PII discovery in S3; finds SSN, credit cards, emails; generates findings  
**Glue DataBrew** – Visual masking transforms: redact, replace, encrypt, hash PII columns  
**Redshift dynamic data masking** – Masking policies applied at query time per role; original data unchanged  

```sql
-- Usage: Redshift dynamic data masking policy
CREATE MASKING POLICY mask_email
WITH (email VARCHAR(256))
USING (
  CASE WHEN current_role() = 'analyst_role'
       THEN regexp_replace(email, '(.*)@', '***@')
       ELSE email
  END
);
ATTACH MASKING POLICY mask_email ON users(email) TO ROLE analyst_role;
```

---

## VPC for Data Services
*Network isolation for data workloads*

**Glue connection** – JDBC connections run inside VPC subnets; requires Security Group with self-referencing rule  
**Redshift in VPC** – Always deploy in private subnet; access via bastion or Query Editor v2  
**EMR in VPC** – Cluster in private subnet; S3 access via VPC Gateway Endpoint (no NAT needed)  
**S3 VPC Gateway Endpoint** – Free; routes S3 traffic within AWS backbone; avoids NAT Gateway costs  
**Interface endpoints** – For Kinesis, Glue API, Secrets Manager inside VPC (PrivateLink; has cost)  

```
# Recommended VPC data architecture
Private Subnet:
  └── Redshift cluster
  └── EMR cluster
  └── Glue connections
VPC Endpoints:
  └── Gateway: S3, DynamoDB (free)
  └── Interface: Kinesis, Glue, KMS (paid)
```

---

## Best Practices

**Encryption**: Use SSE-KMS for S3 data that needs audit trail; enforce `aws:SecureTransport` via bucket policy  
**Lake Formation**: Never bypass via direct S3 ACLs — always grant through Lake Formation  
**IAM**: Use resource-based conditions (`s3:prefix`) to restrict Glue/Athena to specific prefixes  
**PII**: Run Macie on all ingestion S3 buckets; use DataBrew masking before sharing with analysts  
**VPC**: Always use S3 Gateway Endpoint in data VPCs to avoid NAT costs and keep traffic private  
