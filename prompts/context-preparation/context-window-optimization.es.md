# Optimización de Ventana de Contexto

**Categoría:** context-preparation
**Cuándo usar:** Reducir el footprint de tokens de contexto sin perder información crítica para la tarea.

---

Eres un ingeniero de sistemas de IA especializado en eficiencia de ventana de contexto. Analiza el contexto a continuación y reduce su huella de tokens sin perder la información que afecta la calidad de salida del modelo.

Principios de optimización en orden de prioridad:
1. **Eliminar redundancia:** La información que el modelo ya conoce por entrenamiento (e.g., "Python es un lenguaje de programación") desperdicia tokens.
2. **Comprimir instrucciones verbosas:** Las instrucciones largas pueden acortarse sin perder significado. Encuentra cada instrucción que pueda reescribirse en la mitad de palabras.
3. **Priorizar recencia:** En historiales de conversación largos, los turnos anteriores importan menos que los recientes. Resume el contexto más antiguo; mantén el contexto reciente verbatim.
4. **Mover contexto estable al system prompt:** La información que no cambia por solicitud pertenece al system prompt, no al turno del usuario.
5. **Truncar contenido de baja señal:** Archivos de log, stack traces largos, contenidos de archivos completos — identifica qué partes son de alta señal y corta el resto.

Para cada sección del contexto:
1. Estimación de tokens actual
2. Qué puede cortarse o comprimirse
3. Versión revisada
4. Estimación de tokens después de la revisión

**Reducción objetivo:** [e.g., reducir de 15,000 a menos de 8,000 tokens preservando información crítica para la tarea]

**Contexto a optimizar:**
```
[pega el contexto completo: system prompt, historial de conversación, documentos inyectados, resultados de herramientas]
```

---

## Ejemplo de output

**Section: System prompt (estimated 1,200 tokens)**
Compression opportunities:
- Lines 4–12 explain what JSON is and why it's used — model knows this, cut entirely (saves ~150 tokens).
- Lines 15–24 have 4 bullet points that all say "be thorough" in different words — collapse to one line.

Revised system prompt section: [compressed version — 680 tokens]
Savings: 520 tokens (43% reduction)

**Section: Conversation history (estimated 8,000 tokens)**
Turns 1–15 (old context) can be summarized to:
"User is debugging a Rust async function that deadlocks when called concurrently. We identified the Arc<Mutex> wrapping is correct but the lock is held across an await point. User confirmed the structure."
This summary: ~80 tokens vs. 3,200 tokens for the turns. Savings: 3,120 tokens.

**Section: Stack trace (estimated 2,400 tokens)**
Only the first 3 frames and the error message are diagnostic. Cut frames 4–47.
Savings: ~1,800 tokens.

**Total: from 11,600 to 5,440 tokens — 53% reduction** with no loss of task-critical information.
