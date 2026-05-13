# System Design: Messaging
*Queues, events, and async communication*

## Synchronous vs Asynchronous
*Two communication models*

**Synchronous** – Caller waits for response; tight coupling  
**Asynchronous** – Caller sends message and continues; decoupled  

```
Sync:   Client → API → DB → Response (all in one request)
Async:  Client → API → Queue → Worker processes later
        API responds "accepted" immediately → 202
```

**Use async when**: task takes >200ms, result not needed immediately, fan-out to multiple consumers.

---

## Message Queue
*Buffer between producers and consumers*

**Producer** – Publishes messages to queue  
**Consumer** – Reads and processes messages  
**Message** – Payload; usually JSON  
**At-least-once delivery** – Message may be delivered more than once; consumers must be idempotent  
**At-most-once delivery** – May lose messages; no retries  
**Exactly-once** – Hardest; requires transactions or deduplication IDs  

```
Producer → [Queue] → Consumer
             │
             └── DLQ (failed messages after N retries)
```

---

## Event-Driven Architecture
*Services communicate via events*

**Event** – Something that happened; immutable, past tense (`OrderPlaced`, `UserCreated`)  
**Event Bus** – Routes events to interested consumers (SNS, EventBridge, Kafka)  
**Consumer Group** – Multiple consumers sharing load on the same queue  

```
Order Service publishes: OrderPlaced { order_id, user_id, amount }
    │
    ├── Payments Service → charge card
    ├── Inventory Service → reserve stock
    └── Email Service → send confirmation
```

---

## Kafka vs SQS
*When to use each*

| | SQS | Kafka |
|---|---|---|
| Model | Queue (consume and delete) | Log (retain; replay) |
| Retention | Up to 14 days | Configurable (days–forever) |
| Ordering | FIFO queue only | Per partition |
| Throughput | Moderate | Very high (millions/s) |
| Ops complexity | Managed (serverless) | Self-managed or MSK |
| Use case | Decouple microservices | Event streaming, analytics |

---

## Idempotency
*Process same message multiple times safely*

```python
def process_payment(payment_id: str, amount: float):
    # Check if already processed (deduplication)
    if db.exists(f"processed:{payment_id}"):
        return  # already done, skip

    charge_card(amount)
    db.set(f"processed:{payment_id}", "1", ex=86400)  # 24h TTL
```

**Idempotent operation** – Running N times has same effect as running once.  
Always design message consumers to be idempotent; queues guarantee at-least-once delivery.
