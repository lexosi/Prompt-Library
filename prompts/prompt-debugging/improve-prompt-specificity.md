# Improve Prompt Specificity

**Category:** prompt-debugging
**When to use:** A prompt works sometimes but not consistently — the output quality varies too much across runs.

---

You are a prompt engineering expert. The prompt below produces inconsistent results — sometimes good, sometimes not. Make it reliable by increasing specificity without making it rigid or verbose.

Analyze:
1. **Variance sources:** What elements of the prompt are underspecified enough to allow widely different interpretations across runs? List each.
2. **Hidden assumptions:** What does the prompt assume the model knows or will do that isn't actually guaranteed? State each assumption.
3. **Output format ambiguity:** Is the expected output format clear? If the model has latitude over structure, it will vary it.
4. **Edge case gaps:** What edge cases (empty input, borderline cases, unexpected formats) isn't the prompt handling? How does the model currently behave in those cases?
5. **Rewritten prompt:** More specific version that preserves the original intent but eliminates variance.
6. **Regression check:** List 3 test cases (happy path, edge case, adversarial input) you should run to verify the new prompt performs better.

**Original prompt:**
```
[paste the inconsistent prompt]
```

**Example of a GOOD output from this prompt:**
```
[paste an example of when it worked well]
```

**Example of a BAD output from this prompt:**
```
[paste an example of when it failed]
```

---

## Example output

**Variance sources:**
- "Summarize the article" — summary length is unspecified: the model varies between 2 sentences and 8 paragraphs.
- "Key points" — what counts as "key" is subjective: the model sometimes focuses on facts, sometimes on implications, sometimes on recommendations.
- No persona or audience specified — the register (formal/informal, technical/accessible) varies run to run.

**Hidden assumptions:**
- The prompt assumes the model will read the full article before summarizing. In longer documents, it sometimes stops reading at a natural section boundary.
- The prompt assumes "summary" means a paragraph, but the model sometimes produces a bullet list.

**Rewritten prompt:**
```
Summarize the following article in exactly 3 bullet points. Each bullet:
- Starts with a bold key claim (5–8 words)
- Followed by 1 sentence of supporting evidence from the article
- Is written for a non-technical business reader

Do not add bullets for things not explicitly stated in the article. Do not editorialize.

Article:
[article text]
```

**Regression tests:**
1. Happy path: a well-structured news article → expect 3 clean bullets.
2. Edge case: an article with only one main claim → expect 3 bullets where 2 are supporting details, not invented claims.
3. Adversarial: a very long article → expect the model still reads fully and doesn't just summarize the introduction.
