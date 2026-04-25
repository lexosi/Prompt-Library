# Build vs. Buy Decision

**Category:** decision-making
**When to use:** Deciding whether to build a capability internally or purchase/integrate an existing solution.

---

You are a principal engineer advising on a build-vs-buy decision. Give me a concrete recommendation — not a framework. I'll provide the context; you provide the judgment.

**Capability in question:**
[e.g., "vector database for our RAG system," "authentication service," "job queue"]

**Context:**
- What we need it to do: [functional requirements]
- Scale: [now and in 1–2 years]
- Team: [who would build or maintain it]
- Budget: [rough annual budget for this component]
- Time to need it working: [deadline]
- Existing use elsewhere in company: [is anything similar already in use?]
- Data sensitivity: [can this live in a vendor's cloud or must it be self-hosted?]

**Answer these specifically:**
1. Build or buy — and which specific product/library if buy?
2. The decisive factor in this context that tips it one way.
3. The hidden cost of your recommendation that I should plan for.
4. What the wrong choice looks like 18 months from now — paint the scenario.
5. If I choose to build: what's the minimal version that should replace the interim solution?

---

## Example output

**Recommendation:** Buy — use Qdrant (self-hosted, open-source).

**Decisive factor:** Your team of 3 doesn't have the bandwidth to build and maintain a vector index with production reliability, HNSW tuning, and backup/recovery. Qdrant's self-hosted option keeps your data on-premises (satisfying your compliance requirement) while eliminating 3–6 months of building what's already solved.

**Hidden cost:** Qdrant infrastructure management. Someone on your team needs to own the Qdrant cluster — updates, monitoring, disk management as your index grows. Budget 2–4 hours/week of DevOps time. This is dramatically less than building, but it's not zero.

**Wrong choice scenario (build):** 14 months from now, you've shipped a custom vector index that works for your current 100k documents. Your corpus triples to 300k. You need to re-implement HNSW tuning and sharding. One of the two engineers who built it has left. You spend 3 weeks on infrastructure work instead of product. Meanwhile Qdrant added the exact feature you needed natively.

**Minimum build version (if you choose build):** A wrapper around FAISS with a REST API, PostgreSQL for metadata, and daily backups. Nothing more — defer everything else until the FAISS approach actually hits its limits.
