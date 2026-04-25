# Introducción a Contribución Comunitaria

**Categoría:** outreach
**Cuándo usar:** Presentarte a ti mismo o una contribución a una comunidad de desarrolladores como participante genuino.

---

Escribe un mensaje de introducción para una comunidad de desarrolladores. El objetivo es ser recordado como un contribuidor genuino, no un autopromotor. El mensaje debe:

- Decir quién eres en una oración concreta — qué construyes, no tu título de trabajo
- Explicar específicamente por qué estás en esta comunidad — qué estás aprendiendo, construyendo o contribuyendo
- Hacer referencia a algo específico sobre la comunidad — una discusión reciente, un proyecto o una decisión que encontraste interesante
- Si compartes una contribución (PR, herramienta, artículo): comienza con el problema que resuelve, no con la cosa en sí
- Terminar con una pregunta genuina o una invitación a retroalimentación — muestra que estás aquí para participar, no solo para anunciar

Menos de 150 palabras.

**Contexto:**
- Comunidad: [nombre y enfoque — e.g., "Discord de Rust, canal #async"]
- Por qué te unes: [razón específica]
- Qué estás contribuyendo (si algo): [descripción]
- En qué estás genuinamente curioso en esta comunidad: [pregunta o tema técnico específico]

---

## Ejemplo de output

Hey everyone — I build AI agent systems in Rust and Python, and I've been lurking in the UEFN Creators Discord for a few weeks before posting.

I wanted to share something I built that solved a problem I kept seeing mentioned in #verse-scripting: managing shared mutable state across multiple Verse devices without race conditions. I wrote a small state management pattern using Verse's `sync` and `weak_map` primitives — the post is here: [link].

The question I'm genuinely unsure about: is there a better primitive for this in the current UEFN SDK? I saw the discussion last week about `manager` classes and wasn't sure if that's the intended solution for this pattern.

Happy to get any feedback — especially if I'm missing something obvious.
