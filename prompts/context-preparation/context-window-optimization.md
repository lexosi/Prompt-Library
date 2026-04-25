# Context Window Optimization

**Category:** context-preparation
**When to use:** The context package for an agent or LLM call is too large — hitting token limits, slowing responses, or increasing costs without improving quality.

---

You are an AI systems engineer specializing in context window efficiency. Analyze the context below and reduce its token footprint without losing the information that affects model output quality.

Optimization principles in priority order:
1. **Remove redundancy:** Information the model already knows from training (e.g., "Python is a programming language") wastes tokens.
2. **Compress verbose instructions:** Long instructions can be shortened without losing meaning. Find every instruction that could be rewritten in half the words.
3. **Prioritize recency:** In long conversation histories, earlier turns matter less than recent ones. Summarize older context; keep recent context verbatim.
4. **Move stable context to system prompt:** Information that doesn't change per request belongs in the system prompt, not the user turn.
5. **Truncate low-signal content:** Log files, long stack traces, full file contents — identify which parts are high-signal and cut the rest.

For each section of the context:
1. Current token estimate
2. What can be cut or compressed
3. Revised version
4. Token estimate after revision

**Target reduction:** [e.g., reduce from 15,000 to under 8,000 tokens while preserving task-critical information]

**Context to optimize:**
```
[paste the full context: system prompt, conversation history, injected documents, tool results]
```

---

## Example output

**Section: System prompt (estimated 1,200 tokens)**
Compression opportunities:
- Lines 4–12 explain what JSON is and why it's used — model knows this, cut entirely (saves ~150 tokens).
- Lines 15–24 have 4 bullet points that all say "be thorough" in different words — collapse to one line.

Revised system prompt section: [compressed version — 680 tokens]
Savings: 520 tokens (43% reduction)

**Section: Conversation history (estimated 8,000 tokens)**
Turns 1–15 (old context) can be summarized to:
"User is debugging a Rust async function that deadlocks when called concurrently. We identified the Arc<Mutex> wrapping is correct but the lock is held across an await point. User confirmed the structure."
This summary: ~80 tokens vs. 3,200 tokens for the turns. Savings: 3,120 tokens.

**Section: Stack trace (estimated 2,400 tokens)**
Only the first 3 frames and the error message are diagnostic. Cut frames 4–47.
Savings: ~1,800 tokens.

**Total: from 11,600 to 5,440 tokens — 53% reduction** with no loss of task-critical information.
