# Few-Shot Examples Design

**Category:** context-preparation
**When to use:** Creating few-shot examples that reliably steer model behavior toward a specific output format or reasoning pattern.

---

You are a prompt engineer specializing in few-shot example design. Create a set of high-quality few-shot examples for the task below. Well-designed few-shot examples do more than show the output format — they demonstrate the reasoning pattern, handle edge cases, and implicitly teach the model what NOT to do.

For each example:
1. Cover a distinct scenario — happy path, edge case, and at least one "tricky" case where the wrong approach is tempting.
2. Show the exact input-output pair — nothing more.
3. If the task involves reasoning, show the reasoning in the output (not as a separate "think" step).

After the examples, provide:
- **Coverage analysis:** What cases are covered and what's still missing.
- **Anti-pattern example:** One example showing what BAD output looks like — labeled clearly, for use in the system prompt as a "do NOT do this" example.

**Task description:**
[describe exactly what the model needs to do — input type, output type, decision rules]

**Desired output format:**
[show the exact output structure you want]

**Edge cases to cover:**
[list the edge cases you know exist]

---

## Example output

**Task:** Classify customer support messages as: Bug Report / Feature Request / Billing Question / Other. Return only the classification and a one-sentence reason.

**Example 1 (happy path — Bug Report):**
Input: "The export button stopped working after yesterday's update. It just shows a loading spinner forever."
Output: Bug Report — The user describes behavior that worked previously and is now broken after a specific event.

**Example 2 (happy path — Feature Request):**
Input: "It would be great if I could export reports in CSV format, not just PDF."
Output: Feature Request — The user is asking for new functionality that doesn't currently exist.

**Example 3 (tricky — could be Bug OR Feature):**
Input: "The search doesn't find results when I use quotes around phrases."
Output: Bug Report — Quoted phrase search is an expected behavior in most search interfaces; its absence is more likely a broken feature than a missing one.

**Example 4 (edge case — ambiguous):**
Input: "I was charged twice this month."
Output: Billing Question — The user is reporting a financial discrepancy, regardless of whether it's a bug or a billing system issue.

**Anti-pattern (do NOT do this):**
Input: "The export button stopped working."
Output: ❌ This could be a Bug Report or Feature Request or Billing Question — I need more information. → This output delays resolution. Classify with the most likely category based on available information.
