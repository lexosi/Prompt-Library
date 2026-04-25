# Depurar Cadena de Pensamiento

**Categoría:** prompt-debugging
**Cuándo usar:** Encontrar el paso exacto donde el razonamiento multi-paso falla y corregir el prompt.

---

Eres un experto en ingeniería de prompts especializado en razonamiento en cadena de pensamiento. La cadena de razonamiento a continuación llega a una conclusión incorrecta. Identifica exactamente dónde se equivocó el razonamiento y corrígelo.

Analiza:
1. **Diagnóstico a nivel de paso:** Revisa cada paso de razonamiento e identifica el primer paso donde el modelo comete un error (factual, lógico o aritmético). Todo lo que sigue a un paso incorrecto es razonamiento sobre una premisa falsa.
2. **Tipo de error:** ¿Es esto un error factual (información incorrecta), error lógico (inferencia inválida), error aritmético, o un error de encuadre (el modelo resolvió un problema diferente al pretendido)?
3. **Causa raíz en el prompt:** ¿Qué en el prompt o contexto original causó que el modelo cometiera este error? (¿Fraseo ambiguo, contexto faltante, suposición implícitamente incorrecta?)
4. **Corrección del prompt:** ¿Cómo debería cambiar el prompt para prevenir este error específico? Opciones:
   - Agregar puntos de control intermedios ("Antes de continuar, verifica que X sea verdadero")
   - Agregar restricciones explícitas ("No asumas Y — verifícalo en el contexto")
   - Reestructurar la tarea en sub-preguntas
5. **Prompt reescrito:** El prompt revisado con la corrección aplicada.

**Prompt original:**
```
[pega el prompt que produjo la cadena de razonamiento defectuosa]
```

**Cadena de razonamiento defectuosa:**
```
[pega el razonamiento paso a paso del modelo y la conclusión incorrecta]
```

**Respuesta correcta:** [cuál debería ser la respuesta]

---

## Ejemplo de output

**Step-level diagnosis:**
- Step 1: "The request has 3 items" — CORRECT
- Step 2: "Each item costs $12.50" — CORRECT
- Step 3: "Total = 3 × $12.50 = $36.50" — ERROR. 3 × 12.50 = 37.50, not 36.50. This is an arithmetic error.
- Step 4 onward: All subsequent reasoning uses $36.50 as the base — all subsequent answers are wrong.

**Error type:** Arithmetic error in a multiplication step.

**Root cause in the prompt:** The prompt asked the model to "work through the math step by step" but did not ask it to verify intermediate calculations. The model performs the arithmetic inline without checking it.

**Prompt fix:** Add a verification checkpoint after arithmetic steps:
```
After each calculation, verify your result by computing it a second way (e.g., repeated addition instead of multiplication).
```

**Rewritten prompt:**
```
[original task]

Work through this step by step. After any multiplication or division, verify the result using an alternative method (e.g., verify 3 × 12.50 by adding 12.50 + 12.50 + 12.50). If the two methods disagree, recompute before continuing.
```

**Why this works:** The verification step forces the model to catch arithmetic errors before they propagate through the rest of the chain.
