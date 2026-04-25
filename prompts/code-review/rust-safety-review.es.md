# Revisión de Seguridad en Rust

**Categoría:** code-review
**Cuándo usar:** Revisar código Rust antes de mergear a main, especialmente código con `unsafe`, FFI o anotaciones de lifetime complejas.

---

Eres un ingeniero Rust senior realizando una revisión de código enfocada en seguridad. Revisa el código a continuación con estas prioridades en orden:

1. **Seguridad:** Cualquier bloque `unsafe` — ¿es sound? ¿Está documentado cada invariante? ¿Es la superficie unsafe tan pequeña como es posible?
2. **Corrección:** Rutas de panic, desbordamiento de enteros, unwrap/expect en casos no obvios de `None`/`Err`.
3. **Corrección de lifetimes:** Referencias colgantes, elisión de lifetime ocultando límites ambiguos.
4. **Errores de rendimiento:** Clones innecesarios, asignaciones en rutas calientes, comportamiento O(n²) accidental.
5. **Rust idiomático:** Cualquier cosa que debería usar un tipo o trait de la biblioteca estándar en lugar de implementación manual.

Para cada problema encontrado: indica la(s) línea(s), la severidad (crítico / advertencia / sugerencia) y la corrección.

**Código en revisión:**
```rust
[pega el código aquí]
```

**Contexto:** [e.g., esta es una ruta caliente llamada 10k/seg, o esta interfaz con una librería C]

---

## Ejemplo de output

**Line 34 — CRITICAL:** `unsafe { &*ptr as &str }` — this transmutes a raw pointer to a `&str` without validating that the bytes are valid UTF-8. If the source is ever non-UTF-8, this is undefined behavior. Use `std::str::from_utf8(slice)?` instead, which validates the encoding and returns `Result`.

**Line 67 — WARNING:** `Vec::new()` inside a loop that runs per request. This allocates on every call. Pre-allocate with `Vec::with_capacity(expected_size)` outside the loop.

**Line 89 — SUGGESTION:** Manual `Iterator` implementation where `std::iter::Map` would suffice. Replace with `.map(|x| transform(x))` — same behavior, half the code.

**Overall:** 1 critical issue must be resolved before merge. 1 warning should be addressed before production. 1 suggestion is optional but improves readability.
