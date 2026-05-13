# AWS DEA-C01 Domain 3: Data Operations and Support

## Athena
*Serverless SQL queries on S3*

**Pricing** – $5 per TB of data scanned  
**Cost reduction**: Use Parquet/ORC (columnar) and partition pruning  
**Workgroups** – Isolate query costs, set per-query/per-workgroup data scan limits  
**CTAS (CREATE TABLE AS SELECT)** – Creates new table from query results; use to convert CSV → Parquet  
**Federated queries** – Lambda data source connectors query external sources (RDS, DynamoDB, Redis)  

```sql
-- Usage: CTAS to convert CSV to Parquet with partitioning
CREATE TABLE orders_parquet
WITH (
  format = 'PARQUET',
  external_location = 's3://bucket/orders-parquet/',
  partitioned_by = ARRAY['year', 'month']
)
AS SELECT * FROM orders_csv;
```

---

## EMR (Elastic MapReduce)
*Managed big data cluster*

**Instance groups**:
- `Master` – Coordinates cluster (1 node, not Spot)
- `Core` – HDFS storage + compute (avoid Spot — data loss risk)
- `Task` – Compute only (safe for Spot — no data stored)

**EMR Serverless** – No cluster management; auto-scales workers; pay-per-use  
**Common engines**: Spark, Hive, HBase, Presto, Flink  
**Use cases**: Large-scale batch ETL, ML training, streaming with Spark Structured Streaming  

```
# Instance strategy for cost optimization
Master:  On-Demand (always)
Core:    On-Demand (always — HDFS data)
Task:    Spot (safe — stateless compute)
```

---

## AWS Glue Workflows
*Orchestrate crawlers and jobs*

**Workflow** – DAG of crawlers, jobs, and triggers  
**Triggers**:
- Schedule (cron)
- Event-based (on-demand or job completion)
- Conditional (start next job only if previous succeeded)

**Job bookmarks** – Track last-processed S3 objects/JDBC offsets; avoid reprocessing  
**Job metrics** – Published to CloudWatch: `glue.driver.ExecutorAllocationManager.executors.numberAllExecutors`, `glue.ALL.s3.filesystem.write_bytes`  

---

## Step Functions for Data Pipelines
*State machine orchestration*

**State types**:
- `Task` – Invoke Lambda, Glue, EMR, ECS, Athena, etc.
- `Choice` – Conditional branching
- `Parallel` – Run branches concurrently
- `Map` – Iterate over array items
- `Wait` – Pause execution

**Standard workflows** – Long-running (up to 1 year), exactly-once, audit history  
**Express workflows** – High-volume (up to 5 min), at-least-once, lower cost  

```json
// Usage: Glue job task state
{
  "Type": "Task",
  "Resource": "arn:aws:states:::glue:startJobRun.sync",
  "Parameters": {
    "JobName": "transform-orders"
  },
  "Next": "LoadToRedshift"
}
```

---

## CloudWatch for Data Ops
*Monitoring and alerting*

**Key Kinesis metrics**:
- `IncomingBytes` / `IncomingRecords` – Throughput
- `GetRecords.IteratorAgeMilliseconds` – Consumer lag (high = falling behind)
- `WriteProvisionedThroughputExceeded` – Shard capacity exceeded

**Key Glue metrics**:
- `glue.driver.aggregate.numFailedTasks`
- `glue.driver.aggregate.bytesRead`

**Logs Insights** – Query log groups with SQL-like syntax  
**Alarms** – Trigger SNS, Auto Scaling, or Lambda on metric threshold  
**Dashboards** – Unified view across Kinesis, Glue, EMR, DMS  

```
# Logs Insights query — find slow Glue jobs
fields @timestamp, jobName, @message
| filter @message like /ExecutionTime/
| sort ExecutionTime desc
| limit 10
```

---

## Data Pipeline Monitoring
*Tracking job health and history*

**Glue job run history** – Console + CloudWatch: status, error messages, duration  
**DMS task logs** – Task-level logs in CloudWatch Logs (`dms-tasks-<task-id>`)  

**Redshift query monitoring views**:
- `STL_QUERY` – Completed query history with execution time
- `SVL_QLOG` – Summarized query log (faster to query)
- `STL_LOAD_ERRORS` – COPY command error details

```sql
-- Usage: find long-running Redshift queries
SELECT query, datediff(seconds, starttime, endtime) AS duration_s, trim(querytxt) AS sql
FROM STL_QUERY
ORDER BY duration_s DESC
LIMIT 10;
```

---

## EventBridge for Orchestration
*Event-driven pipeline triggers*

**Schedule** – Cron or rate expressions trigger targets  
**Event patterns** – Filter AWS events (S3 PutObject, Glue job state change, DMS task failure)  
**EventBridge Pipes** – Source → optional enrichment (Lambda/API) → target; point-to-point  
**Partner event sources** – Receive events from SaaS (Salesforce, Zendesk, etc.)  

```
# Common data pipeline triggers
S3 PutObject → EventBridge rule → Step Functions
Glue job FAILED → EventBridge → SNS alert
Schedule (daily 2am UTC) → EventBridge → Glue Workflow
```

---

## Best Practices

**Athena**: Always partition data and use columnar formats; use workgroups to enforce scan limits  
**EMR**: Use Spot only for task nodes; keep core nodes On-Demand to prevent HDFS corruption  
**Glue workflows**: Enable job bookmarks for incremental processing; monitor iterator age in Kinesis  
**Step Functions**: Prefer Standard workflows for audit trails; use Map state for parallel file processing  
**EventBridge**: Use event patterns over polling; set DLQ on rules for failed invocations  
