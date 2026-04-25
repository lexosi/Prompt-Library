# Coordinar Tarea Multi-Agente

**Categoría:** task-delegation
**Cuándo usar:** Descomponer una tarea en agentes paralelos con grafo de dependencias y lógica de orquestación.

---

Eres un ingeniero de orquestación de IA. Necesito descomponer la siguiente tarea en un plan de ejecución multi-agente donde los agentes se ejecuten en paralelo donde sea posible. Diseña el plan completo de coordinación.

Tu salida debe incluir:

**DESCOMPOSICIÓN DE TAREA:**
Divide la tarea en subtareas. Para cada subtarea:
- Nombre del agente y rol
- Entrada: qué recibe (del usuario, de otro agente, de una herramienta)
- Salida: qué produce (formato, schema)
- ¿Puede ejecutarse en paralelo con otros agentes? Si es así, ¿con cuáles?

**GRAFO DE DEPENDENCIAS:**
Muestra qué agentes deben completarse antes de que otros puedan comenzar. Usa un formato simple:
```
A → B (B depende de la salida de A)
A, C → D (D depende de A y C)
```

**LÓGICA DEL ORQUESTADOR:**
Escribe el pseudocódigo o código real para el orquestador que:
- Inicia los agentes independientes simultáneamente
- Espera dependencias antes de lanzar agentes dependientes
- Maneja fallos de agentes (reintentar, fallback o detener)
- Ensambla la salida final de todas las salidas de agentes

**CONTRATO DE ESTADO:**
Define la estructura de datos pasada entre agentes. Usa tipos TypeScript o TypedDicts de Python.

**Tarea a descomponer:**
[describe la tarea completa]

**Framework de agentes:** [e.g., Claude tool use, LangGraph, AutoGen, personalizado]
**Lenguaje:** [Python / TypeScript]

---

## Ejemplo de output

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
