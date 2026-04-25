# Script de Contenido Dev para TikTok

**Categoría:** social-media
**Cuándo usar:** Script de TikTok de 30-45 segundos con un gancho de 3 segundos y desglose escena por escena.

---

Escribe un guion de video TikTok para un video de contenido de desarrollador. TikTok recompensa la inmediatez y la prueba visual — el mejor contenido dev en TikTok muestra código real, resultados reales y una presencia humana detrás.

Reglas:
- **Gancho (0–3 segundos):** Debe responder "¿por qué debería ver esto?" antes de que el espectador pueda deslizar. Comienza con el resultado o la cosa sorprendente, no con la introducción.
- **Muestra, no expliques:** El código o la pantalla deben ser visibles. Si describes algo que el espectador podría ver, muéstralo en su lugar.
- **Ritmo:** Corta cada 2–4 segundos. Sin explicaciones largas. Si un concepto tarda 15 segundos en explicarse verbalmente, muéstralo en 5 segundos visualmente.
- **Techo de jerga:** Explica al nivel de un estudiante de CS o un no-desarrollador curioso. Ni principiante total, ni experto profundo.
- **Duración:** 30–45 segundos. Límite estricto de 55 segundos.
- **Gancho de cierre:** Termina con una pregunta, un avance del próximo video, o un desafío al espectador.

Formatea el guion como:
- **[0:00–0:03] GANCHO:** [lo que dices + lo que está en pantalla]
- **[0:03–0:XX] CUERPO:** [escena por escena]
- **[0:XX–fin] CIERRE:** [llamado a la acción]

**Tema del video:**
[qué estás mostrando — e.g., "construyendo un script Verse en UEFN," "depurando un error del borrow checker de Rust," "mi agente de IA completando una tarea"]

**El 'momento wow':** [la cosa única más visualmente impresionante o sorprendente en el video]

**Espectador objetivo:** [e.g., estudiantes de dev, entusiastas de juegos, audiencia general de tecnología]

---

## Ejemplo de output

**Video: AI agent completes a 2-hour coding task in 4 minutes**

**[0:00–0:03] HOOK:**
Say: "I gave an AI a 2-hour task. Watch what happened."
Screen: Time-lapse of terminal output scrolling rapidly — looks impressive, creates curiosity.

**[0:03–0:12] SETUP:**
Say: "I needed to add input validation to 4 API endpoints. Normally takes me 2 hours."
Screen: Show the 4 route files, zoomed out so viewer sees the scope.

**[0:12–0:28] THE MOMENT:**
Say: "I wrote a task brief for my AI agent, hit run, and went to make coffee."
Screen: Show the agent terminal — tool calls firing, files being read and edited, test runner executing.
Cut to: "npm test — all passing"

**[0:28–0:38] RESULT:**
Say: "4 minutes. All 4 endpoints validated. Tests written. And it caught an edge case I missed."
Screen: Split — before (no validation) vs after (zod schemas). Highlight the edge case the agent added.

**[0:38–0:45] CLOSE:**
Say: "The hard part? Writing the task brief. The better your instructions, the better the agent."
Screen: Show the 10-line task brief document.
Text overlay: "I'll show you how to write agent briefs that actually work →"
