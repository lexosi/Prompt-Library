# Ejemplos Few-Shot

**Categoría:** context-preparation
**Cuándo usar:** Diseñar ejemplos few-shot que cubran el camino feliz, casos límite y anti-patrones.

---

Eres un ingeniero de prompts especializado en diseño de ejemplos few-shot. Crea un conjunto de ejemplos few-shot de alta calidad para la tarea a continuación. Los ejemplos few-shot bien diseñados hacen más que mostrar el formato de salida — demuestran el patrón de razonamiento, manejan casos límite e implícitamente enseñan al modelo qué NO hacer.

Para cada ejemplo:
1. Cubre un escenario distinto — ruta feliz, caso límite y al menos un caso "difícil" donde el enfoque incorrecto es tentador.
2. Muestra el par entrada-salida exacto — nada más.
3. Si la tarea implica razonamiento, muestra el razonamiento en la salida (no como un paso "pensar" separado).

Después de los ejemplos, proporciona:
- **Análisis de cobertura:** Qué casos están cubiertos y qué falta aún.
- **Ejemplo de anti-patrón:** Un ejemplo que muestre cómo se ve una salida MALA — etiquetado claramente, para usar en el system prompt como un ejemplo de "NO hagas esto."

**Descripción de la tarea:**
[describe exactamente qué debe hacer el modelo — tipo de entrada, tipo de salida, reglas de decisión]

**Formato de salida deseado:**
[muestra la estructura de salida exacta que deseas]

**Casos límite a cubrir:**
[lista los casos límite que sabes que existen]

---

## Ejemplo de output

**Task:** Classify customer support messages as: Bug Report / Feature Request / Billing Question / Other. Return only the classification and a one-sentence reason.

**Example 1 (happy path — Bug Report):**
Input: "The export button stopped working after yesterday's update. It just shows a loading spinner forever."
Output: Bug Report — The user describes behavior that worked previously and is now broken after a specific event.

**Example 2 (happy path — Feature Request):**
Input: "It would be great if I could export reports in CSV format, not just PDF."
Output: Feature Request — The user is asking for new functionality that doesn't currently exist.

**Example 3 (tricky — could be Bug OR Feature):**
Input: "The search doesn't find results when I use quotes around phrases."
Output: Bug Report — Quoted phrase search is an expected behavior in most search interfaces; its absence is more likely a broken feature than a missing one.

**Example 4 (edge case — ambiguous):**
Input: "I was charged twice this month."
Output: Billing Question — The user is reporting a financial discrepancy, regardless of whether it's a bug or a billing system issue.

**Anti-pattern (do NOT do this):**
Input: "The export button stopped working."
Output: ❌ This could be a Bug Report or Feature Request or Billing Question — I need more information. → This output delays resolution. Classify with the most likely category based on available information.
