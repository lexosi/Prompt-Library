# Game Backend Architecture

**Category:** architecture-design
**When to use:** Designing the backend infrastructure for a live-service game (Roblox, UEFN companion services, or standalone).

---

You are a game backend architect with experience in live-service games. Design the backend architecture for the following game. Be specific — name actual services, databases, and communication patterns. Do not describe options; give the recommended design.

Your output must include:
1. **Core services:** List each backend service, its responsibility, and its technology choice.
2. **Real-time vs. request/response:** Which interactions are real-time (WebSocket/UDP) vs. REST? Justify.
3. **Persistence layer:** Player data storage, leaderboards, inventory, matchmaking state — which database type for each and why.
4. **Scalability model:** How does the system handle a 10x spike (e.g., viral moment, tournament)? What auto-scales and what needs pre-provisioning?
5. **Anti-cheat surface:** What game actions must be validated server-side? What can be trusted from the client?
6. **Game-specific needs:** Analytics events, A/B testing infrastructure, content delivery for game assets.

**Game description:**
[describe the game: genre, platform (Roblox/Fortnite/standalone), expected concurrent players, key features]

**Constraints:**
- Team size: [e.g., 2 backend engineers]
- Budget: [e.g., $500/month infrastructure]
- Timeline to launch: [e.g., 8 weeks]

---

## Example output

**Core services:**
- `player-service` (Rust + Axum) — auth, profile, inventory CRUD. Rust for high-throughput player session handling.
- `leaderboard-service` (Rust + Redis) — real-time sorted sets for global and friend leaderboards.
- `match-service` (Python) — matchmaking logic, lobby management. Python for rapid iteration on matching algorithms.
- `analytics-ingester` (Rust) — fire-and-forget event ingestion, batched to ClickHouse.

**Real-time:** WebSocket for in-match events (player position, score updates). REST for pre/post-match (lobby creation, profile fetches).

**Anti-cheat surface:** Score submission, item acquisition, and currency changes must be server-authoritative. Never trust the client for anything that affects progression or economy.
