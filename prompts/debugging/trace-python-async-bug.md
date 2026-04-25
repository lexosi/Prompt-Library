# Trace Python Async Bug

**Category:** debugging
**When to use:** An asyncio-based Python program is deadlocking, racing, or producing inconsistent results across runs.

---

You are a Python concurrency expert. I have an asyncio bug I cannot reproduce reliably. Analyze the code and error below and:

1. Identify whether the issue is a deadlock, race condition, event loop blocking, or coroutine lifecycle problem.
2. Pinpoint the exact lines responsible.
3. Explain what happens in the event loop at the moment of failure.
4. Show the corrected code with a comment on each changed line explaining why.

Assume Python 3.11+. Do not suggest switching to threading or multiprocessing unless the event loop itself is the wrong tool.

**Error / symptom:**
```
[paste stack trace or describe the symptom: hangs, wrong value, never resolves]
```

**Code:**
```python
[paste the relevant async functions and their callers]
```

**Runtime context:** [e.g., FastAPI endpoint, standalone script, pytest-asyncio test]

---

## Example output

**Issue type:** Event loop blocking — a synchronous I/O call inside an async function is blocking the event loop thread.

**Line responsible:** `result = requests.get(url)` on line 23. `requests` is synchronous and blocks the entire event loop while waiting for the HTTP response.

**What happens:** When `fetch_data()` is awaited, Python schedules it as a coroutine. But `requests.get()` is a blocking call — it doesn't yield control back to the event loop, so all other coroutines waiting to run are frozen until the HTTP call completes.

**Fix:**
```python
import httpx

async def fetch_data(url: str) -> dict:
    async with httpx.AsyncClient() as client:   # non-blocking HTTP client
        response = await client.get(url)         # yields control to event loop while waiting
        return response.json()
```
