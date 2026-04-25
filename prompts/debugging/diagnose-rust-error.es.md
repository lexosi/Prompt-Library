# Diagnosticar Error de Rust

**Categoría:** debugging
**Cuándo usar:** Tienes un error del compilador de Rust, una violación del borrow checker o un panic en runtime que no puedes explicar de inmediato.

---

Eres un ingeniero Rust senior. Voy a darte un error de Rust y el código relevante. Tu trabajo es:

1. Identificar la causa raíz exacta del error en una sola oración.
2. Explicar por qué el compilador o el runtime de Rust lo está lanzando — el mecanismo, no solo el síntoma.
3. Proporcionar la corrección mínima con el fragmento de código corregido.
4. Si existe un enfoque estructural mejor que prevenga esta clase de errores, mostrarlo como alternativa.

No expliques qué es Rust. No agregues sugerencias no relacionadas. Enfócate únicamente en este error.

**Mensaje de error:**
```
[pega aquí la salida completa del error]
```

**Código relevante:**
```rust
[pega aquí el código que falla]
```

**Lo que esperaba que ocurriera:**
[describe el comportamiento esperado]

---

## Ejemplo de output

**Root cause:** The value `config` is moved into the closure on line 14 but then used again on line 18 after the move.

**Why:** Rust's ownership model does not allow a value to be used after it has been moved. The closure captures `config` by move because it's used in a `thread::spawn` call, which requires `'static` lifetime. After the spawn, `config` no longer exists in the outer scope.

**Fix:**
```rust
let config = Arc::new(config);
let config_clone = Arc::clone(&config);
thread::spawn(move || {
    process(config_clone);
});
println!("{}", config.name); // now valid — Arc keeps the data alive
```

**Structural alternative:** Wrap shared state in `Arc<Mutex<T>>` from the start when any value will be accessed across thread boundaries. This eliminates this entire class of move errors.
