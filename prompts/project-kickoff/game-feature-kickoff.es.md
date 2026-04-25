# Kickoff de Feature de Juego

**Categoría:** project-kickoff
**Cuándo usar:** Documento de alineación pre-producción para una feature de Fortnite o Roblox con suposiciones de diversión declaradas explícitamente.

---

Escribe un documento de kickoff de característica para una nueva característica de juego. Este documento alinea al diseñador y al desarrollador antes de que comience el trabajo, previniendo la fuente más común de retrabajo: construir algo técnicamente correcto pero funcionalmente incorrecto.

El documento debe cubrir:

**NOMBRE DE LA CARACTERÍSTICA Y PLATAFORMA:** [e.g., "Mecánica de Cambio de Gravedad — UEFN Fortnite Creative"]

**PITCH DE UNA LÍNEA:** Qué hace esta característica desde la perspectiva del jugador. No técnico. No interno. Lo que experimenta el jugador.

**FANTASÍA DEL JUGADOR:** ¿Qué siente el jugador al usar esta característica? (¿Poder, tensión, descubrimiento, competencia?) Este es el norte verdadero.

**LOOP PRINCIPAL:** ¿Cómo encaja esta característica en el loop momento a momento del juego? Antes → Durante → Después de la interacción con la característica.

**RESTRICCIONES UEFN/ROBLOX:**
- UEFN: ¿Qué dispositivos Verse y APIs están involucrados? ¿Alguna limitación conocida?
- Roblox: ¿Qué servicios (DataStore, RemoteEvent, etc.)? ¿Restricciones de rendimiento?

**SUPOSICIÓN DE DIVERSIÓN:** ¿Qué debe ser cierto para que esto sea divertido? Establécelo explícitamente — esta es la suposición que probarás primero.

**ALCANCE:**
- En V1: [la versión más pequeña que prueba la suposición de diversión]
- Fuera de V1: [las ideas geniales que vienen después si V1 funciona]

**CRITERIOS DE PRUEBA:** ¿Cómo harás el playtest de esto? ¿Qué observarás específicamente?

**Descripción de la característica:**
[describe la característica]
**Plataforma:** [UEFN / Roblox / ambas]

---

## Ejemplo de output

**FEATURE NAME:** Wall-Run — UEFN Fortnite Creative

**ONE-LINE PITCH:** Players can sprint horizontally across any vertical wall surface for up to 3 seconds before launching into a jump.

**PLAYER FANTASY:** Feeling like a parkour athlete — fluid, fast, and in total control of the environment. The satisfaction comes from chaining wall-runs with jumps to cross gaps that look impossible.

**CORE LOOP:** Normal sprint → collide with wall → wall-run activates (visual FX + audio cue) → player can steer along the wall → wall-run ends → player launches → land or chain to next wall.

**UEFN CONSTRAINTS:** Custom player movement via Verse `player_movement_component`. No native wall detection — must use raycasting via `GetHitResult`. Frame budget: movement logic must complete in < 2ms to avoid hitching at 60fps.

**FUN ASSUMPTION:** Players will feel rewarded when they successfully chain two wall-runs in a row. Test this first — if chaining feels inconsistent or accidental, the feature won't be fun.

**SCOPE V1:** Straight walls only, fixed 3-second duration, single wall surface. No diagonal runs, no ceiling runs, no speed boost on exit.
