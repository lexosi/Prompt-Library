# Diagnose Vague Output

**Category:** prompt-debugging
**When to use:** The AI is producing generic, non-specific responses — surface-level answers when you need depth and specificity.

---

You are a prompt engineering expert. I'm getting vague, generic output from an AI model when I need specific, detailed responses. Diagnose why and fix it.

Analyze the prompt and the bad output below:

1. **Specificity diagnosis:** What is the prompt failing to specify that allows the model to give a generic answer? List each missing constraint.
2. **Ambiguity diagnosis:** What terms in the prompt could be interpreted multiple ways? The model is choosing the safest/easiest interpretation.
3. **Format diagnosis:** Is the prompt missing format instructions that would force specificity (e.g., "give exactly 3 examples," "format as a table," "cite specific line numbers")?
4. **Rewritten prompt:** Provide a revised prompt that addresses all identified issues.
5. **Prediction:** What specifically will be different in the output with the new prompt?

**Original prompt:**
```
[paste the prompt that's producing vague output]
```

**Bad output example:**
```
[paste an example of the vague/generic response you're getting]
```

**What you actually wanted:**
[describe the specific, detailed response you needed]

---

## Example output

**Specificity diagnosis:**
- "Analyze the code" — the model doesn't know what dimension to analyze: performance? security? style? correctness? It's picking all of them shallowly.
- "Give feedback" — feedback at what level? The model is defaulting to high-level architectural comments when you want line-level specifics.
- No scope limit — the model is spreading attention across the entire file instead of focusing on the critical paths.

**Ambiguity diagnosis:**
- "Good code" is a value judgment that varies by context. The model has no defined standard to evaluate against.

**Rewritten prompt:**
```
Review ONLY the authentication middleware in the code below. For each security vulnerability you find:
1. Quote the exact line(s) where it occurs
2. Name the vulnerability type (e.g., "timing attack," "SQL injection surface")
3. Rate severity: Critical / High / Medium
4. Give the 1–3 line fix

Ignore style, performance, and architecture. Only security.
```

**Prediction:** Output will cite specific line numbers, name specific vulnerability types, and provide concrete fixes instead of general recommendations.
