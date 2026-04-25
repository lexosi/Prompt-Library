# UEFN Scripting Prompts

**Domain:** Game Development
**Language:** Verse
**Platform:** UEFN (Unreal Editor for Fortnite)

## When to Use

Use these prompts when writing or debugging Verse scripts for UEFN. Verse is a concurrent, strongly-typed scripting language designed for Fortnite Creative — these prompts account for its unique constraints (no null, effect system, concurrency model).

## Prompts in This Category

| File | Situation |
|------|-----------|
| `verse-script-template.md` | Starting a new Verse script with correct structure and patterns |
| `device-interaction-script.md` | Scripting interactions between UEFN devices via Verse |
| `player-mechanics-verse.md` | Implementing custom player movement or ability mechanics in Verse |
| `debug-verse-error.md` | Diagnosing Verse compilation errors and runtime failures |

## Tips

- Verse has no null — always use `option` types and handle the `false` case explicitly.
- The effect system in Verse is strict: mark your functions with `<suspends>` when they need to await async events.
- UEFN's device API changes frequently — if a script stopped working, check if the device API was updated.
