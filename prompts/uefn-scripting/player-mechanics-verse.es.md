# Mecánicas de Jugador en Verse

**Categoría:** uefn-scripting
**Cuándo usar:** Implementar movimiento personalizado del jugador o habilidades usando la API de character de Verse.

---

Eres un desarrollador UEFN senior especializado en mecánicas personalizadas de jugador. Implementa la siguiente mecánica de jugador usando la API de personaje de jugador de Verse. Este tipo de scripting tiene restricciones específicas — abórdalas explícitamente.

Restricciones clave a manejar:
1. **Acceso al personaje del jugador:** Siempre verifica que `fort_character[Agent]` tenga éxito — falla para espectadores y jugadores eliminados.
2. **Mecánicas concurrentes:** Si esta mecánica puede desencadenarse mientras ya está activa, maneja el caso concurrente (bloquear, apilar o reiniciar).
3. **Limpieza al ser eliminado:** Si la mecánica modifica el estado del jugador, restaura los valores predeterminados cuando el jugador es eliminado.
4. **Corrección multijugador:** Las modificaciones de estado deben ser por jugador, no variables de clase compartidas.
5. **Rendimiento:** Verse se ejecuta en el hilo de simulación — evita bucles por fotograma. Usa patrones basados en eventos en su lugar.

Tu salida:
1. Implementación completa de Verse lista para compilar.
2. Un comentario por patrón no obvio explicando por qué se hace de esa manera.
3. Una lista de pasos de configuración del editor (qué debe configurar el desarrollador en el editor UEFN para que este script funcione).

**Mecánica a implementar:**
[describe la mecánica personalizada del jugador]

**Condición de activación:**
[qué activa la mecánica — presión de botón, entrar en una zona, recoger un ítem?]

**Duración y cooldown:**
[cuánto dura, si tiene cooldown]

---

## Ejemplo de output

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
