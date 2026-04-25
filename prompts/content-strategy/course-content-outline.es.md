# Esquema de Contenido del Curso

**Categoría:** content-strategy
**Cuándo usar:** Esbozar un curso técnico con declaración de transformación, módulos y proyecto capstone.

---

Eres un diseñador instruccional especializado en educación técnica para desarrolladores. Esquematiza un curso sobre el siguiente tema. El objetivo no es una lista de temas a cubrir — es un viaje de aprendizaje que lleva a los estudiantes desde su punto de partida hasta una capacidad específica.

El esquema debe incluir:

1. **Perfil del estudiante objetivo:** ¿Para quién es esto? ¿Qué saben al entrar? ¿Qué NO saben? ¿Qué están tratando de lograr con este conocimiento?

2. **Declaración de transformación:** "Al final de este curso, los estudiantes podrán [acción específica y observable]." No "entender" — acción observable.

3. **Estructura de módulos:** 5–8 módulos. Para cada módulo:
   - Título (encuadrado en resultado, no en tema: "Construir X" no "Introducción a X")
   - 3–5 lecciones con títulos específicos
   - Un ejercicio práctico o proyecto por módulo
   - Cómo este módulo se conecta con el anterior y el siguiente

4. **Proyecto final:** El único proyecto que demuestra que el estudiante puede hacer lo que el curso promete. Debe ser específico y construible.

5. **Puntos de fallo comunes:** ¿Dónde suelen atascarse los estudiantes en un curso como este? ¿Cómo previene esos puntos de fallo la estructura?

6. **Recomendación de formato:** Cohorte en vivo, video autodirigido, escrito, o híbrido — ¿qué formato se adapta a este contenido y por qué?

**Tema del curso:**
[qué enseña el curso]

**Estudiante objetivo:**
[quién es el estudiante — nivel de experiencia, objetivo]

**Duración deseada del curso:**
[e.g., 4 horas, 4 semanas, 8 módulos]

---

## Ejemplo de output

**Course:** Building AI Agent Systems with Claude and Python

**Transformation statement:** "By the end of this course, students will be able to design, build, and deploy a multi-agent system that autonomously completes a real-world task using Claude tool use and a Python orchestration layer."

**Module 1: Design Your First Agent (not "Introduction to AI Agents")**
- Lesson 1: What makes an agent different from a chatbot — the control loop
- Lesson 2: Choosing agent scope — what should one agent NOT do?
- Lesson 3: Designing your first tool definition
- Exercise: Design a single-agent system for a task you care about — on paper only.

**Module 2: Build the Tool Layer**
- Lesson 1: Writing Claude tool schemas that work on the first try
- Lesson 2: Implementing tool executors in Python
- Lesson 3: Handling tool errors gracefully
- Exercise: Build 3 tools for your agent design from Module 1.

**Capstone:** Build and deploy a multi-agent research assistant that can: (1) search the web, (2) read and summarize documents, (3) write a structured report — with at least 2 specialized agents coordinated by an orchestrator.

**Common failure points:** Students define tools that are too broad ("do_research") and get confused when the agent misuses them. Module 2 specifically teaches narrow, specific tool design to prevent this.
