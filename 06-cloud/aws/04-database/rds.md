# AWS RDS
*Managed relational database service*

## What is RDS
*Managed relational DB — no OS or DB admin needed*

**RDS (Relational Database Service)** – Managed SQL databases on AWS  
**Supported engines**: PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Aurora  
**Managed for you**: provisioning, patching, backups, failover  
**You manage**: schema design, queries, indexes, security groups  

---

## Key Concepts
*RDS components*

**DB Instance** – Running database server  
**DB Instance Class** – CPU + RAM (`db.t3.micro`, `db.m5.large`)  
**Multi-AZ** – Standby replica in another AZ; auto-failover (~60s)  
**Read Replica** – Async copy for read scaling; no auto-failover  
**Parameter Group** – DB engine config (max connections, charset...)  
**Subnet Group** – Set of VPC subnets where RDS can be placed  

---

## Create and Connect
*Launch RDS and access it*

```bash
# Create via CLI
aws rds create-db-instance \
  --db-instance-identifier my-postgres \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password secret123 \
  --allocated-storage 20 \
  --no-publicly-accessible

# Get endpoint
aws rds describe-db-instances \
  --db-instance-identifier my-postgres \
  --query 'DBInstances[0].Endpoint.Address'

# Connect (from EC2 or with VPN/Bastion)
psql -h <endpoint> -U admin -d mydb
```

---

## Backups and Snapshots
*Data recovery options*

**Automated Backups** – Daily snapshot + transaction logs; kept 0–35 days  
**Manual Snapshot** – User-triggered; kept until deleted  
**Point-in-Time Recovery** – Restore to any second within retention window  

```bash
# Create snapshot
aws rds create-db-snapshot \
  --db-instance-identifier my-postgres \
  --db-snapshot-identifier my-snapshot-2024

# Restore from snapshot
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier my-postgres-restored \
  --db-snapshot-identifier my-snapshot-2024
```

---

## Aurora
*AWS-native high-performance database*

**Aurora** – AWS-built MySQL/PostgreSQL-compatible engine  
**Aurora vs RDS**: 5× faster than MySQL, 3× faster than PostgreSQL  
**Storage**: auto-grows 10 GB up to 128 TB; replicated 6 ways across 3 AZs  
**Aurora Serverless v2** – Auto-scales ACUs (Aurora Capacity Units) per demand  

| Feature | RDS PostgreSQL | Aurora PostgreSQL |
|---------|----------------|-------------------|
| Storage | Up to 64 TB | Up to 128 TB, auto-grow |
| Read Replicas | Up to 5 | Up to 15 |
| Failover | ~60s | ~30s |
| Cost | Lower | Higher (~20%) |

---

## Security
*Protect your database*

- Deploy in private subnet (no public access)
- Use Security Groups to restrict port 5432/3306
- Enable encryption at rest (KMS) and in transit (SSL)
- Rotate credentials with AWS Secrets Manager

```python
# Connect with SSL in Python
import psycopg2, boto3

client = boto3.client("secretsmanager")
secret = client.get_secret_value(SecretId="prod/db")
# parse JSON secret → get password
```
