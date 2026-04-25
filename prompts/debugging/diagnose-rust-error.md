# Diagnose Rust Error

**Category:** debugging
**When to use:** You have a Rust compiler error, borrow checker violation, or runtime panic you can't immediately explain.

---

You are a senior Rust engineer. I'm going to give you a Rust error and the relevant code. Your job is to:

1. Identify the exact root cause of the error in one sentence.
2. Explain why the Rust compiler or runtime is raising it — the mechanism, not just the symptom.
3. Provide the minimal fix with the corrected code snippet.
4. If there's a better structural approach that prevents this class of error, show it as an alternative.

Do not explain what Rust is. Do not add unrelated suggestions. Focus only on this error.

**Error message:**
```
[paste full error output here]
```

**Relevant code:**
```rust
[paste the failing code here]
```

**What I expected to happen:**
[describe expected behavior]

---

## Example output

**Root cause:** The value `config` is moved into the closure on line 14 but then used again on line 18 after the move.

**Why:** Rust's ownership model does not allow a value to be used after it has been moved. The closure captures `config` by move because it's used in a `thread::spawn` call, which requires `'static` lifetime. After the spawn, `config` no longer exists in the outer scope.

**Fix:**
```rust
let config = Arc::new(config);
let config_clone = Arc::clone(&config);
thread::spawn(move || {
    process(config_clone);
});
println!("{}", config.name); // now valid — Arc keeps the data alive
```

**Structural alternative:** Wrap shared state in `Arc<Mutex<T>>` from the start when any value will be accessed across thread boundaries. This eliminates this entire class of move errors.
