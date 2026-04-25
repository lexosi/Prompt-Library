# Client Project Kickoff

**Category:** project-kickoff
**When to use:** Aligning with a client before starting billed work — to prevent scope creep, miscommunication, and billing disputes.

---

Write a client kickoff document that will be shared with a client before project work begins. This document is a contract of understanding, not a technical spec. It should be clear to a non-technical reader.

The document must cover:

**PROJECT SUMMARY:** What we're building and why. Written for the client, not the engineer. 2–3 sentences.

**WHAT SUCCESS LOOKS LIKE:** Specific, observable outcomes from the client's perspective. Not "a working system" — "users can log in, create a profile, and receive their first report within 5 minutes."

**DELIVERABLES:** An explicit list of what will be handed over at project end. Format: [ ] item — format — acceptance criteria.

**WHAT'S NOT INCLUDED:** Explicitly listed items that are out of scope. This is the most important section — clients often assume things are included that aren't.

**TIMELINE:** Phase-by-phase with dates. Include a milestone that requires client review/approval at each phase.

**CLIENT RESPONSIBILITIES:** What the client must provide or decide for work to proceed — assets, credentials, approvals, feedback windows.

**COMMUNICATION PLAN:** How often you'll update them, via what channel, and what triggers an unscheduled update.

**CHANGE PROCESS:** How scope changes are handled — what requires a new estimate, what's covered.

**Project name:**
[name]
**What needs to be built:**
[description]
**Client type:** [technical/non-technical]
**Project duration:** [estimate]

---

## Example output

**PROJECT SUMMARY:** We're building an AI-powered customer support chatbot for your e-commerce store. It will handle your 50 most common support questions automatically, reduce your support ticket volume by an estimated 40%, and escalate complex issues to your human team.

**WHAT SUCCESS LOOKS LIKE:**
- Customers get an accurate answer to their question within 10 seconds, 24/7.
- Your support team receives only tickets the bot couldn't handle.
- The bot correctly handles 80%+ of conversations in our initial test period.

**DELIVERABLES:**
- [ ] Deployed chatbot widget — embedded on your website — passes 50-question accuracy test
- [ ] Admin panel — web interface — you can update bot responses without code
- [ ] Handoff integration — Zendesk — bot escalates to human with full conversation context

**WHAT'S NOT INCLUDED:** Mobile app integration, multi-language support, phone/voice channel, email automation, CRM integration beyond Zendesk.

**CLIENT RESPONSIBILITIES:** Provide 50 most common support questions with correct answers by Day 3. Provide Zendesk API credentials by Day 1. Designate one person to review bot responses during the test period.
