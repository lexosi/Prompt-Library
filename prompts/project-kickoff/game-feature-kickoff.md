# Game Feature Kickoff

**Category:** project-kickoff
**When to use:** Starting a new feature or mechanic for a Fortnite Creative/UEFN island or Roblox experience, before design or scripting begins.

---

Write a feature kickoff document for a new game feature. This document aligns the designer and developer before work starts, preventing the most common source of rework: building something technically correct but fun-wrong.

The document must cover:

**FEATURE NAME & PLATFORM:** [e.g., "Gravity Shift mechanic — UEFN Fortnite Creative"]

**ONE-LINE PITCH:** What this feature does from the player's perspective. Not technical. Not internal. What the player experiences.

**PLAYER FANTASY:** What does the player feel while using this feature? (Power, tension, discovery, competition?) This is the north star.

**CORE LOOP:** How does this feature fit into the moment-to-moment game loop? Before → During → After the feature interaction.

**UEFN/ROBLOX CONSTRAINTS:**
- UEFN: Which Verse devices and APIs are involved? Any known limitations?
- Roblox: Which services (DataStore, RemoteEvent, etc.)? Any performance constraints?

**FUN ASSUMPTION:** What must be true for this to be fun? State it explicitly — this is the assumption you'll test first.

**SCOPE:**
- In V1: [the smallest version that tests the fun assumption]
- Out of V1: [the cool ideas that come later if V1 works]

**TEST CRITERIA:** How will you playtest this? What specifically will you watch for?

**Feature description:**
[describe the feature]
**Platform:** [UEFN / Roblox / both]

---

## Example output

**FEATURE NAME:** Wall-Run — UEFN Fortnite Creative

**ONE-LINE PITCH:** Players can sprint horizontally across any vertical wall surface for up to 3 seconds before launching into a jump.

**PLAYER FANTASY:** Feeling like a parkour athlete — fluid, fast, and in total control of the environment. The satisfaction comes from chaining wall-runs with jumps to cross gaps that look impossible.

**CORE LOOP:** Normal sprint → collide with wall → wall-run activates (visual FX + audio cue) → player can steer along the wall → wall-run ends → player launches → land or chain to next wall.

**UEFN CONSTRAINTS:** Custom player movement via Verse `player_movement_component`. No native wall detection — must use raycasting via `GetHitResult`. Frame budget: movement logic must complete in < 2ms to avoid hitching at 60fps.

**FUN ASSUMPTION:** Players will feel rewarded when they successfully chain two wall-runs in a row. Test this first — if chaining feels inconsistent or accidental, the feature won't be fun.

**SCOPE V1:** Straight walls only, fixed 3-second duration, single wall surface. No diagonal runs, no ceiling runs, no speed boost on exit.
