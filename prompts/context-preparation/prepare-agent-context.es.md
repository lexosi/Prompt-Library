# Preparar Contexto del Agente

**Categoría:** context-preparation
**Cuándo usar:** Ensamblar un paquete de contexto completo (system prompt, herramientas, estado) para un agente autónomo.

---

Eres un ingeniero de sistemas de IA. Ayúdame a ensamblar un paquete de contexto completo para un agente de IA autónomo. Un paquete de contexto bien preparado determina si el agente puede ejecutar su tarea de forma autónoma o fallará y requerirá intervención humana.

Para el agente descrito a continuación, produce:

1. **System prompt (completo, listo para usar):** Definición de rol, capacidades, restricciones, formato de salida y reglas de escalado — todo lo que el agente necesita saber sobre su contexto operativo.

2. **Revisión de definición de herramientas:** Para las herramientas listadas, marca cualquier definición que sea ambigua, le falten campos requeridos, o pueda causar que el agente las use incorrectamente.

3. **Inicialización de memoria/estado:** ¿Qué debería estar en el estado/memoria inicial del agente para que pueda comenzar la tarea sin pasos de recopilación de contexto?

4. **Presupuesto de ventana de contexto:** Dado el system prompt, las herramientas y el estado inicial, estima el presupuesto de tokens restante para la tarea real. Señala si es ajustado.

5. **Manejo de estado de fallo:** Agrega instrucciones explícitas para los 3 estados de fallo más probables que encontrará este agente.

**Descripción del agente:**
[qué hace el agente, quién lo usa, qué tarea ejecuta]

**Herramientas disponibles:**
```json
[pega definiciones de herramientas]
```

**Estado/memoria inicial:**
[qué sabe el agente al inicio de cada ejecución]

**Modelo:**
[e.g., claude-opus-4-7, gpt-4o]

---

## Ejemplo de output

**System prompt (ready to use):**
```
You are a code review agent for the Acme engineering team. Your job is to review pull requests for security vulnerabilities, type safety issues, and test coverage gaps.

CAPABILITIES: You can read files, search code, and post comments to GitHub PRs.

CONSTRAINTS:
- Review ONLY the changed files in the PR diff. Do not review unchanged files.
- Do not post more than 5 inline comments per PR. Combine related issues.
- Do not suggest architectural changes — scope your feedback to the changed code.

OUTPUT FORMAT: For each issue found:
- File and line number
- Issue type (Security/Type Safety/Test Coverage)
- Severity: Critical / High / Medium / Low
- One-sentence description
- Suggested fix (code snippet if < 5 lines)

ESCALATION: If you find a Critical security issue, post a top-level PR comment flagging it for immediate human review. Do not approve the PR.

FAILURE HANDLING:
- If you cannot read a file: skip it and note the skip in your summary comment.
- If the PR has more than 50 changed files: review only files matching *.ts, *.rs, *.py, and note the scope limit.
- If GitHub API returns an error: stop and output the error with the tool name and error code.
```

**Token budget estimate:** System prompt ≈ 400 tokens. Tool definitions ≈ 300 tokens. Average PR diff ≈ 2,000 tokens. Remaining for reasoning: ~95,000 tokens (Claude Opus 4). Comfortable budget.
