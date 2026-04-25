# Delegate to Junior Developer

**Category:** task-delegation
**When to use:** Assigning a scoped, well-defined task to a junior developer in a way that sets them up to succeed independently.

---

I need to write a task assignment for a junior developer. The task should be scoped so they can complete it in [timeframe] without getting blocked. Write the assignment using this structure:

**TASK TITLE:** Short, specific name.

**WHAT I NEED:** Clear description of the deliverable — not the process, but the result.

**WHY THIS MATTERS:** One sentence on how this task fits into the larger project. Gives context without overwhelming detail.

**STARTING POINT:** Exactly where to begin — which file, which function, which branch.

**RESOURCES:** Links, docs, or examples they should look at before starting.

**DEFINITION OF DONE:**
- [ ] Specific, testable criteria that confirm the work is complete.
- [ ] Include: code runs, tests pass, edge case X is handled, code reviewed.

**WHERE TO GET HELP:**
- If blocked on X, ask [person/channel].
- If uncertain about [specific decision], make the simpler choice and note it in the PR.

**OUT OF SCOPE:** Explicitly list what they should NOT do — prevents scope creep and wasted effort.

**Task to delegate:**
[describe what needs to be done]
**Developer level:** [junior / early-mid]
**Timeframe:** [e.g., 1 day, 3 days]

---

## Example output

**TASK TITLE:** Add pagination to the `/api/users` endpoint

**WHAT I NEED:** The `/api/users` GET endpoint currently returns all users. It needs to support `?page=1&limit=20` query parameters and return a paginated response with `{ data, total, page, totalPages }`.

**WHY THIS MATTERS:** This endpoint is causing timeouts as our user base grows. Pagination is the immediate fix before we address the underlying query performance.

**STARTING POINT:** `src/routes/users.ts`, line 34, the `GET /users` handler.

**RESOURCES:**
- Existing pagination in `src/routes/posts.ts` — same pattern, copy the approach.
- Prisma pagination docs: `skip` and `take` parameters.

**DEFINITION OF DONE:**
- [ ] `GET /api/users?page=1&limit=20` returns 20 users and correct metadata
- [ ] `GET /api/users` without params defaults to page 1, limit 20
- [ ] Existing tests in `users.test.ts` still pass
- [ ] 2 new tests: one for valid pagination, one for out-of-range page

**OUT OF SCOPE:** Do not change the user query itself, add filtering, or touch the auth middleware.
