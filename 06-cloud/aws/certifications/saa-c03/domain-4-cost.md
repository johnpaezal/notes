# Domain 4 – Design Cost-Optimized Architectures

*EC2 pricing, S3 tiers, data transfer, right-sizing*

---

## EC2 Cost Optimization

*Purchasing options and savings*

**On-Demand** – Pay per second; no commitment; for unpredictable or short-term workloads  
**Reserved Instances (RI)** – 1yr or 3yr commitment; up to 72% discount  
**Savings Plans** – Flexible RI alternative; commitment in $/hour, not specific instances  
**Spot Instances** – Unused EC2 capacity; up to 90% off; can be interrupted with 2-min notice  

### Reserved Instances Types

*Standard vs Convertible*

**Standard RI** – Highest discount (up to 72%); cannot change instance family/OS  
**Convertible RI** – Lower discount (up to 66%); can change instance family, OS, tenancy  
**Scheduled RI** – Reserved for specific time windows; deprecated (use Savings Plans instead)  

### Savings Plans Types

| Type | Flexibility | Discount |
|------|------------|---------|
| Compute Savings Plan | Any instance family, region, OS | Up to 66% |
| EC2 Instance Savings Plan | Specific family + region; flexible size/OS | Up to 72% |
| SageMaker Savings Plan | SageMaker only | Up to 64% |

### Spot Instances

*Maximize savings for fault-tolerant workloads*

**Spot Fleet** – Collection of Spot + On-Demand; auto-replaces interrupted instances  
**Spot capacity pools** – Specific instance type + AZ + OS combinations  
**Use cases** – Batch processing, CI/CD, big data, stateless web, fault-tolerant HPC  
**Not suitable for** – Databases, critical stateful workloads, jobs that cannot be interrupted  

```bash
# Usage: request spot instance with fallback to on-demand
aws ec2 run-instances \
  --instance-market-options '{"MarketType":"spot","SpotOptions":{"MaxPrice":"0.05","InstanceInterruptionBehavior":"terminate"}}' \
  --instance-type m5.large \
  --image-id ami-12345678
```

---

## S3 Cost Optimization

*Storage classes and lifecycle*

**S3 Standard** – Frequent access; highest cost; 3+ AZ; 99.99% availability  
**S3 Standard-IA** – Infrequent access; lower storage cost; retrieval fee; 3+ AZ  
**S3 One Zone-IA** – Single AZ; cheaper than Standard-IA; for reproducible data  
**S3 Glacier Instant Retrieval** – Archive; millisecond retrieval; minimum 90-day storage  
**S3 Glacier Flexible Retrieval** – Minutes to 12h retrieval; minimum 90-day storage  
**S3 Glacier Deep Archive** – Lowest cost; 12–48h retrieval; minimum 180-day storage  
**S3 Intelligent-Tiering** – Auto-moves objects between tiers based on access patterns; monitoring fee  

### S3 Lifecycle Policies

*Automate object transitions and deletion*

```yaml
# Usage: lifecycle rule example (conceptual YAML)
Rules:
  - ID: archive-old-logs
    Filter:
      Prefix: logs/
    Transitions:
      - Days: 30
        StorageClass: STANDARD_IA
      - Days: 90
        StorageClass: GLACIER
    Expiration:
      Days: 365   # delete after 1 year
```

> Minimum storage durations: Standard-IA = 30 days, Glacier Instant = 90 days, Glacier Flexible = 90 days, Deep Archive = 180 days.

---

## Data Transfer Costs

*What is free vs paid*

**Free**: Data into AWS (ingress), S3 → CloudFront, same-AZ same-service transfers  
**Paid**: Data out to internet (egress), cross-region transfers, cross-AZ transfers  

### Cost Reduction Strategies

*Avoid unnecessary transfer fees*

- **Gateway VPC Endpoint for S3/DynamoDB** – Free; avoids NAT Gateway data processing cost ($0.045/GB)
- **CloudFront** – Cache at edge; reduces S3/origin egress costs
- **S3 Transfer Acceleration** – Uses CloudFront edge for uploads; paid but faster
- **Same-AZ deployment** – Place Lambda, EC2, RDS in same AZ when possible

> Using a NAT Gateway to access S3 incurs both NAT Gateway data processing AND EC2-to-S3 egress. Use Gateway Endpoint instead.

---

## Right-Sizing

*Match resources to actual needs*

**AWS Compute Optimizer** – ML-based recommendations for EC2, Lambda, ECS, EBS  
**Trusted Advisor** – Checks underutilized EC2, idle load balancers, unattached EBS volumes  
**CloudWatch metrics** – CPU, memory (requires CloudWatch Agent), network I/O  

### Right-Sizing Targets

| Service | Tool | Action |
|---------|------|--------|
| EC2 | Compute Optimizer | Downsize or change family |
| Lambda | Compute Optimizer | Adjust memory (affects CPU allocation) |
| ECS | Compute Optimizer | Adjust vCPU/memory in task definition |
| RDS | Trusted Advisor | Downsize or use Aurora Serverless |

---

## Serverless for Cost

*Pay only for usage*

**Lambda** – Pay per invocation + duration (GB-seconds); free tier 1M req/month  
**Fargate** – Pay per vCPU + memory per second; no idle EC2 costs  
**Aurora Serverless v2** – Pay per ACU-hour; scales to zero (v1 only); ideal for variable load  
**API Gateway** – Pay per API call + data transfer; no server costs  
**DynamoDB on-demand** – Pay per read/write request unit; no capacity planning needed  

> Serverless shifts cost from fixed (reserved servers) to variable (actual usage). Analyze break-even vs Reserved Instances for steady-state workloads.

---

## Cost Visibility and Governance

*Track, allocate, and forecast spend*

**Cost Allocation Tags** – Tag resources (e.g., `env: prod`, `team: backend`); group costs in reports  
**AWS Budgets** – Set spend/usage alerts; actions to stop services when budget exceeded  
**Cost Explorer** – Visualize and analyze spend; RI utilization; rightsizing recommendations  
**Reserved Instance recommendations** – Cost Explorer suggests RIs based on usage patterns  
**Savings Plans recommendations** – Suggests optimal commitment level based on past usage  

```bash
# Usage: create a budget with email alert
aws budgets create-budget \
  --account-id 123456789012 \
  --budget '{"BudgetName":"monthly-limit","BudgetLimit":{"Amount":"500","Unit":"USD"},"TimeUnit":"MONTHLY","BudgetType":"COST"}' \
  --notifications-with-subscribers '[{"Notification":{"NotificationType":"ACTUAL","ComparisonOperator":"GREATER_THAN","Threshold":80},"Subscribers":[{"SubscriptionType":"EMAIL","Address":"me@example.com"}]}]'
```
