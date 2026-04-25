# Technical Proposal

**Category:** client-communication
**When to use:** Proposing a technical approach or solution to a client before beginning work — to get buy-in and surface concerns early.

---

Write a technical proposal document for a client. The document should be readable by a non-technical stakeholder but credible to a technical one. It should answer their unspoken question: "Do these people know what they're doing, and will it actually work?"

Structure:
1. **Problem statement:** What we're solving — in the client's language, not technical terms.
2. **Proposed approach:** The technical solution in plain language. One paragraph. No implementation details yet.
3. **Why this approach:** 2–3 specific reasons this approach fits their situation. Not generic benefits — reasons tied to their context.
4. **How it works (technical summary):** A short, honest technical description for technical readers. Diagrams optional.
5. **What we need from you:** Prerequisites, access, data, decisions the client must provide before work starts.
6. **Timeline and phases:** Phases with durations. What's delivered at each phase end.
7. **Risks and mitigations:** 2–3 real risks, honestly stated, with how you'll mitigate them.
8. **Investment:** Cost and payment structure. Clear and specific.

**Context:**
- Client: [describe]
- Problem: [describe]
- Proposed solution: [describe]
- Timeline: [estimate]
- Budget: [amount]

---

## Example output

**Problem statement:** Your support team spends 4–6 hours daily answering the same 40 questions. As your customer base grows, this scales linearly — more customers means more headcount, not better service.

**Proposed approach:** We'll build an AI assistant trained on your existing support documentation that answers common questions instantly, 24/7. Complex or sensitive questions are automatically routed to your team with the full conversation context.

**Why this approach for you:** (1) Your documentation is already well-organized — this dramatically reduces the training time and cost. (2) Your customer base is primarily technical — they'll tolerate (and often prefer) AI assistance over waiting for a human. (3) Zendesk integration means no workflow change for your support team.

**Risks:** Integration complexity with your legacy ticketing system. Mitigation: We'll build a thin adapter layer rather than deep integration, keeping the risk surface small.

**Investment:** $12,000 total. 50% upfront, 50% on delivery. Timeline: 6 weeks.
