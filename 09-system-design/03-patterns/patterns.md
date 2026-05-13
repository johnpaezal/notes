# System Design Patterns
*Common architectural patterns for distributed systems*

## API Gateway Pattern
*Single entry point for all clients*

**API Gateway** – Reverse proxy at the edge; routes to backend services  

**Responsibilities**: authentication, rate limiting, SSL termination, request routing, response transformation  

```
Mobile App   ─┐
Web App      ─┤──→ API Gateway ──→ User Service
Third-party  ─┘                ──→ Order Service
                                ──→ Product Service
```

---

## Circuit Breaker
*Stop calling a failing service*

**Closed** – Normal; requests pass through  
**Open** – Service failing; requests blocked immediately (fail fast)  
**Half-Open** – Test if service recovered; allow one request through  

```python
# Conceptual circuit breaker
class CircuitBreaker:
    def call(self, func):
        if self.state == "open":
            raise ServiceUnavailableError()
        try:
            result = func()
            self.record_success()
            return result
        except Exception:
            self.record_failure()
            if self.failure_count > self.threshold:
                self.state = "open"
            raise
```

---

## Rate Limiting
*Prevent abuse and protect resources*

**Token Bucket** – Tokens added at fixed rate; request consumes token; burst allowed  
**Fixed Window** – Count requests per time window (100 req/min)  
**Sliding Window** – Smoother; count requests in last N seconds rolling  

```python
# Redis-based rate limit
def is_rate_limited(user_id: str, limit: int = 100) -> bool:
    key = f"rate:{user_id}:{datetime.now().minute}"
    count = redis.incr(key)
    redis.expire(key, 60)
    return count > limit
```

---

## Saga Pattern
*Distributed transactions across services*

**Problem**: transaction spans multiple services; no global ACID  
**Saga**: sequence of local transactions; each publishes event to trigger next  
**Compensating Transaction**: rollback action if a step fails  

```
CreateOrder → ReserveInventory → ProcessPayment → ConfirmOrder
     ↑               ↑                 ↑
  Compensate    ReleaseInventory   RefundPayment
  (cancel order)    (on failure)    (on failure)
```

---

## CQRS
*Separate read and write models*

**CQRS (Command Query Responsibility Segregation)** – Different models for reads and writes  
**Command** – Changes state (Create, Update, Delete); returns nothing or ID  
**Query** – Returns data; no side effects  

```
Write Path:  POST /orders → Order Service → orders DB (normalized)
Read Path:   GET /orders  → Query Service → read DB (denormalized, optimized for queries)
```

**Use when**: read/write patterns are very different, read-heavy with complex queries.

---

## Strangler Fig
*Incremental migration of legacy systems*

```
Phase 1: All traffic → Legacy System
Phase 2: New features → New Service, old → Legacy
Phase 3: Gradually migrate old features
Phase 4: Legacy decommissioned
```

Route at API Gateway or reverse proxy level. No big-bang rewrites.

---

## Bulkhead Pattern
*Isolate failures to one subsystem*

**Bulkhead** – Separate resource pools per service/consumer; one pool exhaustion doesn't affect others  

```
Without bulkhead: one slow service exhausts all DB connections → everything fails
With bulkhead:    slow service has its own connection pool (max 20) → others unaffected
```
