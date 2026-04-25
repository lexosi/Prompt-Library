# Developer Documentation

**Category:** content-strategy
**When to use:** Writing clear, scannable documentation for a developer tool, API, or library — documentation that developers actually read and use.

---

You are a technical writer specializing in developer documentation. Write documentation for the following developer tool or API. Developer documentation must be written for someone in a hurry — they're blocked on a problem and need the answer immediately.

Principles:
- Lead with what the developer needs to DO, not what the system IS.
- Every code example must be copy-paste ready — no pseudocode, no placeholder that requires significant modification.
- Include the failure case: what happens when it goes wrong, and how to fix it.
- Structure for scanning: headings should be outcomes ("Authenticate a user"), not topics ("Authentication").

Your documentation must include:

1. **Quick start (< 5 minutes to first success):** The minimal steps to get something working. Include: installation, configuration, and one real working example.

2. **Core concepts (1 page):** The 3–5 concepts the developer must understand to use this correctly. Brief. Diagram if it clarifies.

3. **Reference:** For each major function/endpoint/method:
   - Signature with types
   - Parameter table (name, type, required, description)
   - Return value description
   - One working code example
   - Common errors and their solutions

4. **Guides:** 2–3 task-oriented guides ("How to handle pagination," "How to authenticate with OAuth"). These are different from reference — they solve a complete task.

5. **Changelog note:** What changed in the most recent version that developers upgrading need to know.

**Tool/API to document:**
[describe what it does]

**Audience:**
[who uses it — experience level, language/framework context]

**Most common developer mistake:**
[what developers typically get wrong with this tool]

---

## Example output

# Quick Start — Verse State Manager

**Install**
```bash
# UEFN package manager (add to your project's verse.toml)
[dependencies]
verse_state_manager = "1.2.0"
```

**First working example (copy-paste ready)**
```verse
using { /YourNamespace/verse_state_manager }

my_game_manager := class(creative_device):
    var State : game_state_manager = game_state_manager{}

    OnBegin<override>()<suspends> : void =
        State.Initialize(InitialPhase := game_phase.lobby)
        State.PhaseChanged.Subscribe(OnPhaseChanged)

    OnPhaseChanged(NewPhase : game_phase) : void =
        Print("Phase changed to: {NewPhase}")
```

**Core concepts:**
1. **State machine** — All game state lives in one `game_state_manager`. Never track phase in multiple variables.
2. **PhaseChanged event** — Subscribe to this, don't poll. The manager fires the event on every valid transition.
3. **Invalid transitions** — Transitioning from `ended` to any state other than `lobby` throws a Verse error. Check the transition table in Reference.

**Common mistake:** Developers initialize `game_state_manager` inside an event handler instead of `OnBegin`. This creates a new state machine on every event, losing all subscriptions.
