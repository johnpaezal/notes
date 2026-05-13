# Domain 3 – Design High-Performing Architectures

*Compute, storage, caching, networking, messaging*

---

## EC2 Performance

*Instance types and placement*

**Compute optimized (C)** – CPU-intensive: batch processing, gaming, HPC  
**Memory optimized (R/X/z)** – In-memory DBs, big data, SAP HANA  
**Storage optimized (I/D/H)** – High IOPS local storage: OLTP, data warehousing  
**Accelerated (P/G/Inf)** – GPU/FPGA: ML training, graphics rendering  

### Placement Groups

*Control EC2 physical placement*

**Cluster** – All instances in same rack/AZ; ultra-low latency, 10 Gbps; single point of failure  
**Spread** – Each instance on different hardware; max 7 per AZ; for critical distinct instances  
**Partition** – Groups of instances on separate racks; for distributed systems (Kafka, Cassandra)  

**Enhanced Networking (ENA)** – Higher bandwidth, lower latency, lower PPS jitter via SR-IOV  
**Instance store** – Ephemeral NVMe local disk; highest IOPS; lost on stop/terminate  
**EBS** – Persistent block storage; network-attached; survives instance stop  

---

## EBS Volume Types

*Block storage performance tiers*

| Type | Category | Max IOPS | Max Throughput | Use Case |
|------|----------|----------|----------------|----------|
| gp3 | SSD general | 16,000 | 1,000 MB/s | Default; independently tune IOPS+throughput |
| gp2 | SSD general | 16,000 | 250 MB/s | Older default; IOPS tied to size (3 IOPS/GB) |
| io2 Block Express | SSD provisioned | 256,000 | 4,000 MB/s | Mission-critical DBs, sub-ms latency |
| io1 | SSD provisioned | 64,000 | 1,000 MB/s | High IOPS DBs |
| st1 | HDD throughput | 500 | 500 MB/s | Big data, log processing, sequential reads |
| sc1 | HDD cold | 250 | 250 MB/s | Archival, infrequent access, lowest cost |

> st1 and sc1 cannot be boot volumes.

---

## Caching

*Reduce latency and backend load*

**ElastiCache Redis** – Persistence (RDB/AOF), Pub/Sub, sorted sets, Lua scripts, Multi-AZ  
**ElastiCache Memcached** – Simple key-value, multi-threaded, no persistence, horizontal scale  
**DAX (DynamoDB Accelerator)** – In-memory cache for DynamoDB; microsecond reads; write-through  
**CloudFront** – CDN; caches HTTP/HTTPS at edge locations; reduces origin load  

### ElastiCache Redis vs Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| Persistence | Yes (RDB, AOF) | No |
| Data structures | Strings, hashes, sets, sorted sets, lists | Strings only |
| Pub/Sub | Yes | No |
| Multi-AZ failover | Yes | No |
| Multi-thread | No (single-thread) | Yes |
| Use cases | Sessions, leaderboards, queues, rate limiting | Simple caching, multi-thread scale |

### CloudFront

*Global CDN configuration*

**Origin** – S3 bucket, ALB, EC2, or custom HTTP server  
**TTL** – Time-to-live for cached objects; default 24h; controlled by Cache-Control headers  
**Invalidation** – Remove cached content before TTL expires; costs per path  
**Origin Access Control (OAC)** – Restricts S3 bucket access to CloudFront only  
**Geo-restriction** – Allow or block countries  

---

## Database Performance

*Scaling reads and query patterns*

**RDS Read Replicas** – Offload SELECT queries from primary; up to 5 replicas; async  
**Aurora Serverless v2** – Auto-scales in fine-grained increments; ideal for variable workloads  
**DynamoDB on-demand** – Auto-scales; pay per request; no capacity planning  
**DynamoDB provisioned + DAX** – Predictable load; DAX adds microsecond read cache  
**Redshift** – Columnar, MPP analytics DB; for OLAP queries on petabytes of data  
**Redshift Spectrum** – Query S3 data directly from Redshift without loading  

---

## Networking Performance

*Global routing and acceleration*

**Global Accelerator** – Static anycast IPs; routes to nearest healthy endpoint; works for TCP/UDP  
**CloudFront** – HTTP/HTTPS caching at edge; content delivery; does not accelerate non-cacheable TCP  

### Global Accelerator vs CloudFront

| Feature | Global Accelerator | CloudFront |
|---------|-------------------|------------|
| Protocol | TCP, UDP | HTTP, HTTPS |
| Caching | No | Yes |
| Use case | Gaming, IoT, non-HTTP APIs, IP whitelisting | Static/dynamic web content |
| IPs | 2 static anycast IPs | Dynamic IPs per edge |
| Health check | Yes (failover) | Yes (origin failover) |

---

## Lambda Performance

*Cold starts and concurrency control*

**Provisioned concurrency** – Pre-initializes execution environments; eliminates cold starts  
**Reserved concurrency** – Limits max concurrent executions; prevents one function throttling others  
**Lambda@Edge** – Runs at CloudFront edge; full Node.js/Python; max 30s; viewer/origin events  
**CloudFront Functions** – JavaScript only; sub-millisecond; viewer request/response only; lighter  

```python
# Usage: set provisioned concurrency via boto3
import boto3
lambda_client = boto3.client('lambda')

lambda_client.put_provisioned_concurrency_config(
    FunctionName='my-function',
    Qualifier='prod',          # alias or version
    ProvisionedConcurrentExecutions=50
)
```

---

## SQS / SNS / Kinesis

*Messaging and streaming services*

**SQS Standard** – At-least-once delivery; best-effort ordering; unlimited throughput  
**SQS FIFO** – Exactly-once; strict order; 300 TPS (3,000 with batching)  
**SNS** – Pub/Sub; push to multiple subscribers (SQS, Lambda, HTTP, email)  
**SNS fan-out** – One SNS topic → multiple SQS queues; decouple producers from consumers  

### Kinesis

*Real-time data streaming*

**Kinesis Data Streams** – Custom consumers; retention 1–365 days; 1 MB/s in, 2 MB/s out per shard  
**Kinesis Firehose** – Managed delivery to S3, Redshift, OpenSearch; no custom consumers; near real-time  
**Kinesis Data Analytics** – SQL or Flink on streaming data  

| Feature | Data Streams | Firehose |
|---------|-------------|---------|
| Consumers | Custom (Lambda, KCL) | Managed (S3, Redshift, ES) |
| Latency | Real-time | Near real-time (60s buffer) |
| Retention | 1–365 days | No retention |
| Scaling | Manual shard split/merge | Auto-scales |
