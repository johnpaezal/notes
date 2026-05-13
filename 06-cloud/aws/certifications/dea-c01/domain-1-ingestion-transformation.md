# AWS DEA-C01 Domain 1: Data Ingestion and Transformation

## Kinesis Data Streams
*Real-time streaming data ingestion*

**Shard** – Capacity unit: 1 MB/s in, 2 MB/s out  
**Partition Key** – Routes record to a shard (hash-based)  
**Sequence Number** – Unique ID per record within a shard  
**Retention** – Default 24h, configurable 1–365 days  

**Consumer models**:
- `GetRecords` – polling, shared 2 MB/s across all consumers per shard
- `SubscribeToShard` (enhanced fan-out) – 2 MB/s **per consumer per shard**, push-based

**KCL (Kinesis Client Library)** – Manages shard balancing and checkpointing; for complex consumers  
**Lambda consumer** – Simple serverless processing; event-driven, batch size configurable  

```python
# Usage — put record to Kinesis
import boto3
client = boto3.client('kinesis')

client.put_record(
    StreamName='orders-stream',
    Data=b'{"order_id": 123}',
    PartitionKey='order-123'
)
```

---

## Kinesis Data Firehose
*Managed delivery to data stores*

**Buffer size** – 1–128 MB (flush when reached)  
**Buffer interval** – 60–900 seconds (flush when reached)  
**Destinations**: S3, Redshift (via S3 COPY), OpenSearch, Splunk, HTTP endpoint  

- Supports **Lambda transformation** before delivery (inline processing)
- **No replay capability** — records not stored; use Kinesis Data Streams for replay
- Automatically handles compression (GZIP, Snappy) and format conversion (JSON → Parquet)

```
# Firehose flow
Producer → Firehose → [Lambda transform] → S3/Redshift/OpenSearch
```

---

## Kinesis Data Analytics (Managed Apache Flink)
*SQL and Flink on streaming data*

**Tumbling window** – Fixed, non-overlapping (e.g., 1-min buckets)  
**Sliding window** – Overlapping (e.g., last 5 min, every 1 min)  
**Session window** – Groups by inactivity gap  

- Supports Apache Flink (Java/Scala/Python) and SQL
- Use cases: real-time aggregations, anomaly detection, stream enrichment

---

## AWS Glue
*Serverless ETL and data catalog*

**Glue Catalog** – Central metadata store (databases, tables, partitions); shared with Athena, Redshift Spectrum, EMR  
**Crawlers** – Auto-discover schema from S3, JDBC, DynamoDB; update Catalog  
**Glue Jobs** – ETL scripts in Spark (PySpark), Python shell, or Ray  
**Glue DataBrew** – Visual no-code data transformation tool  
**DPU (Data Processing Unit)** – Billing unit; default 10 DPUs per job  

```python
# Usage — Glue PySpark job skeleton
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)

datasource = glueContext.create_dynamic_frame.from_catalog(
    database='sales_db',
    table_name='orders_raw'
)
# Apply mappings, filters, writes...
```

---

## AWS DMS (Database Migration Service)
*Migrate databases to AWS*

**Full Load** – One-time bulk copy of existing data  
**CDC (Change Data Capture)** – Ongoing replication of changes after full load  
**Replication instance** – EC2 instance that runs the migration task  
**Source/Target endpoints** – Connection config for source and target DB  

**Homogeneous** – Same DB engine (MySQL → MySQL); no schema conversion needed  
**Heterogeneous** – Different engines (Oracle → PostgreSQL); requires SCT  
**SCT (Schema Conversion Tool)** – Converts schema + stored procedures for heterogeneous migrations  

---

## Lambda for ETL
*Lightweight serverless transforms*

**Triggers**: S3 events, Kinesis Data Streams, DynamoDB Streams, SQS, EventBridge  
**Limit**: 15-minute max execution — not suitable for heavy batch processing  
**Use cases**: Small transforms, file validation, enrichment, fan-out logic  

```python
# Usage — Lambda triggered by S3 put event
import boto3, json

def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    # Process the file at s3://bucket/key
    return {'statusCode': 200}
```

---

## Kafka vs Kinesis Comparison

| Feature | Amazon MSK (Kafka) | Kinesis Data Streams |
|---|---|---|
| Management | Managed Kafka cluster | Fully serverless option |
| Retention | Configurable, up to unlimited | 1–365 days |
| Consumer model | Consumer groups (pull) | Shared / Enhanced fan-out |
| Partitioning | Partitions (manual) | Shards (manual) |
| Replication | Multi-AZ via Kafka | Built-in |
| Ecosystem | Kafka Connect, Kafka Streams | AWS-native (Lambda, Firehose) |
| Use when | Kafka expertise, open-source tooling | AWS-first, simpler ops |

**MSK Serverless** – No cluster management; auto-scales capacity  

---

## Best Practices

**Kinesis Streams**: Use enhanced fan-out for multiple consumers needing low latency  
**Firehose**: Enable compression + Parquet conversion to reduce S3 cost  
**Glue**: Use job bookmarks to avoid reprocessing; push-down predicates for large datasets  
**DMS**: Always test CDC before cutover; monitor replication lag  
**Lambda ETL**: Keep functions small and idempotent; use DLQ for failures  
