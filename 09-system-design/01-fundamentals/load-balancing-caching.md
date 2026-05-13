# Load Balancing & Caching
*Distribute load and speed up responses*

## Load Balancing
*Spread traffic across multiple servers*

**Load Balancer** – Single entry point that distributes requests across a server pool  
**Health Check** – Periodic ping to remove unhealthy servers from rotation  
**Session Affinity (Sticky Sessions)** – Same client always hits the same server  

---

## Load Balancing Algorithms
*How the LB chooses a server*

**Round Robin** – Requests go to servers in order: A → B → C → A → ...  
**Weighted Round Robin** – Servers with more capacity get more requests  
**Least Connections** – Send to server with fewest active connections  
**IP Hash** – Hash client IP → always same server (sticky by IP)  
**Random** – Pick random server  

---

## Load Balancer Layers
*L4 vs L7*

**L4 (Transport)** – Routes based on IP + TCP port; fast; no content inspection  
**L7 (Application)** – Routes based on URL, headers, cookies; can do path-based routing  

```
L7 example:
  /api/*     → API servers
  /static/*  → CDN / static servers
  /ws/*      → WebSocket servers
```

**AWS**: ALB = L7, NLB = L4.

---

## Caching Strategies
*When and where to cache*

**Cache-Aside (Lazy Loading)** – App checks cache first; miss → load from DB → populate cache  
**Write-Through** – Write to cache and DB simultaneously  
**Write-Back (Write-Behind)** – Write to cache only; flush to DB asynchronously  
**Read-Through** – Cache sits in front of DB; app only talks to cache  

```python
# Cache-aside with Redis
def get_user(user_id: int):
    cached = redis.get(f"user:{user_id}")
    if cached:
        return json.loads(cached)          # cache hit

    user = db.query(User).get(user_id)    # cache miss
    redis.setex(f"user:{user_id}", 300, json.dumps(user))  # TTL 5 min
    return user
```

---

## Cache Invalidation
*Hardest problem in caching*

**TTL (Time-to-Live)** – Expire cache entry after N seconds  
**Event-Based** – Invalidate on write (update user → delete `user:{id}` from cache)  
**Versioning** – Change cache key on update (`user:{id}:v2`)  

```python
def update_user(user_id, data):
    db.update(user_id, data)
    redis.delete(f"user:{user_id}")   # invalidate on write
```

---

## Cache Eviction Policies
*When cache is full, which items to remove*

**LRU (Least Recently Used)** – Evict item not used for the longest time  
**LFU (Least Frequently Used)** – Evict item accessed least often  
**FIFO** – Evict oldest inserted item  
**TTL** – Evict expired items first  

Redis default: `noeviction` (returns error when full). Common for caches: `allkeys-lru`.
