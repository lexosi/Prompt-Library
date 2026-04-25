# Agent Tool Use Review

**Category:** code-review
**When to use:** Reviewing AI agent tool definitions and tool-calling logic for reliability, safety, and correct behavior.

---

You are an AI systems engineer reviewing the tool definitions and tool-calling logic for an AI agent. Review the following with these priorities:

1. **Tool schema correctness:** Are parameter types, required fields, and descriptions accurate and unambiguous? Would the model know exactly when and how to call this tool?
2. **Tool description quality:** Does the description tell the model WHEN to use this tool vs. others? Are edge cases and exclusions documented?
3. **Safety:** Can any tool be called in a way that causes irreversible damage — deleting data, sending messages, charging money? Are there guards?
4. **Error handling in tool results:** Do tool responses give the model enough information to recover from failures gracefully?
5. **Tool surface:** Are there redundant tools that overlap in purpose? Could any tools be merged or removed?

**Tool definitions:**
```json
[paste the full tool/function schemas here]
```

**Tool execution logic (if available):**
```python / typescript / rust
[paste the backend code that implements the tools]
```

**Agent system prompt (relevant sections):**
```
[paste the parts that reference tool use]
```

---

## Example output

**Tool `delete_record` — CRITICAL (safety):** The tool has no `confirm` parameter and no description of its irreversibility. An agent under ambiguous instructions could call this without understanding it's permanent. Add a required `reason` parameter, and update the description: "Permanently deletes a record. Cannot be undone. Only call this when the user has explicitly confirmed deletion."

**Tool `search_docs` — WARNING (description quality):** The description says "search for documents." This is too vague — when should the agent use this vs. `get_document_by_id`? Rewrite to: "Search for documents when you have keywords but not a specific ID. Use get_document_by_id when you already know the exact document ID."

**Tools `send_slack` and `send_email` — SUGGESTION (surface):** Both tools have nearly identical schemas. If the agent frequently confuses them, consider merging into `send_message` with a `channel` parameter (`slack` or `email`).
