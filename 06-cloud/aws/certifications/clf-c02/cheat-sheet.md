# AWS CLF-C02 Cheat Sheet

## Domain Weights
*Exam score breakdown*

| Domain | Title | Weight |
|--------|-------|--------|
| 1 | Cloud Concepts | 24% |
| 2 | Security and Compliance | 30% |
| 3 | Cloud Technology and Services | 34% |
| 4 | Billing, Pricing, and Support | 12% |

**Total**: 65 questions, 90 minutes, passing score ~700/1000  
**Question types**: Multiple choice (1 answer), Multiple response (2+ answers)  

---

## Well-Architected Pillars Mnemonic
*OSRPCS — remember the six pillars*

**O** – Operational Excellence  
**S** – Security  
**R** – Reliability  
**P** – Performance Efficiency  
**C** – Cost Optimization  
**S** – Sustainability  

Mnemonic: **"Our Security Really Pays Consistent Savings"**

---

## Numbers to Know
*Key limits and quotas*

**Lambda** – Max execution timeout: 15 minutes  
**S3** – Max object size: 5 TB; max single PUT: 5 GB (use multipart above 100 MB)  
**EC2 Free Tier** – t2.micro or t3.micro, 750 hours/month for 12 months  
**S3 Free Tier** – 5 GB Standard storage, 12 months  
**RDS Free Tier** – db.t2.micro, 750 hours/month, 20 GB storage, 12 months  
**DynamoDB Free Tier** – 25 GB storage, 25 RCU + 25 WCU (always free)  
**Lambda Free Tier** – 1 million requests/month + 400,000 GB-seconds (always free)  
**CloudWatch Free Tier** – 10 custom metrics, 10 alarms (always free)  
**Support: < 1h response** – Business or Enterprise plan (production system down)  
**Support: < 15 min response** – Enterprise only (business critical system down)  
**AZs per Region** – Minimum 2, typically 3, up to 6  
**S3 durability** – 11 nines (99.999999999%)  

---

## Service → Use Case Quick Reference
*Map service to primary scenario*

| Service | Primary Use Case |
|---------|----------------|
| **EC2** | Virtual server with full OS control |
| **Lambda** | Run code without servers, event-driven |
| **S3** | Store files, images, backups, static websites |
| **RDS** | Managed relational database (MySQL, PostgreSQL) |
| **DynamoDB** | Serverless NoSQL for low-latency key-value lookups |
| **Aurora** | High-performance managed relational DB |
| **ElastiCache** | In-memory cache to reduce DB load |
| **Redshift** | SQL analytics on petabyte-scale data warehouse |
| **CloudFront** | CDN — serve content fast globally |
| **Route 53** | DNS service and domain registration |
| **VPC** | Isolate and control network for AWS resources |
| **Direct Connect** | Dedicated private line from on-premises to AWS |
| **CloudFormation** | Infrastructure as Code (IaC) with templates |
| **CloudWatch** | Monitor metrics, logs, set alarms |
| **CloudTrail** | Audit log of all AWS API calls |
| **IAM** | Control who can do what in AWS |
| **KMS** | Create and manage encryption keys |
| **GuardDuty** | Threat detection using ML on logs |
| **WAF** | Block malicious web traffic at HTTP layer |
| **Shield** | DDoS protection (Standard = free, Advanced = paid) |
| **Macie** | Discover sensitive data (PII) in S3 |
| **Trusted Advisor** | Best practice recommendations (cost, security, perf) |
| **Cost Explorer** | Visualize and analyze AWS spend |
| **AWS Budgets** | Alerts when spend exceeds threshold |
| **Snowball** | Physically transfer large data sets to AWS |
| **Athena** | Run SQL queries directly on S3 data |
| **Kinesis** | Real-time streaming data ingestion |
| **SageMaker** | Build, train, and deploy ML models |
| **Elastic Beanstalk** | Deploy app without managing infrastructure |
| **Rekognition** | AI image and video analysis |

---

## Common Exam Traps
*Watch out for these on test day*

### Shared Responsibility Edge Cases
- **RDS**: AWS patches OS and DB engine → you manage DB users, data, encryption at rest  
- **Lambda**: AWS manages runtime → you manage code, IAM execution role, env variables  
- **EC2**: You manage OS patches, security group rules, app code, data  
- **S3**: AWS secures storage infrastructure → you manage bucket policies, ACLs, encryption  

### Pricing Traps
- **On-Demand vs Reserved**: Never say Reserved is "cheaper per hour" — say "lower effective rate with commitment"  
- **Spot Instances**: Can be interrupted with 2-minute notice — not suitable for time-critical workloads  
- **Free Tier**: EC2 free tier is t2.micro OR t3.micro, not both simultaneously  
- **Data transfer**: Inbound to AWS is free; outbound to internet is charged  

### Support Plan Traps
- **< 1 hour response** requires Business or Enterprise (not Developer)  
- **TAM (Technical Account Manager)** is Enterprise-only  
- **Trusted Advisor full checks** require Business or Enterprise (Developer gets only 7 core checks)  
- Developer plan has no phone support — email only during business hours  

### Service Confusion
- **CloudTrail vs CloudWatch**: CloudTrail = API audit logs; CloudWatch = metrics and performance  
- **Config vs CloudTrail**: Config = what did the resource look like; CloudTrail = who called what API  
- **Inspector vs GuardDuty**: Inspector = vulnerability scans on EC2/containers; GuardDuty = threat detection on logs  
- **Shield vs WAF**: Shield = DDoS (L3/L4); WAF = HTTP rule-based filtering (L7)  
- **Macie vs GuardDuty**: Macie = sensitive data in S3; GuardDuty = general threat intelligence  
- **ECS vs EKS**: ECS = AWS-native containers; EKS = Kubernetes  
- **Snowball vs DataSync**: Snowball = offline physical transfer; DataSync = online network transfer  

### Global Infrastructure
- **Region**: You choose; data stays in region unless you replicate  
- **AZ**: Multiple AZs = high availability within a region  
- **Edge Location**: Used by CloudFront and Route 53; NOT for deploying EC2  
- **Local Zone**: Extension for ultra-low latency; NOT the same as AZ  

---

## Quick Compliance Reference
*Artifact and programs*

**AWS Artifact** – Download compliance reports; sign agreements (BAA for HIPAA)  
**SOC 2** – Security/availability controls audit  
**PCI DSS** – Required for credit card data processing  
**HIPAA** – Required for US healthcare patient data  
**ISO 27001** – International security standard  
