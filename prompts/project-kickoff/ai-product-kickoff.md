# AI Product Kickoff

**Category:** project-kickoff
**When to use:** Starting a new AI-powered product with an engineering team and needing a kickoff document that creates alignment before a single line of code is written.

---

Write a kickoff document for an AI-powered product. The document should fit on one page and create alignment across engineering, product, and any stakeholders before work begins.

The document must cover:

**PRODUCT SUMMARY:** What it does, for whom, and the specific problem it solves — in 3 sentences max.

**SUCCESS METRICS:** How will we know in 30 days, 90 days, and 6 months that this is working? Name specific, measurable metrics.

**TECHNICAL APPROACH:** The core AI mechanism (RAG, agent, fine-tune, classifier, etc.), the model(s), and the infrastructure. Not a full architecture — the key decisions.

**IN SCOPE (V1):** A bulleted list of exactly what will be built. Short phrases, not paragraphs.

**OUT OF SCOPE (V1):** Explicitly what will NOT be built now. This section prevents the most expensive conversations.

**RISKS & OPEN QUESTIONS:**
- Technical risks: [list the 2-3 things most likely to cause delays or rework]
- Open questions: [things that need decisions before the team can proceed]

**TEAM & OWNERSHIP:**
- Who owns the product decisions?
- Who owns the technical decisions?
- Who is executing (engineers, agents)?

**TIMELINE:** Key milestones with dates. Be realistic — add 30%.

**Product/project name:**
[name]
**What it does:**
[description]
**Team:**
[who's involved]

---

## Example output

**PRODUCT SUMMARY:** `CodeLens` is an AI code review assistant that automatically reviews PRs for security issues, type safety violations, and architectural drift. It targets mid-sized engineering teams (10–50 engineers) who can't afford dedicated security reviewers but are shipping production code weekly.

**SUCCESS METRICS:**
- 30 days: 3 beta teams using it on real PRs, NPS > 7.
- 90 days: Average 2 critical issues caught per week per team that would have reached production.
- 6 months: 20% reduction in post-merge security incidents in beta teams.

**TECHNICAL APPROACH:** Claude as the reasoning model. Static AST analysis (tree-sitter) runs deterministically first; findings feed into Claude with the diff as context. GitHub Actions integration. No fine-tuning in V1.

**IN SCOPE (V1):** GitHub PR webhook, security finding detection, TypeScript + Python support, GitHub comment posting, severity scoring.

**OUT OF SCOPE (V1):** GitLab/Bitbucket, auto-fix suggestions, custom rule configuration, fine-tuning, dashboard UI.
