# Code Review Prompts

**Domain:** Technical
**Stack:** Rust, Python, TypeScript, AI Agent tools

## When to Use

Use these prompts when you need a structured, thorough review of code before merging, deploying, or handing off to a client. They go beyond style — they check for correctness, safety, performance, and maintainability.

## Prompts in This Category

| File | Situation |
|------|-----------|
| `rust-safety-review.md` | Reviewing Rust code for memory safety, panics, and unsafe misuse |
| `python-ai-pipeline-review.md` | Reviewing Python ML/AI pipelines for correctness and efficiency |
| `typescript-api-review.md` | Reviewing TypeScript REST or GraphQL APIs |
| `agent-tool-use-review.md` | Reviewing AI agent tool definitions and tool-calling logic |

## Tips

- Paste the full file or function — partial snippets lead to partial reviews.
- State the context: is this going to production, a prototype, or a shared library?
- If there are known constraints (performance budget, existing conventions), mention them.
