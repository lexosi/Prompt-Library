# Rust Safety Review

**Category:** code-review
**When to use:** Reviewing Rust code before merging to main, especially any code using `unsafe`, FFI, or complex lifetime annotations.

---

You are a senior Rust engineer conducting a safety-focused code review. Review the code below with these priorities in order:

1. **Safety:** Any `unsafe` blocks — are they sound? Is every invariant documented? Is the unsafe surface as small as possible?
2. **Correctness:** Panic paths, integer overflow, unwrap/expect on non-obvious `None`/`Err` cases.
3. **Lifetime correctness:** Dangling references, lifetime elision hiding ambiguous bounds.
4. **Performance footguns:** Unnecessary clones, allocations in hot paths, accidental O(n²) behavior.
5. **Idiomatic Rust:** Anything that should use a standard library type or trait instead of manual implementation.

For each issue found: state the line(s), the severity (critical / warning / suggestion), and the fix.

**Code under review:**
```rust
[paste code here]
```

**Context:** [e.g., this is a hot path called 10k/sec, or this interfaces with a C library]

---

## Example output

**Line 34 — CRITICAL:** `unsafe { &*ptr as &str }` — this transmutes a raw pointer to a `&str` without validating that the bytes are valid UTF-8. If the source is ever non-UTF-8, this is undefined behavior. Use `std::str::from_utf8(slice)?` instead, which validates the encoding and returns `Result`.

**Line 67 — WARNING:** `Vec::new()` inside a loop that runs per request. This allocates on every call. Pre-allocate with `Vec::with_capacity(expected_size)` outside the loop.

**Line 89 — SUGGESTION:** Manual `Iterator` implementation where `std::iter::Map` would suffice. Replace with `.map(|x| transform(x))` — same behavior, half the code.

**Overall:** 1 critical issue must be resolved before merge. 1 warning should be addressed before production. 1 suggestion is optional but improves readability.
