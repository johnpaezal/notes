# Logging & Observability

## Structured vs Plain Text Logging
*Why structured logs win*

**Plain text log** – Human-readable string, hard to query programmatically  
**Structured log** – JSON key-value pairs, queryable by any log system  
**Benefit** – Filter by `user_id`, `status_code`, `duration_ms` without regex  

```
# Plain text (bad for querying)
2024-01-15 10:23:01 ERROR Failed to process payment for user 42

# Structured JSON (good)
{"timestamp":"2024-01-15T10:23:01Z","level":"ERROR","event":"payment_failed",
 "user_id":42,"amount":99.99,"error":"card_declined"}

# Usage: parse with CloudWatch Insights, Datadog, or grep -E on JSON keys
```

---

## Python: logging & structlog
*Configure Python loggers*

**`logging`** – Standard library, configure with `basicConfig` or `dictConfig`  
**`structlog`** – Third-party, outputs JSON logs with minimal setup  

```python
# Standard logging with structured formatter
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
logger = logging.getLogger(__name__)
logger.info("User created", extra={"user_id": 42})

# structlog (JSON output)
import structlog
log = structlog.get_logger()
log.info("payment_processed", user_id=42, amount=99.99)

# Usage: pip install structlog  — outputs {"event":"payment_processed",...}
```

---

## Log Levels
*When to use each level*

**DEBUG** – Detailed trace info, dev environments only, never prod  
**INFO** – Normal operations, requests served, jobs completed  
**WARNING** – Unexpected but handled (retry needed, fallback used)  
**ERROR** – Operation failed, requires attention, service degraded  
**CRITICAL** – System down, data loss risk, immediate action needed  

**Rule**: Default level is `INFO` in prod; `DEBUG` only in local dev  

---

## What to Log
*Signal vs noise*

**Log**: Request in (method, path, user id), response out (status code, duration ms)  
**Log**: Errors with full stack trace, correlation ID  
**Log**: Business events (user created, order placed, payment processed)  
**Log**: External calls (service name, endpoint, response time, status)  

**Never log**:  
- Passwords and tokens (JWT, API keys, session tokens)  
- PII: emails, phone numbers, SSN, full names in prod  
- Credit card numbers (even partial — use last 4 only)  
- Request bodies that may contain any of the above  

---

## Correlation ID Pattern
*Trace a request end-to-end*

**Correlation ID** – UUID generated once per request, attached to every log line  
**Benefit** – Search all logs for one request across multiple services  
**Rule** – Generate at entry point (API gateway or first service), propagate via HTTP header  

```python
import uuid
from fastapi import Request
import structlog

log = structlog.get_logger()

async def logging_middleware(request: Request, call_next):
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
    with structlog.contextvars.bound_contextvars(correlation_id=correlation_id):
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = correlation_id
        return response

# Usage: every log.info/error inside the request now includes correlation_id
```

---

## AWS CloudWatch Logging
*Centralized log management on AWS*

**Log group** – Container for related log streams (one per service/Lambda)  
**Log stream** – Sequence of log events from one instance  
**CloudWatch Insights** – SQL-like query language to filter and aggregate JSON logs  

```python
# CloudWatch Insights query example
# fields @timestamp, level, event, user_id
# | filter level = "ERROR"
# | sort @timestamp desc
# | limit 50

# Ensure logs are JSON so Insights can parse fields automatically
import json, logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        })

# Usage: attach JsonFormatter to handler; ship stdout to CloudWatch log group
```
