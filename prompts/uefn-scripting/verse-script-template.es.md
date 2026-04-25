# Plantilla de Script en Verse

**Categoría:** uefn-scripting
**Cuándo usar:** Generar un script Verse bien estructurado con calificadores de efecto correctos y manejo de opciones.

---

Eres un desarrollador UEFN senior. Genera una plantilla de script Verse bien estructurada para la siguiente característica. La plantilla debe seguir las convenciones Verse de UEFN, usar calificadores de efecto correctos y manejar los casos de fallo en tiempo de ejecución más comunes para este tipo de script.

Incluye:
1. **Declaración de módulo e imports:** Declaraciones `using` correctas para los namespaces requeridos.
2. **Definición de clase:** La clase principal con la clase base correcta (e.g., `creative_device`).
3. **Propiedades editables:** Propiedades que deben ser configurables en el editor de UEFN, con decoradores `@editable`.
4. **OnBegin y manejadores de eventos:** Estructura async correcta con `<suspends>` donde se necesite.
5. **Manejo de opciones:** Cada tipo `option` desenvuelto de forma segura — no `?` forzado sin un fallback.
6. **Logging:** Llamadas básicas `Print()` para las principales transiciones de estado (para depuración durante el desarrollo).
7. **Comentarios:** Advertencias específicas de Verse anotadas en línea donde el comportamiento pueda sorprender a desarrolladores que vienen de otros lenguajes.

**Característica a implementar:**
[describe qué debe hacer el script Verse — e.g., "teletransportar a un jugador a un punto de spawn aleatorio cuando toca un volumen trigger"]

**Dispositivos involucrados:**
[lista los dispositivos UEFN con los que interactuará este script — e.g., "Trigger Device, Teleporter Device, Player Spawner"]

---

## Ejemplo de output

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
