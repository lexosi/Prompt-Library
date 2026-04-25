# Prompt Library Index

Every prompt in the library, organized by category. Each entry links directly to the prompt file.

---

## Debugging

| Prompt | Description |
|--------|-------------|
| [Diagnose Rust Error](prompts/debugging/diagnose-rust-error.md) · [ES](prompts/debugging/diagnose-rust-error.es.md) | Root-cause a Rust compiler error or runtime panic with a minimal fix |
| [Trace Python Async Bug](prompts/debugging/trace-python-async-bug.md) · [ES](prompts/debugging/trace-python-async-bug.es.md) | Identify deadlocks, race conditions, and event loop blocking in asyncio code |
| [TypeScript Type Error Analysis](prompts/debugging/typescript-type-error-analysis.md) · [ES](prompts/debugging/typescript-type-error-analysis.es.md) | Resolve TypeScript type mismatches and trace `any` leakage to its source |
| [AI Agent Loop Debug](prompts/debugging/ai-agent-loop-debug.md) · [ES](prompts/debugging/ai-agent-loop-debug.es.md) | Diagnose an AI agent stuck in a loop, calling wrong tools, or hallucinating state |

---

## Code Review

| Prompt | Description |
|--------|-------------|
| [Rust Safety Review](prompts/code-review/rust-safety-review.md) · [ES](prompts/code-review/rust-safety-review.es.md) | Review Rust code for unsafe blocks, panics, lifetime issues, and performance footguns |
| [Python AI Pipeline Review](prompts/code-review/python-ai-pipeline-review.md) · [ES](prompts/code-review/python-ai-pipeline-review.es.md) | Review Python ML/AI pipelines for data leakage, resource efficiency, and observability |
| [TypeScript API Review](prompts/code-review/typescript-api-review.md) · [ES](prompts/code-review/typescript-api-review.es.md) | Review TypeScript APIs for type safety, security, and N+1 query patterns |
| [Agent Tool Use Review](prompts/code-review/agent-tool-use-review.md) · [ES](prompts/code-review/agent-tool-use-review.es.md) | Review AI agent tool definitions and tool-calling logic for safety and clarity |

---

## Architecture Design

| Prompt | Description |
|--------|-------------|
| [Design AI Agent System](prompts/architecture-design/design-ai-agent-system.md) · [ES](prompts/architecture-design/design-ai-agent-system.es.md) | Design a multi-agent orchestration system with concrete roles, tools, and failure handling |
| [Microservices: Rust + Python](prompts/architecture-design/microservices-rust-python.md) · [ES](prompts/architecture-design/microservices-rust-python.es.md) | Plan a monolith-to-microservices split with language assignment rationale and migration sequence |
| [RAG Pipeline Architecture](prompts/architecture-design/rag-pipeline-architecture.md) · [ES](prompts/architecture-design/rag-pipeline-architecture.es.md) | Design a production RAG pipeline with specific embedding models, retrieval strategy, and evaluation |
| [Game Backend Architecture](prompts/architecture-design/game-backend-architecture.md) · [ES](prompts/architecture-design/game-backend-architecture.es.md) | Design backend infrastructure for a live-service game with scalability and anti-cheat in mind |

---

## Refactor

| Prompt | Description |
|--------|-------------|
| [Rust Idiomatic Refactor](prompts/refactor/rust-idiomatic-refactor.md) · [ES](prompts/refactor/rust-idiomatic-refactor.es.md) | Refactor Rust code to eliminate clones, use iterators, and implement standard traits |
| [Python Async Refactor](prompts/refactor/python-async-refactor.md) · [ES](prompts/refactor/python-async-refactor.es.md) | Migrate sync Python to genuine async/await with concurrent I/O operations |
| [TypeScript Clean Architecture](prompts/refactor/typescript-clean-architecture.md) · [ES](prompts/refactor/typescript-clean-architecture.es.md) | Separate business logic, infrastructure, and HTTP handling in a TypeScript codebase |
| [Monolith to Agents](prompts/refactor/monolith-to-agents.md) · [ES](prompts/refactor/monolith-to-agents.es.md) | Decompose a monolithic process into a coordinated multi-agent system |

