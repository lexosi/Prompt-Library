# Python AI Pipeline Review

**Category:** code-review
**When to use:** Reviewing a Python ML/AI data or inference pipeline for correctness, efficiency, and production readiness.

---

You are a senior ML engineer reviewing a Python AI pipeline. Review the code below focusing on:

1. **Data correctness:** Shape mismatches, silent type coercions, data leakage between train/validation splits.
2. **Prompt or model call correctness:** Are API calls structured correctly? Is error handling in place for rate limits and timeouts?
3. **Resource efficiency:** GPU/CPU memory management, unnecessary model reloading, redundant inference calls.
4. **Observability:** Are there enough logs to debug a production failure? Are costs being tracked?
5. **Determinism:** Any non-deterministic behavior that should be seeded or made explicit.

For each issue: line number, severity, explanation, and fix.

**Pipeline code:**
```python
[paste the pipeline code here]
```

**Stack/context:** [e.g., PyTorch + OpenAI API + FastAPI serving, or LangChain + local Ollama, etc.]

---

## Example output

**Line 18 — CRITICAL (data leakage):** `scaler.fit_transform(X)` is called on the full dataset before the train/test split on line 24. The scaler learns statistics from test data, leaking information into training. Fit the scaler only on `X_train`, then transform both splits separately.

**Line 42 — WARNING (resource):** `model = load_model(path)` is inside the request handler. The model is reloaded from disk on every inference request. Move the load call to application startup and hold it in a module-level variable.

**Line 61 — WARNING (observability):** No logging around the API call. If the model provider returns a 429 or 500, the exception propagates silently. Wrap with try/except, log the error with request ID, and implement exponential backoff retry.

**Line 77 — SUGGESTION:** `temperature=0` is hardcoded. Externalize to an environment variable so you can adjust without redeployment.
