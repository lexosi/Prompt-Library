# Decisión de Stack Técnico

**Categoría:** decision-making
**Cuándo usar:** Obtener una recomendación concreta de lenguaje/framework con el factor decisivo y el riesgo.

---

Eres un asesor técnico senior. Necesito tomar una decisión de stack para la siguiente situación. No me des una visión equilibrada de todas las opciones — dame una recomendación concreta con tradeoffs honestos.

**Decisión a tomar:**
[e.g., "¿Deberíamos usar Rust o Go para nuestro nuevo servicio de procesamiento de eventos?"]

**Contexto:**
- Qué hace el sistema: [describe]
- Requisitos de rendimiento: [latencia, throughput, SLAs]
- Equipo: [quién lo construirá y mantendrá — nivel de experiencia, lenguajes conocidos]
- Plazo: [cuánto tiempo para llegar a producción]
- Stack existente: [qué ya está en uso — evitar diversidad innecesaria]
- Expectativas de escala: [ahora vs. en 2 años]

**Dame:**
1. Tu recomendación — una opción, declarada directamente.
2. El único argumento más fuerte A FAVOR de esta elección en este contexto.
3. El único riesgo o costo más grande de esta elección.
4. Qué cambiaría tu recomendación — la condición específica bajo la cual elegirías diferente.
5. Lo único que debemos hacer bien para que esta elección funcione.

---

## Ejemplo de output

**Recommendation:** Use Rust.

**Strongest argument for Rust:** Your team already has 2 engineers with production Rust experience, and the service's core requirement — processing 50k events/sec at < 10ms p99 latency — is exactly the domain where Rust's zero-cost abstractions and deterministic memory management pay off versus Go's GC pauses.

**Biggest risk:** Hiring. If either of your two Rust engineers leaves in the next 18 months, you'll have a critical system in a language with thin team coverage. Rust has a steeper learning curve than Go for engineers coming from Python or JavaScript.

**What would change my recommendation:** If your timeline were 4 weeks instead of 12, I'd choose Go. You'd ship faster and iterate faster, and the performance gap wouldn't matter at your current scale. Revisit Rust when the throughput actually becomes a bottleneck.

**The one thing you must get right:** Error handling. Rust's `Result`-based error handling is a superpower, but teams that fight it with excessive `unwrap()` calls end up with production panics that are harder to debug than Go's equivalent. Establish the error handling convention in week one.
