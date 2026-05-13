# AWS SQS & SNS
*Messaging and notification services*

## SQS
*Simple Queue Service — decouple producers from consumers*

**SQS (Simple Queue Service)** – Managed message queue; producers send, consumers poll  
**Queue** – Buffer that holds messages  
**Message** – Data payload; up to 256 KB  
**Visibility Timeout** – Time a message is hidden after a consumer receives it (default 30s)  
**Dead Letter Queue (DLQ)** – Queue for messages that failed processing N times  

---

## Queue Types
*Standard vs FIFO*

| | Standard Queue | FIFO Queue |
|---|---|---|
| Throughput | Unlimited | 300 msg/s (3000 with batching) |
| Ordering | Best-effort | Strict (first-in, first-out) |
| Duplicates | At-least-once | Exactly-once |
| Use case | High throughput, order not critical | Financial, order processing |

---

## SQS with Boto3
*Send and receive messages*

```python
import boto3, json

sqs = boto3.client("sqs")
QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/123/my-queue"

# Send message
sqs.send_message(
    QueueUrl=QUEUE_URL,
    MessageBody=json.dumps({"order_id": "123", "amount": 50})
)

# Receive and process
response = sqs.receive_message(
    QueueUrl=QUEUE_URL,
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20      # long polling (reduce empty responses)
)
for msg in response.get("Messages", []):
    body = json.loads(msg["Body"])
    print(body)
    sqs.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=msg["ReceiptHandle"])
```

---

## SNS
*Simple Notification Service — pub/sub fan-out*

**SNS (Simple Notification Service)** – Pub/sub; one message → multiple subscribers  
**Topic** – Channel publishers send to  
**Subscription** – Endpoint that receives topic messages  
**Supported endpoints**: SQS, Lambda, HTTP/HTTPS, Email, SMS  

```
Publisher → SNS Topic → SQS Queue (consumer A)
                      → Lambda (consumer B)
                      → Email (consumer C)
```

```python
sns = boto3.client("sns")
TOPIC_ARN = "arn:aws:sns:us-east-1:123:my-topic"

# Publish
sns.publish(
    TopicArn=TOPIC_ARN,
    Message=json.dumps({"event": "order_placed", "order_id": "123"}),
    Subject="New Order"
)
```

---

## SQS + SNS Fan-out Pattern
*Decouple and scale event-driven systems*

```
Order Service
    │
    ▼
SNS Topic: order-events
    ├── SQS: payments-queue    → Payments Service
    ├── SQS: inventory-queue   → Inventory Service
    └── SQS: notification-queue → Email Service
```

**Benefits**: producers don't know consumers, each consumer processes independently, DLQ per queue for error handling.
