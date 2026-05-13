# AWS Lambda
*Serverless function execution*

## What is Lambda
*Run code without managing servers*

**Lambda** – Serverless compute; run functions in response to events  
**Function** – Code + runtime + config deployed to Lambda  
**Handler** – Entry point function called on each invocation  
**Runtime** – Language environment (Python 3.11, Node.js 20, Java 21...)  
**Invocation** – One execution of the function  

**Billing**: per request + duration (rounded to 1ms). Free tier: 1M requests/month.

---

## Function Structure
*Basic Lambda handler in Python*

```python
import json

def handler(event, context):
    """
    event   — input data (dict from trigger)
    context — runtime info (function name, timeout remaining)
    """
    name = event.get("name", "World")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hello, {name}!"})
    }

# Usage (test event)
# {"name": "Alice"} → {"statusCode": 200, "body": "{\"message\": \"Hello, Alice!\"}"}
```

---

## Triggers
*What invokes a Lambda function*

**API Gateway** – HTTP request → Lambda (REST API, WebSocket)  
**S3** – Object upload/delete events  
**SQS** – Process messages from a queue  
**EventBridge** – Scheduled events (cron), rule-based routing  
**DynamoDB Streams** – React to table changes  
**SNS** – Subscribe to topics  
**ALB** – Application Load Balancer target  

---

## Configuration
*Key Lambda settings*

**Timeout** – Max execution time (default 3s, max 15 min)  
**Memory** – 128 MB to 10 GB; CPU scales proportionally  
**Concurrency** – Max parallel executions (default 1000/region)  
**Cold Start** – First invocation delay; container is initialized  
**Warm Start** – Reuses existing container; much faster  

```bash
# Deploy via CLI
aws lambda create-function \
  --function-name my-fn \
  --runtime python3.11 \
  --handler lambda_function.handler \
  --role arn:aws:iam::123456:role/lambda-role \
  --zip-file fileb://function.zip

# Invoke
aws lambda invoke \
  --function-name my-fn \
  --payload '{"name":"Alice"}' \
  response.json
```

---

## Environment Variables
*Pass config to Lambda*

```bash
aws lambda update-function-configuration \
  --function-name my-fn \
  --environment "Variables={DB_URL=postgresql://...,SECRET=abc}"
```

```python
import os

DB_URL = os.environ["DB_URL"]   # read in handler
```

---

## Lambda with API Gateway
*Expose Lambda as HTTP endpoint*

```
Client → API Gateway → Lambda → Response

# Minimal HTTP event structure
{
  "httpMethod": "GET",
  "path": "/users",
  "queryStringParameters": {"page": "1"},
  "headers": {"Authorization": "Bearer ..."},
  "body": null
}
```

Use **AWS SAM** or **Serverless Framework** to manage Lambda + API Gateway together in production.
