# Diagnosticar Output Vago

**Categoría:** prompt-debugging
**Cuándo usar:** Identificar por qué un prompt produce respuestas genéricas y reescribirlo para mayor especificidad.

---

Eres un experto en ingeniería de prompts. Estoy obteniendo salidas vagas y genéricas de un modelo de IA cuando necesito respuestas específicas y detalladas. Diagnostica por qué y corrígelo.

Analiza el prompt y la mala salida a continuación:

1. **Diagnóstico de especificidad:** ¿Qué le falta especificar al prompt que permite al modelo dar una respuesta genérica? Lista cada restricción faltante.
2. **Diagnóstico de ambigüedad:** ¿Qué términos en el prompt podrían interpretarse de múltiples maneras? El modelo está eligiendo la interpretación más segura/fácil.
3. **Diagnóstico de formato:** ¿Le faltan al prompt instrucciones de formato que forzarían especificidad (e.g., "da exactamente 3 ejemplos," "formatea como tabla," "cita números de línea específicos")?
4. **Prompt reescrito:** Proporciona un prompt revisado que aborde todos los problemas identificados.
5. **Predicción:** ¿Qué será específicamente diferente en la salida con el nuevo prompt?

**Prompt original:**
```
[pega el prompt que está produciendo salida vaga]
```

**Ejemplo de mala salida:**
```
[pega un ejemplo de la respuesta vaga/genérica que estás obteniendo]
```

**Lo que realmente querías:**
[describe la respuesta específica y detallada que necesitabas]

---

## Ejemplo de output

**Specificity diagnosis:**
- "Analyze the code" — the model doesn't know what dimension to analyze: performance? security? style? correctness? It's picking all of them shallowly.
- "Give feedback" — feedback at what level? The model is defaulting to high-level architectural comments when you want line-level specifics.
- No scope limit — the model is spreading attention across the entire file instead of focusing on the critical paths.

**Ambiguity diagnosis:**
- "Good code" is a value judgment that varies by context. The model has no defined standard to evaluate against.

**Rewritten prompt:**
```
Review ONLY the authentication middleware in the code below. For each security vulnerability you find:
1. Quote the exact line(s) where it occurs
2. Name the vulnerability type (e.g., "timing attack," "SQL injection surface")
3. Rate severity: Critical / High / Medium
4. Give the 1–3 line fix

Ignore style, performance, and architecture. Only security.
```

**Prediction:** Output will cite specific line numbers, name specific vulnerability types, and provide concrete fixes instead of general recommendations.
