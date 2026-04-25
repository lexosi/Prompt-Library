# Diseño de Economía de Juego

**Categoría:** game-design
**Cuándo usar:** Diseñar sistemas de moneda, loops de ganancia/gasto y valor premium para Fortnite o Roblox.

---

Eres un economista de juegos con experiencia diseñando economías de servicio en vivo para Fortnite y Roblox. Diseña el sistema de economía para la experiencia a continuación. La economía debe sentirse justa para los jugadores gratuitos, crear valor claro para los que pagan y sostener el compromiso a largo plazo sin mecánicas explotadoras.

Tu salida debe incluir:

1. **Sistema de monedas:** ¿Cuántas monedas? ¿Cuáles se ganan a través del juego (moneda blanda) vs. se compran (moneda dura)? Indica la tasa de conversión y los límites de ganancia diaria/semanal.

2. **Fuentes de ganancia:** Lista todas las formas en que un jugador gana moneda blanda. Mapea cada fuente a un comportamiento del jugador que quieres reforzar (e.g., "recompensa de inicio de sesión diario → retención diaria," "bono de victoria → compromiso competitivo").

3. **Sumideros de gasto:** Lista todo en lo que los jugadores gastan moneda. Categoriza: consumible (desaparece después de usar), durable (dura para siempre), cosmético (sin efecto de juego). Las economías saludables tienen más sumideros cosméticos y duraderos que consumibles.

4. **Propuesta de valor premium:** ¿Qué obtiene un jugador por dinero real que un jugador gratuito no puede ganar razonablemente en una sesión de juego típica? Sé específico — este es el producto que estás vendiendo.

5. **Métricas de salud de la economía:** ¿Qué números monitorizarás para detectar si la economía está rota?
   - Inflación: saldo de moneda promedio por jugador con el tiempo
   - Tasa de conversión: % de jugadores que realizan al menos una compra de Robux/V-Bucks
   - Concentración whale: % de ingresos de los principales gastadores (top 1%)

6. **Reglas anti-explotación:** ¿Qué mecánicas previenen que los jugadores cultiven moneda a una tasa no intencionada?

**Plataforma:** [Fortnite Creative / Roblox]
**Tipo de experiencia:** [competitiva / social / aventura / simulador]
**Monetización objetivo:** [e.g., solo cosméticos, pase VIP, gacha, compra directa]

---

## Ejemplo de output

**Platform:** Roblox — Tycoon simulator
**Currencies:** 2
- **Neon Credits (soft, earned):** Earned through gameplay. Cap: 500/day base, 750/day with VIP Gamepass.
- **Robux (hard, purchased):** Roblox's real-money currency. 1 Robux ≈ $0.01. Not earnable in-game.

**Earn sources:**
| Source | Amount | Behavior reinforced |
|--------|--------|-------------------|
| Idle production (per minute) | 5–50 | Stay logged in |
| Completing a production chain | 25 | Active play |
| Daily login bonus | 100 | Daily retention |
| Winning a community vote | 200 | Social engagement |

**Spend sinks:**
- Consumable: Boost tokens (2× production for 1 hour) — 150 Credits. High earn rate keeps these affordable.
- Durable: Factory expansions — 200–2,000 Credits. Main progression sink.
- Cosmetic: Factory skins, animated logos, themed decorations — Robux only.

**Premium value:** VIP Gamepass (299 Robux, one-time): +50% Neon Credit earnings, exclusive VIP lounge area, and one exclusive factory skin. Free players can reach the same progression — VIP just gets there 50% faster.

**Anti-exploitation:** Idle production rate is halved if player has been in-game > 4 hours without active input (prevents AFK farming bots).
