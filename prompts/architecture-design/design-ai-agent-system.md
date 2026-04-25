# Design AI Agent System

**Category:** architecture-design
**When to use:** Starting a new multi-agent system or redesigning an existing one that has outgrown its original structure.

---

You are a principal AI systems architect. I need to design a multi-agent system for the following task. Produce a concrete architecture — not a list of options, but a specific recommended design with clear reasoning.

Your output must include:
1. **Agent roles:** List each agent, its single responsibility, its inputs, and its outputs.
2. **Orchestration model:** How do agents coordinate — pipeline, parallel fan-out, hierarchical, event-driven? Justify why this model fits.
3. **Tool surface:** What tools does each agent need? Flag any tools that are shared vs. exclusive.
4. **State management:** Where does state live? How is it passed between agents? What happens if an agent fails mid-task?
5. **Failure modes:** The two most likely ways this system will break in production and how to detect them.
6. **Implementation starting point:** The first three components to build, in order.

**Task the system must accomplish:**
[describe the end-to-end task the agent system needs to handle]

**Constraints:**
- Model: [e.g., Claude 3.5 Sonnet, GPT-4o]
- Latency budget: [e.g., < 10 seconds end-to-end]
- Team: [e.g., 2 engineers, 3 weeks]
- Existing infrastructure: [e.g., Python backend, PostgreSQL, Redis]

---

## Example output

**System:** Automated code review pipeline for pull requests.

**Agent roles:**
- `DiffParser` — Receives raw git diff, outputs structured list of changed functions with context. Tools: none (pure LLM reasoning).
- `SecurityReviewer` — Receives changed functions, outputs security findings. Tools: `search_vulnerability_db`.
- `StyleReviewer` — Receives changed functions, checks against project conventions. Tools: `read_style_guide`.
- `Synthesizer` — Receives findings from both reviewers, outputs a single formatted review comment. Tools: `post_github_comment`.

**Orchestration:** Parallel fan-out. DiffParser runs first, then SecurityReviewer and StyleReviewer run in parallel, then Synthesizer waits for both to complete before posting.

**State:** Git diff passed as input. Findings stored in-memory as structured JSON. No persistent state needed — each PR review is stateless.

**First three components to build:** (1) DiffParser agent + tests, (2) GitHub webhook handler, (3) Synthesizer + GitHub comment posting.
