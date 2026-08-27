---
title: I Turned Off Manual Approval Two Months Ago. Here's What Actually Happened.
tags: claude-code, ai-engineering, developer-tools, automation, productivity
seo_title: Should You Turn Off Manual Approval in Claude Code?
seo_description: Two months running Claude Code with manual approval off. What the classifier caught, what it let through, and when to trust a guardrail instead.
---

<!-- 
BANNER IMAGE
============
SVG hero (generated): blog-hero.svg — upload this to Hashnode as the cover image.

To generate a higher-res version with an external tool, use the prompt below:

PROMPT:
Editorial illustration for a tech blog, minimal and dark, a single human hand releasing a small glowing token into a calm horizontal current of light, the token flowing freely downstream past a subtle translucent watching presence that lets it pass without friction, one faint dimmed hand in the background still gripping a row of small tokens tightly to suggest the old habit of holding on, deep charcoal and navy background with a single warm accent color (amber or soft gold) on the released token and the current, abstract and conceptual, calm and confident mood, not literal software UI, wide banner format

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

# I Turned Off Manual Approval Two Months Ago. Here's What Actually Happened.

Two months ago I turned off manual approval in Claude Code. Every "yes" I used to click, I stopped clicking. I still haven't turned it back on.

That single change tells you something. Not because I got reckless. Because the thing that used to sit between me and every action Claude took has gotten good enough that clicking "yes" forty times a session stopped being safety and started being noise.

## The problem

Most people I talk to are still doing "yes, yes, yes, yes." Every file edit, every command, every tool call, a prompt pops up and they approve it. Ask them why and the answer is always some version of the same thing: they're scared it'll break something.

That fear made sense a year ago. It doesn't hold up as well now, and almost nobody has gone back to check.

Here's the part that gets missed: most of that "yes, yes, yes" is redundant. Something like 90% of the actions you're manually rubber-stamping today are things an auto classifier would already catch and handle correctly on its own, without you. You're not adding safety by clicking through them. You're adding friction, and eventually you click without reading, which is worse than not reviewing at all.

The auto classifier that does this job has been running in the background of my sessions for over two months now. And I've watched it go from "interesting feature I should keep an eye on" to something I genuinely don't think about anymore. That's the whole story of this post: how it earned that.

## The reframe

The instinct is to think "no manual approval" means "no oversight." That's not what's actually happening.

What's happening is the oversight moved. It didn't disappear, it changed shape. Instead of a tired human clicking yes on the fortieth prompt of the day, there's a system evaluating each action on its own terms, every time, without getting worn down by the thirty-ninth one before it.

I noticed this most clearly with connectors. I've got a fair number of them wired into Claude Code, along with broad permissions. In theory, that's a lot of surface area for something to go sideways. In practice, if Claude tries to act on my behalf through one of those connectors and I haven't explicitly told it to, it stops. It blocks the action until I say so directly in the chat. Not a vague "are you sure," a hard stop that waits for me to specifically name what I want.

That's not what I expected from turning approval off. I expected more risk. I got a system that's more precise about what actually needs my attention than I was being when I approved everything by reflex.

## The solution

So what am I actually relying on, if not clicking approve on everything myself?

Two different things, and which one matters depends on what I'm doing.

**While I'm actively working**, sitting at the CLI or in an editor with a session open, I lean on the auto classifier. It's watching each action Claude wants to take and deciding, in real time, whether that action is something reasonable given what I asked for, or something outside the lines. If it's outside the lines, non-instructed, destructive, or anything that looks unintended, it blocks. I don't do yes-yes-yes anymore. I trust the classifier to catch the thing I'd otherwise be clicking past anyway.

**Where I've automated something to run unattended**, an agent doing a job without me watching every step, the classifier barely enters the picture. There, I rely on guardrails instead: rules I've written up front that say exactly what that agent can and can't touch. If I'm not there to react in the moment, I'm not going to lean on a real-time judgment call. I want the boundary set in advance, in writing, before the agent ever starts.

Active session, trust the classifier. Unattended agent, trust the guardrail you wrote. Two different problems, two different answers, and mixing them up is where I think the fear actually comes from. People imagine turning off manual approval means turning off both. It doesn't. You still get to decide which one applies, and when.

## What two months of this actually looked like

I've been running this way for more than two months now. Not a weekend experiment, real day-to-day work, actively coding, editing, running commands, with connectors wired in and broad permissions granted.

In that time, I haven't hit a single case where the classifier let something misused or wrong actually go through. Not once. Every time it mattered, it caught it. The connector example above wasn't a one-off, it's the pattern: the moment something crosses from "clearly what I asked for" into "acting on my behalf without being told to," it stops and waits for me.

That's the actual data point behind this post. Not a benchmark, not a study. Two months of using it for real, in the exact conditions where a false negative would have actually cost me something, and it hasn't had one yet.

## What makes this different from just turning approvals off

**It isn't "no oversight," it's oversight that doesn't get tired.** A human clicking yes on the fortieth prompt of the day is a worse reviewer than the first prompt of the day, every time. The classifier doesn't have a fortieth prompt problem.

**It defaults to blocking, not allowing, when intent is unclear.** The connector behavior is the clearest example. Broad permissions granted, and it still stops and waits for me to say something explicitly before it acts on my behalf. That's the opposite of what people assume "auto mode" means.

**It's a different tool for a different situation, not a blanket replacement.** Active session versus unattended agent isn't a detail, it's the actual decision that determines whether you should be trusting the classifier or trusting a guardrail you wrote yourself.

**The fear is outdated, not irrational.** It was a reasonable position when the tooling was less mature. Two months of daily use is what changed my mind, not an argument. If you haven't rechecked that assumption recently, it might be worth an afternoon.

## When to lean on the classifier

- You're actively at the keyboard, watching the session, able to react
- You're doing iterative work, edits, tests, commands, that would otherwise mean approving the same categories of action over and over
- You've noticed yourself clicking yes without reading anymore, that's the actual sign the old approval habit stopped protecting you
- You're not comfortable yet: start there anyway, just watch it for a session before deciding

## When to lean on a guardrail instead

- The agent is running unattended, with nobody there to catch a bad call in the moment
- You already know exactly what should and shouldn't be touched, so write it down once instead of trusting a judgment call every time
- The blast radius of a mistake is high enough that you want the boundary fixed in advance, not decided live

## Try this now

Turn off manual approval for one real session. Not a toy example, actual work you're doing today. Watch what the classifier catches and what it lets through. You'll learn more from that one session than from any argument I could make here, mine included.

## Over to you

Are you still doing yes-yes-yes on every prompt, and if so, what's the actual thing you're afraid of? Have you tried auto mode and hit a case where it let something through it shouldn't have, or blocked something you wish it hadn't? I want to hear the real answer, not the cautious one.

If this changed how you think about it, even a little, a like helps more people see it before they write off the idea without testing it.

## Where this fits

If you want the technical breakdown, what exactly the classifier checks, the architecture behind it, the full block and allow lists, that's a separate piece in this series. This one was just the lived version: two months of actually running with it off, and what I'd tell a friend who's still scared to try.

---

## Post assets

| File | Use |
|------|-----|
| [blog-hero.svg](./blog-hero.svg) | Hashnode cover image (SVG, 1600×900) |
| [03-banner-prompt.md](./03-banner-prompt.md) | Prompt to regenerate with Midjourney / DALL·E / Ideogram |
| [02-title-options.md](./02-title-options.md) | All title options — edit frontmatter above to switch |
