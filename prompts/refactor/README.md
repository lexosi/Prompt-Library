# Refactor Prompts

**Domain:** Technical
**Stack:** Rust, Python, TypeScript

## When to Use

Use these prompts when code works but is becoming a liability — hard to read, test, extend, or reason about. Refactoring prompts are not about rewriting; they are about targeted improvements that reduce future cost.

## Prompts in This Category

| File | Situation |
|------|-----------|
| `rust-idiomatic-refactor.md` | Making Rust code more idiomatic and reducing unsafe surface |
| `python-async-refactor.md` | Migrating sync Python code to proper async/await |
| `typescript-clean-architecture.md` | Restructuring TypeScript for separation of concerns |
| `monolith-to-agents.md` | Breaking a monolithic process into coordinated AI agents |

## Tips

- Refactor one concern at a time — don't try to fix structure, style, and performance simultaneously.
- State what you want to preserve: public API, behavior, test coverage.
- If there are tests, paste them so the AI can validate that refactored code still passes.
