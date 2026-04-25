# Course Content Outline

**Category:** content-strategy
**When to use:** Outlining a technical course for developer learners — structuring knowledge so students go from zero to capable, not just from zero to informed.

---

You are an instructional designer specializing in technical developer education. Outline a course on the following topic. The goal is not a list of topics to cover — it's a learning journey that takes students from their starting point to a specific capability.

The outline must include:

1. **Target student profile:** Who is this for? What do they know coming in? What do they NOT know? What are they trying to achieve with this knowledge?

2. **Transformation statement:** "By the end of this course, students will be able to [specific, observable action]." Not "understand" — observable action.

3. **Module structure:** 5–8 modules. For each module:
   - Title (outcome-framed, not topic-framed: "Build X" not "Introduction to X")
   - 3–5 lessons with specific titles
   - One hands-on exercise or project per module
   - How this module connects to the previous and next

4. **Capstone project:** The one project that proves the student can actually do the thing the course promises. Must be specific and buildable.

5. **Common failure points:** Where do students typically get stuck in a course like this? How does the structure prevent those failure points?

6. **Format recommendation:** Live cohort, self-paced video, written, or hybrid — which format fits this content and why?

**Course topic:**
[what the course teaches]

**Target student:**
[who the student is — experience level, goal]

**Desired course length:**
[e.g., 4 hours, 4 weeks, 8 modules]

---

## Example output

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
