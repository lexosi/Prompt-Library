# Player Mechanics in Verse

**Category:** uefn-scripting
**When to use:** Implementing custom player movement, abilities, or interactions in UEFN using Verse's player character APIs.

---

You are a senior UEFN developer specializing in custom player mechanics. Implement the following player mechanic using Verse's player character API. This type of scripting has specific constraints — address them explicitly.

Key constraints to handle:
1. **Player character access:** Always check that `fort_character[Agent]` succeeds — it fails for spectators and eliminateed players.
2. **Concurrent mechanics:** If this mechanic can be triggered while already active, handle the concurrent case (block, stack, or reset).
3. **Cleanup on elimination:** If the mechanic modifies player state, restore defaults when the player is eliminated.
4. **Multiplayer correctness:** State modifications must be per-player, not shared class variables.
5. **Performance:** Verse runs on the simulation thread — avoid per-frame loops. Use event-driven patterns instead.

Your output:
1. Full Verse implementation ready to compile.
2. One comment per non-obvious pattern explaining why it's done that way.
3. A list of editor configuration steps (what the developer must set up in UEFN editor to make this script work).

**Mechanic to implement:**
[describe the custom player mechanic]

**Triggering condition:**
[what triggers the mechanic — button press, entering a zone, picking up an item?]

**Duration and cooldown:**
[how long it lasts, if it has a cooldown]

---

## Example output

```verse
# speed_boost_device.verse
# Grants a player a 3-second speed boost when they enter the trigger zone.
# Cooldown: 10 seconds per player (prevents spam abuse).

using { /Fortnite.com/Devices }
using { /Fortnite.com/Characters }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

speed_boost_device := class(creative_device):

    @editable
    ActivationZone : trigger_device = trigger_device{}

    @editable
    BoostDurationSeconds : float = 3.0

    @editable
    CooldownSeconds : float = 10.0

    # Per-player cooldown tracking — must be a map to avoid shared state bugs.
    # Each player has their own cooldown flag.
    var PlayerCooldowns : [player]logic = map{}

    OnBegin<override>()<suspends> : void =
        ActivationZone.TriggeredEvent.Subscribe(OnZoneEntered)

    OnZoneEntered(Agent : agent) : void =
        if (Player := player[Agent]):
            # Check per-player cooldown — NOT a class-level flag.
            if (PlayerCooldowns[Player] = true):
                return  # Player is on cooldown — ignore this trigger.

            # Spawn a separate task per player so boost/cooldown are independent.
            spawn { ApplyBoost(Player) }

    ApplyBoost(Player : player)<suspends> : void =
        if (Character := fort_character[Player]):
            # Set cooldown BEFORE the boost so a second trigger while boosted is blocked.
            if (set PlayerCooldowns[Player] = true) {}

            # Modify movement speed — Verse uses multipliers, not absolute values.
            Character.SetMaxWalkSpeed(1200.0)  # Default is ~600 — 2× speed
            Print("speed_boost_device: Boost applied to player.")

            Sleep(BoostDurationSeconds)

            # Restore default speed. Always restore — even if player was damaged.
            Character.SetMaxWalkSpeed(600.0)
            Print("speed_boost_device: Boost expired.")

            Sleep(CooldownSeconds)

            if (set PlayerCooldowns[Player] = false) {}
            Print("speed_boost_device: Cooldown cleared for player.")

# EDITOR SETUP:
# 1. Place this device in your UEFN level.
# 2. Assign a Trigger Device to the ActivationZone property.
# 3. Set the trigger volume to "Any Player" activation mode.
# 4. Adjust BoostDurationSeconds and CooldownSeconds in the device properties panel.
```
