# Case Study: URL Shortener
*End-to-end system design walkthrough*

## Requirements
*Define scope before designing*

**Functional**:
- User submits long URL → receives short URL (`sho.rt/abc123`)
- User visits short URL → redirected to original URL
- Optional: custom alias, expiration date

**Non-Functional**:
- 100M URLs created/day (creation: ~1,200 RPS)
- 10B redirects/day (read: ~115,000 RPS)
- Reads >> Writes (read-heavy → cache aggressively)
- Short URLs must be unique
- Redirect latency <10ms

---

## Estimation
*Back-of-envelope numbers*

```
Writes: 100M/day = 100M / 86400s ≈ 1200 RPS
Reads:  10B/day  = 10B  / 86400s ≈ 115,000 RPS
Read:Write ratio = 10,000:1

Storage per URL ≈ 500 bytes
5 years × 100M/day = 182B URLs × 500B = ~90 TB
```

---

## Short Code Generation
*How to create unique 7-char codes*

**Option 1 — Hash**: `md5(long_url)[:7]` → collisions possible  
**Option 2 — Counter**: `base62(auto_increment_id)` → sequential, predictable  
**Option 3 — Random**: `random.choices(BASE62, k=7)` → check uniqueness in DB  

```python
import random, string

BASE62 = string.ascii_letters + string.digits  # 62 chars

def generate_code(length=7):
    return ''.join(random.choices(BASE62, k=length))
# 62^7 = 3.5 trillion possible codes
```

---

## High-Level Design

```
Client
  │
  ▼
API Gateway / CDN
  │
  ├── POST /shorten  → URL Service → DB (write)
  │
  └── GET /{code}   → Redirect Service
                           │
                     Redis Cache (hot URLs)
                           │ cache miss
                     DB Read Replica
                           │
                     301/302 Redirect response
```

**301 vs 302**:  
- 301 Permanent – browser caches redirect → reduces server load, but can't change target  
- 302 Temporary – no browser cache → every visit hits server; allows analytics  

---

## Database Schema

```sql
CREATE TABLE urls (
  id         BIGINT PRIMARY KEY AUTO_INCREMENT,
  code       VARCHAR(10) UNIQUE NOT NULL,
  long_url   TEXT NOT NULL,
  user_id    BIGINT,
  created_at TIMESTAMP DEFAULT NOW(),
  expires_at TIMESTAMP
);

CREATE INDEX idx_code ON urls(code);  -- hot path
```

---

## Scaling the Read Path

```
115,000 RPS for redirects → must cache

Cache strategy:
  Key:   short code ("abc123")
  Value: long URL
  TTL:   1 hour (or based on expiration)

Cache hit ratio target: 99%+
  → Only 1,150 RPS reach DB
  → DB read replicas handle this easily
```
