# Revisión de Uso de Herramientas del Agente

**Categoría:** code-review
**Cuándo usar:** Revisar definiciones de herramientas de agentes IA y lógica de llamadas para seguridad y claridad.

---

Eres un ingeniero de sistemas de IA revisando las definiciones de herramientas y la lógica de llamadas a herramientas de un agente de IA. Revisa lo siguiente con estas prioridades:

1. **Corrección del schema de herramienta:** ¿Son precisos e inequívocos los tipos de parámetros, campos requeridos y descripciones? ¿Sabría el modelo exactamente cuándo y cómo llamar a esta herramienta?
2. **Calidad de descripción de herramienta:** ¿Le dice la descripción al modelo CUÁNDO usar esta herramienta vs. otras? ¿Están documentados los casos límite y exclusiones?
3. **Seguridad:** ¿Puede alguna herramienta ser llamada de una manera que cause daño irreversible — eliminar datos, enviar mensajes, cobrar dinero? ¿Hay guardas?
4. **Manejo de errores en resultados de herramientas:** ¿Dan las respuestas de herramientas suficiente información al modelo para recuperarse de fallos de forma elegante?
5. **Superficie de herramientas:** ¿Hay herramientas redundantes que se superponen en propósito? ¿Podrían fusionarse o eliminarse herramientas?

**Definiciones de herramientas:**
```json
[pega aquí los schemas completos de herramientas/funciones]
```

**Lógica de ejecución de herramientas (si está disponible):**
```python / typescript / rust
[pega el código backend que implementa las herramientas]
```

**System prompt del agente (secciones relevantes):**
```
[pega las partes que hacen referencia al uso de herramientas]
```

---

## Ejemplo de output

**Tool `delete_record` — CRITICAL (safety):** The tool has no `confirm` parameter and no description of its irreversibility. An agent under ambiguous instructions could call this without understanding it's permanent. Add a required `reason` parameter, and update the description: "Permanently deletes a record. Cannot be undone. Only call this when the user has explicitly confirmed deletion."

**Tool `search_docs` — WARNING (description quality):** The description says "search for documents." This is too vague — when should the agent use this vs. `get_document_by_id`? Rewrite to: "Search for documents when you have keywords but not a specific ID. Use get_document_by_id when you already know the exact document ID."

**Tools `send_slack` and `send_email` — SUGGESTION (surface):** Both tools have nearly identical schemas. If the agent frequently confuses them, consider merging into `send_message` with a `channel` parameter (`slack` or `email`).
