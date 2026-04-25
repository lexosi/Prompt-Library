# Script de Interacción de Dispositivos

**Categoría:** uefn-scripting
**Cuándo usar:** Coordinar múltiples dispositivos UEFN con suscripción a eventos correcta y gestión de estado.

---

Eres un desarrollador UEFN senior especializado en scripting de dispositivos. Escribe un script Verse que coordine los siguientes dispositivos UEFN. El script debe usar el modelo de suscripción a eventos de UEFN correctamente y manejar los problemas de temporización y orden que comúnmente rompen los scripts de interacción de dispositivos.

Incluye:
1. **Referencias de dispositivos:** Todos los dispositivos como miembros de clase `@editable` — nunca codificados.
2. **Suscripciones a eventos:** Suscribirse a los eventos correctos en `OnBegin` — no dentro de manejadores de eventos (causa suscripciones duplicadas).
3. **Secuenciación de activación de dispositivos:** Si los dispositivos deben activarse en orden, usa `Sleep()` o encadenamiento de eventos, no suposiciones arbitrarias de temporización.
4. **Gestión de estado:** Si el script rastrea estado (e.g., "qué fase está activa"), usa una variable de estado clara, no suposiciones implícitas sobre qué eventos se han disparado.
5. **Casos límite manejados:**
   - ¿Qué ocurre si el mismo evento se dispara dos veces rápidamente (debounce si es necesario)?
   - ¿Qué ocurre si una referencia de dispositivo no está asignada en el editor?
   - ¿Qué ocurre si un jugador se va a mitad de la interacción?

**Dispositivos a coordinar:**
[lista los dispositivos — e.g., "Trigger Device → desbloquear una puerta bloqueada via Item Granter Device después de que el jugador recoja una llave"]

**Flujo de interacción deseado:**
[describe paso a paso qué debería ocurrir, cuándo, en respuesta a qué]

---

## Ejemplo de output

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
