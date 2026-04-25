# AI Agent Loop Debug

**Category:** debugging
**When to use:** An AI agent is stuck in a loop, calling the wrong tools repeatedly, or producing hallucinated state that derails its task.

---

You are an AI systems engineer specializing in LLM agent architectures. I have an agent that is misbehaving. Analyze the agent's trajectory below and:

1. Identify the failure mode: is this a loop, a wrong tool selection, hallucinated context, or a goal misinterpretation?
2. Pinpoint the exact step in the trajectory where the agent went off track.
3. Explain why the agent made that decision — what in the prompt or context caused it.
4. Provide a concrete fix: either a prompt change, a tool definition improvement, or a state management fix.

**Agent framework:** [e.g., Claude tool use, LangChain, AutoGen, custom]
**System prompt:** [paste or describe]

**Tool definitions (abbreviated):**
```json
[paste relevant tool schemas]
```

**Agent trajectory (full turn history):**
```
[paste the sequence of user turns, assistant turns, and tool calls/results]
```

**Expected behavior:**
[what should the agent have done]

---

## Example output

**Failure mode:** Tool selection loop. The agent is calling `search_documents` repeatedly with slightly rephrased queries because it never receives a clear termination signal when the search returns empty results.

**Where it went wrong:** Turn 4. The tool returned `{"results": []}` and the agent interpreted this as "search was incomplete" rather than "no documents match." This is a prompt-level ambiguity.

**Why:** The system prompt says "keep searching until you find the answer" — the agent is following instructions correctly, but the instruction doesn't account for the case where no answer exists.

**Fix — system prompt change:**
```
Search for information using search_documents. If the tool returns empty results after 2 attempts with different queries, respond with "I could not find relevant information" and stop. Do not search more than 3 times total.
```

**Fix — tool output improvement:** Add an `exhausted` field to the tool response schema so the agent gets an explicit signal when there's nothing more to find.
