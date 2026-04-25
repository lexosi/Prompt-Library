# Prompt Debugging Prompts

**Domain:** AI Engineering
**Audience:** Prompt engineers, AI product leads, LLM developers

## When to Use

Use these prompts when an AI model is producing bad output and you need to figure out why. Prompt debugging is a systematic discipline — these prompts treat it as such.

## Prompts in This Category

| File | Situation |
|------|-----------|
| `diagnose-vague-output.md` | AI is producing generic, non-specific responses |
| `fix-hallucinating-prompt.md` | AI is confidently making up facts or code |
| `improve-prompt-specificity.md` | Tightening a prompt that works sometimes but not consistently |
| `chain-of-thought-debug.md` | Debugging multi-step reasoning that goes wrong mid-chain |

## Tips

- Always paste the exact failing prompt and the exact bad output — paraphrasing introduces error.
- State what you expected the AI to do differently.
- Try to isolate whether the problem is in the system prompt, the user turn, or the context.
