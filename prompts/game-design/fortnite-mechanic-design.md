# Fortnite Creative Mechanic Design

**Category:** game-design
**When to use:** Designing a core gameplay mechanic for a Fortnite Creative island — needs to be fun, buildable in UEFN, and work within Fortnite's systems.

---

You are a senior game designer specializing in Fortnite Creative and UEFN. Design a gameplay mechanic for the description below.

Your output must include:

1. **Mechanic summary:** What the player does and what they experience — in player-facing language, not developer language.

2. **Core loop integration:** Where does this mechanic fit in the 30-second loop, 3-minute loop, and session loop? How does it reward both new and returning players differently?

3. **UEFN implementation approach:** Which Verse APIs, devices (Trigger Volume, Player Reference Device, Class Designer, etc.), and events are needed? Flag any mechanic that UEFN doesn't currently support natively.

4. **Tuning parameters:** List the 3–5 numbers that determine if this mechanic feels good — cooldown, radius, duration, damage multiplier, etc. State the starting values and the expected tuning range.

5. **Fail states and countplay:** What stops this mechanic from being overpowered? What's the skill expression — how does a skilled player use it better than a beginner?

6. **Fortnite-native fit:** How does this mechanic interact with Fortnite's existing building, shooting, and movement systems? Does it complement or conflict?

**Mechanic idea:**
[describe the mechanic in one or two sentences]

**Island context:** [genre, theme, target player type — e.g., "competitive 1v1 arena," "cooperative survival," "casual party game"]

---

## Example output

**Mechanic: Shadow Dash** — Player expends 1 "Shadow Charge" (max 3, regenerates every 8 seconds) to teleport 6 meters in their movement direction, briefly becoming intangible and passing through bullets.

**Core loop integration:** 30-second loop — Used as an escape or repositioning tool during combat. 3-minute loop — Players must manage their 3 charges; burning them early means vulnerability later. Session loop — Players learn to reserve 1 charge for emergency escapes, creating meaningful tension with the temptation to use all 3 offensively.

**UEFN implementation:** Player Character Verse API (`movement_component`) for velocity manipulation. Custom `ShadowCharge` manager class tracking charges per player. `TriggerVolume` for the intangibility window. Visual FX: particle system on teleport origin and destination.

**Tuning parameters:**
- Teleport distance: start 6m (test range 4–10m)
- Intangibility window: start 0.3s (test range 0.1–0.5s)
- Charge regen time: start 8s (test range 5–12s)
- Max charges: start 3 (test range 2–4)

**Skill expression:** A beginner uses Shadow Dash reactively to escape. An expert uses it to dodge a specific shot they predicted, then immediately repositions to take the counter-shot during the opponent's recovery animation.

**Fortnite-native fit:** Complements building — players can dash through a wall and build a defensive structure mid-dash, creating a new high-skill play. Conflicts minimally with shooting — the 0.3s intangibility window is short enough to not break fights.
