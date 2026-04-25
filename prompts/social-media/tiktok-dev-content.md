# TikTok Dev Content Script

**Category:** social-media
**When to use:** Scripting a short-form TikTok video about developer work, game development, or AI engineering — designed for a general tech-curious audience.

---

Write a TikTok video script for a developer content video. TikTok rewards immediacy and visual proof — the best dev content on TikTok shows real code, real results, and a human presence behind it.

Rules:
- **Hook (0–3 seconds):** Must answer "why should I watch this?" before the viewer can swipe away. Start with the result or the surprising thing, not the setup.
- **Show, don't explain:** The code or screen should be visible. If you describe something a viewer could see, show it instead.
- **Pacing:** Cut every 2–4 seconds. No long explanations. If a concept takes 15 seconds to explain verbally, show it in 5 seconds visually.
- **Jargon ceiling:** Explain at the level of a CS student or curious non-developer. Not total beginner, not deep expert.
- **Duration:** 30–45 seconds. Hard cap at 55 seconds.
- **Closing hook:** End with a question, a teaser for the next video, or a challenge to the viewer.

Format the script as:
- **[0:00–0:03] HOOK:** [what you say + what's on screen]
- **[0:03–0:XX] BODY:** [scene by scene]
- **[0:XX–end] CLOSE:** [call to action]

**Video topic:**
[what you're showing — e.g., "building a Verse script in UEFN," "debugging a Rust borrow checker error," "my AI agent completing a task"]

**The "wow moment":** [the single most visually impressive or surprising thing in the video]

**Target viewer:** [e.g., dev students, gaming enthusiasts, general tech audience]

---

## Example output

**Video: AI agent completes a 2-hour coding task in 4 minutes**

**[0:00–0:03] HOOK:**
Say: "I gave an AI a 2-hour task. Watch what happened."
Screen: Time-lapse of terminal output scrolling rapidly — looks impressive, creates curiosity.

**[0:03–0:12] SETUP:**
Say: "I needed to add input validation to 4 API endpoints. Normally takes me 2 hours."
Screen: Show the 4 route files, zoomed out so viewer sees the scope.

**[0:12–0:28] THE MOMENT:**
Say: "I wrote a task brief for my AI agent, hit run, and went to make coffee."
Screen: Show the agent terminal — tool calls firing, files being read and edited, test runner executing.
Cut to: "npm test — all passing"

**[0:28–0:38] RESULT:**
Say: "4 minutes. All 4 endpoints validated. Tests written. And it caught an edge case I missed."
Screen: Split — before (no validation) vs after (zod schemas). Highlight the edge case the agent added.

**[0:38–0:45] CLOSE:**
Say: "The hard part? Writing the task brief. The better your instructions, the better the agent."
Screen: Show the 10-line task brief document.
Text overlay: "I'll show you how to write agent briefs that actually work →"
