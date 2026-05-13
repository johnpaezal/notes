# SAA-C03 Cheat Sheet

*Quick reference for exam decision points*

---

## Architecture Decision Tables

*When to use X vs Y*

### Messaging: SQS vs SNS vs EventBridge

| Service | Pattern | Use Case |
|---------|---------|---------|
| SQS | Queue (pull) | Decouple producers/consumers; buffer load; async tasks |
| SNS | Pub/Sub (push) | Fan-out to multiple subscribers simultaneously |
| EventBridge | Event bus (routing) | Event-driven; route by content; SaaS integrations |

> SNS + SQS fan-out = SNS pushes to multiple SQS queues simultaneously. Use when each subscriber needs its own copy of the message.

### Load Balancers: ALB vs NLB vs CLB

| Feature | ALB | NLB | CLB (legacy) |
|---------|-----|-----|--------------|
| Layer | 7 (HTTP/HTTPS) | 4 (TCP/UDP/TLS) | 4 & 7 |
| Use case | Web apps, microservices, gRPC | High performance, static IP, gaming, IoT | Avoid; migrate to ALB/NLB |
| Target types | IP, instance, Lambda | IP, instance, ALB | Instance only |
| WebSockets | Yes | Yes | No |
| Static IP | No | Yes (Elastic IP) | No |

### Storage: S3 vs EFS vs EBS

| Feature | S3 | EFS | EBS |
|---------|-----|-----|-----|
| Type | Object | File (NFS) | Block |
| Access | HTTP API | Mount on Linux EC2 | Single EC2 (or Multi-Attach io1/io2) |
| Scale | Unlimited | Auto-scale | Fixed size (elastic volumes) |
| Use case | Backups, static sites, data lake | Shared file system, CMS, home dirs | OS disk, databases, boot volume |
| Cost | Lowest | Mid | Mid |

### Databases: RDS vs DynamoDB vs Aurora vs Redshift

| Service | Type | Use Case |
|---------|------|---------|
| RDS | Relational (MySQL, Postgres, etc.) | Traditional OLTP, existing SQL apps |
| Aurora | Relational (MySQL/Postgres compat.) | High throughput OLTP, managed, 5x faster |
| DynamoDB | NoSQL key-value/document | Serverless, single-digit ms, massive scale, flexible schema |
| Redshift | Columnar OLAP | Analytics, BI, data warehouse, petabyte scale |

### Networking: CloudFront vs Global Accelerator

| Feature | CloudFront | Global Accelerator |
|---------|-----------|-------------------|
| Protocol | HTTP/HTTPS | TCP, UDP |
| Caching | Yes | No |
| IPs | Dynamic | 2 static anycast IPs |
| Use case | Web content, APIs, media | Gaming, IoT, VoIP, IP whitelisting needed |
| DDoS | Shield Standard built-in | Shield Standard built-in |

### Secrets: Secrets Manager vs Parameter Store

| Feature | Secrets Manager | Parameter Store |
|---------|----------------|----------------|
| Cost | ~$0.40/secret/month | Free (Standard) |
| Rotation | Native automatic | Manual (Lambda) |
| Use case | DB credentials, API keys needing rotation | Config values, feature flags, non-rotating secrets |

### Compute: EC2 vs Lambda vs Fargate vs Elastic Beanstalk

| Service | Control | Use Case |
|---------|---------|---------|
| EC2 | Full OS control | Legacy apps, GPU, persistent long-running processes |
| Lambda | Zero infra | Event-driven, short functions (max 15 min), APIs |
| Fargate | Container (no EC2 management) | Containerized apps, microservices, batch |
| Elastic Beanstalk | PaaS abstraction | Quick deploy without infra knowledge; uses EC2 underneath |

### Pricing: Reserved vs Spot vs On-Demand

| Option | Cost | Reliability | Use Case |
|--------|------|------------|---------|
| On-Demand | High | Guaranteed | Unpredictable, short-term |
| Reserved (1yr/3yr) | Low | Guaranteed | Steady-state, predictable |
| Savings Plans | Low | Guaranteed | Flexible reserved across families |
| Spot | Lowest (90% off) | Interruptible | Fault-tolerant, batch, stateless |

---

## Key Numbers to Memorize

*Critical limits and SLAs*

| Fact | Value |
|------|-------|
| RDS Multi-AZ failover | ~60 seconds |
| Aurora replica failover | ~30 seconds |
| Aurora Global DB replication lag | < 1 second |
| S3 durability | 99.999999999% (11 nines) |
| S3 Standard availability | 99.99% |
| Lambda max execution time | 15 minutes |
| Lambda max memory | 10,240 MB (10 GB) |
| Lambda max deployment package | 50 MB (zipped), 250 MB (unzipped) |
| SQS max message size | 256 KB |
| SQS Standard max retention | 14 days |
| SQS FIFO max throughput | 300 TPS (3,000 with batching) |
| Kinesis shard ingest | 1 MB/s or 1,000 records/s |
| Kinesis shard egress | 2 MB/s |
| Kinesis max retention | 365 days |
| DynamoDB item max size | 400 KB |
| EFS throughput mode (bursting) | Tied to storage size |
| ALB target groups per rule | 5 |
| ASG max instances per group | 2,000 (default) |
| EC2 Spot interruption notice | 2 minutes |
| NACLs rule limit per VPC | 20 (soft) |

---

## Common Exam Traps

*Frequent gotchas*

**NACLs are stateless** – Must add both inbound AND outbound rules; response traffic is not auto-allowed  
**Security Groups are stateful** – Response traffic is automatically allowed regardless of outbound rules  
**S3 is a global service but buckets are regional** – Bucket names globally unique; data stays in chosen region  
**IAM is global** – Users, groups, roles, policies are not region-specific  
**Most services are regional** – EC2, RDS, Lambda, etc. are tied to a region  
**Read Replicas ≠ Multi-AZ** – Read Replicas scale reads; Multi-AZ provides HA failover  
**Multi-AZ standby is not readable** – Unlike Read Replicas; it only serves as failover  
**S3 replication is not retroactive** – Only objects uploaded after enabling replication are replicated  
**CloudFront invalidation costs money** – Avoid mass invalidations; use versioned file names instead  
**Spot interruption = 2-min notice** – Design workloads to checkpoint and resume  
**Reserved Instances apply per account by default** – Can share across org with RI sharing enabled  
**Global Accelerator does NOT cache** – It routes; CloudFront caches  
**Lambda@Edge max duration** – 30s (viewer) / 30s (origin); CloudFront Functions max 1ms  
**SSE-C keys are not stored by AWS** – Customer must provide the key on every request  
**Envelope encryption DEK is stored encrypted** – The plaintext DEK is only used transiently  
**SCP Allow alone is not enough** – IAM policy must also allow; SCP is a ceiling, not a grant  
**Gateway Endpoints are free; Interface Endpoints cost** – Prefer Gateway for S3/DynamoDB  
**ALB cannot have static IP** – Use NLB (with Elastic IP) when static IP is required  
**DynamoDB Global Tables require on-demand or provisioned with auto-scaling** – Not compatible with local secondary indexes across regions  
