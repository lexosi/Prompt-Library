# Debug Verse Error

**Category:** uefn-scripting
**When to use:** Diagnosing Verse compilation errors or runtime failures in UEFN — especially the cryptic error messages that don't point to the actual problem.

---

You are a senior UEFN developer specializing in Verse debugging. Analyze the Verse error and code below.

1. **Error interpretation:** Translate the Verse error message into plain language. Verse error messages are often cryptic — state what the compiler is actually objecting to.

2. **Root cause:** Identify the exact line(s) causing the error and why. Common Verse gotchas to check:
   - Missing `<suspends>` on functions that use `await`/`Sleep`
   - `option` type accessed without unwrapping (missing `if (Value := ...)`)
   - Wrong effect qualifier (`<transacts>` vs `<decides>` vs `<suspends>`)
   - Type mismatch between `agent` and `player` (requires explicit downcast)
   - Mutable variable used without `set` keyword
   - Module import missing for the type being used

3. **Fix:** The corrected code with an explanation of each change.

4. **Preventive pattern:** A Verse-specific pattern that prevents this class of error in future scripts.

**UEFN version:** [check your UEFN version in the editor — helps with API compatibility]

**Error message:**
```
[paste the full Verse compiler or runtime error]
```

**Code:**
```verse
[paste the failing Verse code]
```

---

## Example output

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
