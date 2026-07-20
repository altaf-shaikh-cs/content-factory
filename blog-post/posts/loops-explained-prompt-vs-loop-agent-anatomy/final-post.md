---
title: Stop Prompting Agents. Start Designing Loops.
tags: ai-engineering, claude-code, automation, agents, llm-orchestration
seo_title: Prompt vs Loop: How to Design AI Agent Loops That Finish
seo_description: Still re-prompting the same AI task by hand every week? Here's the anatomy of a real agent loop, and the four-question test for when to build one.
---

<!-- 
BANNER IMAGE
============
SVG hero (generated): blog-hero.svg — upload this to Hashnode as the cover image.

To generate a higher-res version with an external tool, use the prompt below:

PROMPT:
A dark, minimal editorial illustration. Deep charcoal background. A single glowing circular loop of thin light, unbroken, with one small bright node traveling around its path as if mid-cycle. Off to one side, a loose scatter of small dim disconnected dots, static and unconnected to anything. The loop is the visual focus, calm but clearly in motion. Muted single accent color (cyan or amber) traces the loop and its traveling node. Generous negative space. Wide banner format, no text, no logos, no user interface elements, no code, no photorealism, flat conceptual editorial tech-blog illustration style.

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

# Stop Prompting Agents. Start Designing Loops.

You type a request. You wait. The output is close but not quite right. You fix it by hand, or you type another request and wait again. Repeat until it's done, or until you give up and finish it yourself.

That's how most people use AI agents today. One instruction at a time, babysitting every step, doing the actual repetition themselves while the "automation" only ever runs once per click.

## The problem

A prompt is a single instruction. You write it, the model responds, and the interaction is over. If the result is wrong, that's on you to notice and on you to fix, by writing the next prompt.

This works fine for one-off tasks. It falls apart the moment the task repeats. Every day you re-explain the same job, re-paste the same context, re-check the same things by eye. The model never gets better at catching its own mistakes, because nothing is actually checking. You are the check. You're also the trigger, the memory, and the retry logic, all done manually, all day.

## The reframe

A prompt is an instruction. A loop is a goal the agent keeps working toward until it actually gets there.

That distinction comes from a widely shared breakdown by Anatoli Kopadze, built on a line from Peter Steinberger: "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." The shift isn't about writing better prompts. It's about not being the one who has to notice when the output is wrong and manually ask again.

## The solution: the loop cycle

A real loop runs five stages: **DISCOVER → PLAN → EXECUTE → VERIFY → ITERATE.** Three of those do the actual work of turning "an agent that responds" into "an agent that finishes."

**Verify is the heart of the loop.** Without a real check, a hard test, a measurable condition, a rubric, you don't have a loop. You have the model agreeing with itself on repeat. The same model that did the work is a far too generous grader of its own homework. If nothing external can reject a bad answer, the loop can't tell success from a confident guess.

**State is what makes the loop learn.** A real loop keeps a small record: what's done, what failed, what's next. Tomorrow's run resumes from that record instead of starting from zero, which is the entire difference between a loop and a chatbot you happen to run twice.

**A stop condition keeps it sane.** Two valid exits: success, or a hard limit like "after 8 tries, stop and report." Skip this and you've built something that can run all night producing nothing, quietly burning tokens on a task it decided it already finished. That failure mode has a name in the piece: the Ralph Wiggum loop, after a pattern Geoffrey Huntley documented, where the agent calls it done too early and the loop keeps spending with nothing to show for it.

Before wiring any of this up, there's a four-question test worth running, and all four have to be true:

1. The task repeats, at least weekly
2. Something can automatically reject bad output: a test, a type check, a build, a linter
3. The agent can do the work end to end
4. "Done" is objective, not a judgment call

Miss one of those, and it should stay a manual prompt. Looping a task that fails the test doesn't make it more reliable, it just makes the failure automatic.

## Real walkthrough

Claude Code ships all five building blocks a real loop needs, and none of them are exotic:

