# Refactor Idiomático de Rust

**Categoría:** refactor
**Cuándo usar:** Refactorizar código Rust para eliminar clones, usar iteradores e implementar traits estándar.

---

Eres un ingeniero Rust senior. Refactoriza el código a continuación para que sea más idiomático en Rust sin cambiar su comportamiento ni su API pública.

Enfócate en:
1. **Manejo de errores:** Reemplaza `unwrap()`/`expect()` con propagación correcta de `?` y tipos `Result`/`Option`.
2. **Ownership:** Elimina clones innecesarios. Encuentra lugares donde el borrowing es suficiente.
3. **Cadenas de iteradores:** Reemplaza bucles `for` manuales que construyen colecciones con `.map()`, `.filter()`, `.fold()`, `.collect()`.
4. **Type aliases y newtypes:** Si se usan primitivos raw como IDs o valores de dominio, sugiere wrappers de newtype.
5. **Uso de traits:** Implementa `From`/`Into`, `Display`, `Default`, o `Iterator` donde eliminen boilerplate.
6. **Reducción de `unsafe`:** Si algún bloque `unsafe` puede reemplazarse con abstracciones seguras, muestra cómo.

Para cada cambio: muestra el antes y el después, y explica por qué la versión idiomática es mejor.

**Código a refactorizar:**
```rust
[pega el código aquí]
```

**Preservar:** [cualquier comportamiento específico o superficie de API que no debe cambiar]

---

## Ejemplo de output

**Change 1 — Error propagation (lines 12–18):**

Before:
```rust
let file = File::open(path).unwrap();
let contents = read_to_string(file).unwrap();
```

After:
```rust
let contents = std::fs::read_to_string(path)?;
```

Why: `read_to_string` on a path handles both open and read in one call. `?` propagates errors to the caller rather than panicking. Callers can now decide how to handle the error.

**Change 2 — Iterator chain (lines 34–42):**

Before:
```rust
let mut results = Vec::new();
for item in items {
    if item.score > 0 {
        results.push(item.name.clone());
    }
}
```

After:
```rust
let results: Vec<_> = items.iter()
    .filter(|item| item.score > 0)
    .map(|item| item.name.as_str())
    .collect();
```

Why: No clone needed — we borrow `name`. The iterator chain expresses intent directly. The compiler can optimize the allocation better with a single `.collect()`.
