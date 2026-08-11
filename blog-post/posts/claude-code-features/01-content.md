<!-- 
BANNER IMAGE
============
Generate this image using Midjourney, DALL·E, Ideogram, or any image tool, then upload to Hashnode as the cover image.

PROMPT:
[filled in from Phase 3]

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

# 25 Things I've Learned Shipping a Lot of Features With Claude Code

You open the agent, type a rough sentence, and hit enter. Twenty minutes later you're untangling a diff that touched six files you didn't mean to touch, half of which you now have to explain to yourself before you can explain them to anyone else.

That was my normal for a while. Not because the model was bad. Because I was treating it like a vending machine: put in a vague request, expect a finished feature to fall out.

## The problem

Most people's first instinct with a coding agent is to skip straight to the ask. "Add a login page." "Fix the bug in checkout." Then they sit back and hope the agent fills in everything they didn't say.

The agent will fill in the gaps. It just fills them in with guesses, and guesses compound. A vague prompt on step one becomes a wrong assumption on step three, which becomes a broken edge case on step seven. By the time you notice, you're not debugging a feature, you're debugging a chain of assumptions you never actually approved.

## The reframe

The agent isn't the bottleneck. Your clarity is.

Claude Code (or any AI coding agent, this isn't tool-specific) amplifies whatever you feed it. Feed it a clear spec, clean context, and a tight scope, and it ships something close to right on the first pass. Feed it a one-line wish, and it ships something close to your one-line wish's ambiguity, at full speed.

Once I stopped blaming the model and started treating my own input as the actual lever, the failure rate dropped hard.

## The solution

After shipping a lot of features this way, the habits that actually moved the needle cluster into four groups.

**Plan before you prompt.** Writing the feature spec before opening the agent is most of the work. Give it everything a competent teammate would need to start cold: screenshots, file structures, database schemas, API docs. A screenshot dropped straight into the terminal carries more context than three paragraphs describing the same screen. And when you're stuck mid-task, that's usually a sign you're still confused about what you actually want, not that the agent is confused.

**Structure beats prose.** Prompts formatted as structured data, XML tags around requirements, constraints, and examples, get parsed far more reliably than a wall of plain sentences. The same goes for your rules files: keep them short. A concise 80-line CLAUDE.md that the agent actually follows beats a 400-line one it skims.

**Design many small agents, not one big one.** A single mega-agent trying to handle frontend, backend, and database work at once behaves like a generalist pulled in three directions. Splitting that into specialized roles that each do one thing well produces cleaner, more predictable output. Custom commands for the tasks you repeat daily save real time, and hooks that fire automatically on events you'd otherwise remember to do yourself are underused for exactly that reason: set once, benefit on every run after.

**Guardrails keep momentum from turning into mess.** One feature per chat. Commit after every feature that actually works, so reverting is always cheaper than fixing forward. Set explicit checkpoints ("stop after this and wait") so a long task doesn't wander past where you meant to check in. And restart the session once you're roughly halfway through the context window. Model quality degrades quietly as compaction kicks in; you won't always notice until the output already got worse.

## Real walkthrough

Here's the same request handled two ways.

**Before:** "Add a login feature." The agent picks an auth approach, guesses at your existing user model, invents a session strategy, and hands you something that technically logs a user in, using none of the conventions the rest of your codebase already follows.

**After:** A short spec file first. What the login flow needs to support, a screenshot of the existing signup screen for visual consistency, the current user schema, and one line: "match the session pattern already used in the billing module." Requirements wrapped in XML tags so the important constraints don't get lost in prose. Then one instruction after the diff lands: "explain what you changed and why," which forces the agent, and you, to actually verify the reasoning instead of skimming green checkmarks.

Same feature. Same model. The difference was entirely in what went in before the first line of code came out.

## What makes it different

**It moves the fix upstream.** Instead of debugging bad output after the fact, you're preventing bad input before it happens. Cheaper every time.

**It treats context as a budget, not an afterthought.** Screenshots, schemas, and a spec aren't extra steps, they're the actual payload. The prompt itself is just the request wrapped around them.

**It scales your review, not just your output.** Asking the agent to explain its own changes, and asking yourself what might still be broken, catches problems while they're still cheap to fix.

**It compounds.** A DONT_DO.md of past failures, a PROJECT_CONTEXT.md kept current, a rules file the agent actually reads: none of these pay off on day one. By week three, they're the reason your sessions start faster and drift less.

## When to use this

- Any feature that touches more than one file or more than one person's mental model of the system
- Any bug fix where "should work" hasn't been verified by actually running it
- Any session where you notice yourself getting confused about the ask, because the agent is about to get confused too
- Any repeated task you've now done by hand three times

## Try this

Before your next session, write the spec first. Not a paragraph, an actual list: what needs to happen, what it touches, what it should look like when it's done. Then hand that to the agent instead of the one-line version you'd normally type. Watch how much less cleanup the diff needs.

## Let's talk

What's the messiest cleanup you've had to do after a one-line prompt went sideways? Do you keep a running DONT_DO.md, or something like it, and has it actually changed how you brief the agent? And for the multi-agent habit: have you split frontend, backend, and database work into separate roles, or does one agent still handle all of it for you?

If this was useful, a like helps more people find it. Next up: what it actually looks like to build your first small team of specialized agents instead of one generalist.

---

This is the mindset layer underneath everything else in this series: the agent is only ever as good as what you hand it. Once that clicks, the rest, tools, structure, workflows, gets a lot easier to build on top of.
