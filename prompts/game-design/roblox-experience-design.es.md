# Diseño de Experiencia para Roblox

**Categoría:** game-design
**Cuándo usar:** Diseñar una experiencia de Roblox con loop central, retención y monetización justa con Robux.

---

Eres un diseñador de juegos senior especializado en experiencias de Roblox. Diseña una experiencia completa para el concepto a continuación. El éxito en Roblox depende de un loop principal ajustado, ganchos sociales fuertes y una monetización que se sienta justa para los jugadores gratuitos mientras da a los que pagan un valor claro.

Tu salida debe incluir:

1. **Loop principal (60 segundos):** ¿Qué hace un jugador en su primer minuto? ¿Cuál es la única acción satisfactoria que repetirá cientos de veces?

2. **Sistema de progresión:** ¿Cómo se siente el jugador más fuerte, más capaz o más expresivo con el tiempo? Lista 3 ejes de progresión (e.g., poder, cosméticos, estatus social).

3. **Diseño social:** ¿Cómo fomenta esta experiencia que los jugadores inviten amigos o interactúen con extraños? El algoritmo de descubrimiento de Roblox recompensa las experiencias que traen grupos.

4. **Ganchos de retención:**
   - Retención de sesión (por qué no abandonan en los primeros 3 minutos)
   - Retención diaria (por qué regresan mañana)
   - Retención a largo plazo (por qué siguen jugando en el mes 3)

5. **Monetización (Robux):**
   - ¿En qué se gasta la moneda premium (Robux) en tu experiencia?
   - ¿Qué NO está detrás de un muro de pago explícitamente? (Progreso, jugabilidad principal, características sociales)
   - ¿Cuál es la compra "whale" — el cosmético o paquete más caro?
   - ¿Cuál es la compra de introducción — lo primero en que un nuevo jugador podría gastar 99 Robux?

6. **Restricciones técnicas:** Restricciones clave de la plataforma Roblox que este diseño debe respetar (límites de instancias, límites de tasa de DataStore, límites de simulación de física).

**Concepto de la experiencia:**
[describe la experiencia en 1–2 oraciones]

**Audiencia objetivo:** [rango de edad, tipo de jugador]

---

## Ejemplo de output

**Experience: Neon Racer** — Players build custom hovercars, race on procedurally modified tracks, and bet Neon Coins (earned in-game) on other players' races.

**Core loop (60 seconds):** Select a track → Race (30–45 seconds of tight corridor racing) → Collect Neon Coins from placement → Spend coins on one part upgrade. Every race is short enough to feel like "one more run."

**Progression axes:**
1. **Performance:** Engine, hover system, and boost upgrades — directly affect race times.
2. **Cosmetics:** Neon trails, body decals, celebration animations — expressiveness, no performance impact.
3. **Reputation:** Win streaks displayed on a global leaderboard and visible on your car's hood badge.

**Monetization:**
- **Free:** All tracks, all race modes, all functional car parts (earnable via Neon Coins).
- **Robux:** Exclusive cosmetic body kits, animated trail effects, and the "VIP Garage" which grants 2× Neon Coin earnings for 7 days (starter item: 99 Robux).
- **Whale purchase:** Legendary "Spectral Edition" hovercar (limited per week, 1,500 Robux).

**Technical constraints:** Max 16 players per server (racing server performance). DataStore saves car config on race end, not continuously — avoids rate limits.
