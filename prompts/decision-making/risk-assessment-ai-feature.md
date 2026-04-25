# Risk Assessment: AI Feature

**Category:** decision-making
**When to use:** Before shipping an AI-powered feature to production — evaluating failure modes, user harm, and business risk.

---

You are an AI product safety engineer. Assess the risks of shipping the following AI feature. Be specific — name real failure modes with realistic probability and impact estimates, not abstract categories.

**Feature description:**
[describe what the AI feature does, who uses it, and how it integrates into the product]

**Model and prompting approach:**
[e.g., Claude 3.5 Sonnet with a RAG-augmented system prompt, zero-shot]

**User population:**
[who will use this — technical sophistication, stakes of the decisions they make with it]

**Assess these risk dimensions:**

1. **Hallucination risk:** In what specific situations will the model confidently produce wrong outputs? What's the user impact when it does?

2. **Misuse risk:** How could a user intentionally use this feature to cause harm — to themselves, others, or the business?

3. **Data/privacy risk:** What sensitive data does this feature touch? What happens if it leaks?

4. **Dependency risk:** What happens if the model provider has an outage? If the model is deprecated?

5. **Drift risk:** How will you know if the feature's quality degrades over time (model updates, distribution shift, prompt injection)?

**For each risk:** Probability (Low/Medium/High), Impact (Low/Medium/High/Critical), and the specific mitigation you recommend.

**Ship/don't ship recommendation:** Given the above, is this ready to ship? If not, what must be true before shipping?

---

## Example output

**Feature:** AI medical symptom checker that suggests possible conditions based on user-described symptoms.

**Risk 1 — Hallucination (Probability: HIGH, Impact: CRITICAL):** The model will confidently suggest a benign condition when the user has a serious one. Most likely failure: user describes atypical presentation of MI as indigestion; model suggests antacids. Mitigation: Mandatory disclaimer on every response + explicit "if symptoms are severe, call emergency services" trigger for specific keyword combinations. Block output if symptom matches emergency keywords without displaying the suggestion first.

**Risk 2 — Misuse (Probability: MEDIUM, Impact: HIGH):** Users may use the tool to self-diagnose and avoid seeking medical care for serious conditions. Mitigation: Every response must include "This is not medical advice. See a doctor for diagnosis." in a visually prominent format — not buried in fine print.

**Ship recommendation:** Do not ship without: (1) emergency symptom detection with hard-coded redirects to emergency services, (2) mandatory human review of all outputs in the first 30 days, (3) legal sign-off on disclaimers.
