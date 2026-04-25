# Coordinate Multi-Agent Task

**Category:** task-delegation
**When to use:** Decomposing a complex task that needs to run across multiple AI agents in parallel, and designing the coordination logic between them.

---

You are an AI orchestration engineer. I need to decompose the following task into a multi-agent execution plan where agents run in parallel where possible. Design the full coordination plan.

Your output must include:

**TASK DECOMPOSITION:**
Break the task into subtasks. For each subtask:
- Agent name and role
- Input: what it receives (from user, from another agent, from a tool)
- Output: what it produces (format, schema)
- Can it run in parallel with other agents? If so, which ones?

**DEPENDENCY GRAPH:**
Show which agents must complete before others can start. Use a simple format:
```
A → B (B depends on A's output)
A, C → D (D depends on both A and C)
```

**ORCHESTRATOR LOGIC:**
Write the pseudocode or actual code for the orchestrator that:
- Kicks off independent agents simultaneously
- Waits for dependencies before launching dependent agents
- Handles agent failure (retry, fallback, or halt)
- Assembles final output from all agent outputs

**STATE CONTRACT:**
Define the data structure passed between agents. Use TypeScript types or Python TypedDicts.

**Task to decompose:**
[describe the full task]

**Agent framework:** [e.g., Claude tool use, LangGraph, AutoGen, custom]
**Language:** [Python / TypeScript]

---

## Example output

**Task:** Research a company, analyze their tech stack, and write a personalized outreach email.

**Task decomposition:**
- `WebResearcher` — searches for company info. Input: company name. Output: `CompanyProfile`. Parallel: Yes (with `LinkedInScraper`).
- `LinkedInScraper` — finds key contacts. Input: company name. Output: `ContactList`. Parallel: Yes (with `WebResearcher`).
- `TechStackAnalyzer` — analyzes their engineering blog and job postings. Input: `CompanyProfile`. Output: `TechStack`. Parallel: No — depends on `WebResearcher`.
- `EmailWriter` — writes the outreach email. Input: `CompanyProfile + ContactList + TechStack`. Output: final email. Parallel: No — depends on all three.

**Dependency graph:**
```
WebResearcher, LinkedInScraper → TechStackAnalyzer
WebResearcher, LinkedInScraper, TechStackAnalyzer → EmailWriter
```

**Orchestrator (Python):**
```python
async def run_pipeline(company: str) -> str:
    profile, contacts = await asyncio.gather(
        web_researcher.run(company),
        linkedin_scraper.run(company),
    )
    tech_stack = await tech_stack_analyzer.run(profile)
    email = await email_writer.run(profile, contacts, tech_stack)
    return email
```
