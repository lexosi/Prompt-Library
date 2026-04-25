# Debugging Prompts

**Domain:** Technical
**Stack:** Rust, Python, TypeScript, AI Agents

## When to Use

Use these prompts when you need to diagnose a bug you cannot immediately explain. They are structured to extract maximum signal from error messages, stack traces, and unexpected behavior — and give you a concrete hypothesis and next step, not just a theory.

## Prompts in This Category

| File | Situation |
|------|-----------|
| `diagnose-rust-error.md` | Rust compiler errors, borrow checker panics, unsafe blocks |
| `trace-python-async-bug.md` | Async/await race conditions, event loop issues in Python |
| `typescript-type-error-analysis.md` | TypeScript type mismatches and `any`-leakage debugging |
| `ai-agent-loop-debug.md` | AI agent stuck in loops, wrong tool calls, or hallucinated state |

## Tips

- Paste the **full** error message and stack trace — never truncate it.
- Include the surrounding code (20–40 lines), not just the failing line.
- State what you expected to happen vs. what actually happened.
- If the bug is intermittent, describe the conditions under which it occurs.
