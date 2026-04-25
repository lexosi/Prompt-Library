# Technical Stack Decision

**Category:** decision-making
**When to use:** Choosing a programming language, framework, database, or infrastructure provider for a new project or major system component.

---

You are a senior technical advisor. I need to make a stack decision for the following situation. Do not give me a balanced overview of all options — give me a concrete recommendation with honest tradeoffs.

**Decision to make:**
[e.g., "Should we use Rust or Go for our new event processing service?"]

**Context:**
- What the system does: [describe]
- Performance requirements: [latency, throughput, SLAs]
- Team: [who will build and maintain it — experience level, languages known]
- Timeline: [how long to get to production]
- Existing stack: [what's already in use — avoid unnecessary diversity]
- Scale expectations: [now vs. 2 years from now]

**Give me:**
1. Your recommendation — one option, stated directly.
2. The single strongest argument FOR this choice in this context.
3. The single biggest risk or cost of this choice.
4. What would change your recommendation — the specific condition under which you'd choose differently.
5. The one thing we must get right for this choice to work out.

---

## Example output

**Recommendation:** Use Rust.

**Strongest argument for Rust:** Your team already has 2 engineers with production Rust experience, and the service's core requirement — processing 50k events/sec at < 10ms p99 latency — is exactly the domain where Rust's zero-cost abstractions and deterministic memory management pay off versus Go's GC pauses.

**Biggest risk:** Hiring. If either of your two Rust engineers leaves in the next 18 months, you'll have a critical system in a language with thin team coverage. Rust has a steeper learning curve than Go for engineers coming from Python or JavaScript.

**What would change my recommendation:** If your timeline were 4 weeks instead of 12, I'd choose Go. You'd ship faster and iterate faster, and the performance gap wouldn't matter at your current scale. Revisit Rust when the throughput actually becomes a bottleneck.

**The one thing you must get right:** Error handling. Rust's `Result`-based error handling is a superpower, but teams that fight it with excessive `unwrap()` calls end up with production panics that are harder to debug than Go's equivalent. Establish the error handling convention in week one.
