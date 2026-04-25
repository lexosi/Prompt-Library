# Microservices Split: Rust + Python

**Category:** architecture-design
**When to use:** Splitting a monolithic application into Rust and Python microservices, deciding what language owns which domain.

---

You are a systems architect experienced in polyglot microservices. I need to split a monolith into Rust and Python services. Give me a concrete split plan.

Your output must include:
1. **Language assignment rationale:** Which domains belong in Rust (performance-critical, memory-sensitive, latency-bound) vs. Python (ML, rapid iteration, integrations)? State the decision rule you're using.
2. **Service boundary definitions:** List each proposed service, its language, its API surface (gRPC, REST, message queue), and what it replaces in the monolith.
3. **Data ownership:** Which service owns which tables/collections? How are cross-service joins handled?
4. **Communication pattern:** Sync (gRPC/REST) vs. async (Kafka, RabbitMQ, Redis Streams) for each service pair that communicates.
5. **Migration sequence:** In what order do you extract services to minimize risk? What stays in the monolith longest and why?
6. **Operational complexity cost:** What new infrastructure is required and what's the realistic maintenance burden?

**Current monolith description:**
[describe the monolith: language, main responsibilities, database, current pain points]

**Target state:**
[describe what the system should look like in 6–12 months]

---

## Example output

**Language assignment rule:** Rust for anything on the hot path that touches raw data at high volume (ingestion, processing, serving). Python for anything that calls ML models, wraps third-party APIs, or needs to be iterated on weekly.

**Proposed services:**
| Service | Language | API | Replaces |
|---------|----------|-----|---------|
| `event-ingester` | Rust | gRPC | Monolith event handler |
| `ml-ranker` | Python | Internal REST | Monolith ranking module |
| `notification-worker` | Python | Redis Streams consumer | Monolith email/push worker |

**Migration sequence:** (1) Extract `notification-worker` first — lowest risk, well-isolated. (2) Extract `ml-ranker` — Python stays, just separate deploy. (3) Extract `event-ingester` — highest complexity, do last when the pattern is proven.
