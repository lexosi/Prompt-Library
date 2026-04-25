# Delegar a Agente IA

**Categoría:** task-delegation
**Cuándo usar:** Escribir un brief de tarea completo y autónomo para un agente IA con restricciones y criterios de éxito.

---

Escribe un brief completo de tarea para un agente de IA autónomo que ejecutará el siguiente trabajo. El brief debe darle al agente todo lo que necesita para completar la tarea sin hacer preguntas aclaratorias.

Estructura el brief de la siguiente manera:

**TAREA:** Declaración en una oración del objetivo.

**CONTEXTO:** Lo que el agente necesita saber sobre el sistema, codebase o dominio para tomar buenas decisiones.

**PASOS:** Secuencia numerada de acciones. Sé específico — nombra archivos, funciones y endpoints, no categorías.

**HERRAMIENTAS DISPONIBLES:** Lista las herramientas a las que tiene acceso el agente. Para cada una, nota cualquier restricción importante de uso.

**FORMATO DE SALIDA:** Exactamente qué debe producir el agente cuando termine — archivo, JSON, mensaje, PR, etc.

**RESTRICCIONES:**
- Qué NO hacer (sé explícito — los agentes actúan sobre lo que se dice, no sobre lo que se implica)
- Límites de alcance (qué archivos/servicios están fuera de límites)
- Paradas obligatorias (si ocurre X, detén y reporta en lugar de continuar)

**CRITERIOS DE ÉXITO:** Cómo sabrá el agente (y tú) que la tarea está completa y correcta.

**Tarea a delegar:**
[describe la tarea]

---

## Ejemplo de output

**TASK:** Add input validation to all API endpoints in the `orders` service that currently accept raw `req.body` without schema validation.

**CONTEXT:** The codebase is a Fastify + TypeScript API. Validation should use `zod`. The `orders` service is at `src/services/orders/`. There are 4 route files. Tests are in `src/services/orders/__tests__/`.

**STEPS:**
1. Read all 4 route files and identify every endpoint that uses `req.body` without validation.
2. For each endpoint, infer the expected schema from the existing TypeScript types in the same file.
3. Write a `zod` schema for each body and add `.parse()` at the top of each handler.
4. Update existing tests to test both valid and invalid input cases.
5. Run `npm test` — all tests must pass before finishing.

**TOOLS AVAILABLE:** file read, file write, bash (for running `npm test`). Do not use bash for anything other than running tests.

**OUTPUT FORMAT:** List of changed files with a one-line summary of what changed in each.

**CONSTRAINTS:** Do not modify any route in `src/services/auth/` — that service has a separate validation PR in flight. Stop and report if you find any route that mutates the database without authentication middleware.

**SUCCESS CRITERIA:** `npm test` passes. Every `req.body` usage in `orders` routes is preceded by a `zod` parse call.