---

## Task Delegation

| Prompt | Description |
|--------|-------------|
| [Delegate to AI Agent](prompts/task-delegation/delegate-to-ai-agent.md) · [ES](prompts/task-delegation/delegate-to-ai-agent.es.md) | Write a complete, autonomous task brief for an AI agent with constraints and success criteria |
| [Delegate to Junior Developer](prompts/task-delegation/delegate-to-junior-dev.md) · [ES](prompts/task-delegation/delegate-to-junior-dev.es.md) | Assign a scoped task to a junior developer with clear starting point and definition of done |
| [Delegate to Senior Specialist](prompts/task-delegation/delegate-to-senior-specialist.md) · [ES](prompts/task-delegation/delegate-to-senior-specialist.es.md) | Hand off a complex problem to an expert with full context and outcome focus |
| [Coordinate Multi-Agent Task](prompts/task-delegation/coordinate-multi-agent-task.md) · [ES](prompts/task-delegation/coordinate-multi-agent-task.es.md) | Decompose a task into parallel agents with a dependency graph and orchestration logic |

---

## Project Kickoff

| Prompt | Description |
|--------|-------------|
| [AI Product Kickoff](prompts/project-kickoff/ai-product-kickoff.md) · [ES](prompts/project-kickoff/ai-product-kickoff.es.md) | One-page kickoff document that aligns engineering, product, and stakeholders before code is written |
| [Game Feature Kickoff](prompts/project-kickoff/game-feature-kickoff.md) · [ES](prompts/project-kickoff/game-feature-kickoff.es.md) | Pre-production alignment doc for a Fortnite or Roblox feature with fun assumptions stated explicitly |
| [Client Project Kickoff](prompts/project-kickoff/client-project-kickoff.md) · [ES](prompts/project-kickoff/client-project-kickoff.es.md) | Contract-of-understanding document that prevents scope creep before billed work begins |
| [Internal Tool Kickoff](prompts/project-kickoff/internal-tool-kickoff.md) · [ES](prompts/project-kickoff/internal-tool-kickoff.es.md) | Scope a developer tool project with MVP boundaries and success metrics |

---

## Decision Making

| Prompt | Description |
|--------|-------------|
| [Technical Stack Decision](prompts/decision-making/technical-stack-decision.md) · [ES](prompts/decision-making/technical-stack-decision.es.md) | Get a concrete language/framework recommendation with the decisive factor and risk |
| [Build vs. Buy](prompts/decision-making/build-vs-buy.md) · [ES](prompts/decision-making/build-vs-buy.es.md) | Decide whether to build a capability or buy it, with hidden costs and failure scenarios |
| [Risk Assessment: AI Feature](prompts/decision-making/risk-assessment-ai-feature.md) · [ES](prompts/decision-making/risk-assessment-ai-feature.es.md) | Evaluate hallucination, misuse, privacy, and drift risk before shipping an AI feature |
| [Prioritization Framework](prompts/decision-making/prioritization-framework.md) · [ES](prompts/decision-making/prioritization-framework.es.md) | Rank a backlog with one-sentence reasoning per item and hidden dependencies surfaced |

---

## Client Communication

| Prompt | Description |
|--------|-------------|
| [Explain Technical Delay](prompts/client-communication/explain-technical-delay.md) · [ES](prompts/client-communication/explain-technical-delay.es.md) | Communicate a project delay clearly without blame or excessive apology |
| [Scope Change Response](prompts/client-communication/scope-change-response.md) · [ES](prompts/client-communication/scope-change-response.es.md) | Decline an out-of-scope request professionally while keeping the relationship intact |
| [Project Status Update](prompts/client-communication/project-status-update.md) · [ES](prompts/client-communication/project-status-update.es.md) | Sub-200-word weekly update that gives clients full picture without requiring a meeting |
| [Technical Proposal](prompts/client-communication/technical-proposal.md) · [ES](prompts/client-communication/technical-proposal.es.md) | Propose a technical approach credibly to both technical and non-technical readers |

