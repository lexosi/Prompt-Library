# Monolito a Agentes

**Categoría:** refactor
**Cuándo usar:** Descomponer un proceso monolítico en un sistema multi-agente coordinado.

---

Eres un arquitecto de sistemas de IA. Tengo un proceso monolítico que quiero descomponer en un sistema de agentes de IA coordinados. Analiza el proceso a continuación y produce un plan de descomposición.

Tu salida debe incluir:
1. **Límites naturales de agentes:** ¿Dónde en el proceso se separan claramente las responsabilidades? ¿Cuáles son los "puntos de entrega" naturales entre agentes?
2. **Definiciones de agentes:** Para cada agente propuesto: nombre, única responsabilidad, entradas, salidas, herramientas necesarias.
3. **Lógica de orquestación:** ¿Cómo sabe el orquestador cuándo entregar al siguiente agente? ¿Cuál es la estructura de estado pasada entre ellos?
4. **Lo que permanece como código:** ¿Qué partes del proceso deben permanecer como código determinista (no razonamiento LLM) incluso en el sistema de agentes? Explica por qué.
5. **Manejo de fallos:** Si un agente produce una salida incorrecta, ¿cómo detecta y se recupera el sistema?
6. **Costo estimado en tokens:** Estimación aproximada de las llamadas LLM y el uso de tokens por ejecución en el nuevo sistema vs. el prompt monolítico.

**Proceso monolítico actual:**
```
[describe o pega el proceso actual — puede ser un prompt grande, un script Python, o una descripción de pipeline]
```

**Objetivo del refactor:**
[e.g., mejorar confiabilidad, habilitar paralelismo, hacer el sistema testeable por etapa, reducir alucinaciones]

---

## Ejemplo de output

**Natural agent boundaries in a content pipeline:**

1. `ResearchAgent` — gathers source material from web search and document retrieval. Hands off: a structured list of facts with citations.
2. `OutlineAgent` — builds a content structure from facts. Hands off: a hierarchical outline with section assignments.
3. `WritingAgent` — writes each section independently. Can run in parallel per section. Hands off: raw section drafts.
4. `EditingAgent` — reviews all sections for consistency and tone. Hands off: final polished draft.

**What stays code:** Citation formatting, section merging, output rendering to Markdown/HTML. These are deterministic transformations — using an LLM for them adds cost and variability with no benefit.

**Failure handling:** After each agent, validate output against a JSON schema. If the schema check fails, re-run the agent once with the validation error appended to the prompt. If it fails twice, halt and surface the error with the partial output for human review.
