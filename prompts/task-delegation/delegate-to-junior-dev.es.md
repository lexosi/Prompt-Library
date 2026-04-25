# Delegar a Desarrollador Junior

**Categoría:** task-delegation
**Cuándo usar:** Asignar una tarea delimitada a un desarrollador junior con punto de inicio claro y definición de terminado.

---

Necesito escribir una asignación de tarea para un desarrollador junior. La tarea debe estar acotada para que pueda completarla en [plazo] sin bloquearse. Escribe la asignación usando esta estructura:

**TÍTULO DE LA TAREA:** Nombre corto y específico.

**LO QUE NECESITO:** Descripción clara del entregable — no el proceso, sino el resultado.

**POR QUÉ IMPORTA:** Una oración sobre cómo esta tarea encaja en el proyecto mayor. Da contexto sin abrumar con detalles.

**PUNTO DE PARTIDA:** Exactamente dónde comenzar — qué archivo, qué función, qué branch.

**RECURSOS:** Links, docs o ejemplos que deben revisar antes de comenzar.

**DEFINICIÓN DE LISTO:**
- [ ] Criterios específicos y verificables que confirman que el trabajo está completo.
- [ ] Incluye: código funciona, tests pasan, el caso límite X está manejado, código revisado.

**DÓNDE OBTENER AYUDA:**
- Si se bloquea en X, pregunta a [persona/canal].
- Si no está seguro sobre [decisión específica], elige la opción más simple y anótala en el PR.

**FUERA DE ALCANCE:** Lista explícitamente lo que NO deben hacer — previene scope creep y esfuerzo desperdiciado.

**Tarea a delegar:**
[describe qué debe hacerse]
**Nivel del desarrollador:** [junior / early-mid]
**Plazo:** [e.g., 1 día, 3 días]

---

## Ejemplo de output

**TASK TITLE:** Add pagination to the `/api/users` endpoint

**WHAT I NEED:** The `/api/users` GET endpoint currently returns all users. It needs to support `?page=1&limit=20` query parameters and return a paginated response with `{ data, total, page, totalPages }`.

**WHY THIS MATTERS:** This endpoint is causing timeouts as our user base grows. Pagination is the immediate fix before we address the underlying query performance.

**STARTING POINT:** `src/routes/users.ts`, line 34, the `GET /users` handler.

**RESOURCES:**
- Existing pagination in `src/routes/posts.ts` — same pattern, copy the approach.
- Prisma pagination docs: `skip` and `take` parameters.

**DEFINITION OF DONE:**
- [ ] `GET /api/users?page=1&limit=20` returns 20 users and correct metadata
- [ ] `GET /api/users` without params defaults to page 1, limit 20
- [ ] Existing tests in `users.test.ts` still pass
- [ ] 2 new tests: one for valid pagination, one for out-of-range page

**OUT OF SCOPE:** Do not change the user query itself, add filtering, or touch the auth middleware.
