# Kickoff de Herramienta Interna

**Categoría:** project-kickoff
**Cuándo usar:** Delimitar un proyecto de herramienta para desarrolladores con fronteras de MVP y métricas de éxito.

---

Escribe un documento de kickoff para una herramienta interna de desarrolladores. Estas herramientas a menudo están sub-especificadas, llevando a sobre-ingeniería o herramientas que nadie usa. Este documento previene ambos.

El documento debe cubrir:

**NOMBRE Y PROPÓSITO EN UNA LÍNEA:** Qué hace, en términos de qué hace el usuario menos o más rápido.

**EL PROBLEMA QUE RESUELVE:** Describe el dolor actual sin la herramienta. ¿Cuánto tarda la tarea ahora? ¿Con qué frecuencia? ¿Quién la hace?

**USUARIOS OBJETIVO:** Exactamente quién usa esto — sé específico (e.g., "ingenieros backend creando nuevos microservicios," no "el equipo de ingeniería").

**FLUJO PRINCIPAL:** El flujo principal que un usuario tomará a través de la herramienta. 5–8 pasos.

**MÉTRICA DE ÉXITO:** ¿Cómo sabremos en 30 días que valió la pena construir esta herramienta? Una métrica específica (e.g., "la tarea X toma < 2 minutos en lugar de 20").

**ALCANCE MVP:** La versión más simple que resuelve el problema central. Corta sin piedad todo lo no esencial.

**NO-OBJETIVOS:** Lo que esta herramienta intencionalmente NO hace. Previene el scope creep de colegas bien intencionados.

**VERIFICACIÓN CONSTRUIR VS. COMPRAR:** ¿Verificaste que ninguna herramienta existente (open-source o de pago) ya hace esto? ¿Qué verificaste?

**COSTO DE MANTENIMIENTO:** ¿Quién posee esto después de construirse? ¿Cuál es la carga de mantenimiento esperada?

**Propósito de la herramienta:**
[describe qué debería hacer la herramienta]
**Proceso manual actual:**
[describe qué hacen las personas hoy sin ella]

---

## Ejemplo de output

**TOOL NAME:** `service-scaffold` — Generate a new Rust microservice skeleton in < 60 seconds.

**THE PROBLEM:** Creating a new microservice currently takes 45–90 minutes per engineer. They copy-paste from an existing service, manually update 12 config files, and invariably miss 2–3, leading to inconsistencies discovered in code review. This happens 2–3 times per sprint.

**TARGET USERS:** Backend engineers at the company creating new Rust microservices. Not DevOps — they have their own tooling.

**CORE WORKFLOW:**
1. Run `service-scaffold new <name>`
2. Answer 5 prompts: database (yes/no), auth (yes/no), gRPC (yes/no), HTTP (yes/no), initial port.
3. Tool generates directory, all config files, Dockerfile, CI workflow, and basic health endpoint.
4. Engineer runs `cargo build` — it compiles.
5. Engineer pushes to GitHub — CI passes on first run.

**SUCCESS METRIC:** New service setup time < 5 minutes, CI passes on first push 95% of the time.

**MVP SCOPE:** CLI tool, 5 prompts, generates: `src/`, `Cargo.toml`, `Dockerfile`, `.github/workflows/ci.yml`, `README.md`. Nothing else.

**NON-GOALS:** Deployment, infrastructure provisioning, database migration setup, Kubernetes manifests — these come from a separate DevOps process.
