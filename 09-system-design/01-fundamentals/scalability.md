# System Design Fundamentals
*Core concepts for designing large-scale systems*

## Scalability
*Handle growing load without degrading performance*

**Vertical Scaling (Scale Up)** – Bigger machine: more CPU, RAM, disk  
**Horizontal Scaling (Scale Out)** – More machines behind a load balancer  
**Elasticity** – Automatically scale up/down based on load  

| | Vertical | Horizontal |
|---|---|---|
| Cost | Expensive ceiling | Linear cost |
| Limit | Single machine max | Theoretically unlimited |
| Complexity | Low | Higher (distributed) |
| Failure | Single point | Redundancy built-in |

**Stateless** services scale horizontally; **stateful** services need sticky sessions or external state.

---

## Reliability and Availability
*Keep the system working despite failures*

**Availability** – % of time system is operational  
**Reliability** – Probability of correct operation over time  
**Fault Tolerance** – System continues operating when components fail  
**Redundancy** – Multiple copies of critical components  

| Availability | Downtime/year |
|---|---|
| 99% | ~3.65 days |
| 99.9% | ~8.7 hours |
| 99.99% | ~52 minutes |
| 99.999% (5 nines) | ~5 minutes |

---

## Latency vs Throughput
*Two axes of performance*

**Latency** – Time to complete a single request (ms)  
**Throughput** – Number of requests handled per second (RPS)  

**Latency targets** (rough industry benchmarks):
- Database read: <5ms (cache), <20ms (DB)
- API response: <100ms (fast), <500ms (acceptable)
- Page load: <2s (good UX)

---

## CAP Theorem
*Distributed systems trade-off*

**Consistency** – Every read returns the latest write  
**Availability** – Every request gets a response (not guaranteed to be latest)  
**Partition Tolerance** – System works despite network partitions  

**You can only guarantee 2 of 3 during a partition**:  
- **CP** – Consistent + Partition tolerant (sacrifices availability): HBase, ZooKeeper  
- **AP** – Available + Partition tolerant (eventual consistency): Cassandra, DynamoDB  
- **CA** – Consistent + Available (no partition tolerance): traditional RDBMS (single node)

---

## Performance Optimization Patterns
*Common techniques to improve speed*

**Caching** – Store results in memory to avoid recomputation (Redis, Memcached)  
**CDN** – Serve static assets from edge servers close to users  
**Database Indexes** – Speed up reads at the cost of write performance  
**Connection Pooling** – Reuse DB connections instead of creating new ones  
**Async Processing** – Offload heavy work to background queues (SQS + Lambda)  
**Pagination** – Return data in pages, not all at once  
**Compression** – gzip responses to reduce bandwidth  
