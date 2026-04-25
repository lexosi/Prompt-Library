# Rastrear Bug Async en Python

**Categoría:** debugging
**Cuándo usar:** Identificar deadlocks, condiciones de carrera y bloqueos del event loop en código asyncio.

---

Eres un experto en concurrencia de Python. Tengo un bug de asyncio que no puedo reproducir de forma confiable. Analiza el código y el error a continuación y:

1. Identifica si el problema es un deadlock, una condición de carrera, bloqueo del event loop, o un problema en el ciclo de vida de una corrutina.
2. Señala exactamente las líneas responsables.
3. Explica qué ocurre en el event loop en el momento del fallo.
4. Muestra el código corregido con un comentario en cada línea modificada explicando el porqué.

Asume Python 3.11+. No sugieras cambiar a threading o multiprocessing a menos que el event loop sea fundamentalmente la herramienta equivocada.

**Error / síntoma:**
```
[pega el stack trace o describe el síntoma: se cuelga, valor incorrecto, nunca resuelve]
```

**Código:**
```python
[pega las funciones async relevantes y sus llamadores]
```

**Contexto de ejecución:** [e.g., endpoint FastAPI, script independiente, test pytest-asyncio]

---

## Ejemplo de output

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
