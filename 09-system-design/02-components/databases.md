# System Design: Databases
*Choosing and using databases in distributed systems*

## SQL vs NoSQL
*Choose based on data shape and access patterns*

| | SQL (Relational) | NoSQL |
|---|---|---|
| Schema | Fixed, enforced | Flexible, schema-less |
| Query | Flexible (any column) | Optimized for known patterns |
| ACID | Full support | Eventual consistency (usually) |
| Joins | Native | Avoided (denormalize instead) |
| Scale | Vertical (primary) | Horizontal |
| Examples | PostgreSQL, MySQL | DynamoDB, MongoDB, Cassandra |

**Use SQL when**: complex queries, relationships, transactions  
**Use NoSQL when**: high write throughput, known access patterns, horizontal scale needed

---

## Replication
*Copy data for availability and read scaling*

**Primary-Replica (Master-Slave)** – Writes go to primary; replicas handle reads  
**Multi-Primary** – Multiple nodes accept writes; more complex conflict resolution  
**Synchronous Replication** – Write confirmed only after replica acked; no data loss  
**Asynchronous Replication** – Faster writes; replica may lag; risk of data loss on primary failure  

---

## Sharding
*Horizontal partitioning across multiple databases*

**Shard** – One horizontal partition of the data  
**Shard Key** – Attribute used to route data to the correct shard  

```
User table, sharded by user_id:
  Shard 0: user_id 0–999,999
  Shard 1: user_id 1M–1,999,999
  Shard 2: user_id 2M–2,999,999

Consistent Hashing: hash(user_id) % num_shards = shard
```

**Hotspot problem**: popular shard key values overload one shard → use random or composite keys.

---

## Indexing
*Speed up reads at the cost of write overhead*

**B-Tree Index** – Default; good for equality, range, ORDER BY  
**Hash Index** – O(1) lookups; equality only; no range queries  
**Composite Index** – Index on multiple columns; order matters  
**Covering Index** – Index contains all columns needed by query; avoids table scan  

```sql
-- Composite index: helps queries filtering by (user_id, created_at)
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);

-- Only helps: WHERE user_id = 1 AND created_at > ...
-- Does NOT help: WHERE created_at > ... (no user_id)
```

---

## Connection Pooling
*Reuse DB connections*

**Connection Pool** – Pre-created set of DB connections reused across requests  
**Why**: creating a new DB connection is expensive (~50ms); pooling amortizes cost  

```python
# SQLAlchemy pool config
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:pass@host/db",
    pool_size=10,          # permanent connections
    max_overflow=20,       # extra connections when pool full
    pool_timeout=30,       # wait time before error
    pool_recycle=1800      # recycle connection after 30 min
)
```
