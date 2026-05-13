# AWS DEA-C01 Cheat Sheet

## Service Selection
*When to use which service*

### Streaming Ingestion

| Scenario | Service |
|---|---|
| Real-time, need replay, multiple consumers | **Kinesis Data Streams** |
| Deliver to S3/Redshift/OpenSearch, no replay | **Kinesis Data Firehose** |
| Kafka ecosystem, open-source tools, MSK | **Amazon MSK** |
| MSK without cluster management | **MSK Serverless** |

### ETL and Transformation

| Scenario | Service |
|---|---|
| Serverless ETL, Spark, Glue Catalog | **AWS Glue** |
| Large-scale Spark, custom libs, EMR ecosystem | **Amazon EMR** |
| Lightweight transform, event-driven, <15 min | **Lambda** |
| Visual no-code transforms, PII masking | **Glue DataBrew** |

### Query and Analytics

| Scenario | Service |
|---|---|
| Ad-hoc SQL on S3, pay-per-scan | **Athena** |
| Complex analytics, structured DW, BI tools | **Redshift** |
| Query S3 from Redshift without loading | **Redshift Spectrum** |
| Full-text search, log analytics | **OpenSearch Service** |

### Migration

| Scenario | Service |
|---|---|
| DB replication with CDC, ongoing sync | **DMS** |
| Schema conversion (Oracle → PostgreSQL) | **DMS + SCT** |
| One-time bulk ETL from JDBC source | **Glue (JDBC connection)** |

### Orchestration

| Scenario | Service |
|---|---|
| Complex multi-step DAG, retry logic | **Step Functions** |
| Glue-centric DAG (crawlers + jobs) | **Glue Workflows** |
| Event-driven triggers, schedule-based | **EventBridge** |

---

## Key Numbers
*Must-memorize exam values*

**Kinesis Data Streams**:
- Shard: **1 MB/s in**, **2 MB/s out**
- Enhanced fan-out: **2 MB/s per consumer per shard**
- Retention: **1–365 days** (default 24h)

**Kinesis Data Firehose**:
- Buffer size: **1–128 MB**
- Buffer interval: **60–900 seconds**

**AWS Glue**:
- Default DPUs per job: **10**
- DPU = 4 vCPU + 16 GB RAM

**Athena**:
- Price: **$5 per TB scanned**
- Minimum charge: **10 MB per query**

**Redshift**:
- Max nodes RA3: **128 nodes**
- Max concurrency: **500 connections**

**DynamoDB Streams**:
- Retention: **24 hours**

**Lambda**:
- Max execution: **15 minutes**

---

## Exam Traps
*Common wrong answers*

**Firehose cannot replay** — If you need replay or multiple consumers reading at different speeds, use Kinesis Data Streams, not Firehose.

**Glue Catalog is shared** — Athena, Redshift Spectrum, and EMR all use the same Glue Data Catalog. Changes in one service are visible in all.

**Partitioning reduces Athena cost, not just speed** — Fewer partitions scanned = fewer bytes billed. Always partition by your most common filter columns.

**Lake Formation is on top of IAM, not a replacement** — IAM must first allow access; Lake Formation then restricts further at column/row level. You cannot bypass IAM with Lake Formation.

**EMR Spot is unsafe for Core nodes** — Core nodes store HDFS data. If Spot interrupts a Core node, data is lost. Use Spot only for Task nodes (stateless compute).

**DMS CDC requires FULL LOAD first** — CDC alone won't capture existing data; run Full Load + CDC together for complete migration.

**SSE-S3 vs SSE-KMS** — SSE-S3 has no audit trail. SSE-KMS creates CloudTrail events per key usage — required for compliance audit scenarios.

**Redshift COPY > INSERT** — Never use row-by-row INSERT for bulk loads. COPY from S3 is orders of magnitude faster.

---

## Pipeline Patterns
*Reference architectures*

### Batch ETL
```
S3 (raw) → Glue Crawler → Glue Catalog
         → Glue Job (Spark) → S3 (processed/Parquet)
         → Redshift COPY → Redshift (DW)
         → Athena (ad-hoc queries)
```

### Real-time Streaming
```
App/IoT → Kinesis Data Streams → Lambda (transform)
                               → Kinesis Firehose → S3
                               → Managed Flink → DynamoDB / OpenSearch
```

### Real-time Analytics (near-real-time)
```
Producers → Kinesis Firehose → S3 (Parquet, partitioned)
                             → Athena (query) → QuickSight (BI)
```

### Database Migration
```
On-prem DB → DMS Full Load + CDC → RDS / Aurora / Redshift
           → SCT (if heterogeneous) → schema converted
```

### Governed Data Lake
```
S3 (raw zone) → Glue ETL → S3 (curated zone)
Lake Formation: column/row permissions per team
Athena / Redshift Spectrum → query with LF enforcement
```

---

## Domain Weights

| Domain | Weight |
|---|---|
| 1 – Data Ingestion and Transformation | 34% |
| 2 – Storage and Data Management | 26% |
| 3 – Data Operations and Support | 22% |
| 4 – Data Security and Governance | 18% |
