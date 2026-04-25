# Context Preparation Prompts

**Domain:** AI Engineering
**Audience:** AI engineers, agent developers, LLM application builders

## When to Use

Use these prompts when you need to design or improve the context an AI agent receives — system prompts, few-shot examples, tool definitions, and context window management.

## Prompts in This Category

| File | Situation |
|------|-----------|
| `prepare-agent-context.md` | Preparing the full context package for an autonomous AI agent |
| `system-prompt-design.md` | Writing a system prompt from scratch for a specific role |
| `few-shot-examples.md` | Creating few-shot examples that steer model behavior |
| `context-window-optimization.md` | Reducing context size without losing critical information |

## Tips

- A system prompt is a contract: be explicit about what the agent should and should not do.
- Few-shot examples should cover edge cases, not just the happy path.
- When optimizing context, cut redundancy first — information the model already knows from training is usually waste.
