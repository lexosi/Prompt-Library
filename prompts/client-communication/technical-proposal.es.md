# Propuesta Técnica

**Categoría:** client-communication
**Cuándo usar:** Proponer un enfoque técnico de manera creíble tanto para lectores técnicos como no técnicos.

---

Escribe un documento de propuesta técnica para un cliente. El documento debe ser legible para un stakeholder no técnico pero creíble para uno técnico. Debe responder su pregunta no expresada: "¿Sabe esta gente lo que está haciendo, y realmente funcionará?"

Estructura:
1. **Declaración del problema:** Qué estamos resolviendo — en el lenguaje del cliente, no en términos técnicos.
2. **Enfoque propuesto:** La solución técnica en lenguaje sencillo. Un párrafo. Sin detalles de implementación todavía.
3. **Por qué este enfoque:** 2–3 razones específicas por las que este enfoque se ajusta a su situación. No beneficios genéricos — razones vinculadas a su contexto.
4. **Cómo funciona (resumen técnico):** Una descripción técnica corta y honesta para lectores técnicos. Diagramas opcionales.
5. **Lo que necesitamos de ti:** Prerrequisitos, acceso, datos, decisiones que el cliente debe proporcionar antes de que comience el trabajo.
6. **Cronograma y fases:** Fases con duraciones. Qué se entrega al final de cada fase.
7. **Riesgos y mitigaciones:** 2–3 riesgos reales, declarados honestamente, con cómo los mitigarás.
8. **Inversión:** Costo y estructura de pagos. Claro y específico.

**Contexto:**
- Cliente: [describe]
- Problema: [describe]
- Solución propuesta: [describe]
- Cronograma: [estimación]
- Presupuesto: [monto]

---

## Ejemplo de output

**Problem statement:** Your support team spends 4–6 hours daily answering the same 40 questions. As your customer base grows, this scales linearly — more customers means more headcount, not better service.

**Proposed approach:** We'll build an AI assistant trained on your existing support documentation that answers common questions instantly, 24/7. Complex or sensitive questions are automatically routed to your team with the full conversation context.

**Why this approach for you:** (1) Your documentation is already well-organized — this dramatically reduces the training time and cost. (2) Your customer base is primarily technical — they'll tolerate (and often prefer) AI assistance over waiting for a human. (3) Zendesk integration means no workflow change for your support team.

**Risks:** Integration complexity with your legacy ticketing system. Mitigation: We'll build a thin adapter layer rather than deep integration, keeping the risk surface small.

**Investment:** $12,000 total. 50% upfront, 50% on delivery. Timeline: 6 weeks.
