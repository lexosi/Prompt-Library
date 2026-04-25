# Microservicios: Rust + Python

**Categoría:** architecture-design
**Cuándo usar:** Planificar la separación de un monolito en microservicios con justificación de asignación de lenguajes y secuencia de migración.

---

Eres un arquitecto de sistemas con experiencia en microservicios poliglotas. Necesito dividir un monolito en servicios Rust y Python. Dame un plan concreto de división.

Tu salida debe incluir:
1. **Justificación de asignación de lenguaje:** ¿Qué dominios pertenecen a Rust (críticos en rendimiento, sensibles a memoria, limitados por latencia) vs. Python (ML, iteración rápida, integraciones)? Indica la regla de decisión que estás usando.
2. **Definiciones de límites de servicio:** Lista cada servicio propuesto, su lenguaje, su superficie de API (gRPC, REST, cola de mensajes) y qué reemplaza en el monolito.
3. **Propiedad de datos:** ¿Qué servicio posee qué tablas/colecciones? ¿Cómo se manejan los joins entre servicios?
4. **Patrón de comunicación:** Síncrono (gRPC/REST) vs. asíncrono (Kafka, RabbitMQ, Redis Streams) para cada par de servicios que se comunican.
5. **Secuencia de migración:** ¿En qué orden extraes los servicios para minimizar el riesgo? ¿Qué permanece más tiempo en el monolito y por qué?
6. **Costo de complejidad operacional:** ¿Qué infraestructura nueva es necesaria y cuál es la carga de mantenimiento realista?

**Descripción del monolito actual:**
[describe el monolito: lenguaje, responsabilidades principales, base de datos, puntos de dolor actuales]

**Estado objetivo:**
[describe cómo debería verse el sistema en 6–12 meses]

---

## Ejemplo de output

**Language assignment rule:** Rust for anything on the hot path that touches raw data at high volume (ingestion, processing, serving). Python for anything that calls ML models, wraps third-party APIs, or needs to be iterated on weekly.

**Proposed services:**
| Service | Language | API | Replaces |
|---------|----------|-----|---------|
| `event-ingester` | Rust | gRPC | Monolith event handler |
| `ml-ranker` | Python | Internal REST | Monolith ranking module |
| `notification-worker` | Python | Redis Streams consumer | Monolith email/push worker |

**Migration sequence:** (1) Extract `notification-worker` first — lowest risk, well-isolated. (2) Extract `ml-ranker` — Python stays, just separate deploy. (3) Extract `event-ingester` — highest complexity, do last when the pattern is proven.
