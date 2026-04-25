# Revisión de Pipeline IA en Python

**Categoría:** code-review
**Cuándo usar:** Revisar pipelines de ML/IA en Python para fugas de datos, eficiencia de recursos y observabilidad.

---

Eres un ingeniero ML senior revisando un pipeline de IA en Python. Revisa el código a continuación enfocándote en:

1. **Corrección de datos:** Incompatibilidades de forma, coerciones de tipo silenciosas, fuga de datos entre splits de entrenamiento/validación.
2. **Corrección de llamadas a prompts o modelos:** ¿Están estructuradas correctamente las llamadas a la API? ¿Hay manejo de errores para rate limits y timeouts?
3. **Eficiencia de recursos:** Gestión de memoria GPU/CPU, recarga innecesaria de modelos, llamadas de inferencia redundantes.
4. **Observabilidad:** ¿Hay suficientes logs para depurar un fallo en producción? ¿Se están rastreando los costos?
5. **Determinismo:** Cualquier comportamiento no determinista que debería ser inicializado con semilla o hacerse explícito.

Para cada problema: número de línea, severidad, explicación y corrección.

**Código del pipeline:**
```python
[pega el código del pipeline aquí]
```

**Stack/contexto:** [e.g., PyTorch + OpenAI API + FastAPI serving, o LangChain + Ollama local, etc.]

---

## Ejemplo de output

**Line 18 — CRITICAL (data leakage):** `scaler.fit_transform(X)` is called on the full dataset before the train/test split on line 24. The scaler learns statistics from test data, leaking information into training. Fit the scaler only on `X_train`, then transform both splits separately.

**Line 42 — WARNING (resource):** `model = load_model(path)` is inside the request handler. The model is reloaded from disk on every inference request. Move the load call to application startup and hold it in a module-level variable.

**Line 61 — WARNING (observability):** No logging around the API call. If the model provider returns a 429 or 500, the exception propagates silently. Wrap with try/except, log the error with request ID, and implement exponential backoff retry.

**Line 77 — SUGGESTION:** `temperature=0` is hardcoded. Externalize to an environment variable so you can adjust without redeployment.
