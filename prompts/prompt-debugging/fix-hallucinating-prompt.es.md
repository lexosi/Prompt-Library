# Corregir Prompt que Alucina

**Categoría:** prompt-debugging
**Cuándo usar:** Identificar la causa raíz de los desencadenantes de alucinación y reestructurar el prompt para anclar el modelo.

---

Eres un experto en ingeniería de prompts especializado en reducción de alucinaciones. El prompt a continuación está causando que un modelo produzca información falsa con confianza. Diagnostica la causa raíz y corrígelo.

Analiza:
1. **Diagnóstico del disparador de alucinación:** ¿Por qué está alucinando el modelo? Causas comunes: se le pide producir información que no tiene, se le pide especificidades en temas donde carece de conocimiento confiable, presión de formato (e.g., "da 5 ejemplos" fuerza la invención cuando solo existen 3), o contexto de fundamentación faltante.
2. **Problema de calibración de confianza:** ¿Está el modelo presentando información incierta como cierta? ¿Qué en el prompt está suprimiendo su incertidumbre?
3. **Correcciones estructurales:** Cambios al prompt que reducen la alucinación sin reducir la utilidad:
   - Agregar permiso explícito para decir "no sé"
   - Proporcionar material fuente del que el modelo debería extraer
   - Cambiar la tarea de "producir hechos" a "razonar desde contexto proporcionado"
   - Agregar pasos de verificación ("antes de responder, lista en qué estás seguro vs. incierto")
4. **Prompt reescrito:** El prompt revisado.
5. **Riesgo residual:** ¿Qué riesgo de alucinación permanece incluso con la corrección?

**Prompt original:**
```
[pega el prompt que está alucinando]
```

**Ejemplo de salida alucinada:**
```
[pega un ejemplo que muestre la información falsa]
```

**Lo que realmente necesitas:** [describe cómo se vería una salida precisa]

---

## Ejemplo de output

**Hallucination trigger:** The prompt asks the model to "list all papers published on X topic in 2024." The model doesn't have reliable recall of specific publications and dates, but the task demands a complete list — so it invents entries to satisfy the completeness requirement.

**Confidence calibration problem:** The imperative "list all" removes the model's ability to hedge. It interprets the instruction as "produce a complete, confident list," even when it cannot do so reliably.

**Structural fixes:**
1. Switch from open recall to grounded reasoning: provide a list of papers (from a real source) and ask the model to analyze or summarize them.
2. Add explicit uncertainty permission: "If you are not certain a paper exists and was published in this exact year, do not include it. Prefer a short accurate list over a long inaccurate one."
3. Add a verification step: "Before answering, state how confident you are in each entry on a scale of Low/Medium/High."

**Rewritten prompt:**
```
Below is a list of papers on [topic] from 2024 that I have verified. Summarize the key findings from each and identify common themes. Do not add papers not in this list.

[paste your verified paper list here]
```

**Remaining risk:** If the provided source list itself contains errors, the model will reason faithfully from incorrect input. Verify your source material independently.
