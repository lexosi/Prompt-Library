# Arquitectura Limpia en TypeScript

**Categoría:** refactor
**Cuándo usar:** Separar lógica de negocio, infraestructura y manejo HTTP en una base de código TypeScript.

---

Eres un arquitecto TypeScript. Refactoriza el código a continuación para lograr una separación clara de responsabilidades. La estructura objetivo es:
- **Capa de dominio:** Lógica de negocio pura, sin dependencias de framework, sin imports de base de datos.
- **Capa de aplicación:** Casos de uso / funciones de servicio que orquestan la lógica de dominio.
- **Capa de infraestructura:** Adaptadores de base de datos, clientes HTTP, integraciones de servicios externos.
- **Capa de interfaz:** Handlers de rutas, controladores — delgados, delegan todo a la capa de aplicación.

Para cada cambio:
1. Muestra qué código se mueve a dónde y por qué.
2. Define las interfaces (TypeScript `interface` o `type`) que necesita cada límite de capa.
3. Muestra cómo cambia la inyección de dependencias (se prefiere la inyección por constructor sobre imports a nivel de módulo).
4. Identifica cualquier efecto secundario que deba moverse a infraestructura.

No introduzcas un framework de DI completo a menos que el codebase ya use uno. Usa inyección por constructor directamente.

**Código a refactorizar:**
```typescript
[pega los route handlers, servicios o archivos de lógica de negocio]
```

**Framework:** [e.g., Fastify, NestJS, Express]
**ORM:** [e.g., Prisma, TypeORM, Drizzle]

---

## Ejemplo de output

**Before (everything in one route handler):**
```typescript
app.post('/orders', async (req, res) => {
    const user = await db.user.findUnique({ where: { id: req.body.userId } });
    if (user.credits < req.body.amount) throw new Error('Insufficient credits');
    await db.order.create({ data: { ...req.body, status: 'pending' } });
    await sendEmail(user.email, 'Order confirmed');
    res.json({ success: true });
});
```

**After — domain:**
```typescript
// domain/order.ts
export function validateOrder(user: User, amount: number): Result<void, 'INSUFFICIENT_CREDITS'> {
    if (user.credits < amount) return err('INSUFFICIENT_CREDITS');
    return ok();
}
```

**After — application:**
```typescript
// application/create-order.ts
export class CreateOrderUseCase {
    constructor(
        private readonly orders: OrderRepository,
        private readonly notifications: NotificationService,
    ) {}

    async execute(userId: string, amount: number): Promise<OrderId> {
        const user = await this.orders.findUser(userId);
        validateOrder(user, amount).unwrapOrThrow();
        const order = await this.orders.create({ userId, amount, status: 'pending' });
        await this.notifications.sendOrderConfirmation(user.email);
        return order.id;
    }
}
```
