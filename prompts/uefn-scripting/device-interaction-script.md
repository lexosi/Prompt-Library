# Device Interaction Script

**Category:** uefn-scripting
**When to use:** Writing Verse scripts that coordinate multiple UEFN devices — responding to device events, activating devices conditionally, and passing state between devices.

---

You are a senior UEFN developer specializing in device scripting. Write a Verse script that coordinates the following UEFN devices. The script must use UEFN's event subscription model correctly and handle the timing and ordering issues that commonly break device interaction scripts.

Include:
1. **Device references:** All devices as `@editable` class members — never hardcoded.
2. **Event subscriptions:** Subscribe to the right events on `OnBegin` — not inside event handlers (causes duplicate subscriptions).
3. **Device activation sequencing:** If devices must activate in order, use `Sleep()` or event chaining, not arbitrary timing assumptions.
4. **State management:** If the script tracks state (e.g., "which phase is active"), use a clear state variable, not implicit assumptions about which events have fired.
5. **Edge cases handled:**
   - What happens if the same event fires twice quickly (debounce if needed)?
   - What happens if a device reference isn't assigned in the editor?
   - What happens if a player leaves mid-interaction?

**Devices to coordinate:**
[list the devices — e.g., "Trigger Device → unlock a locked door via Item Granter Device after player picks up a key"]

**Desired interaction flow:**
[describe step by step what should happen when, in response to what]

---

## Example output

```verse
# key_door_controller.verse
# Player picks up a key item → door unlocks → congratulation message plays.

using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

key_door_controller := class(creative_device):

    @editable
    KeyPickupTrigger : item_spawner_device = item_spawner_device{}  # Trigger when key is picked up

    @editable
    LockedDoor : prop_mover_device = prop_mover_device{}  # The door that opens

    @editable
    SuccessNotification : hud_message_device = hud_message_device{}

    var DoorUnlocked : logic = false  # Prevent double-unlock if trigger fires twice

    OnBegin<override>()<suspends> : void =
        # Subscribe once on begin — not inside handlers.
        KeyPickupTrigger.ItemPickedUpEvent.Subscribe(OnKeyPickedUp)
        Print("key_door_controller: Ready. Waiting for key pickup.")

    OnKeyPickedUp(Agent : agent) : void =
        if (DoorUnlocked?):
            Print("key_door_controller: Door already unlocked — ignoring duplicate event.")
            return

        set DoorUnlocked = true  # Set before async operations to prevent race condition

        if (Player := player[Agent]):
            Print("key_door_controller: Key picked up by player. Unlocking door.")
            # Activate door movement — the prop_mover plays its animation
            LockedDoor.Activate(Agent)
            # Wait for door animation before showing success message
            Sleep(1.5)
            SuccessNotification.Show(Player)
        else:
            # Non-player picked up the item (shouldn't happen in standard gameplay)
            set DoorUnlocked = false  # Reset so a player can still trigger it
            Print("key_door_controller: Item picked up by non-player — resetting.")
```
