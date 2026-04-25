# CLAUDE.md — Prompt Library Structure Guide

This file tells Claude (and contributors) how to add, modify, and organize prompts in this library.

## Directory Layout

```
prompt-library/
├── CLAUDE.md          ← this file
├── README.md          ← public-facing intro for GitHub visitors
├── index.md           ← flat list of every prompt with descriptions and links
└── prompts/
    └── <category>/
        ├── README.md  ← when to use prompts in this category
        └── <prompt-name>.md
```

## Adding a New Category

1. Create `prompts/<category-name>/` (use kebab-case).
2. Add `prompts/<category-name>/README.md` explaining when to use prompts in that category.
3. Add 3–5 prompt files (see prompt file format below).
4. Add every new prompt to `index.md` under the correct category heading.

## Adding a New Prompt

1. Name the file descriptively in kebab-case: `diagnose-rust-error.md`, not `prompt1.md`.
2. Use **exactly** this structure:

**`<name>.md` (English):**
```markdown
# Prompt Name

**Category:** category-name
**When to use:** one-line description of the exact situation

---

[Full prompt text in English]

---

## Example output

[Short example showing what a good AI response looks like — 5–15 lines]
```

**`<name>.es.md` (Spanish):**
```markdown
# Nombre del Prompt

**Categoría:** category-name
**Cuándo usar:** descripción en una línea de la situación exacta

---

[Texto completo del prompt en español]

---

## Ejemplo de output

[Ejemplo corto mostrando cómo se ve una buena respuesta — 5–15 líneas]
```

3. Update `index.md`: add a line under the category heading:
   `- [Prompt Name](prompts/<category>/<file>.md) — one-line description`

## Conventions

| Rule | Detail |
|------|--------|
| Language | Every prompt must exist in both English and Spanish |
| Specificity | Prompts must be immediately usable, not generic templates |
| Tech stack | Technical prompts assume Rust, Python, TypeScript |
| Platform | Game prompts reference UEFN, Fortnite, and/or Roblox specifically |
| Leadership | Leadership prompts assume the user leads AI agents + human developers |
| Tone | Professional but direct — no filler phrases |

## File conventions

- Every prompt exists as two files: `<name>.md` (English) and `<name>.es.md` (Spanish).
- Ignore all `*.es.md` files unless the user explicitly requests Spanish versions. These files exist for human readers and multilingual teams, not for AI context.
- The `## English` / `## Spanish` split inside a single file is the **old format** — do not use it for new prompts.
- New prompts: create `<name>.md` (English-only) and `<name>.es.md` (Spanish-only) as separate files from the start.

## Categories Reference

| Folder | Domain |
|--------|--------|
| debugging | Technical — diagnosing bugs in Rust/Python/TypeScript/AI agents |
| code-review | Technical — reviewing code for correctness, safety, and style |
| architecture-design | Technical — designing systems and AI pipelines |
| refactor | Technical — improving existing code structure |
| task-delegation | Leadership — assigning work to humans or AI agents |
| project-kickoff | Leadership — starting new projects with clear alignment |
| decision-making | Leadership — structured frameworks for technical decisions |
| client-communication | Business — written communication with clients |
| pitch-and-positioning | Business — pitching products, services, or ideas |
| outreach | Business — cold outreach, partnerships, recruiting |
| prompt-debugging | AI Engineering — diagnosing and improving prompt quality |
| context-preparation | AI Engineering — designing system prompts and context |
| game-design | Game — mechanics, economy, and experience design |
| uefn-scripting | Game — Verse scripting for UEFN/Fortnite Creative |
| content-strategy | Content — thought leadership, courses, documentation |
| social-media | Content — LinkedIn, Twitter/X, TikTok, YouTube |
