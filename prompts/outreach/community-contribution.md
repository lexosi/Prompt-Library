# Community Contribution Intro

**Category:** outreach
**When to use:** Introducing yourself or a contribution (PR, tool, article) to a developer community — Discord, GitHub, Slack, or a forum.

---

Write an introduction message for a developer community. The goal is to be remembered as a genuine contributor, not a self-promoter. The message must:

- Say who you are in one concrete sentence — what you build, not your job title
- Explain specifically why you're in this community — what you're learning, building, or contributing
- Reference something specific about the community — a recent discussion, a project, or a decision you found interesting
- If sharing a contribution (PR, tool, article): lead with the problem it solves, not the thing itself
- End with a genuine question or invitation for feedback — show you're here to participate, not just announce

Under 150 words.

**Context:**
- Community: [name and focus — e.g., "Rust Discord, #async channel"]
- Why you're joining: [specific reason]
- What you're contributing (if anything): [description]
- What you're genuinely curious about in this community: [specific technical question or topic]

---

## Example output

Hey everyone — I build AI agent systems in Rust and Python, and I've been lurking in the UEFN Creators Discord for a few weeks before posting.

I wanted to share something I built that solved a problem I kept seeing mentioned in #verse-scripting: managing shared mutable state across multiple Verse devices without race conditions. I wrote a small state management pattern using Verse's `sync` and `weak_map` primitives — the post is here: [link].

The question I'm genuinely unsure about: is there a better primitive for this in the current UEFN SDK? I saw the discussion last week about `manager` classes and wasn't sure if that's the intended solution for this pattern.

Happy to get any feedback — especially if I'm missing something obvious.
