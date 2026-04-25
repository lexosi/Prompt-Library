# Framework de Priorización

**Categoría:** decision-making
**Cuándo usar:** Clasificar un backlog con razonamiento de una oración por ítem y dependencias ocultas expuestas.

---

Eres un lead de ingeniería senior ayudándome a priorizar un backlog. Aplica pensamiento estructurado y dame una lista ordenada con razonamiento — no un marco que deba aplicar yo mismo.

**Elementos del backlog:**
[lista cada elemento — una línea cada uno, e.g.:]
1. Refactorizar servicio de auth (deuda técnica)
2. Construir dashboard de analytics (solicitud de producto)
3. Corregir fallos intermitentes en tests de CI (salud de ingeniería)
4. Agregar soporte multilingüe (solicitud de ventas)
5. Mejorar caché de respuestas LLM (reducción de costos)

**Contexto para priorización:**
- Mayor punto de dolor actual: [qué está afectando más al equipo o al negocio ahora mismo]
- Fechas límite próximas: [cualquier fecha fija — lanzamientos, compromisos con clientes, demos para inversores]
- Capacidad del equipo: [e.g., 2 ingenieros, sprint de 3 semanas]
- Enfoque estratégico este trimestre: [e.g., retención, reducción de costos, adquisición de nuevos clientes]
- Restricciones de secuencia: [si X debe ocurrir antes que Y, indícalo]

**Dame:**
1. Una lista ordenada (1 = hacer primero) con razonamiento en una oración por elemento.
2. El único elemento que cortarías completamente si la capacidad es menor de lo esperado.
3. Cualquier dependencia oculta que veas en la lista — cosas que deberían secuenciarse juntas.
4. El elemento donde debería ser más escéptico de mi propia intuición sobre su prioridad.

---

## Ejemplo de output

**Ranked backlog:**

1. **Fix intermittent CI failures** — Every day this stays broken, engineers waste time and lose trust in the test suite. This is leverage: fixing it makes everything else faster.

2. **Improve LLM response caching** — Your strategic focus is cost reduction, and this has a direct, measurable ROI. Pairs well with #1 because faster CI catches caching bugs before they reach production.

3. **Auth service refactor** — This is a prerequisite for multi-language support (auth is locale-dependent). Doing it third means you don't do it twice.

4. **Multi-language support** — Sales has a specific client request, but this should follow auth refactor, not precede it. Schedule for next sprint.

5. **Analytics dashboard** — Useful but no hard deadline and no strategic urgency this quarter. Defer.

**Cut if capacity is short:** Analytics dashboard. No deadline, no dependency, no strategic tie-in this quarter.

**Hidden dependency:** Auth refactor → Multi-language. If you do multi-language before refactoring auth, you'll redo the localization work when you eventually refactor auth. Sequence them together or auth first.

**Where to be skeptical:** You probably feel the analytics dashboard is important because someone asked for it recently. But recency bias inflates perceived urgency. Verify: is there an actual deadline, or just a request?
