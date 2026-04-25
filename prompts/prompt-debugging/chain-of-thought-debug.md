# Chain of Thought Debug

**Category:** prompt-debugging
**When to use:** A multi-step reasoning chain produces wrong answers — the model's reasoning looks plausible but reaches an incorrect conclusion.

---

You are a prompt engineering expert specializing in chain-of-thought reasoning. The reasoning chain below reaches a wrong conclusion. Identify exactly where the reasoning went wrong and fix it.

Analyze:
1. **Step-level diagnosis:** Go through each reasoning step and identify the first step where the model makes an error (factual, logical, or arithmetic). Everything after a wrong step is reasoning on a false premise.
2. **Error type:** Is this a factual error (wrong information), logical error (invalid inference), arithmetic error, or a framing error (the model solved a different problem than intended)?
3. **Root cause in the prompt:** What in the original prompt or context caused the model to make this error? (Ambiguous phrasing, missing context, implicitly wrong assumption?)
4. **Prompt fix:** How should the prompt change to prevent this specific error? Options:
   - Add intermediate checkpoints ("Before continuing, verify that X is true")
   - Add explicit constraints ("Do not assume Y — verify it from the context")
   - Restructure the task into sub-questions
5. **Rewritten prompt:** The revised prompt with the fix applied.

**Original prompt:**
```
[paste the prompt that prompted the faulty reasoning chain]
```

**Faulty reasoning chain:**
```
[paste the model's step-by-step reasoning and wrong conclusion]
```

**Correct answer:** [what the answer should be]

---

## Example output

**Step-level diagnosis:**
- Step 1: "The request has 3 items" — CORRECT
- Step 2: "Each item costs $12.50" — CORRECT
- Step 3: "Total = 3 × $12.50 = $36.50" — ERROR. 3 × 12.50 = 37.50, not 36.50. This is an arithmetic error.
- Step 4 onward: All subsequent reasoning uses $36.50 as the base — all subsequent answers are wrong.

**Error type:** Arithmetic error in a multiplication step.

**Root cause in the prompt:** The prompt asked the model to "work through the math step by step" but did not ask it to verify intermediate calculations. The model performs the arithmetic inline without checking it.

**Prompt fix:** Add a verification checkpoint after arithmetic steps:
```
After each calculation, verify your result by computing it a second way (e.g., repeated addition instead of multiplication).
```

**Rewritten prompt:**
```
[original task]

Work through this step by step. After any multiplication or division, verify the result using an alternative method (e.g., verify 3 × 12.50 by adding 12.50 + 12.50 + 12.50). If the two methods disagree, recompute before continuing.
```

**Why this works:** The verification step forces the model to catch arithmetic errors before they propagate through the rest of the chain.