---

## Pitch and Positioning

| Prompt | Description |
|--------|-------------|
| [AI Product Pitch](prompts/pitch-and-positioning/ai-product-pitch.md) · [ES](prompts/pitch-and-positioning/ai-product-pitch.es.md) | 90-second pitch for an AI product with hook, proof, and specific ask |
| [Game Studio Pitch](prompts/pitch-and-positioning/game-studio-pitch.md) · [ES](prompts/pitch-and-positioning/game-studio-pitch.es.md) | Pitch a Fortnite or Roblox experience to a publisher or platform partner |
| [Freelance Positioning](prompts/pitch-and-positioning/freelance-positioning.md) · [ES](prompts/pitch-and-positioning/freelance-positioning.es.md) | Three-version positioning statement (long, short, one-liner) for an AI engineering freelancer |
| [Executive Value Pitch](prompts/pitch-and-positioning/executive-value-pitch.md) · [ES](prompts/pitch-and-positioning/executive-value-pitch.es.md) | Translate AI engineering investment into ROI language for a non-technical exec |

---

## Outreach

| Prompt | Description |
|--------|-------------|
| [Cold Outreach: Technical Leader](prompts/outreach/cold-outreach-technical.md) · [ES](prompts/outreach/cold-outreach-technical.es.md) | Under-120-word cold message to a CTO or senior engineer that earns a reply |
| [Partnership Outreach](prompts/outreach/partnership-outreach.md) · [ES](prompts/outreach/partnership-outreach.es.md) | Mutual-value partnership proposal with specific collaboration idea |
| [Recruiter Response](prompts/outreach/recruiter-response.md) · [ES](prompts/outreach/recruiter-response.es.md) | Three versions: decline, explore, or accept a recruiter message — each under 100 words |
| [Community Contribution Intro](prompts/outreach/community-contribution.md) · [ES](prompts/outreach/community-contribution.es.md) | Introduce yourself or a contribution to a developer community as a genuine participant |

---

## Prompt Debugging

| Prompt | Description |
|--------|-------------|
| [Diagnose Vague Output](prompts/prompt-debugging/diagnose-vague-output.md) · [ES](prompts/prompt-debugging/diagnose-vague-output.es.md) | Identify why a prompt produces generic responses and rewrite it for specificity |
| [Fix Hallucinating Prompt](prompts/prompt-debugging/fix-hallucinating-prompt.md) · [ES](prompts/prompt-debugging/fix-hallucinating-prompt.es.md) | Root-cause hallucination triggers and restructure the prompt to ground the model |
| [Improve Prompt Specificity](prompts/prompt-debugging/improve-prompt-specificity.md) · [ES](prompts/prompt-debugging/improve-prompt-specificity.es.md) | Make an inconsistent prompt reliable by eliminating ambiguity and format variance |
| [Chain of Thought Debug](prompts/prompt-debugging/chain-of-thought-debug.md) · [ES](prompts/prompt-debugging/chain-of-thought-debug.es.md) | Find the exact step where multi-step reasoning goes wrong and fix the prompt |

---

## Context Preparation

| Prompt | Description |
|--------|-------------|
| [Prepare Agent Context](prompts/context-preparation/prepare-agent-context.md) · [ES](prompts/context-preparation/prepare-agent-context.es.md) | Assemble a complete context package (system prompt, tools, state) for an autonomous agent |
| [System Prompt Design](prompts/context-preparation/system-prompt-design.md) · [ES](prompts/context-preparation/system-prompt-design.es.md) | Write a production-ready system prompt with constraints, edge cases, and tone |
| [Few-Shot Examples](prompts/context-preparation/few-shot-examples.md) · [ES](prompts/context-preparation/few-shot-examples.es.md) | Design few-shot examples covering happy path, edge cases, and anti-patterns |
| [Context Window Optimization](prompts/context-preparation/context-window-optimization.md) · [ES](prompts/context-preparation/context-window-optimization.es.md) | Reduce context token footprint without losing task-critical information |

