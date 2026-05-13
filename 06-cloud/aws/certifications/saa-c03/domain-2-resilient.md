# Domain 2 – Design Resilient Architectures

*HA, fault tolerance, DR, scaling, replication*

---

## Core Resilience Concepts

*HA, FT, DR defined*

**High Availability (HA)** – System remains accessible despite component failures  
**Fault Tolerance (FT)** – System continues operating with zero downtime during failures  
**Disaster Recovery (DR)** – Process to restore services after a catastrophic event  
**RTO (Recovery Time Objective)** – Max acceptable time to restore service  
**RPO (Recovery Point Objective)** – Max acceptable data loss measured in time  

---

## EC2 Resilience

*Auto Scaling Groups and ALB*

**Auto Scaling Group (ASG)** – Automatically adds/removes EC2 based on demand  
**Launch Template** – Defines AMI, instance type, key pair, security groups for ASG  
**Min/Max/Desired** – ASG boundaries; desired = current target capacity  

### Scaling Policies

*Trigger types for ASG*

**Target Tracking** – Maintain a metric at a target (e.g., CPU = 50%); simplest  
**Step Scaling** – Adjust capacity by steps based on alarm breach magnitude  
**Scheduled Scaling** – Scale at known times (e.g., business hours)  
**Predictive Scaling** – ML-based forecast; proactively adjusts before demand spikes  

### ALB + ASG Integration

*Load balancing with auto scaling*

- ASG registers instances with ALB target group automatically
- ALB health checks replace EC2 health checks for ASG
- ALB distributes traffic only to healthy instances
- Multi-AZ ALB: at least one subnet per AZ; cross-zone load balancing enabled by default

```bash
# Usage: attach ASG to ALB target group
aws autoscaling attach-load-balancer-target-groups \
  --auto-scaling-group-name my-asg \
  --target-group-arns arn:aws:elasticloadbalancing:...:targetgroup/my-tg/abc
```

---

## Multi-AZ Patterns

*Distribute across availability zones*

**RDS Multi-AZ** – Synchronous replication to standby in another AZ; automatic failover ~60s  
**ElastiCache Multi-AZ** – Redis with automatic failover; Memcached uses multiple nodes  
**ALB across AZs** – Registers target groups in multiple AZs; handles AZ failure automatically  

### RDS Multi-AZ vs Read Replica

| Feature | Multi-AZ | Read Replica |
|---------|---------|--------------|
| Purpose | HA / failover | Read scaling |
| Replication | Synchronous | Asynchronous |
| Failover | Automatic | Manual promote |
| Readable standby | No | Yes |
| Cross-region | No (same region) | Yes |

---

## S3 Resilience

*Durability, versioning, replication*

**Durability** – 11 nines (99.999999999%); data stored across minimum 3 AZs (Standard)  
**Availability** – 99.99% (Standard); varies by storage class  
**Versioning** – Preserves all versions; enables recovery from accidental delete  
**MFA Delete** – Extra protection; requires versioning to be enabled  

**Cross-Region Replication (CRR)** – Replicates to bucket in different region; requires versioning  
**Same-Region Replication (SRR)** – Replicates within same region; log aggregation, compliance  

> Replication is not retroactive; only new objects are replicated after enabling.

---

## Database Resilience

*RDS, Aurora replication options*

**RDS Read Replica** – Async replication; up to 5 replicas; can be cross-region; not for HA  
**Aurora Read Replica** – Up to 15 replicas; minimal lag; auto-promoted on primary failure  
**Aurora Global Database** – Cross-region replication < 1 second; 1 primary + up to 5 secondary regions  
**Aurora Multi-Master** – Multiple write nodes in same region; all nodes handle reads and writes  

```bash
# Usage: create RDS read replica in another region
aws rds create-db-instance-read-replica \
  --db-instance-identifier my-replica \
  --source-db-instance-identifier my-primary \
  --source-region us-east-1 \
  --db-instance-class db.t3.medium \
  --region eu-west-1
```

---

## Route 53 Routing Policies

*DNS-based traffic management*

**Simple** – One record, one or more values; no health checks  
**Weighted** – Split traffic by percentage; A/B testing, gradual migrations  
**Latency** – Route to region with lowest latency for the user  
**Failover** – Primary/secondary; Route 53 checks health of primary; fails to secondary  
**Geolocation** – Route based on user's geographic location (country/continent)  
**Geoproximity** – Route based on location + bias value; requires Traffic Flow  
**Multi-Value** – Up to 8 healthy records returned; client-side load balancing (not a load balancer)  

> Failover requires a health check on the primary record.

---

## Disaster Recovery Strategies

*RTO/RPO tradeoffs*

| Strategy | RTO | RPO | Cost | Description |
|---------|-----|-----|------|-------------|
| Backup & Restore | Hours | Hours | Lowest | Backup to S3; restore on disaster |
| Pilot Light | 10–30 min | Minutes | Low | Core services running; scale up on disaster |
| Warm Standby | Minutes | Seconds | Medium | Scaled-down production running; scale up |
| Multi-Site Active-Active | Near zero | Near zero | Highest | Full duplicate; traffic split across regions |

**RPO drives replication strategy; RTO drives recovery automation investment.**
