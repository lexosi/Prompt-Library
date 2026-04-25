# Rust Idiomatic Refactor

**Category:** refactor
**When to use:** Rust code that works but uses C-style patterns, excessive cloning, manual memory management, or misses standard library opportunities.

---

You are a senior Rust engineer. Refactor the code below to be more idiomatic Rust without changing its behavior or public API.

Focus on:
1. **Error handling:** Replace `unwrap()`/`expect()` with proper `?` propagation and `Result`/`Option` types.
2. **Ownership:** Eliminate unnecessary clones. Find places where borrowing is sufficient.
3. **Iterator chains:** Replace manual `for` loops that build collections with `.map()`, `.filter()`, `.fold()`, `.collect()`.
4. **Type aliases and newtypes:** If raw primitives are used as IDs or domain values, suggest newtype wrappers.
5. **Trait usage:** Implement `From`/`Into`, `Display`, `Default`, or `Iterator` where they'd eliminate boilerplate.
6. **`unsafe` reduction:** If any `unsafe` block can be replaced with safe abstractions, show how.

For each change: show the before and after, and explain why the idiomatic version is better.

**Code to refactor:**
```rust
[paste code here]
```

**Preserve:** [any specific behavior or API surface that must not change]

---

## Example output

**Change 1 — Error propagation (lines 12–18):**

Before:
```rust
let file = File::open(path).unwrap();
let contents = read_to_string(file).unwrap();
```

After:
```rust
let contents = std::fs::read_to_string(path)?;
```

Why: `read_to_string` on a path handles both open and read in one call. `?` propagates errors to the caller rather than panicking. Callers can now decide how to handle the error.

**Change 2 — Iterator chain (lines 34–42):**

Before:
```rust
let mut results = Vec::new();
for item in items {
    if item.score > 0 {
        results.push(item.name.clone());
    }
}
```

After:
```rust
let results: Vec<_> = items.iter()
    .filter(|item| item.score > 0)
    .map(|item| item.name.as_str())
    .collect();
```

Why: No clone needed — we borrow `name`. The iterator chain expresses intent directly. The compiler can optimize the allocation better with a single `.collect()`.
