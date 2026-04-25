# Delegate to Senior Specialist

**Category:** task-delegation
**When to use:** Handing off a complex, high-judgment problem to a domain expert — someone who needs context and outcome, not step-by-step instructions.

---

Write a task brief for a senior specialist. Unlike junior delegation, this should give them the full context, the outcome you need, and the constraints — then get out of their way.

Structure:

**PROBLEM:** What's broken, slow, or uncertain. Be specific with data if you have it.

**OUTCOME NEEDED:** What success looks like — in measurable terms where possible.

**CONTEXT PACKAGE:**
- Relevant architecture or system description (not the full codebase — the parts they need)
- Decisions already made that are not up for debate
- Decisions still open that are theirs to make

**CONSTRAINTS:**
- Timeline
- Budget or resource limits
- Compatibility requirements (must work with X, cannot break Y)

**WHAT I'VE ALREADY TRIED:** Prevent duplication. Be honest about what failed and why you think it failed.

**DELIVERABLE:** What you expect to receive — recommendation doc, PR, architecture diagram, working prototype.

**REVIEW CHECKPOINT:** When and how you'd like to check in (not micromanage — just stay aligned).

**Task to delegate:**
[describe the problem]
**Specialist domain:** [e.g., Rust performance, ML infrastructure, security, game design]

---

## Example output

**PROBLEM:** Our Rust event ingester processes 8,000 events/sec at p99 latency of 340ms. We need to hit 50,000 events/sec at p99 < 50ms. Profiling shows 60% of time in JSON deserialization.

**OUTCOME NEEDED:** A working implementation that processes 50k events/sec at p99 < 50ms on the same hardware (4-core, 16GB RAM). Or a documented architectural reason why it's not achievable without hardware changes.

**CONTEXT PACKAGE:**
- Ingester code: `src/ingest/` — the hot path is `src/ingest/processor.rs`
- We use `serde_json`. Switching serialization format is on the table.
- We cannot change the input wire format (producers are external).
- We can change everything internal.

**CONSTRAINTS:** 2 weeks. No additional infra cost. Must remain compatible with the existing Kafka consumer interface.

**WHAT I'VE ALREADY TRIED:** Switched from `Vec<u8>` to `Bytes` for zero-copy reads — reduced latency by 15% but not enough. Tried `rayon` for parallelism — contention on the output queue made it worse.

**DELIVERABLE:** A PR with the changes + a brief writeup explaining the approach and the performance measurements.

**REVIEW CHECKPOINT:** Async update after 5 days with findings. Full review when PR is ready.
