# Refactor Async de Python

**Categoría:** refactor
**Cuándo usar:** Migrar Python síncrono a async/await genuino con operaciones de I/O concurrentes.

---

Eres un experto en concurrencia de Python. Refactoriza el código a continuación para usar async/await correctamente. El objetivo no es solo agregar palabras clave `async` sino hacer que las operaciones vinculadas a I/O sean genuinamente concurrentes.

Para cada cambio:
1. Muestra el código antes y después.
2. Explica qué estaba bloqueando y qué hace ahora en su lugar.
3. Marca cualquier operación que NO deba hacerse async (trabajo vinculado a CPU que necesita `ProcessPoolExecutor`).
4. Si alguna operación puede ejecutarse concurrentemente (no solo async secuencialmente), muestra cómo usar `asyncio.gather()` o `asyncio.TaskGroup`.
5. Identifica cualquier librería síncrona que deba reemplazarse (e.g., `requests` → `httpx`, `psycopg2` → `asyncpg`).

**Código síncrono actual:**
```python
[pega el código aquí]
```

**Contexto de ejecución:** [e.g., app FastAPI, script CLI standalone, Celery worker, suite pytest]

**Objetivo de rendimiento:** [e.g., manejar 100 solicitudes concurrentes, reducir latencia de 5s a < 1s]

---

## Ejemplo de output

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
