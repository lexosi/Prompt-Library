# Internal Tool Kickoff

**Category:** project-kickoff
**When to use:** Scoping and starting an internal developer tooling project — where the users are engineers and the value is measured in time saved.

---

Write a kickoff document for an internal developer tool. These tools are often under-specified, leading to over-engineering or tools nobody uses. This document prevents both.

The document must cover:

**TOOL NAME & ONE-LINE PURPOSE:** What it does, in terms of what the user does less of or faster.

**THE PROBLEM IT SOLVES:** Describe the current pain without the tool. How long does the task take now? How often? Who does it?

**TARGET USERS:** Exactly who uses this — be specific (e.g., "backend engineers creating new microservices," not "the engineering team").

**CORE WORKFLOW:** The primary flow a user will take through the tool. 5–8 steps.

**SUCCESS METRIC:** How will we know in 30 days that this tool was worth building? One specific metric (e.g., "task X takes < 2 minutes instead of 20").

**MVP SCOPE:** The simplest version that solves the core problem. Ruthlessly cut everything non-essential.

**NON-GOALS:** What this tool intentionally does NOT do. Prevents scope creep from well-meaning colleagues.

**BUILD VS. BUY CHECK:** Did you verify no existing tool (open-source or paid) already does this? What did you check?

**MAINTENANCE COST:** Who owns this after it's built? What's the expected maintenance burden?

**Tool purpose:**
[describe what the tool should do]
**Current manual process:**
[describe what people do today without it]

---

## Example output

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
