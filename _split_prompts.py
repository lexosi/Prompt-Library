#!/usr/bin/env python3
"""Split bilingual prompt files into English .md and Spanish .es.md files."""
import os
import re

BASE_DIR = r"F:\proyectosprog\Prompt Library"
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
INDEX_PATH = os.path.join(BASE_DIR, "index.md")

# (Spanish title, Spanish "when to use")
TRANSLATIONS = {
    # debugging
    "diagnose-rust-error": (
        "Diagnosticar Error de Rust",
        "Tienes un error del compilador de Rust, una violación del borrow checker o un panic en runtime que no puedes explicar de inmediato.",
    ),
    "trace-python-async-bug": (
        "Rastrear Bug Async en Python",
        "Identificar deadlocks, condiciones de carrera y bloqueos del event loop en código asyncio.",
    ),
    "typescript-type-error-analysis": (
        "Análisis de Error de Tipo en TypeScript",
        "Resolver discrepancias de tipos en TypeScript y rastrear fugas de `any` hasta su origen.",
    ),
    "ai-agent-loop-debug": (
        "Depurar Bucle de Agente IA",
        "Diagnosticar un agente IA atascado en un bucle, que llama herramientas incorrectas o alucina estado.",
    ),
    # code-review
    "rust-safety-review": (
        "Revisión de Seguridad en Rust",
        "Revisar código Rust antes de mergear a main, especialmente código con `unsafe`, FFI o anotaciones de lifetime complejas.",
    ),
    "python-ai-pipeline-review": (
        "Revisión de Pipeline IA en Python",
        "Revisar pipelines de ML/IA en Python para fugas de datos, eficiencia de recursos y observabilidad.",
    ),
    "typescript-api-review": (
        "Revisión de API en TypeScript",
        "Revisar APIs de TypeScript para type safety, seguridad y patrones de consulta N+1.",
    ),
    "agent-tool-use-review": (
        "Revisión de Uso de Herramientas del Agente",
        "Revisar definiciones de herramientas de agentes IA y lógica de llamadas para seguridad y claridad.",
    ),
    # architecture-design
    "design-ai-agent-system": (
        "Diseñar Sistema de Agentes IA",
        "Diseñar un sistema de orquestación multi-agente con roles concretos, herramientas y manejo de fallos.",
    ),
    "microservices-rust-python": (
        "Microservicios: Rust + Python",
        "Planificar la separación de un monolito en microservicios con justificación de asignación de lenguajes y secuencia de migración.",
    ),
    "rag-pipeline-architecture": (
        "Arquitectura de Pipeline RAG",
        "Diseñar un pipeline RAG en producción con modelos de embedding específicos, estrategia de recuperación y evaluación.",
    ),
    "game-backend-architecture": (
        "Arquitectura de Backend para Juegos",
        "Diseñar infraestructura backend para un juego live-service con escalabilidad y anti-cheat en mente.",
    ),
    # refactor
    "rust-idiomatic-refactor": (
        "Refactor Idiomático de Rust",
        "Refactorizar código Rust para eliminar clones, usar iteradores e implementar traits estándar.",
    ),
    "python-async-refactor": (
        "Refactor Async de Python",
        "Migrar Python síncrono a async/await genuino con operaciones de I/O concurrentes.",
    ),
    "typescript-clean-architecture": (
        "Arquitectura Limpia en TypeScript",
        "Separar lógica de negocio, infraestructura y manejo HTTP en una base de código TypeScript.",
    ),
    "monolith-to-agents": (
        "Monolito a Agentes",
        "Descomponer un proceso monolítico en un sistema multi-agente coordinado.",
    ),
    # task-delegation
    "delegate-to-ai-agent": (
        "Delegar a Agente IA",
        "Escribir un brief de tarea completo y autónomo para un agente IA con restricciones y criterios de éxito.",
    ),
    "delegate-to-junior-dev": (
        "Delegar a Desarrollador Junior",
        "Asignar una tarea delimitada a un desarrollador junior con punto de inicio claro y definición de terminado.",
    ),
    "delegate-to-senior-specialist": (
        "Delegar a Especialista Senior",
        "Transferir un problema complejo a un experto con contexto completo y enfoque en resultado.",
    ),
    "coordinate-multi-agent-task": (
        "Coordinar Tarea Multi-Agente",
        "Descomponer una tarea en agentes paralelos con grafo de dependencias y lógica de orquestación.",
    ),
    # project-kickoff
    "ai-product-kickoff": (
        "Kickoff de Producto IA",
        "Documento de kickoff de una página que alinea ingeniería, producto y stakeholders antes de escribir código.",
    ),
    "game-feature-kickoff": (
        "Kickoff de Feature de Juego",
        "Documento de alineación pre-producción para una feature de Fortnite o Roblox con suposiciones de diversión declaradas explícitamente.",
    ),
    "client-project-kickoff": (
        "Kickoff de Proyecto con Cliente",
        "Documento de contrato-de-entendimiento que previene scope creep antes de que comience el trabajo facturado.",
    ),
    "internal-tool-kickoff": (
        "Kickoff de Herramienta Interna",
        "Delimitar un proyecto de herramienta para desarrolladores con fronteras de MVP y métricas de éxito.",
    ),
    # decision-making
    "technical-stack-decision": (
        "Decisión de Stack Técnico",
        "Obtener una recomendación concreta de lenguaje/framework con el factor decisivo y el riesgo.",
    ),
    "build-vs-buy": (
        "Construir vs. Comprar",
        "Decidir si construir una capacidad o comprarla, con costos ocultos y escenarios de fallo.",
    ),
    "risk-assessment-ai-feature": (
        "Evaluación de Riesgo: Feature IA",
        "Evaluar riesgo de alucinación, mal uso, privacidad y deriva antes de lanzar una feature de IA.",
    ),
    "prioritization-framework": (
        "Framework de Priorización",
        "Clasificar un backlog con razonamiento de una oración por ítem y dependencias ocultas expuestas.",
    ),
    # client-communication
    "explain-technical-delay": (
        "Explicar Retraso Técnico",
        "Comunicar un retraso en el proyecto claramente sin culpas ni exceso de disculpas.",
    ),
    "scope-change-response": (
        "Respuesta a Cambio de Alcance",
        "Rechazar una solicitud fuera del alcance de forma profesional manteniendo la relación intacta.",
    ),
    "project-status-update": (
        "Actualización de Estado del Proyecto",
        "Actualización semanal de menos de 200 palabras que da al cliente una imagen completa sin requerir una reunión.",
    ),
    "technical-proposal": (
        "Propuesta Técnica",
        "Proponer un enfoque técnico de manera creíble tanto para lectores técnicos como no técnicos.",
    ),
    # pitch-and-positioning
    "ai-product-pitch": (
        "Pitch de Producto IA",
        "Pitch de 90 segundos para un producto IA con gancho, prueba y solicitud específica.",
    ),
    "game-studio-pitch": (
        "Pitch de Estudio de Juegos",
        "Presentar una experiencia de Fortnite o Roblox a un publisher o socio de plataforma.",
    ),
    "freelance-positioning": (
        "Posicionamiento Freelance",
        "Declaración de posicionamiento en tres versiones (larga, corta, una línea) para un freelancer de ingeniería IA.",
    ),
    "executive-value-pitch": (
        "Pitch de Valor para Ejecutivos",
        "Traducir la inversión en ingeniería IA a lenguaje de ROI para un ejecutivo no técnico.",
    ),
    # outreach
    "cold-outreach-technical": (
        "Outreach Frío: Líder Técnico",
        "Mensaje frío de menos de 120 palabras a un CTO o ingeniero senior que logra una respuesta.",
    ),
    "partnership-outreach": (
        "Outreach de Asociación",
        "Propuesta de asociación de valor mutuo con idea de colaboración específica.",
    ),
    "recruiter-response": (
        "Respuesta a Reclutador",
        "Tres versiones: rechazar, explorar o aceptar un mensaje de reclutador, cada uno de menos de 100 palabras.",
    ),
    "community-contribution": (
        "Introducción a Contribución Comunitaria",
        "Presentarte a ti mismo o una contribución a una comunidad de desarrolladores como participante genuino.",
    ),
    # prompt-debugging
    "diagnose-vague-output": (
        "Diagnosticar Output Vago",
        "Identificar por qué un prompt produce respuestas genéricas y reescribirlo para mayor especificidad.",
    ),
    "fix-hallucinating-prompt": (
        "Corregir Prompt que Alucina",
        "Identificar la causa raíz de los desencadenantes de alucinación y reestructurar el prompt para anclar el modelo.",
    ),
    "improve-prompt-specificity": (
        "Mejorar Especificidad del Prompt",
        "Hacer un prompt inconsistente confiable eliminando ambigüedad y varianza de formato.",
    ),
    "chain-of-thought-debug": (
        "Depurar Cadena de Pensamiento",
        "Encontrar el paso exacto donde el razonamiento multi-paso falla y corregir el prompt.",
    ),
    # context-preparation
    "prepare-agent-context": (
        "Preparar Contexto del Agente",
        "Ensamblar un paquete de contexto completo (system prompt, herramientas, estado) para un agente autónomo.",
    ),
    "system-prompt-design": (
        "Diseño de System Prompt",
        "Escribir un system prompt listo para producción con restricciones, casos límite y tono.",
    ),
    "few-shot-examples": (
        "Ejemplos Few-Shot",
        "Diseñar ejemplos few-shot que cubran el camino feliz, casos límite y anti-patrones.",
    ),
    "context-window-optimization": (
        "Optimización de Ventana de Contexto",
        "Reducir el footprint de tokens de contexto sin perder información crítica para la tarea.",
    ),
    # game-design
    "fortnite-mechanic-design": (
        "Diseño de Mecánica para Fortnite",
        "Diseñar una mecánica de Fortnite Creative con enfoque de implementación UEFN y parámetros de ajuste.",
    ),
    "roblox-experience-design": (
        "Diseño de Experiencia para Roblox",
        "Diseñar una experiencia de Roblox con loop central, retención y monetización justa con Robux.",
    ),
    "uefn-island-concept": (
        "Concepto de Isla UEFN",
        "Desarrollar un concepto completo de isla UEFN desde una idea de una línea hasta un GDD listo para producción.",
    ),
    "game-economy-design": (
        "Diseño de Economía de Juego",
        "Diseñar sistemas de moneda, loops de ganancia/gasto y valor premium para Fortnite o Roblox.",
    ),
    # uefn-scripting
    "verse-script-template": (
        "Plantilla de Script en Verse",
        "Generar un script Verse bien estructurado con calificadores de efecto correctos y manejo de opciones.",
    ),
    "device-interaction-script": (
        "Script de Interacción de Dispositivos",
        "Coordinar múltiples dispositivos UEFN con suscripción a eventos correcta y gestión de estado.",
    ),
    "player-mechanics-verse": (
        "Mecánicas de Jugador en Verse",
        "Implementar movimiento personalizado del jugador o habilidades usando la API de character de Verse.",
    ),
    "debug-verse-error": (
        "Depurar Error de Verse",
        "Traducir errores crípticos del compilador de Verse a lenguaje claro con una corrección correcta.",
    ),
    # content-strategy
    "ai-thought-leadership": (
        "Liderazgo de Pensamiento en IA",
        "Escribir un artículo de liderazgo de pensamiento de 600-900 palabras con una afirmación específica y debatible.",
    ),
    "technical-blog-strategy": (
        "Estrategia de Blog Técnico",
        "Planificar un calendario editorial de 12 posts con pilares de contenido y estrategia de distribución.",
    ),
    "course-content-outline": (
        "Esquema de Contenido del Curso",
        "Esbozar un curso técnico con declaración de transformación, módulos y proyecto capstone.",
    ),
    "developer-documentation": (
        "Documentación para Desarrolladores",
        "Escribir documentación para desarrolladores escaneable con inicio rápido, referencia y guías orientadas a tareas.",
    ),
    # social-media
    "linkedin-technical-post": (
        "Post Técnico en LinkedIn",
        "Post de LinkedIn de 150-250 palabras con una primera línea específica e insight concreto.",
    ),
    "twitter-thread-ai": (
        "Hilo de Twitter/X sobre IA",
        "Hilo de 7-10 tweets con una afirmación de apertura contraintuitiva y un tweet 8 retweeteable.",
    ),
    "tiktok-dev-content": (
        "Script de Contenido Dev para TikTok",
        "Script de TikTok de 30-45 segundos con un gancho de 3 segundos y desglose escena por escena.",
    ),
    "youtube-description": (
        "Descripción de Video de YouTube",
        "Descripción de YouTube con primeras 2 oraciones optimizadas para búsqueda, timestamps y recursos.",
    ),
}


