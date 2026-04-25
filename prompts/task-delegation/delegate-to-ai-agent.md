# Delegate to AI Agent

**Category:** task-delegation
**When to use:** Writing a task brief for an autonomous AI agent — when you need the agent to execute a multi-step task without checking back with you at every step.

---

Write a complete task brief for an autonomous AI agent that will execute the following work. The brief must give the agent everything it needs to complete the task without asking clarifying questions.

Structure the brief as:

**TASK:** One-sentence statement of the goal.

**CONTEXT:** What the agent needs to know about the system, codebase, or domain to make good decisions.

**STEPS:** Numbered sequence of actions. Be specific — name files, functions, and endpoints, not categories.

**TOOLS AVAILABLE:** List the tools the agent has access to. For each, note any important usage constraint.

**OUTPUT FORMAT:** Exactly what the agent should produce when done — file, JSON, message, PR, etc.

**CONSTRAINTS:**
- What NOT to do (be explicit — agents act on what's said, not what's implied)
- Scope limits (which files/services are off-limits)
- Any hard stops (if X happens, stop and report rather than proceeding)

**SUCCESS CRITERIA:** How the agent (and you) will know the task is complete and correct.

**Task to delegate:**
[describe the task]

---

## Example output

**TASK:** Add input validation to all API endpoints in the `orders` service that currently accept raw `req.body` without schema validation.

**CONTEXT:** The codebase is a Fastify + TypeScript API. Validation should use `zod`. The `orders` service is at `src/services/orders/`. There are 4 route files. Tests are in `src/services/orders/__tests__/`.

**STEPS:**
1. Read all 4 route files and identify every endpoint that uses `req.body` without validation.
2. For each endpoint, infer the expected schema from the existing TypeScript types in the same file.
3. Write a `zod` schema for each body and add `.parse()` at the top of each handler.
4. Update existing tests to test both valid and invalid input cases.
5. Run `npm test` — all tests must pass before finishing.

**TOOLS AVAILABLE:** file read, file write, bash (for running `npm test`). Do not use bash for anything other than running tests.

**OUTPUT FORMAT:** List of changed files with a one-line summary of what changed in each.

**CONSTRAINTS:** Do not modify any route in `src/services/auth/` — that service has a separate validation PR in flight. Stop and report if you find any route that mutates the database without authentication middleware.

**SUCCESS CRITERIA:** `npm test` passes. Every `req.body` usage in `orders` routes is preceded by a `zod` parse call.
