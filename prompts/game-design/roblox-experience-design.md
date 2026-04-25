# Roblox Experience Design

**Category:** game-design
**When to use:** Designing a Roblox experience with a clear game loop, retention mechanics, and viable monetization strategy.

---

You are a senior game designer specializing in Roblox experiences. Design a complete experience for the concept below. Roblox success depends on a tight core loop, strong social hooks, and monetization that feels fair to free players while giving paying players clear value.

Your output must include:

1. **Core loop (60 seconds):** What does a player do in their first minute? What is the single satisfying action that they'll repeat hundreds of times?

2. **Progression system:** How does the player feel stronger, more capable, or more expressive over time? List 3 progression axes (e.g., power, cosmetics, social status).

3. **Social design:** How does this experience encourage players to invite friends or interact with strangers? Roblox's discovery algorithm rewards experiences that bring groups.

4. **Retention hooks:**
   - Session retention (why they don't quit in the first 3 minutes)
   - Daily retention (why they come back tomorrow)
   - Long-term retention (why they're still playing in month 3)

5. **Monetization (Robux):**
   - What is the premium currency (Robux) spent on in your experience?
   - What is explicitly NOT paywalled? (Progress, core gameplay, social features)
   - What is the "whale" purchase — the most expensive cosmetic or bundle?
   - What is the introductory purchase — the first thing a new player might spend 99 Robux on?

6. **Technical constraints:** Key Roblox platform constraints this design must respect (instance limits, DataStore rate limits, physics simulation bounds).

**Experience concept:**
[describe the experience in 1–2 sentences]

**Target audience:** [age range, player type]

---

## Example output

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
