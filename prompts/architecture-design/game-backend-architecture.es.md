# Arquitectura de Backend para Juegos

**Categoría:** architecture-design
**Cuándo usar:** Diseñar infraestructura backend para un juego live-service con escalabilidad y anti-cheat en mente.

---

Eres un arquitecto de backend de juegos con experiencia en juegos live-service. Diseña la arquitectura de backend para el siguiente juego. Sé específico — nombra servicios, bases de datos y patrones de comunicación reales. No describas opciones; da el diseño recomendado.

Tu salida debe incluir:
1. **Servicios principales:** Lista cada servicio de backend, su responsabilidad y su elección tecnológica.
2. **Tiempo real vs. request/response:** ¿Qué interacciones son en tiempo real (WebSocket/UDP) vs. REST? Justifica.
3. **Capa de persistencia:** Almacenamiento de datos del jugador, tablas de clasificación, inventario, estado de matchmaking — qué tipo de base de datos para cada uno y por qué.
4. **Modelo de escalabilidad:** ¿Cómo maneja el sistema un pico 10x (e.g., momento viral, torneo)? ¿Qué escala automáticamente y qué necesita pre-aprovisionamiento?
5. **Superficie anti-trampas:** ¿Qué acciones del juego deben validarse del lado del servidor? ¿Qué puede confiarse desde el cliente?
6. **Necesidades específicas del juego:** Eventos de analytics, infraestructura de A/B testing, entrega de contenido para assets del juego.

**Descripción del juego:**
[describe el juego: género, plataforma (Roblox/Fortnite/independiente), jugadores concurrentes esperados, características clave]

**Restricciones:**
- Tamaño del equipo: [e.g., 2 ingenieros backend]
- Presupuesto: [e.g., $500/mes en infraestructura]
- Plazo para el lanzamiento: [e.g., 8 semanas]

---

## Ejemplo de output

**Core services:**
- `player-service` (Rust + Axum) — auth, profile, inventory CRUD. Rust for high-throughput player session handling.
- `leaderboard-service` (Rust + Redis) — real-time sorted sets for global and friend leaderboards.
- `match-service` (Python) — matchmaking logic, lobby management. Python for rapid iteration on matching algorithms.
- `analytics-ingester` (Rust) — fire-and-forget event ingestion, batched to ClickHouse.

**Real-time:** WebSocket for in-match events (player position, score updates). REST for pre/post-match (lobby creation, profile fetches).

**Anti-cheat surface:** Score submission, item acquisition, and currency changes must be server-authoritative. Never trust the client for anything that affects progression or economy.
