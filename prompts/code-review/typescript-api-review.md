# TypeScript API Review

**Category:** code-review
**When to use:** Reviewing a TypeScript REST or GraphQL API for type safety, security, and correctness before deployment.

---

You are a TypeScript architect reviewing an API implementation. Review the code below with these priorities:

1. **Type safety:** Any `any`, unvalidated `unknown`, missing return types, or places where runtime values are trusted without validation.
2. **Security:** Input validation, SQL/command injection surfaces, authentication/authorization gaps, sensitive data in logs or responses.
3. **Error handling:** Unhandled promise rejections, missing error status codes, errors that expose internal stack traces to clients.
4. **API contract:** Is the response shape consistent? Are status codes semantically correct?
5. **Performance:** N+1 query patterns, missing pagination, synchronous operations that should be async.

Format: line number, category, severity (critical/warning/suggestion), explanation, fix.

**API code:**
```typescript
[paste the route handlers, middleware, and types here]
```

**Framework:** [e.g., Express, Fastify, NestJS, tRPC]
**Database:** [e.g., PostgreSQL via Prisma, MongoDB]

---

## Example output

**Line 12 — CRITICAL (security):** `const userId = req.body.userId` is used directly in a database query without validation. Even with an ORM, validate that `userId` is a valid UUID before using it. Use `zod` or similar:
```typescript
const { userId } = z.object({ userId: z.string().uuid() }).parse(req.body);
```

**Line 28 — WARNING (error handling):** `catch (e) { res.status(500).json({ error: e.message }) }` — `e.message` may contain internal database error strings that reveal schema or connection details to the client. Replace with a generic message and log the full error server-side.

**Line 45 — WARNING (performance):** Each post in the array triggers a separate `findUser()` call — classic N+1. Batch-load users with a single `WHERE id IN (...)` query.

**Line 61 — SUGGESTION (type safety):** `as any` on the Prisma result. Define and use the generated Prisma type directly — `Prisma.UserGetPayload<typeof userQuery>` — instead of casting.
