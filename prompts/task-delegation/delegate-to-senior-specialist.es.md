# Delegar a Especialista Senior

**Categoría:** task-delegation
**Cuándo usar:** Transferir un problema complejo a un experto con contexto completo y enfoque en resultado.

---

Escribe un brief de tarea para un especialista senior. A diferencia de la delegación a junior, este debe darle el contexto completo, el resultado que necesitas y las restricciones — luego dejar que trabajen.

Estructura:

**PROBLEMA:** Qué está roto, lento o incierto. Sé específico con datos si los tienes.

**RESULTADO NECESARIO:** Cómo se ve el éxito — en términos medibles donde sea posible.

**PAQUETE DE CONTEXTO:**
- Descripción de arquitectura o sistema relevante (no el codebase completo — las partes que necesitan)
- Decisiones ya tomadas que no están en debate
- Decisiones aún abiertas que son suyas para tomar

**RESTRICCIONES:**
- Plazo
- Límites de presupuesto o recursos
- Requisitos de compatibilidad (debe funcionar con X, no puede romper Y)

**LO QUE YA INTENTÉ:** Prevenir duplicación. Sé honesto sobre qué falló y por qué crees que falló.

**ENTREGABLE:** Qué esperas recibir — documento de recomendación, PR, diagrama de arquitectura, prototipo funcional.

**PUNTO DE REVISIÓN:** Cuándo y cómo quieres hacer check-in (no microgestionar — solo mantenerse alineado).

**Tarea a delegar:**
[describe el problema]
**Dominio del especialista:** [e.g., rendimiento Rust, infraestructura ML, seguridad, diseño de juegos]

---

## Ejemplo de output

**PROBLEM:** Our Rust event ingester processes 8,000 events/sec at p99 latency of 340ms. We need to hit 50,000 events/sec at p99 < 50ms. Profiling shows 60% of time in JSON deserialization.

**OUTCOME NEEDED:** A working implementation that processes 50k events/sec at p99 < 50ms on the same hardware (4-core, 16GB RAM). Or a documented architectural reason why it's not achievable without hardware changes.

**CONTEXT PACKAGE:**
- Ingester code: `src/ingest/` — the hot path is `src/ingest/processor.rs`
- We use `serde_json`. Switching serialization format is on the table.
- We cannot change the input wire format (producers are external).
- We can change everything internal.

**CONSTRAINTS:** 2 weeks. No additional infra cost. Must remain compatible with the existing Kafka consumer interface.

**WHAT I'VE ALREADY TRIED:** Switched from `Vec<u8>` to `Bytes` for zero-copy reads — reduced latency by 15% but not enough. Tried `rayon` for parallelism — contention on the output queue made it worse.

**DELIVERABLE:** A PR with the changes + a brief writeup explaining the approach and the performance measurements.

**REVIEW CHECKPOINT:** Async update after 5 days with findings. Full review when PR is ready.
