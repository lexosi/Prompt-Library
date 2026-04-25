# Mejorar Especificidad del Prompt

**Categoría:** prompt-debugging
**Cuándo usar:** Hacer un prompt inconsistente confiable eliminando ambigüedad y varianza de formato.

---

Eres un experto en ingeniería de prompts. El prompt a continuación produce resultados inconsistentes — a veces buenos, a veces no. Hazlo confiable aumentando la especificidad sin hacerlo rígido o verbose.

Analiza:
1. **Fuentes de varianza:** ¿Qué elementos del prompt están suficientemente sub-especificados para permitir interpretaciones muy diferentes entre ejecuciones? Lista cada uno.
2. **Suposiciones ocultas:** ¿Qué asume el prompt que el modelo sabe o hará que en realidad no está garantizado? Indica cada suposición.
3. **Ambigüedad de formato de salida:** ¿Está claro el formato de salida esperado? Si el modelo tiene latitud sobre la estructura, la variará.
4. **Brechas en casos límite:** ¿Qué casos límite (entrada vacía, casos fronterizos, formatos inesperados) no está manejando el prompt? ¿Cómo se comporta actualmente el modelo en esos casos?
5. **Prompt reescrito:** Versión más específica que preserva la intención original pero elimina la varianza.
6. **Verificación de regresión:** Lista 3 casos de prueba (ruta feliz, caso límite, entrada adversarial) que deberías ejecutar para verificar que el nuevo prompt funciona mejor.

**Prompt original:**
```
[pega el prompt inconsistente]
```

**Ejemplo de una BUENA salida de este prompt:**
```
[pega un ejemplo de cuando funcionó bien]
```

**Ejemplo de una MALA salida de este prompt:**
```
[pega un ejemplo de cuando falló]
```

---

## Ejemplo de output

**Variance sources:**
- "Summarize the article" — summary length is unspecified: the model varies between 2 sentences and 8 paragraphs.
- "Key points" — what counts as "key" is subjective: the model sometimes focuses on facts, sometimes on implications, sometimes on recommendations.
- No persona or audience specified — the register (formal/informal, technical/accessible) varies run to run.

**Hidden assumptions:**
- The prompt assumes the model will read the full article before summarizing. In longer documents, it sometimes stops reading at a natural section boundary.
- The prompt assumes "summary" means a paragraph, but the model sometimes produces a bullet list.

**Rewritten prompt:**
```
Summarize the following article in exactly 3 bullet points. Each bullet:
- Starts with a bold key claim (5–8 words)
- Followed by 1 sentence of supporting evidence from the article
- Is written for a non-technical business reader

Do not add bullets for things not explicitly stated in the article. Do not editorialize.

Article:
[article text]
```

**Regression tests:**
1. Happy path: a well-structured news article → expect 3 clean bullets.
2. Edge case: an article with only one main claim → expect 3 bullets where 2 are supporting details, not invented claims.
3. Adversarial: a very long article → expect the model still reads fully and doesn't just summarize the introduction.
