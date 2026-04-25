# Monolith to Agents Refactor

**Category:** refactor
**When to use:** Decomposing a large monolithic process (script, service, or pipeline) into coordinated AI agents.

---

You are an AI systems architect. I have a monolithic process that I want to decompose into a system of coordinated AI agents. Analyze the process below and produce a decomposition plan.

Your output must include:
1. **Natural agent boundaries:** Where in the process do concerns cleanly separate? What are the natural "hand-off points" between agents?
2. **Agent definitions:** For each proposed agent: name, single responsibility, inputs, outputs, tools needed.
3. **Orchestration logic:** How does the orchestrator know when to hand off to the next agent? What's the state structure passed between them?
4. **What stays code:** Which parts of the process should remain deterministic code (not LLM reasoning) even in the agent system? Explain why.
5. **Failure handling:** If one agent produces bad output, how does the system detect and recover?
6. **Estimated token cost:** Rough estimate of the LLM calls and token usage per run in the new system vs. the monolithic prompt.

**Current monolithic process:**
```
[describe or paste the current process — could be a large prompt, a Python script, or a pipeline description]
```

**Goal of the refactor:**
[e.g., improve reliability, enable parallelism, make the system testable per stage, reduce hallucinations]

---

## Example output

**Natural agent boundaries in a content pipeline:**

1. `ResearchAgent` — gathers source material from web search and document retrieval. Hands off: a structured list of facts with citations.
2. `OutlineAgent` — builds a content structure from facts. Hands off: a hierarchical outline with section assignments.
3. `WritingAgent` — writes each section independently. Can run in parallel per section. Hands off: raw section drafts.
4. `EditingAgent` — reviews all sections for consistency and tone. Hands off: final polished draft.

**What stays code:** Citation formatting, section merging, output rendering to Markdown/HTML. These are deterministic transformations — using an LLM for them adds cost and variability with no benefit.

**Failure handling:** After each agent, validate output against a JSON schema. If the schema check fails, re-run the agent once with the validation error appended to the prompt. If it fails twice, halt and surface the error with the partial output for human review.
