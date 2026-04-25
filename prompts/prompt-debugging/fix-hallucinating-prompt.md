# Fix Hallucinating Prompt

**Category:** prompt-debugging
**When to use:** The AI is confidently producing factually wrong information, fabricating citations, or inventing code that doesn't exist.

---

You are a prompt engineering expert specializing in hallucination reduction. The prompt below is causing a model to confidently produce false information. Diagnose the root cause and fix it.

Analyze:
1. **Hallucination trigger diagnosis:** Why is the model hallucinating? Common causes: being asked to produce information it doesn't have, being asked for specifics on topics where it lacks confident knowledge, format pressure (e.g., "give 5 examples" forces invention when only 3 exist), or missing grounding context.
2. **Confidence calibration problem:** Is the model presenting uncertain information as certain? What in the prompt is suppressing its uncertainty?
3. **Structural fixes:** Changes to the prompt that reduce hallucination without reducing usefulness:
   - Adding explicit permission to say "I don't know"
   - Providing source material the model should draw from
   - Changing the task from "produce facts" to "reason from provided context"
   - Adding verification steps ("before answering, list what you're certain about vs. uncertain about")
4. **Rewritten prompt:** The revised prompt.
5. **Remaining risk:** What hallucination risk remains even with the fix?

**Original prompt:**
```
[paste the hallucinating prompt]
```

**Example of hallucinated output:**
```
[paste an example showing the false information]
```

**What you actually need:** [describe what accurate output would look like]

---

## Example output

**Hallucination trigger:** The prompt asks the model to "list all papers published on X topic in 2024." The model doesn't have reliable recall of specific publications and dates, but the task demands a complete list — so it invents entries to satisfy the completeness requirement.

**Confidence calibration problem:** The imperative "list all" removes the model's ability to hedge. It interprets the instruction as "produce a complete, confident list," even when it cannot do so reliably.

**Structural fixes:**
1. Switch from open recall to grounded reasoning: provide a list of papers (from a real source) and ask the model to analyze or summarize them.
2. Add explicit uncertainty permission: "If you are not certain a paper exists and was published in this exact year, do not include it. Prefer a short accurate list over a long inaccurate one."
3. Add a verification step: "Before answering, state how confident you are in each entry on a scale of Low/Medium/High."

**Rewritten prompt:**
```
Below is a list of papers on [topic] from 2024 that I have verified. Summarize the key findings from each and identify common themes. Do not add papers not in this list.

[paste your verified paper list here]
```

**Remaining risk:** If the provided source list itself contains errors, the model will reason faithfully from incorrect input. Verify your source material independently.
