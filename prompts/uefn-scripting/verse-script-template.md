# Verse Script Template

**Category:** uefn-scripting
**When to use:** Starting a new Verse script for UEFN with correct structure, naming conventions, and patterns — avoiding the common mistakes that waste hours in compilation errors.

---

You are a senior UEFN developer. Generate a well-structured Verse script template for the following feature. The template must follow UEFN's Verse conventions, use correct effect qualifiers, and handle the most common runtime failure cases for this type of script.

Include:
1. **Module declaration and imports:** Correct `using` declarations for the required namespaces.
2. **Class definition:** The main class with the correct base class (e.g., `creative_device`).
3. **Editable properties:** Properties that should be configurable in the UEFN editor, with `@editable` decorators.
4. **OnBegin and event handlers:** Proper async structure with `<suspends>` where needed.
5. **Option handling:** Every `option` type unwrapped safely — no forced `?` without a fallback.
6. **Logging:** Basic `Print()` calls for the main state transitions (for debugging during development).
7. **Comments:** Verse-specific caveats noted inline where behavior might surprise developers coming from other languages.

**Feature to implement:**
[describe what the Verse script should do — e.g., "teleport a player to a random spawn point when they touch a trigger volume"]

**Devices involved:**
[list the UEFN devices this script will interact with — e.g., "Trigger Device, Teleporter Device, Player Spawner"]

---

## Example output

```verse
# random_teleport_device.verse
# Teleports a player to a random spawn point when they activate a trigger.

using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

random_teleport_device := class(creative_device):

    # Editor-configurable teleporter devices. Assign at least one in the UEFN editor.
    @editable
    Teleporters : []teleporter_device = array{}

    # Optional trigger that activates the teleport.
    @editable
    ActivationTrigger : trigger_device = trigger_device{}

    OnBegin<override>()<suspends> : void =
        if (Teleporters.Length = 0):
            Print("random_teleport_device: No teleporters assigned — device inactive.")
            return  # Exit early; nothing to do without targets.

        # Subscribe to the trigger event. Agent is the player who activated it.
        ActivationTrigger.TriggeredEvent.Subscribe(OnTriggerActivated)
        Print("random_teleport_device: Ready. {Teleporters.Length} teleporters registered.")

    # Verse event handlers cannot be <suspends> — use a wrapper task if you need async logic.
    OnTriggerActivated(Agent : agent) : void =
        if (Player := player[Agent]):      # Downcast agent to player — may fail for NPCs.
            TeleportToRandom(Player)
        else:
            Print("random_teleport_device: Trigger activated by non-player agent — skipping.")

    TeleportToRandom(Player : player) : void =
        # GetRandomInt upper bound is exclusive — use Length, not Length - 1.
        Index := GetRandomInt(0, Teleporters.Length)
        if (Target := Teleporters[Index]):  # Array access returns option<T> — always check.
            Target.Teleport(Player)
            Print("random_teleport_device: Teleported player to index {Index}.")
        else:
            Print("random_teleport_device: Failed to access teleporter at index {Index}.")
```
