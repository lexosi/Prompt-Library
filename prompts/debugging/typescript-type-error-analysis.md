# TypeScript Type Error Analysis

**Category:** debugging
**When to use:** TypeScript is raising a type error you can't resolve, or `any` has leaked through the type system and is causing silent failures.

---

You are a TypeScript expert with deep knowledge of the type system. Analyze the type error and code below:

1. State exactly what TypeScript believes the types are at the point of failure.
2. Explain why those types are incompatible — the structural reason, not just "type X is not assignable to type Y."
3. Provide the correct fix. If the fix requires a generic, show the generic. If it requires a type guard, write the type guard.
4. Flag if the underlying issue is `any` leakage — trace where the `any` entered and how to eliminate it.

Do not suggest `as any` or `@ts-ignore` as solutions.

**TypeScript version:** [e.g., 5.4]
**tsconfig strict mode:** [yes/no]

**Error:**
```
[paste the full TypeScript error including file, line, and error code]
```

**Code:**
```typescript
[paste the relevant types, interfaces, and the failing expression]
```

---

## Example output

**What TypeScript sees:** At line 31, TypeScript infers `handler` as `(event: MouseEvent | TouchEvent) => void`, but `addEventListener` expects `(event: Event) => void`. These are structurally incompatible because `MouseEvent | TouchEvent` is a subtype of `Event`, and function parameter types are contravariant.

**Root cause:** You're assigning a more-specific handler to a slot that accepts a more-general event type. TypeScript correctly rejects this because calling the handler with a plain `Event` would violate the type contract.

**Fix:**
```typescript
function handleInput(event: Event): void {
    if (event instanceof MouseEvent) {
        console.log(event.clientX); // narrowed to MouseEvent
    } else if (event instanceof TouchEvent) {
        console.log(event.touches[0]); // narrowed to TouchEvent
    }
}
element.addEventListener('click', handleInput); // now compatible
```
