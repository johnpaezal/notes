# AWS DynamoDB
*Managed NoSQL key-value and document database*

## What is DynamoDB
*Serverless, single-digit millisecond NoSQL*

**DynamoDB** – Fully managed NoSQL database; scales to any size automatically  
**Table** – Top-level container (like a SQL table, but schema-flexible)  
**Item** – Row; collection of attributes  
**Attribute** – Key-value pair within an item (like a column)  
**Partition Key** – Primary key; determines the partition the item is stored in  
**Sort Key** – Optional second key; allows range queries within a partition  

---

## Key Design
*Choose keys carefully — they determine access patterns*

```
Table: Orders

Partition Key: user_id     Sort Key: order_date#order_id
─────────────────────────────────────────────────────
"user-123"   │  "2024-01-15#ord-001"  │ {amount: 50, status: "shipped"}
"user-123"   │  "2024-01-20#ord-002"  │ {amount: 30, status: "pending"}
"user-456"   │  "2024-02-01#ord-003"  │ {amount: 99, status: "delivered"}
```

Query: `user_id = "user-123"` → all orders for that user  
Query: `user_id = "user-123" AND order_date BEGINS_WITH "2024-01"` → January orders

---

## Basic Operations
*CRUD with Boto3*

```python
import boto3

table = boto3.resource("dynamodb").Table("Orders")

# Put (create/replace)
table.put_item(Item={
    "user_id": "user-123",
    "order_id": "ord-001",
    "amount": 50,
    "status": "pending"
})

# Get (exact key)
response = table.get_item(Key={"user_id": "user-123", "order_id": "ord-001"})
item = response.get("Item")

# Query (partition key + optional sort key condition)
from boto3.dynamodb.conditions import Key
response = table.query(
    KeyConditionExpression=Key("user_id").eq("user-123")
)
items = response["Items"]

# Delete
table.delete_item(Key={"user_id": "user-123", "order_id": "ord-001"})
```

---

## Capacity Modes
*How you pay for throughput*

**Provisioned** – Pre-define read/write capacity units (RCU/WCU); cheaper for stable load  
**On-Demand** – Pay per request; auto-scales; more expensive per request  

**RCU (Read Capacity Unit)** – 1 strongly consistent read of ≤4 KB/s  
**WCU (Write Capacity Unit)** – 1 write of ≤1 KB/s  

---

## Secondary Indexes
*Query on non-primary-key attributes*

**GSI (Global Secondary Index)** – New partition+sort key on any attributes; separate capacity  
**LSI (Local Secondary Index)** – Same partition key, different sort key; must be created with table  

```python
# Query a GSI
response = table.query(
    IndexName="status-index",
    KeyConditionExpression=Key("status").eq("pending")
)
```

---

## When to Use DynamoDB
*vs SQL databases*

**Use DynamoDB when**: access patterns are known upfront, need infinite scale, single-digit ms latency, serverless architecture  
**Use RDS when**: complex queries/joins, ACID transactions across tables, schema changes often, relational data model
