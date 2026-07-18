# Post Plan — fable5-hybrid-orchestration-patterns

## Core Insight
"Which model should I use?" is the wrong question. The right question is "which model should handle which part of this task?" Published benchmark data shows two hybrid patterns (cheap executor + expensive advisor, or expensive planner + cheap workers) that keep 92 to 96 percent of top-model quality at roughly half the cost.

## Target Audience
Engineers and tech leads building AI agents or heavy Claude/LLM workflows who are watching their API bills climb. Early-to-mid career developers in India's tech hubs experimenting with Claude Code and multi-agent setups.

## Structure
1. The trap: everyone routes every token through the biggest model, and pays for it
2. Pattern 1, Advisor: cheap model runs the loop, calls the expensive model as an on-demand advisor roughly once per task (92% of solo score at 63% of the price on SWE-bench Pro)
3. Pattern 2, Orchestrator: expensive model plans, fans work out to cheap worker sub-agents ($18.53 vs $40.56 per problem on BrowseComp, 96% of the performance at 46% of the price; all-cheap was $16.01 but accuracy fell to 77.8%)
4. How to do it today in Claude Code: define a helper role in `~/.claude/agents/worker.md` on a cheaper model with lower reasoning effort; a short instructions file tells the main model what to hand off

## CTA
Open question: "How are you splitting work across models in your agent setups?" Plus a note that source links go in the first comment.

## Tone Range
Educational with an authoritative edge. Practical, numbers-forward, no hype.

## Hashtags
#AIEngineering #AIAgents #ClaudeCode

## Image Brief
- Advisor pattern: 92% of the score at 63% of the price (SWE-bench Pro)
- Orchestrator pattern: 96% of the performance at 46% of the price (BrowseComp)
- $18.53 vs $40.56 per problem (hybrid vs solo top model)
- All-cheap baseline: $16.01 but accuracy drops to 77.8% (vs 86.8% hybrid, 90.8% solo)
- Tagline: "The wrong question: which model? The right question: which model for which part?"
- Framing: split-screen of the two patterns (escalate up vs delegate down)

## Performance Context
- Best performing angle so far: Contrarian (7.43%) and Story-first (6.39% avg); Bold claim-first is inconsistent (3.86% avg)
- Hook styles that drove comments: uncomfortable truths and reframed beliefs ("indictment beats scene")
- Hook styles that drove passive reactions only: scene-setting openers and capability announcements (routines: 848 imp, 2.48%)
- Topics/themes that resonated: practical skill-building, developer tool comparisons, "taking sides" posts
- What to avoid repeating: abstract "I built a system" process posts with slow hooks; links in the post body
- Implication for THIS post: this idea is a natural "taking sides" topic (hybrid vs solo, cost vs quality) with hero numbers. Lead with the reframe or the numbers, not a scene. Keep links out of the body, point to first comment.

## Angle Assignments
Fixed angles (always used):
- Angle A: Story-first — open with a personal moment or real scenario, let the insight emerge
- Angle B: Bold claim-first — lead with the provocative insight, then back it with evidence/story

Chosen Angle C: **Tactical/how-to-first** because decision rule 2 matched — the idea teaches two concrete, repeatable orchestration patterns plus an exact Claude Code setup (`~/.claude/agents/worker.md`), which is material the story and claim angles structurally cannot lead with.
