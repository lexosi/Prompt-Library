# Evaluación de Riesgo: Feature IA

**Categoría:** decision-making
**Cuándo usar:** Evaluar riesgo de alucinación, mal uso, privacidad y deriva antes de lanzar una feature de IA.

---

Eres un ingeniero de seguridad de productos de IA. Evalúa los riesgos de lanzar la siguiente característica de IA. Sé específico — nombra modos de fallo reales con estimaciones realistas de probabilidad e impacto, no categorías abstractas.

**Descripción de la característica:**
[describe qué hace la característica de IA, quién la usa y cómo se integra en el producto]

**Modelo y enfoque de prompting:**
[e.g., Claude 3.5 Sonnet con system prompt aumentado por RAG, zero-shot]

**Población de usuarios:**
[quién la usará — sofisticación técnica, apuestas de las decisiones que toman con ella]

**Evalúa estas dimensiones de riesgo:**

1. **Riesgo de alucinación:** ¿En qué situaciones específicas producirá el modelo salidas incorrectas con confianza? ¿Cuál es el impacto en el usuario cuando lo hace?

2. **Riesgo de mal uso:** ¿Cómo podría un usuario usar intencionalmente esta característica para causar daño — a sí mismo, a otros o al negocio?

3. **Riesgo de datos/privacidad:** ¿Qué datos sensibles toca esta característica? ¿Qué ocurre si se filtran?

4. **Riesgo de dependencia:** ¿Qué ocurre si el proveedor del modelo tiene una interrupción? ¿Si el modelo es deprecado?

5. **Riesgo de deriva:** ¿Cómo sabrás si la calidad de la característica se degrada con el tiempo (actualizaciones del modelo, cambio de distribución, inyección de prompts)?

**Para cada riesgo:** Probabilidad (Baja/Media/Alta), Impacto (Bajo/Medio/Alto/Crítico), y la mitigación específica que recomiendas.

**Recomendación de lanzar/no lanzar:** Dado lo anterior, ¿está listo para lanzarse? Si no, ¿qué debe ser cierto antes de lanzar?

---

## Ejemplo de output

**Feature:** AI medical symptom checker that suggests possible conditions based on user-described symptoms.

**Risk 1 — Hallucination (Probability: HIGH, Impact: CRITICAL):** The model will confidently suggest a benign condition when the user has a serious one. Most likely failure: user describes atypical presentation of MI as indigestion; model suggests antacids. Mitigation: Mandatory disclaimer on every response + explicit "if symptoms are severe, call emergency services" trigger for specific keyword combinations. Block output if symptom matches emergency keywords without displaying the suggestion first.

**Risk 2 — Misuse (Probability: MEDIUM, Impact: HIGH):** Users may use the tool to self-diagnose and avoid seeking medical care for serious conditions. Mitigation: Every response must include "This is not medical advice. See a doctor for diagnosis." in a visually prominent format — not buried in fine print.

**Ship recommendation:** Do not ship without: (1) emergency symptom detection with hard-coded redirects to emergency services, (2) mandatory human review of all outputs in the first 30 days, (3) legal sign-off on disclaimers.
