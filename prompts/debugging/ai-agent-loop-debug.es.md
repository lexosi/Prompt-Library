# Depurar Bucle de Agente IA

**Categoría:** debugging
**Cuándo usar:** Diagnosticar un agente IA atascado en un bucle, que llama herramientas incorrectas o alucina estado.

---

Eres un ingeniero de sistemas de IA especializado en arquitecturas de agentes LLM. Tengo un agente que está funcionando mal. Analiza la trayectoria del agente a continuación y:

1. Identifica el modo de fallo: ¿es un bucle, una selección incorrecta de herramienta, contexto alucinado o una mala interpretación del objetivo?
2. Señala el paso exacto en la trayectoria donde el agente se desvió.
3. Explica por qué el agente tomó esa decisión — qué en el prompt o el contexto lo causó.
4. Proporciona una corrección concreta: un cambio en el prompt, una mejora en la definición de herramienta, o una corrección en la gestión de estado.

**Framework del agente:** [e.g., Claude tool use, LangChain, AutoGen, personalizado]
**System prompt:** [pega o describe]

**Definiciones de herramientas (abreviadas):**
```json
[pega los schemas de herramientas relevantes]
```

**Trayectoria del agente (historial completo de turnos):**
```
[pega la secuencia de turnos del usuario, respuestas del asistente y llamadas/resultados de herramientas]
```

**Comportamiento esperado:**
[qué debería haber hecho el agente]

---

## Ejemplo de output

**Failure mode:** Tool selection loop. The agent is calling `search_documents` repeatedly with slightly rephrased queries because it never receives a clear termination signal when the search returns empty results.

**Where it went wrong:** Turn 4. The tool returned `{"results": []}` and the agent interpreted this as "search was incomplete" rather than "no documents match." This is a prompt-level ambiguity.

**Why:** The system prompt says "keep searching until you find the answer" — the agent is following instructions correctly, but the instruction doesn't account for the case where no answer exists.

**Fix — system prompt change:**
```
Search for information using search_documents. If the tool returns empty results after 2 attempts with different queries, respond with "I could not find relevant information" and stop. Do not search more than 3 times total.
```

**Fix — tool output improvement:** Add an `exhausted` field to the tool response schema so the agent gets an explicit signal when there's nothing more to find.