def process_file(filepath, slug):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    # Normalize line endings
    content = raw.replace("\r\n", "\n")

    # Split on section separators (blank-line + --- + blank-line)
    parts = re.split(r"\n\n---\n\n", content)

    if len(parts) != 4:
        print(f"  ERROR {slug}: expected 4 parts, got {len(parts)}")
        return False

    header_raw, english_raw, spanish_raw, example_raw = parts

    # --- Parse header ---
    header_lines = header_raw.strip().split("\n")
    title_en = header_lines[0].lstrip("# ").strip()
    category = ""
    when_to_use_en = ""
    for line in header_lines:
        if line.startswith("**Category:**"):
            category = line.replace("**Category:**", "").strip()
        elif line.startswith("**When to use:**"):
            when_to_use_en = line.replace("**When to use:**", "").strip()

    # --- Strip section headers ---
    def strip_section_header(raw):
        lines = raw.strip().split("\n")
        if lines and lines[0].startswith("## "):
            rest = "\n".join(lines[1:]).lstrip("\n")
            return rest
        return raw.strip()

    english_content = strip_section_header(english_raw)
    spanish_content = strip_section_header(spanish_raw)
    example_content = strip_section_header(example_raw)

    # --- Get translations ---
    if slug not in TRANSLATIONS:
        print(f"  ERROR {slug}: no translation entry")
        return False
    title_es, when_to_use_es = TRANSLATIONS[slug]

    # --- Build English-only .md ---
    en_md = (
        f"# {title_en}\n\n"
        f"**Category:** {category}\n"
        f"**When to use:** {when_to_use_en}\n\n"
        f"---\n\n"
        f"{english_content}\n\n"
        f"---\n\n"
        f"## Example output\n\n"
        f"{example_content}\n"
    )

    # --- Build Spanish .es.md ---
    es_md = (
        f"# {title_es}\n\n"
        f"**Categoría:** {category}\n"
        f"**Cuándo usar:** {when_to_use_es}\n\n"
        f"---\n\n"
        f"{spanish_content}\n\n"
        f"---\n\n"
        f"## Ejemplo de output\n\n"
        f"{example_content}\n"
    )

    # Write files
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(en_md)

    es_path = filepath[:-3] + ".es.md"
    with open(es_path, "w", encoding="utf-8") as f:
        f.write(es_md)

    return True


