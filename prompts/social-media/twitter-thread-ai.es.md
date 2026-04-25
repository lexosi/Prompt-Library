# Hilo de Twitter/X sobre IA

**Categoría:** social-media
**Cuándo usar:** Hilo de 7-10 tweets con una afirmación de apertura contraintuitiva y un tweet 8 retweeteable.

---

Escribe un hilo de Twitter/X sobre un tema de ingeniería de IA. Los hilos que funcionan bien en Twitter/X hacen una afirmación contraintuitiva en el tweet 1 y luego la prueban tweet a tweet.

Reglas:
- **Tweet 1:** Debe hacer una afirmación con la que un ingeniero razonable estaría en desacuerdo. No "la IA está cambiando la ingeniería" — algo como "Deja de llamar a tu cosa un 'agente de IA.' El 90% de lo que se llama agente es solo un LLM con un if-statement." El primer tweet debe ganarse el click-through.
- **Tweets 2–7:** Cada tweet debe ser un insight independiente que apoye la afirmación inicial. No una continuación de una oración — cada tweet debe funcionar por sí solo.
- **Tweet 8 (o penúltimo):** El tweet más retweeteado del hilo — el insight individual más denso.
- **Tweet final:** Llamado a la acción. No "sígueme" — algo que haga que el lector reflexione o participe.
- Longitud de tweet: 240–270 caracteres cada uno (deja espacio para quote-tweets).
- Longitud del hilo: 7–10 tweets.

**Tema:**
[sobre qué es el hilo]

**La afirmación contraintuitiva que quieres hacer:**
[tu posición específica y debatible]

**Tu evidencia más sólida:**
[los ejemplos u observaciones que apoyan tu afirmación]

---

## Ejemplo de output

**Tweet 1:**
Your "AI agent" probably isn't an agent. It's a prompt with a for-loop.

Real agents have: a control loop, persistent state, the ability to decide WHEN to act, and recovery from failure. Most "agents" in production have zero of those things.

Thread on what separates agents from fancy prompts 🧵

**Tweet 2:**
An LLM that calls a function is not an agent. It's an LLM that calls a function.

An agent has a control loop: it observes, reasons, acts, observes the result, and adjusts. Without the adjustment step, you have a one-shot inference call with extra steps.

**Tweet 3:**
The hardest part of building a real agent isn't the model — it's failure handling.

What does your "agent" do when the tool call fails? When the API is down? When it's called 3 times with the same broken input?

Most agents I've seen: crash silently and return empty.

**Tweet 8 (most retweetable):**
The real test: can your agent tell you WHY it took the action it took?

If the answer is buried in a token stream with no structure, it's not an agent — it's a black box with ambitions. Real agents produce auditable reasoning you can debug.

**Final tweet:**
What's the most "agent-like" system you've actually built in production?

I'm curious whether the field is converging on what "agent" actually means in practice.
