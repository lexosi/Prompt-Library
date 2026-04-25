# Diseñar Sistema de Agentes IA

**Categoría:** architecture-design
**Cuándo usar:** Diseñar un sistema de orquestación multi-agente con roles concretos, herramientas y manejo de fallos.

---

Eres un arquitecto principal de sistemas de IA. Necesito diseñar un sistema multi-agente para la siguiente tarea. Produce una arquitectura concreta — no una lista de opciones, sino un diseño específico recomendado con razonamiento claro.

Tu salida debe incluir:
1. **Roles de agentes:** Lista cada agente, su única responsabilidad, sus entradas y sus salidas.
2. **Modelo de orquestación:** ¿Cómo coordinan los agentes — pipeline, fan-out paralelo, jerárquico, event-driven? Justifica por qué este modelo es el adecuado.
3. **Superficie de herramientas:** ¿Qué herramientas necesita cada agente? Marca las herramientas compartidas vs. exclusivas.
4. **Gestión de estado:** ¿Dónde vive el estado? ¿Cómo se pasa entre agentes? ¿Qué ocurre si un agente falla a mitad de tarea?
5. **Modos de fallo:** Las dos formas más probables en que este sistema fallará en producción y cómo detectarlas.
6. **Punto de partida de implementación:** Los primeros tres componentes a construir, en orden.

**Tarea que el sistema debe realizar:**
[describe la tarea de extremo a extremo que el sistema de agentes debe manejar]

**Restricciones:**
- Modelo: [e.g., Claude 3.5 Sonnet, GPT-4o]
- Presupuesto de latencia: [e.g., < 10 segundos end-to-end]
- Equipo: [e.g., 2 ingenieros, 3 semanas]
- Infraestructura existente: [e.g., backend Python, PostgreSQL, Redis]

---

## Ejemplo de output

**System:** Automated code review pipeline for pull requests.

**Agent roles:**
- `DiffParser` — Receives raw git diff, outputs structured list of changed functions with context. Tools: none (pure LLM reasoning).
- `SecurityReviewer` — Receives changed functions, outputs security findings. Tools: `search_vulnerability_db`.
- `StyleReviewer` — Receives changed functions, checks against project conventions. Tools: `read_style_guide`.
- `Synthesizer` — Receives findings from both reviewers, outputs a single formatted review comment. Tools: `post_github_comment`.

**Orchestration:** Parallel fan-out. DiffParser runs first, then SecurityReviewer and StyleReviewer run in parallel, then Synthesizer waits for both to complete before posting.

**State:** Git diff passed as input. Findings stored in-memory as structured JSON. No persistent state needed — each PR review is stateless.

**First three components to build:** (1) DiffParser agent + tests, (2) GitHub webhook handler, (3) Synthesizer + GitHub comment posting.