def update_index(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update footer note
    content = content.replace(
        "*64 prompts across 16 categories. All prompts available in English and Spanish.*",
        "*64 prompts across 16 categories. Each prompt has an English `.md` file and a Spanish `.es.md` file.*",
    )

    # Replace each table row: add ES link
    # Pattern: | [Title](prompts/cat/file.md) | description |
    def add_es_link(m):
        title = m.group(1)
        path = m.group(2)
        desc = m.group(3)
        es_path = path.replace(".md", ".es.md")
        return f"| [{title}]({path}) · [ES]({es_path}) | {desc} |"

    content = re.sub(
        r"\| \[([^\]]+)\]\((prompts/[^)]+\.md)\) \| ([^|]+) \|",
        add_es_link,
        content,
    )

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)


# ── Main ──────────────────────────────────────────────────────────────────────
errors = []
count = 0

for cat_entry in sorted(os.scandir(PROMPTS_DIR), key=lambda e: e.name):
    if not cat_entry.is_dir():
        continue
    for file_entry in sorted(os.scandir(cat_entry.path), key=lambda e: e.name):
        name = file_entry.name
        if name == "README.md" or not name.endswith(".md") or name.endswith(".es.md"):
            continue
        slug = name[:-3]
        ok = process_file(file_entry.path, slug)
        if ok:
            count += 1
            print(f"  OK  {cat_entry.name}/{slug}")
        else:
            errors.append(f"{cat_entry.name}/{slug}")

print(f"\nProcessed: {count} files")

if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors:
        print(f"  {e}")
else:
    print("No errors.")
    print("Updating index.md …")
    update_index(INDEX_PATH)
    print("index.md updated.")
