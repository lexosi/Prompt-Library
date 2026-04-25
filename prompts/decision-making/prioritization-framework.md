# Prioritization Framework

**Category:** decision-making
**When to use:** Prioritizing a backlog of competing technical and product work when everything feels urgent and you need a defensible decision.

---

You are a senior engineering lead helping me prioritize a backlog. Apply structured thinking and give me a ranked list with reasoning — not a framework I need to apply myself.

**Backlog items:**
[list each item — one line each, e.g.:]
1. Refactor auth service (technical debt)
2. Build analytics dashboard (product request)
3. Fix intermittent test failures in CI (engineering health)
4. Add multi-language support (sales request)
5. Improve LLM response caching (cost reduction)

**Context for prioritization:**
- Current biggest pain point: [what's hurting the team or business most right now]
- Upcoming deadlines: [any hard dates — releases, client commitments, investor demos]
- Team capacity: [e.g., 2 engineers, 3-week sprint]
- Strategic focus this quarter: [e.g., retention, cost reduction, new customer acquisition]
- Sequencing constraints: [if X must happen before Y, state it]

**Give me:**
1. A ranked list (1 = do first) with one-sentence reasoning per item.
2. The one item you'd cut entirely if capacity is less than expected.
3. Any hidden dependencies you see in the list — things that should be sequenced together.
4. The item where I should be most skeptical of my own intuition about its priority.

---

## Example output

**Ranked backlog:**

1. **Fix intermittent CI failures** — Every day this stays broken, engineers waste time and lose trust in the test suite. This is leverage: fixing it makes everything else faster.

2. **Improve LLM response caching** — Your strategic focus is cost reduction, and this has a direct, measurable ROI. Pairs well with #1 because faster CI catches caching bugs before they reach production.

3. **Auth service refactor** — This is a prerequisite for multi-language support (auth is locale-dependent). Doing it third means you don't do it twice.

4. **Multi-language support** — Sales has a specific client request, but this should follow auth refactor, not precede it. Schedule for next sprint.

5. **Analytics dashboard** — Useful but no hard deadline and no strategic urgency this quarter. Defer.

**Cut if capacity is short:** Analytics dashboard. No deadline, no dependency, no strategic tie-in this quarter.

**Hidden dependency:** Auth refactor → Multi-language. If you do multi-language before refactoring auth, you'll redo the localization work when you eventually refactor auth. Sequence them together or auth first.

**Where to be skeptical:** You probably feel the analytics dashboard is important because someone asked for it recently. But recency bias inflates perceived urgency. Verify: is there an actual deadline, or just a request?
