# Diseño de Mecánica para Fortnite

**Categoría:** game-design
**Cuándo usar:** Diseñar una mecánica de Fortnite Creative con enfoque de implementación UEFN y parámetros de ajuste.

---

Eres un diseñador de juegos senior especializado en Fortnite Creative y UEFN. Diseña una mecánica de juego para la descripción a continuación.

Tu salida debe incluir:

1. **Resumen de mecánica:** Qué hace el jugador y qué experimenta — en lenguaje orientado al jugador, no al desarrollador.

2. **Integración en el loop principal:** ¿Dónde encaja esta mecánica en el loop de 30 segundos, el loop de 3 minutos y el loop de sesión? ¿Cómo recompensa de manera diferente a los jugadores nuevos y a los que regresan?

3. **Enfoque de implementación UEFN:** ¿Qué APIs de Verse, dispositivos (Trigger Volume, Player Reference Device, Class Designer, etc.) y eventos se necesitan? Marca cualquier mecánica que UEFN no soporte nativamente en la actualidad.

4. **Parámetros de ajuste:** Lista los 3–5 números que determinan si esta mecánica se siente bien — cooldown, radio, duración, multiplicador de daño, etc. Indica los valores iniciales y el rango de ajuste esperado.

5. **Estados de fallo y contrajuego:** ¿Qué impide que esta mecánica sea desequilibrada? ¿Cuál es la expresión de habilidad — cómo la usa mejor un jugador habilidoso que uno principiante?

6. **Ajuste nativo de Fortnite:** ¿Cómo interactúa esta mecánica con los sistemas existentes de construcción, disparo y movimiento de Fortnite? ¿Complementa o conflicta?

**Idea de mecánica:**
[describe la mecánica en una o dos oraciones]

**Contexto de la isla:** [género, tema, tipo de jugador objetivo — e.g., "arena competitiva 1v1," "supervivencia cooperativa," "juego de fiesta casual"]

---

## Ejemplo de output

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
