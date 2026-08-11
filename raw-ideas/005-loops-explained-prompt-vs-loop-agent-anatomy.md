# Loops Explained: Stop Prompting Agents, Start Designing Loops

## Context

A viral X article (18M views) by Anatoli Kopadze breaking down why the best AI engineers stopped prompting and started designing loops. Core reframe: a prompt is a single instruction; a loop is a goal the AI keeps working toward until it gets there. Most people still use AI the slowest way possible: type a request, wait, fix it, ask again, all by hand. Quote from Peter Steinberger: "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."

**The loop cycle:** DISCOVER → PLAN → EXECUTE → VERIFY → ITERATE. Three parts do the real work:
- **Verify is the heart.** Without a real check (a hard test, a measurable condition, a rubric), you don't have a loop, you have the agent agreeing with itself on repeat. The model that did the work is far too generous a grader of its own homework.
- **State is what makes the loop learn.** A real loop keeps a small record: what is done, what failed, what is next. Tomorrow's run resumes instead of starting from zero.
- **A stop condition keeps it sane.** Two exits: success, and a hard limit ("after 8 tries, stop and report"). Skip this and you built a machine that runs all night for nothing.

**Do you even need one? The 4-question test** (all four must be true):
1. The task repeats, at least weekly
2. Something can automatically reject bad output (test, type check, build, linter)
3. The agent can do the work end-to-end
4. "Done" is objective, not a judgment call
Miss one box, keep it as a manual prompt.

**The five building blocks of a real loop** (Claude Code ships all five): the automation/trigger (/loop, hooks, cron, CI), the skill (reusable saved instructions), sub-agents (split the maker from the checker: writer fast and cheap, reviewer slow and strict; that separation is most of the quality), connectors (so it acts instead of suggesting: opens the PR, links the ticket, pings the channel), and the verifier gate (the one block that decides if the loop helps or just spends money).

**The cost nobody mentions:** context is re-sent every iteration and grows each pass. A loop that runs ten times costs ten prompts that each keep getting bigger. Rough cost of one loop: 50,000 to 200,000 tokens for a single agent on one medium task. The metric that matters and almost nobody tracks: **cost per accepted change**, not tokens spent. Below a 50 percent accept rate the loop costs more than it gives back. Loops also fail quietly: the "Ralph Wiggum loop" (Geoffrey Huntley), where the agent decides it is done too early and the loop keeps spending while producing nothing.

**The order that actually works:** 1) get ONE manual run reliable first, 2) turn it into a skill, 3) wrap the skill in a loop (gate + stop condition), 4) THEN put it on a schedule. Scheduling something you have not made reliable by hand is exactly how loops blow up while you sleep.

**The light version anyone can run:** a self-checking loop prompt pasted into any LLM: give it a task, strict success criteria, and a protocol (PLAN, DO, VERIFY scoring 1 to 10 per criterion, DECIDE: if every criterion is 8+ print FINAL, else iterate on the weakest point). The missing part of the light version: you are still the trigger; close the tab and it is gone.

Strong personal angle available: Altaf's content factory IS this exact architecture (skills + /loop prompts + scheduled cloud routines + editor/verifier agents + TODO.md as state), built independently and matching the article's playbook step for step.

Note: the article's second half promotes Mira, a Telegram-based agent product. Treat that section as promotional; the loop anatomy is the substance.

## Source

- https://x.com/AnatoliKopadze/status/2068328135611822149

## Inspiration

Original PDF capture: `./(6) Anatoli Kopadze on X_ _Loops explained_ Claude, GPT, Mira and what actually works_ _ X.pdf` (16 pages, includes the loop spec and self-checking prompt verbatim)
