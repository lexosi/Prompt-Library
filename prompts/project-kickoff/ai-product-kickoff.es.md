# Kickoff de Producto IA

**Categoría:** project-kickoff
**Cuándo usar:** Documento de kickoff de una página que alinea ingeniería, producto y stakeholders antes de escribir código.

---

Escribe un documento de kickoff para un producto impulsado por IA. El documento debe caber en una página y crear alineación entre ingeniería, producto y cualquier stakeholder antes de que comience el trabajo.

El documento debe cubrir:

**RESUMEN DEL PRODUCTO:** Qué hace, para quién, y el problema específico que resuelve — en máximo 3 oraciones.

**MÉTRICAS DE ÉXITO:** ¿Cómo sabremos en 30 días, 90 días y 6 meses que esto está funcionando? Nombra métricas específicas y medibles.

**ENFOQUE TÉCNICO:** El mecanismo central de IA (RAG, agente, fine-tune, clasificador, etc.), los modelos y la infraestructura. No una arquitectura completa — las decisiones clave.

**EN ALCANCE (V1):** Una lista de viñetas de exactamente qué se construirá. Frases cortas, no párrafos.

**FUERA DE ALCANCE (V1):** Explícitamente qué NO se construirá ahora. Esta sección previene las conversaciones más costosas.

**RIESGOS Y PREGUNTAS ABIERTAS:**
- Riesgos técnicos: [lista las 2-3 cosas más propensas a causar retrasos o retrabajos]
- Preguntas abiertas: [cosas que necesitan decisiones antes de que el equipo pueda proceder]

**EQUIPO Y PROPIEDAD:**
- ¿Quién posee las decisiones de producto?
- ¿Quién posee las decisiones técnicas?
- ¿Quién está ejecutando (ingenieros, agentes)?

**CRONOGRAMA:** Hitos clave con fechas. Sé realista — agrega 30%.

**Nombre del producto/proyecto:**
[nombre]
**Qué hace:**
[descripción]
**Equipo:**
[quiénes están involucrados]

---

## Ejemplo de output

**PRODUCT SUMMARY:** `CodeLens` is an AI code review assistant that automatically reviews PRs for security issues, type safety violations, and architectural drift. It targets mid-sized engineering teams (10–50 engineers) who can't afford dedicated security reviewers but are shipping production code weekly.

**SUCCESS METRICS:**
- 30 days: 3 beta teams using it on real PRs, NPS > 7.
- 90 days: Average 2 critical issues caught per week per team that would have reached production.
- 6 months: 20% reduction in post-merge security incidents in beta teams.

**TECHNICAL APPROACH:** Claude as the reasoning model. Static AST analysis (tree-sitter) runs deterministically first; findings feed into Claude with the diff as context. GitHub Actions integration. No fine-tuning in V1.

**IN SCOPE (V1):** GitHub PR webhook, security finding detection, TypeScript + Python support, GitHub comment posting, severity scoring.

**OUT OF SCOPE (V1):** GitLab/Bitbucket, auto-fix suggestions, custom rule configuration, fine-tuning, dashboard UI.
