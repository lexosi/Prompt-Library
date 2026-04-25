# Python Async Refactor

**Category:** refactor
**When to use:** Migrating synchronous Python code to async/await, or fixing async code that runs sequentially when it should run concurrently.

---

You are a Python concurrency expert. Refactor the code below to use proper async/await. The goal is not just to add `async` keywords but to make I/O-bound operations genuinely concurrent.

For each change:
1. Show the before and after code.
2. Explain what was blocking and what it's doing now instead.
3. Flag any operations that should NOT be made async (CPU-bound work that needs `ProcessPoolExecutor`).
4. If any operations can run concurrently (not just sequentially async), show how to use `asyncio.gather()` or `asyncio.TaskGroup`.
5. Identify any sync libraries that need to be replaced (e.g., `requests` → `httpx`, `psycopg2` → `asyncpg`).

**Current synchronous code:**
```python
[paste code here]
```

**Runtime context:** [e.g., FastAPI app, standalone CLI script, Celery worker, pytest suite]

**Performance goal:** [e.g., handle 100 concurrent requests, reduce latency from 5s to < 1s]

---

## Example output

**Change 1 — Sequential HTTP calls → concurrent:**

Before:
```python
def fetch_all(urls: list[str]) -> list[dict]:
    results = []
    for url in urls:
        r = requests.get(url)   # blocks — each call waits for the previous
        results.append(r.json())
    return results
```

After:
```python
import httpx
import asyncio

async def fetch_all(urls: list[str]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)   # all fire concurrently
        return [r.json() for r in responses]
```

What changed: `requests` blocked the event loop per call — 10 URLs × 200ms = 2 seconds sequentially. `httpx` + `asyncio.gather` fires all requests simultaneously — 10 URLs × 200ms = ~200ms total.

**Library replacements needed:**
- `requests` → `httpx[asyncio]`
- `psycopg2` → `asyncpg` (if database calls exist)
