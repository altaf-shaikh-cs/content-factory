---
title: Your Usage Dashboard Is Lying to You
tags: ai-engineering, claude-code, developer-tools, llm, cost-optimization
seo_title: Why Your AI Agent Token Bill Is Higher Than It Looks
seo_description: Your usage dashboard hides the real cost driver. Here's how reading raw session transcripts found a single config change cutting AI agent spend in half.
---

<!-- 
BANNER IMAGE
============
SVG hero (generated): blog-hero.svg — upload this to Hashnode as the cover image.

To generate a higher-res version with an external tool, use the prompt below:

PROMPT:
A dark, minimal editorial illustration of a small simple bar chart on the surface of dark water, with a massive abstract data structure or network of glowing nodes submerged and barely visible beneath the surface, implying hidden scale. Muted teal and amber accent lighting against near-black background. Atmosphere: quiet, technical, slightly ominous. Wide banner format, 16:9 aspect ratio. No text, no logos, no code, no photorealism, flat editorial illustration style.

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

Your AI coding agent's usage dashboard has a chart on it. Some input tokens, a big bar of output tokens, and a much bigger bar you've probably never asked about: cache. Most people glance at the small numbers, feel fine about the bill, and move on.

I didn't move on. I pulled my own session transcripts for a week and did the math by hand.

## The problem

Here's what the dashboard told me for one week: 52.3k tokens in, 19.4M tokens out. Not cheap, but not alarming either. Here's what the transcripts actually said:

| | tokens |
|---|---|
| fresh input | 11k |
| output | 5.6M |
| cache writes | 31.5M |
| cache reads | 1,196M |

Twelve hundred million cache reads. That's 213 tokens re-read for every single token the model produced. At the rates I'm on ($5/$25 per million tokens, $0.50 for a cache read, $10 for a 1-hour-TTL cache write) that week cost roughly $1,050. Somewhere around $600 of it was pure re-reading of context I'd already paid once to build.

The dashboard's "in/out" legend isn't lying. It's just not the number that matters. The number that matters is buried in a bar labeled "cache," and nobody designs a chart to make you click into that one.

## The reframe

I assumed the bill was a usage problem: I'm doing more work, so I'm spending more. It isn't. It's a shape problem. The cost of one agentic session is roughly average context size multiplied by number of API calls, and that grows close to quadratically with how long the session runs. Every extra turn doesn't just add its own cost, it re-pays for every turn before it, because the whole conversation gets re-sent and re-cached on each call.

A model with a bigger context window doesn't remove that cost. It removes the thing that used to *cap* it.

## The solution

I'd switched my default model setting to a 1M-context variant a while back, for the rare session that genuinely needed the extra room. On a smaller window, something called auto-compact kicks in around 160-180k tokens and trims the conversation before it can balloon. That's a ceiling, and ceilings are annoying right up until you look at what happens when you remove one.

With the ceiling gone, nothing stops a session from growing. Here's how my week's 32 sessions actually distributed:

| context size | calls | % of calls | % of tokens |
|---|---|---|---|
| 0k-100k | 1,569 | 27.4% | 9.5% |
| 100k-200k | 1,863 | 32.6% | 21.1% |
| 200k-400k | 1,371 | 24.0% | 31.7% |
| 400k-800k | 920 | 16.1% | 37.7% |

The top bracket is 16% of calls and 38% of the entire week's spend. Six sessions out of thirty-two burned 76% of my total tokens, peaking at 734k, 593k, 555k, 501k, 449k, and 446k tokens of context. Those six sessions are where the ceiling would have fired, and didn't.

## Real walkthrough

I went looking for what was actually filling those contexts up, tool by tool.

| tool | calls | tokens | avg per call |
|---|---|---|---|
| Read | 136 | 2,938,201 | 21,604 |
| Bash | 2,285 | 1,620,121 | 709 |

Bash is cheap per call and I make a lot of them, which is fine, that's what a coding agent does. Read is the one that hurts, because a Read result doesn't leave the conversation once it's been added. It gets included, unchanged, in every single API call for the rest of that session. One file read at call #200 of a 947-call session gets re-sent 747 more times. That one read, roughly 21k tokens, ends up costing about 15.7M tokens and around $8, by itself, because nothing ever needed to see it again.

The four worst sessions of the week made the pattern obvious:

| session | duration | user messages | API calls | max context |
|---|---|---|---|---|
| A | 5.4h | 32 | 947 | 593k |
| B | 8.1h | 42 | 718 | 734k |
| C | 12.2h | 5 | 427 | 501k |
| D | 28.4h | 42 | 481 | 555k |

Session C is the one that should worry anyone running agents unattended: five user messages, twelve hours, 427 API calls. That's not five turns of conversation, that's an agentic loop running on its own for half a day with nobody checking in, quietly re-reading half a million tokens of context on every step. Session D ran for 28 hours straight on a single conversation thread, one continuous session accumulating cost the entire time instead of resetting between distinct pieces of work.

## What makes this different

**It's measured, not estimated.** Every number above came out of the transcript JSONL usage fields, not a guess based on how the work "felt." The dashboard chart and the transcript reality disagreed by a factor of roughly 20x on the numbers that matter.

**It found the lever, not just the symptom.** "Costs are high" isn't actionable. "One config line removed your compaction ceiling" is a single edit.

**It separates diagnosis from fix.** I didn't touch a setting until I understood exactly which behavior was responsible for which slice of the bill. Change the config first and you'll never know if it actually worked, because you never measured the baseline.

**It generalizes past one project.** The worst offenders weren't tied to one codebase. One long-running project accounted for a disproportionate share of transcript volume on disk, which was itself a signal, not the cause: long sessions and whole-file reads compound anywhere you let them run unchecked.

## When to do this yourself

- Your usage bill jumped and the dashboard's summary chart doesn't explain why
- You're running agentic loops or subagents unattended for hours
- You've set a large-context model as your *default* rather than reaching for it on demand
- A session has been open across more than one distinct task
- You want a real number before you change a setting, not after

## Call to action

Open your own settings file today. Check what model your agent defaults to, and whether that default quietly removed a cost ceiling you didn't know existed. If you can, pull a week of your own transcripts before you touch anything. The fix is only worth applying once you've seen the shape of the actual bill.

## Let's talk about it

Have you looked at what's inside your "cache" bar instead of just the input/output numbers? If you have, what did it show?

Where does your context actually go: long files, long conversations, or agentic loops that don't checkpoint?

If you found a lever like this in your own setup, what was it?

If this was useful, a like helps more people see it before they get the surprise bill I got.

Part of this series is about the mechanics under an agent's hood, not just the prompts you type into it. Next up: what actually happens inside a session when auto-compact fires, and why that ceiling exists in the first place.

## Series connector

If you missed the earlier posts on how agentic loops and subagents actually spend their context, start there, this one builds directly on the "cost = context × calls" idea from that thread.

---

## Post assets

| File | Use |
|------|-----|
| [blog-hero.svg](./blog-hero.svg) | Hashnode cover image (SVG, 1600×900) |
| [03-banner-prompt.md](./03-banner-prompt.md) | Prompt to regenerate with Midjourney / DALL·E / Ideogram |
| [02-title-options.md](./02-title-options.md) | All title options — edit frontmatter above to switch |
