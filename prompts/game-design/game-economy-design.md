# Game Economy Design

**Category:** game-design
**When to use:** Designing in-game economies for Fortnite Creative (V-Bucks/island currency) or Roblox (Robux) — ensuring the economy feels fair, sustains engagement, and monetizes ethically.

---

You are a game economist with experience designing live-service economies for Fortnite and Roblox. Design the economy system for the experience below. The economy must feel fair to free players, create clear value for paying players, and sustain long-term engagement without exploitative mechanics.

Your output must include:

1. **Currency system:** How many currencies? Which are earned through play (soft currency) vs. purchased (hard currency)? State the conversion rate and daily/weekly earn caps.

2. **Earn sources:** List every way a player earns soft currency. Map each source to a player behavior you want to reinforce (e.g., "daily login reward → daily retention," "win bonus → competitive engagement").

3. **Spend sinks:** List everything players spend currency on. Categorize: consumable (gone after use), durable (lasts forever), cosmetic (no gameplay effect). Healthy economies have more cosmetic and durable sinks than consumables.

4. **Premium value proposition:** What does a player get for real money that a free player cannot reasonably earn in a typical play session? Be specific — this is the product you're selling.

5. **Economy health metrics:** What numbers will you monitor to detect if the economy is broken?
   - Inflation: average currency balance per player over time
   - Conversion rate: % of players who make at least one Robux/V-Bucks purchase
   - Whale concentration: % of revenue from the top 1% of spenders

6. **Anti-exploitation rules:** What mechanics prevent players from farming currency at an unintended rate?

**Platform:** [Fortnite Creative / Roblox]
**Experience type:** [competitive / social / adventure / simulator]
**Target monetization:** [e.g., cosmetics-only, VIP pass, gacha, direct purchase]

---

## Example output

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
