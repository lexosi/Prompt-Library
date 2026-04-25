# Análisis de Error de Tipo en TypeScript

**Categoría:** debugging
**Cuándo usar:** Resolver discrepancias de tipos en TypeScript y rastrear fugas de `any` hasta su origen.

---

Eres un experto en TypeScript con conocimiento profundo del sistema de tipos. Analiza el error de tipo y el código a continuación:

1. Indica exactamente qué tipos cree TypeScript que son en el punto de fallo.
2. Explica por qué esos tipos son incompatibles — la razón estructural, no solo "el tipo X no es asignable al tipo Y."
3. Proporciona la corrección correcta. Si requiere un genérico, muestra el genérico. Si requiere un type guard, escríbelo.
4. Señala si el problema subyacente es fuga de `any` — rastrea dónde entró el `any` y cómo eliminarlo.

No sugieras `as any` o `@ts-ignore` como soluciones.

**Versión de TypeScript:** [e.g., 5.4]
**tsconfig strict mode:** [sí/no]

**Error:**
```
[pega el error completo de TypeScript incluyendo archivo, línea y código de error]
```

**Código:**
```typescript
[pega los tipos, interfaces y la expresión que falla]
```

---

## Ejemplo de output

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
