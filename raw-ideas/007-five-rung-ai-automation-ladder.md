# The Five-Rung Ladder: Why Your AI Automation Keeps Collapsing

## Context

This is a DERIVED idea. It does not come from a single source. It was synthesized on 2026-08-09 by reading the whole `raw-ideas/` library at once and noticing that almost every idea in it is describing the same structure from a different height. No single idea file contains this framing.

**The core reframe:** everyone talks about AI capability as a flat question ("can AI do X?"). It is not flat, it is a ladder with five rungs. Each rung is a different amount of the work you have handed over. And the rung only holds if the rung below it is already reliable. Most people fail not because they picked the wrong rung, but because they jumped.

### The five rungs

**Rung 1 — Prompt.** One instruction, one output, you drive every step. You are the memory, the planner, and the checker. Nothing is saved. Close the tab and it is gone.
Library evidence: `just text.md` (fundamentals are the thing that compounds, tools change), `gen-ai-roadmap.md` (people collect tutorials and prompts while fundamentals stay weak), `005-loops` (most people use AI the slowest way possible: type a request, wait, fix it, ask again, all by hand).

**Rung 2 — Skill.** The instruction stops being typed and becomes saved. Your structure, your conventions, your rules, written once and picked up automatically every time a task fits.
Library evidence: `006-claude-four-building-blocks` (Skills are about consistency; no more copy-pasting the same instructions into a new chat every Monday), `iphone-shortcit-to-generate-slide` (the whole win was baking the learned slide structure into a reusable prompt so the raw note reaches a polished deck without willpower), `claude code features.md` (custom commands for repetitive tasks, rules files under 100 lines).

**Rung 3 — Loop.** Not an instruction anymore, a goal the system keeps working toward. Requires three parts that a prompt does not have: a verifier that can reject bad output, a small state record so tomorrow resumes instead of restarting, and a stop condition.
Library evidence: `005-loops` (DISCOVER, PLAN, EXECUTE, VERIFY, ITERATE; "without a real check you don't have a loop, you have the agent agreeing with itself on repeat"; the model that did the work is far too generous a grader of its own homework), `003-claude-new-feature-loop` (the /loop feature itself).

**Rung 4 — Routine.** The loop leaves your machine and runs on a schedule. The trigger is no longer you.
Library evidence: `ROUTINES.MD` ("until now, if you closed your laptop, your AI automation died"), the shift from a tool you manually trigger to a persistent agent running in the cloud.

**Rung 5 — Agent team.** Roles instead of one worker. The critical split is maker from checker, and a planner that routes work rather than doing it.
Library evidence: `build-your-first-agents-team.md` ("prompting just finishes the work, but a system solves problems"), `first-autonoumsly-dveloped-todo-app.md` (handed over a PRD, agents planned, executed, tested across ticks, output was a working app), `run-your-own-agent-acengy-with-paperclip.md` (a whole company of assigned roles), `004-fable5-hybrid-orchestration-patterns.md` (advisor pattern escalates up, orchestrator pattern delegates down; the real question is not "which model" but "which model handles which part").

### The non-obvious part (this is the actual post)

**A rung only holds if the rung under it is reliable.** The ladder is not a menu you pick from by ambition, it is a sequence you earn.

`005-loops` states the order explicitly: get ONE manual run reliable first, then turn it into a skill, then wrap the skill in a loop with a gate and a stop condition, and only THEN put it on a schedule. Scheduling something you have not made reliable by hand is how loops blow up while you sleep.

The library also contains the proof of what skipping costs:

- **Skipping to rung 5 without rung 3.** `002-SuperReps-learnings.md`: the AI produced the UI, but features did not work, the UX was missing, and the flows broke. There was no verifier, so the human became the verifier, refining screen by screen. "Not a single prompt is going to do the magic for me." That is a rung-5 ambition running on rung-1 machinery.
- **Why rung 3's verifier is not optional.** `001-claude-vs-codex.md`: the tool that won did not write better code, it opened the browser and checked its own work through the full flow. The other one generated and waited for another prompt. Same class of model, different rung.
- **The cost of climbing at all.** `ai-non-deterministic-code-vs-program-deterministic-code.md`: a program returns the same output forever, an agent does not. Effort levels change, models get swapped under you, instructions get skipped on run four. So every rung you climb adds maintenance you cannot walk away from. "With agents, I am not able to forget it. I am constantly working on it." Climbing is not free, which is exactly why you do not climb higher than you need.

### The diagnostic (what makes this saveable)

Ask which rung you are actually on, not which one you are talking about:

- If you retype context every session, you are on rung 1 and a skill is your next move, not an agent team.
- If you have saved instructions but still read every output before trusting it, you are on rung 2 and your missing piece is a verifier, not a bigger model.
- If something else can reject bad output and it still needs you to press go, you are on rung 3 and the next step is a schedule.
- If it runs without you but one agent both writes and grades its own work, you are on rung 4 and the split you need is maker from checker.
- If you jumped straight to rung 5, you are not automating. You are doing rung 1 work with extra steps and a bigger bill.

The 4-question test from `005-loops` for whether to climb past rung 2 at all (all four must be true): the task repeats at least weekly, something can automatically reject bad output, the agent can do the work end to end, and "done" is objective rather than a judgment call. Miss one and stay on the rung you are on.

### Personal angle available

Altaf built all five rungs in the content factory without initially framing them as a ladder: skills per channel, /loop prompts, scheduled cloud routines, separate strategist and editor and verifier agents, and TODO.md as the state record. The honest reflection is that it only worked in that order, and the rungs he tried to skip early are exactly where the time went.

## Source

Derived from across the library, no external source. Contributing ideas:
`just text.md`, `gen-ai-roadmap.md`, `006-claude-four-building-blocks...md`, `iphone-shortcit-to-generate-slide-from-raw-ideas.md`, `claude code features.md`, `005-loops-explained-prompt-vs-loop-agent-anatomy.md`, `003-claude-new-feature-loop.md`, `ROUTINES.MD`, `build-your-first-agents-team.md`, `first-autonoumsly-dveloped-todo-app.md`, `run-your-own-agent-acengy-with-paperclip.md`, `004-fable5-hybrid-orchestration-patterns.md`, `002-SuperReps-learnings.md`, `001-claude-vs-codex.md`, `ai-non-deterministic-code-vs-program-deterministic-code.md`

## Format note

Requested build: document carousel plus caption copy. The five rungs are sequential, which is the one content shape a carousel does better than a text post. The account has no carousel performance data yet (all logged posts were text plus image), so treat reach expectations as unknown and judge this on engagement rate against the 4.0% baseline.
