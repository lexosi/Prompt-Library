# TypeScript Clean Architecture Refactor

**Category:** refactor
**When to use:** TypeScript codebase where business logic, data access, and HTTP handling are tangled together in route handlers or service files.

---

You are a TypeScript architect. Refactor the code below to achieve clean separation of concerns. The target structure is:
- **Domain layer:** Pure business logic, no framework dependencies, no database imports.
- **Application layer:** Use cases / service functions that orchestrate domain logic.
- **Infrastructure layer:** Database adapters, HTTP clients, external service integrations.
- **Interface layer:** Route handlers, controllers — thin, delegates everything to the application layer.

For each change:
1. Show which code moves where and why.
2. Define the interfaces (TypeScript `interface` or `type`) that each layer boundary needs.
3. Show how dependency injection changes (constructor injection preferred over module-level imports).
4. Identify any side effects that need to move to infrastructure.

Do not introduce a full DI framework unless the codebase already uses one. Use constructor injection directly.

**Code to refactor:**
```typescript
[paste the route handlers, services, or business logic files]
```

**Framework:** [e.g., Fastify, NestJS, Express]
**ORM:** [e.g., Prisma, TypeORM, Drizzle]

---

## Example output

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
