# Depurar Error de Verse

**Categoría:** uefn-scripting
**Cuándo usar:** Traducir errores crípticos del compilador de Verse a lenguaje claro con una corrección correcta.

---

Eres un desarrollador UEFN senior especializado en depuración de Verse. Analiza el error de Verse y el código a continuación.

1. **Interpretación del error:** Traduce el mensaje de error de Verse a lenguaje sencillo. Los mensajes de error de Verse a menudo son crípticos — indica qué está objetando realmente el compilador.

2. **Causa raíz:** Identifica la(s) línea(s) exactas que causan el error y por qué. Errores comunes de Verse a verificar:
   - `<suspends>` faltante en funciones que usan `await`/`Sleep`
   - Tipo `option` accedido sin desenvolver (falta `if (Value := ...)`)
   - Calificador de efecto incorrecto (`<transacts>` vs `<decides>` vs `<suspends>`)
   - Incompatibilidad de tipo entre `agent` y `player` (requiere downcast explícito)
   - Variable mutable usada sin la palabra clave `set`
   - Import de módulo faltante para el tipo que se usa

3. **Corrección:** El código corregido con una explicación de cada cambio.

4. **Patrón preventivo:** Un patrón específico de Verse que previene esta clase de error en futuros scripts.

**Versión de UEFN:** [verifica tu versión de UEFN en el editor — ayuda con compatibilidad de API]

**Mensaje de error:**
```
[pega el error completo del compilador Verse o en tiempo de ejecución]
```

**Código:**
```verse
[pega el código Verse que falla]
```

---

## Ejemplo de output

**Error message:** `Logic error: Function 'Sleep' requires a suspending context but is called in a non-suspending function.`

**Plain language:** You're calling `Sleep()` inside a function that isn't marked as `<suspends>`. Verse requires any function that pauses execution to declare that it can pause — this is the effect system enforcing it.

**Root cause:** Line 23: `OnZoneEntered(Agent : agent) : void =` — event handler functions cannot be `<suspends>` because they're called synchronously by the event system. You're calling `Sleep()` directly inside it.

**Fix:**
```verse
# BEFORE (broken):
OnZoneEntered(Agent : agent) : void =
    Sleep(2.0)  # Error: Sleep requires <suspends>
    ActivateReward(Agent)

# AFTER (correct):
OnZoneEntered(Agent : agent) : void =
    # Spawn a new async task — the handler returns immediately, the task runs concurrently
    spawn { DelayedReward(Agent) }

DelayedReward(Agent : agent)<suspends> : void =
    Sleep(2.0)  # Now valid — this function is marked <suspends>
    ActivateReward(Agent)
```

**Preventive pattern:** Event handler functions (`TriggeredEvent.Subscribe(Handler)`) can never be `<suspends>`. Any async logic triggered by an event must always be wrapped in `spawn { AsyncFunction(args) }`. Remember this rule and you'll never hit this error again.