---

## Game Design

| Prompt | Description |
|--------|-------------|
| [Fortnite Mechanic Design](prompts/game-design/fortnite-mechanic-design.md) · [ES](prompts/game-design/fortnite-mechanic-design.es.md) | Design a Fortnite Creative mechanic with UEFN implementation approach and tuning parameters |
| [Roblox Experience Design](prompts/game-design/roblox-experience-design.md) · [ES](prompts/game-design/roblox-experience-design.es.md) | Design a Roblox experience with core loop, retention, and fair Robux monetization |
| [UEFN Island Concept](prompts/game-design/uefn-island-concept.md) · [ES](prompts/game-design/uefn-island-concept.es.md) | Develop a full UEFN island concept from a one-line idea to production-ready GDD |
| [Game Economy Design](prompts/game-design/game-economy-design.md) · [ES](prompts/game-design/game-economy-design.es.md) | Design currency systems, earn/spend loops, and premium value for Fortnite or Roblox |

---

## UEFN Scripting

| Prompt | Description |
|--------|-------------|
| [Verse Script Template](prompts/uefn-scripting/verse-script-template.md) · [ES](prompts/uefn-scripting/verse-script-template.es.md) | Generate a well-structured Verse script with correct effect qualifiers and option handling |
| [Device Interaction Script](prompts/uefn-scripting/device-interaction-script.md) · [ES](prompts/uefn-scripting/device-interaction-script.es.md) | Coordinate multiple UEFN devices with correct event subscription and state management |
| [Player Mechanics in Verse](prompts/uefn-scripting/player-mechanics-verse.md) · [ES](prompts/uefn-scripting/player-mechanics-verse.es.md) | Implement custom player movement or abilities using Verse's player character API |
| [Debug Verse Error](prompts/uefn-scripting/debug-verse-error.md) · [ES](prompts/uefn-scripting/debug-verse-error.es.md) | Translate cryptic Verse compiler errors into plain language with a correct fix |

---

## Content Strategy

| Prompt | Description |
|--------|-------------|
| [AI Thought Leadership](prompts/content-strategy/ai-thought-leadership.md) · [ES](prompts/content-strategy/ai-thought-leadership.es.md) | Write a 600–900 word thought leadership article with a specific, debatable claim |
| [Technical Blog Strategy](prompts/content-strategy/technical-blog-strategy.md) · [ES](prompts/content-strategy/technical-blog-strategy.es.md) | Plan a 12-post editorial calendar with content pillars and distribution strategy |
| [Course Content Outline](prompts/content-strategy/course-content-outline.md) · [ES](prompts/content-strategy/course-content-outline.es.md) | Outline a technical course with transformation statement, modules, and capstone project |
| [Developer Documentation](prompts/content-strategy/developer-documentation.md) · [ES](prompts/content-strategy/developer-documentation.es.md) | Write scannable developer docs with quick start, reference, and task-oriented guides |

---

## Social Media

| Prompt | Description |
|--------|-------------|
| [LinkedIn Technical Post](prompts/social-media/linkedin-technical-post.md) · [ES](prompts/social-media/linkedin-technical-post.es.md) | 150–250 word LinkedIn post with a specific opening line and concrete insight |
| [Twitter/X Thread on AI](prompts/social-media/twitter-thread-ai.md) · [ES](prompts/social-media/twitter-thread-ai.es.md) | 7–10 tweet thread with a counterintuitive opening claim and a retweetable tweet 8 |
| [TikTok Dev Content Script](prompts/social-media/tiktok-dev-content.md) · [ES](prompts/social-media/tiktok-dev-content.es.md) | 30–45 second TikTok script with a 3-second hook and scene-by-scene breakdown |
| [YouTube Video Description](prompts/social-media/youtube-description.md) · [ES](prompts/social-media/youtube-description.es.md) | YouTube description with search-optimized first 2 sentences, timestamps, and resources |

---

*64 prompts across 16 categories. Each prompt has an English `.md` file and a Spanish `.es.md` file.*
