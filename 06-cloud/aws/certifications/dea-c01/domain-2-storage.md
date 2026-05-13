# AWS DEA-C01 Domain 2: Storage and Data Management

## S3 for Data Lakes
*Object storage as lake foundation*

**Prefix** – Simulated folder path; no real hierarchy  
**Partitioning** – Organize data as `year=/month=/day=` prefixes for pruning  
**Splittable formats** – Parquet, ORC, GZIP-compressed CSV split at block boundaries  

**Columnar vs Row formats**:

| Format | Type | Best For | Notes |
|---|---|---|---|
| Parquet | Columnar | Athena, Glue, Spark queries | Compressed, splittable, schema embedded |
| ORC | Columnar | Hive/EMR workloads | Optimized for Hive, good compression |
| Avro | Row | Schema evolution, streaming | Compact binary, Kafka-friendly |
| CSV | Row | Simple ingestion | No schema, not compressed |
| JSON | Row | Flexible semi-structured | Verbose, slow to scan |

Parquet/ORC: **2–3x faster and cheaper** for Athena/Glue vs CSV/JSON

```
# Recommended S3 partition structure
s3://my-datalake/events/year=2024/month=01/day=15/part-00001.parquet
```

---

## AWS Lake Formation
*Centralized data lake governance*

**Lake Formation** – Builds a governed data lake on S3 with fine-grained access control  
**LF-Tags (ABAC)** – Attribute-based access control; tag columns/tables for policy inheritance  
**Governed Tables** – Transactional tables with ACID support on S3  
**Row filters** – Restrict rows returned per IAM principal  
**Cell-level security** – Restrict specific columns per principal  
**Blueprints** – Pre-built workflows to ingest data from databases and logs into S3  

Lake Formation sits **on top of IAM** — it adds column/row-level controls that IAM alone cannot enforce.

---

## Redshift
*Columnar MPP data warehouse*

**MPP (Massively Parallel Processing)** – Distributes query across all compute nodes  
**Columnar storage** – Only reads columns needed; high compression  

**Distribution styles**:
- `EVEN` – Rows distributed round-robin (no join key known)
- `KEY` – Rows with same key on same node (optimize joins)
- `ALL` – Full copy on every node (small dimension tables)

**Sort keys**:
- `COMPOUND` – Left-to-right column order; efficient for range filters
- `INTERLEAVED` – Equal weight per column; better for multi-column filters

**COPY command** – Bulk load from S3 (fastest ingestion method)  
**Redshift Spectrum** – Query S3 data directly without loading into Redshift  
**RA3 nodes** – Separate compute and storage; scale independently; uses S3 for managed storage  

```sql
-- Usage: COPY from S3
COPY orders
FROM 's3://my-bucket/orders/'
IAM_ROLE 'arn:aws:iam::123456:role/RedshiftRole'
FORMAT AS PARQUET;
```

---

## DynamoDB for Data Engineering
*NoSQL with streaming and export*

**DynamoDB Streams** – Ordered change log (INSERT/UPDATE/DELETE); 24h retention  
**Stream record types**: `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`  
**Global Tables** – Multi-region active-active replication  
**TTL** – Auto-delete expired items; expired items removed within 48h  
**Export to S3** – Full export (any point-in-time within PITR window) or incremental  
**PartiQL** – SQL-compatible syntax to query DynamoDB  

```python
# Usage — enable stream and consume with Lambda
# Trigger: DynamoDB Stream → Lambda
def handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_item = record['dynamodb']['NewImage']
            # process insert...
```

---

## AWS Glue Data Catalog
*Central metadata repository*

**Databases** – Logical grouping of tables  
**Tables** – Schema definition (columns, types, partitions, S3 location)  
**Partitions** – Metadata for each partition prefix (speeds up Athena queries)  

Integrates natively with: **Athena, Redshift Spectrum, EMR, Lake Formation**  
One Catalog per AWS account per region (shared across services — not duplicated).

---

## OpenSearch Service
*Search and log analytics*

**OpenSearch** – Successor to Elasticsearch; full-text search + analytics engine  
**Kibana (OpenSearch Dashboards)** – Visualization layer  
**Use cases**: Log analytics, full-text search, time-series metrics, clickstream analytics  

**Ingestion sources**: Kinesis Data Firehose, Logstash, AWS IoT, CloudWatch Logs subscription filters  

---

## Data Formats Comparison

| Format | Schema | Compression | Splittable | Best Use |
|---|---|---|---|---|
| CSV | None | Optional | Yes (by line) | Simple flat data |
| JSON | Inline | Optional | No (line-delimited only) | Semi-structured |
| Parquet | Embedded | Yes (Snappy/GZIP) | Yes | Analytics queries |
| ORC | Embedded | Yes | Yes | Hive/EMR |
| Avro | External registry | Yes | No | Streaming, schema evolution |

---

## Best Practices

**S3 partitioning**: Partition by query patterns, not by time alone  
**Redshift**: Run VACUUM + ANALYZE after bulk loads to maintain sort order  
**Glue Catalog**: One database per domain; never duplicate table definitions  
**DynamoDB Streams**: Always use `NEW_AND_OLD_IMAGES` for audit use cases  
**Lake Formation**: Grant minimum permissions; use LF-Tags for scalable ABAC  