The **automation** is whatever triggers the run: `/loop`, a hook, a cron schedule, CI. The **skill** is the reusable instruction set the loop executes each time, so you're not re-explaining the task from scratch. **Sub-agents** split the maker from the checker: one agent writes fast and cheap, a separate one reviews slow and strict. That separation alone accounts for most of the quality difference between a loop that drifts and one that doesn't. **Connectors** let the loop act instead of just suggesting: it opens the PR, links the ticket, posts to the channel. And the **verifier gate** is the one block that decides whether the whole loop is worth running, or just quietly spending money.

That last part is not theoretical. I run a content pipeline built on exactly this shape: a skill per channel, a `/loop` prompt that wraps it, scheduled cloud routines that fire it daily, editor and verifier agents that check the output before anything ships, and a `TODO.md` per channel that acts as the state file, tracking what's queued, what's in progress, what's done. I put this together independently, before reading the breakdown that names the pattern. It matches the architecture step for step: trigger, skill, maker/checker split, a place to act, and a gate that decides what's good enough to go out. That's not a coincidence, it's what happens whenever a repeating task gets taken seriously.

The order that got me there matters as much as the pieces: get one run reliable by hand first. Turn it into a skill once it's reliable. Wrap the skill in a loop, with a gate and a stop condition. Only then put it on a schedule. Scheduling something before it's reliable by hand is exactly how a loop turns into the thing that runs all night while you sleep and produces nothing.

## What makes it different

**It moves the checking out of your head and into the system.** Verify isn't a nice-to-have step, it's the thing that makes the loop trustworthy without you watching every run.

**It separates the writer from the reviewer.** One model producing and grading its own work is not a check. Splitting those roles is most of what makes the output hold up over time.

**It treats "done" as something the loop must prove, not assume.** A stop condition with two real exits means the loop either succeeds or reports failure, it never just runs forever hoping.

**It scales through state, not memory.** The loop doesn't need to remember anything, because the state file does. Tomorrow's run reads what yesterday's left behind and continues.

## When to use it

- A task you already do at least weekly, by hand, the same way each time
- Any task where a test, linter, build, or rubric can tell good output from bad
- Work where "done" doesn't depend on a judgment call
- Anything currently costing you a manual re-prompt every single time it repeats

## The cost nobody mentions

Context gets re-sent every iteration, and it grows a little each pass. A loop that runs ten times costs roughly ten prompts, each one bigger than the last. A single medium task run by one agent typically costs somewhere in the 50,000 to 200,000 token range, and almost nobody tracks the metric that actually matters: cost per accepted change, not tokens spent. Below roughly a 50 percent accept rate, the loop is costing you more than it's giving back. Track that number before you decide a loop is worth keeping.

## The light version, if you're not ready to build one

You don't need Claude Code or any specific tooling to try the core idea. Paste this shape into any LLM: give it a task, strict success criteria, and a protocol, PLAN, then DO, then VERIFY by scoring each criterion 1 to 10, then DECIDE, if every criterion scores 8 or higher print FINAL, otherwise iterate on the weakest one.

It's missing the automation piece, you're still the trigger, close the tab and the loop is gone. But it gets you the actual habit change: verify against criteria instead of trusting the first output, and iterate on the weakest point instead of starting over.

## Try this

Pick one task you currently re-prompt by hand at least once a week. Run it through the four-question test. If it passes all four, write down what "done" objectively looks like before you touch a single prompt, that's your verify step, and everything else follows from it.

## Let's talk

What's the task you keep manually re-prompting that probably should've been a loop months ago? Where does your own AI usage fail the four-question test, and did you know it was failing before reading this? And if you've already built something like this, what's your verify step actually checking?

If this was useful, a like helps more people find it. Next up: what it actually looks like to run the maker/checker split with real sub-agents, not just the theory of it.

---

This builds on the same thread as the posts on `/loop` and scheduled routines: automation only holds up if something inside it can tell good output from bad. If you're new to that thread, start there, this post is the anatomy of the loop those pieces were quietly building all along.

---

## Post assets

| File | Use |
|------|-----|
| [blog-hero.svg](./blog-hero.svg) | Hashnode cover image (SVG, 1600×900) |
| [03-banner-prompt.md](./03-banner-prompt.md) | Prompt to regenerate with Midjourney / DALL·E / Ideogram |
| [02-title-options.md](./02-title-options.md) | All title options — edit frontmatter above to switch |
