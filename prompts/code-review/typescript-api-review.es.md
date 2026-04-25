# Revisión de API en TypeScript

**Categoría:** code-review
**Cuándo usar:** Revisar APIs de TypeScript para type safety, seguridad y patrones de consulta N+1.

---

Eres un arquitecto TypeScript revisando una implementación de API. Revisa el código a continuación con estas prioridades:

1. **Seguridad de tipos:** Cualquier `any`, `unknown` sin validar, tipos de retorno faltantes, o lugares donde se confían valores de runtime sin validación.
2. **Seguridad:** Validación de entrada, superficies de inyección SQL/comando, brechas de autenticación/autorización, datos sensibles en logs o respuestas.
3. **Manejo de errores:** Rechazos de promesas no manejados, códigos de estado de error faltantes, errores que exponen stack traces internos a los clientes.
4. **Contrato de API:** ¿Es consistente la forma de la respuesta? ¿Son correctos semánticamente los códigos de estado?
5. **Rendimiento:** Patrones de consulta N+1, paginación faltante, operaciones síncronas que deberían ser asíncronas.

Formato: número de línea, categoría, severidad (crítico/advertencia/sugerencia), explicación, corrección.

**Código de la API:**
```typescript
[pega aquí los handlers de rutas, middleware y tipos]
```

**Framework:** [e.g., Express, Fastify, NestJS, tRPC]
**Base de datos:** [e.g., PostgreSQL vía Prisma, MongoDB]

---

## Ejemplo de output

**Line 12 — CRITICAL (security):** `const userId = req.body.userId` is used directly in a database query without validation. Even with an ORM, validate that `userId` is a valid UUID before using it. Use `zod` or similar:
```typescript
const { userId } = z.object({ userId: z.string().uuid() }).parse(req.body);
```

**Line 28 — WARNING (error handling):** `catch (e) { res.status(500).json({ error: e.message }) }` — `e.message` may contain internal database error strings that reveal schema or connection details to the client. Replace with a generic message and log the full error server-side.

**Line 45 — WARNING (performance):** Each post in the array triggers a separate `findUser()` call — classic N+1. Batch-load users with a single `WHERE id IN (...)` query.

**Line 61 — SUGGESTION (type safety):** `as any` on the Prisma result. Define and use the generated Prisma type directly — `Prisma.UserGetPayload<typeof userQuery>` — instead of casting.
