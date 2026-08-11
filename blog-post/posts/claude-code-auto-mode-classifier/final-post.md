---
title: 89% vs 13.6%: How Claude Code's New Default Catches What You Miss
tags: claude-code, ai-engineering, developer-tools, security, devops
seo_title: Claude Code Auto Mode Explained: How the Safety Classifier Works
seo_description: Tired of clicking approve on every AI coding prompt? See the study behind Claude Code's new auto mode default and exactly what it blocks.
---

<!-- 
BANNER IMAGE
============
SVG hero (generated): blog-hero.svg — upload this to Hashnode as the cover image.

To generate a higher-res version with an external tool, use the prompt below:

PROMPT:
Editorial illustration for a tech blog, minimal and dark, a single glowing geometric sentinel or watchtower shape positioned above a horizontal stream of small abstract tiles flowing through a narrow gate, some tiles glowing green as they pass through cleanly and one tile glowing red as it is stopped at the gate, faint rows of small dimmed human silhouette icons fading into the background on one side to suggest the old manual process being replaced, deep navy and charcoal background with a single accent color (electric teal or amber) on the sentinel and the gate, abstract and conceptual, not literal software UI, calm and authoritative mood, wide banner format

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

# 89% vs 13.6%: How Claude Code's New Default Catches What You Miss

You know the rhythm. Claude wants to edit a file. A dialog pops up. You hit `y`. Claude wants to run a command. Another dialog. You hit `y` again. Twenty prompts into a session, you're not reading them anymore. You're just mashing the approve key so the tool stops interrupting you.

That reflex has a name now: **permission fatigue**. And Anthropic just shipped data proving it's worse than anyone assumed. Starting **August 14, 2026**, Claude Code flips its default permission mode to `auto` for every new session on Pro, Max, and Team plans. Instead of you reviewing each risky action, a **separate classifier model** reviews it in the background, before it runs.

This post is a complete breakdown of how that classifier actually works: the study that justified the change, the dual-layer architecture underneath it, exactly what gets auto-approved versus blocked, and the guardrails that stop the whole system from going rogue.

---

## 🧠 The problem: humans are bad permission reviewers

Anthropic ran a controlled study with **1,053 paid testers** to measure something nobody likes to admit: how good are people actually at catching a dangerous command hidden in a permission prompt?

The results:

- **Humans caught only 13.6%** of a planted dangerous command when reviewing prompts manually.
- **That catch rate dropped to about 5% after 50 prompts** in a single session. Reviewers don't get more careful with practice. They get worse.
- **The classifier caught 89%** of the same planted command, in the same conditions.

Read that gap again. Not 60% versus 89%. **13.6% versus 89%.** The permission prompt was never really protecting anyone. It was a speed bump that trained people to stop looking.

This is the uncomfortable truth about "ask before every action" security models: they scale the wrong way. The more prompts a session generates, the less attention each one gets, and eventually the human becomes a rubber stamp. You've felt this yourself if you've ever run a long Claude Code session and caught yourself approving things without reading them. That's not a personal failing. That's what permission fatigue does to everyone, measured at 1,053-person scale.

---

## 🔀 The reframe: move the check, don't remove it

The obvious bad fix here would be to just stop asking and hope for the best. That's `bypassPermissions` mode, and Anthropic is explicit that it should only be used in isolated containers with no internet access, never on a real machine with real credentials.

The actual fix is smarter: **keep the safety check, but stop routing it through a fatigued human.** Auto mode replaces "ask a person who's clicked yes forty times already" with "ask a dedicated model whose only job this session is to evaluate one action at a time, with no fatigue and no context-switching cost."

That's the whole idea. Not less oversight. **Differently-shaped oversight** that doesn't degrade with volume.

---

## 🏗️ The dual-layer architecture

Auto mode doesn't replace Claude Code's permission system. It sits on top of it. Every action that Claude wants to take runs through a fixed decision order, and the first layer that matches wins:

1. **Your explicit rules resolve first.** If you've written `allow`, `ask`, or `deny` rules in `settings.json`, those are checked before anything else. Deny beats ask, ask beats allow, and this order holds regardless of how specific each rule is. A broad `Bash(aws *)` deny rule blocks a call even if it also matches a narrower `Bash(aws s3 ls)` allow rule.
2. **Read-only actions and in-directory file edits are auto-approved.** This was already true before auto mode. Reading files, grepping, editing something inside your working directory, none of that needs a human or a classifier, except for a short list of "protected paths" (more on that below).
3. **Everything else goes to the classifier.** This is the new layer. Shell commands, network calls, anything with a side effect outside the safe zone, all of it gets evaluated by a model before it executes.
4. **If the classifier blocks it, Claude gets told and tries something else.** Usually the reason Claude receives is just the fixed string `Blocked by classifier`, not a detailed explanation. Claude adapts its approach from there.

Think of it as **Layer 1: deterministic rules you wrote yourself** (fast, absolute, no model call) and **Layer 2: a probabilistic safety net for the long tail of actions nobody thought to write a rule for.** Most teams will never enumerate every dangerous command in advance. The classifier exists for exactly that gap.

One detail worth sitting with: the classifier **does not see tool results**, only user messages, tool calls, and your CLAUDE.md content. That's a deliberate design choice. If a web page or a file Claude reads contains hidden instructions designed to manipulate an AI reviewer (a classic prompt-injection attack), the classifier never sees that content directly, so it can't be talked into approving something it shouldn't. A separate server-side probe scans incoming tool results for suspicious content before Claude even reads them, adding a second line of defense earlier in the pipeline.

The classifier itself runs on **Claude Sonnet 5 by default**, independent of whatever model you're chatting with in your session. That's intentional too: the reviewer isn't the same model doing the work, and its model choice isn't something a session can quietly influence.

---

## ✅ What gets approved automatically

Here's the part people actually want to know: what runs without asking, once auto mode is on?

- Local file operations inside your working directory
- Installing dependencies already declared in your lockfiles or manifests
- Reading `.env` and sending those credentials to the API they're meant for
- Read-only HTTP requests
- Pushing to any branch of the repository you're already working in, including the default branch (branches that look like deploy targets by name, such as `production` or `gh-pages`, are judged on their own terms instead)
- Messages passed between agents collaborating in the same multi-agent or sub-agent session

Notice the pattern: everything on this list is either read-only, scoped tightly to your existing working directory, or something you'd have approved on reflex anyway. The classifier isn't trying to save you clicks on decisions that matter. It's trying to save you clicks on decisions that never should have needed one.

---

## 🚫 What gets blocked by default

This is the list that actually matters, because it's the list the 13.6%-versus-89% gap was measured against. The classifier is built to catch things like:

- **Downloading and executing code**, the classic `curl | bash` pattern
- **Sending sensitive data to external endpoints**
- **Production deploys and database migrations**
- **Mass deletion on cloud storage**
- **Granting IAM or repo permissions**, or modifying shared infrastructure
- **Irreversibly destroying files that existed before the session started**
- **Force push**
- **`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`**, anything presumed to discard uncommitted work
- **Amending a commit** that wasn't created in the current session, or one that's already been pushed
- **`terraform destroy`, `pulumi destroy`, `cdk destroy`**, and similar infrastructure teardown commands
- **Merging a pull request no human approved**, approving Claude's own PR, or disabling CI checks
- **Writing to a secrets manager**, or changing DNS or TLS records
- **Toggling or deleting a production feature flag**
- **Opening a reverse shell or a tunnel** that exposes a local service to the public internet
- **Printing a live credential or token into the transcript**
- **Routing a package install around an internal registry** to a public one
- **Running a command with a flag that disarms a safety guard**, like `--insecure`
- **`rm -rf /` or `rm -rf ~`**, including disguised forms hidden inside command substitution

Every one of those shares a shape: irreversible, aimed outside the environment you're actually working in, or a bigger action than what you asked for. That's the classifier's actual mandate, stated plainly in Anthropic's own docs: it blocks actions that are "irreversible, destructive, or aimed outside your environment."

### The part that surprised me: plain-English boundaries count

If you tell Claude mid-conversation "don't push yet" or "wait for my review before deploying," the classifier treats that as a binding instruction. It will block a matching action even if the default rules would normally allow it. This isn't a stored rule though. The classifier re-reads your conversation each time it checks, so a boundary you stated three hours ago can quietly disappear if your context gets compacted and that message drops out. If you need a boundary to be permanent, write it as an actual `deny` rule in `settings.json` instead of just saying it in chat.

---

## 🛑 The guardrails on the guardrail

A classifier that's wrong 100% of the time in one direction is still a liability, so Auto Mode ships with mechanisms to stop it from either rubber-stamping everything or locking up on false positives:

- **Three strikes and it pauses.** If the classifier blocks an action **3 times in a row, or 20 times total** in one session, auto mode suspends itself and Claude Code falls back to prompting you manually. These thresholds aren't configurable, on purpose, so nobody can tune them away.
- **It strips your own loaded guns on entry.** The moment auto mode activates, it drops any broad allow rule that would grant arbitrary code execution, things like a blanket `Bash(*)` rule. A narrow rule like `Bash(npm test)` survives fine. This closes an obvious loophole: a pre-existing "yes to everything" rule can't quietly neutralize the classifier just because it was already in your settings file.
- **Sub-agents get checked three separate times.** Before a sub-agent is spawned (the task description itself is evaluated), continuously while it runs (same classifier, same rules as the parent session), and after it finishes (a full-history review that can flag concerns retroactively).
- **It's gated by model and plan.** Auto mode currently requires specific models, Opus 4.6+, Sonnet 4.6+, or Fable 5 on the Anthropic API, narrower still on other providers. Administrators can also disable it org-wide with `permissions.disableAutoMode` in managed settings.

Anthropic is also refreshingly blunt about the limits here: **"Auto mode reduces permission prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations."** That's not marketing copy softened for the changelog. It's a direct statement that 89% is not 100%, and you should still review anything that actually matters.

---

## 🎚️ Where auto mode fits among the other permission modes

Auto isn't the only mode, it's one of six, and knowing where it sits helps you pick the right one for the job:

| Mode | What it does |
|---|---|
| `default` (Manual) | Prompts before every side-effecting action. The old default. |
| `acceptEdits` | Auto-approves file edits and a small set of safe filesystem commands only. |
| `plan` | Claude researches and proposes changes without editing anything. |
| `auto` | The classifier-driven mode this post is about. |
| `dontAsk` | Auto-denies anything not explicitly pre-approved. Built for locked-down CI. |
| `bypassPermissions` | Skips every check. Isolated containers and VMs only, never a real machine with network access. |

If you're doing exploratory work on a codebase you don't fully trust yet, `plan` is still the right call. If you're running Claude Code in CI where nothing should ever improvise, `dontAsk` is the right call. Auto mode is aimed squarely at the middle: long, iterative sessions where you trust the general direction and don't want to babysit every step.

---

## 🧩 A concrete walkthrough

Say you ask Claude Code to fix a failing test suite. In a long session, that task might touch a dozen files, run the test runner repeatedly, install a missing dependency, and eventually commit the fix. Under the old default mode, that's a dozen-plus prompts, most of which are "yes, obviously, keep going."

Under auto mode: the file edits inside your working directory run without a prompt (layer 2 of the architecture above). Installing the missing dependency from your lockfile runs without a prompt. Running the test command goes to the classifier, which recognizes it as a routine, scoped, reversible action and approves it silently. If at some point Claude tries something outside that shape, say, pushing directly to a branch named `production`, or running a command with `--insecure` to get past a TLS error, that's exactly the kind of action the classifier is built to catch and block, even though nothing forced it to ask you first.

You get the dozen or so trivial approvals removed from your day, and the one approval that actually mattered still gets caught. That's the trade the 89%-versus-13.6% number is describing in practice, not just in a lab study.

---

## 🔑 What makes this different from just "turning off prompts"

- **It's not a lower-security mode dressed up as a feature.** `bypassPermissions` already exists for people who genuinely want zero checks, and Anthropic keeps that mode explicitly walled off to isolated environments. Auto mode is a different thing: same checks, different reviewer.
- **The reviewer is architecturally separate from the worker.** The classifier runs on its own model (Sonnet 5 by default) and only sees a filtered view of the conversation, specifically excluding tool results, to resist manipulation from content Claude reads.
- **It degrades gracefully instead of failing open.** Repeated blocks pause the whole mode and fall back to manual prompting rather than silently letting more through.
- **It respects rules you already wrote.** Explicit `ask` and `deny` rules in `settings.json` still force a prompt or a block, even in auto mode. The classifier fills gaps; it doesn't override intent you've already encoded.

---

## 🕐 When to use it

- **Long, iterative sessions** where you'd otherwise be approving the same category of safe action over and over
- **Refactors and test-fixing loops** that touch many files but stay inside your working directory
- **Any workflow where you've noticed yourself approving prompts without reading them.** That's the exact failure mode the study measured, and it's a sign the old mode wasn't protecting you anyway
- **Not** for one-off changes to production infrastructure, secrets, or anything you genuinely need to review line by line before it happens. Use `plan` or manual mode there instead

---

## ⚙️ How to check and configure it

You don't need to install anything new. Auto mode ships inside Claude Code itself.

**Check if it's available to you:** it depends on your plan, your organization's settings, and the model you're running (Opus 4.6+, Sonnet 4.6+, or Fable 5 on the Anthropic API). If Claude Code reports auto mode as unavailable, one of those requirements isn't met.

**Switch to it manually right now, before the August 14 default flip:**

```bash
claude --permission-mode auto
```

**Or press `Shift+Tab`** during a CLI session to cycle through modes once auto mode is enabled for your account.

**Set it as your permanent default** in `~/.claude/settings.json`:

```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

**See exactly what the classifier allows and blocks** by running:

```bash
claude auto-mode defaults
```

This prints the full rule lists as JSON, useful if you want to audit the behavior yourself instead of trusting a blog post's summary of it.

**If your team needs auto mode off entirely**, an administrator sets `permissions.disableAutoMode` to `"disable"` in managed settings. This removes `auto` from the mode cycle and rejects `--permission-mode auto` at startup, so individual developers can't quietly turn it back on.

---

## 🚀 What to do with this right now

If you're on Pro, Max, or Team, this change is arriving whether you opt in or not on August 14. The useful move isn't to panic about it, it's to spend ten minutes before then running `claude auto-mode defaults` and reading the actual block list for your own workflow. If you have infrastructure or commands that don't fit neatly into "reversible and inside my working directory," write explicit `deny` or `ask` rules for them now, rather than trusting the classifier to guess correctly on the first try.

And if you've been the person mashing `y` through forty prompts a session, this is your actual permission to stop. That reflex was never protecting anything. Now something else is.

---

**A question for you:** have you already hit a false positive from auto mode, something safe that got blocked, or something risky that made it through? That's exactly the kind of signal Anthropic wants reported through `/feedback`, and it's also the most useful comment you could leave here. If you're still on manual mode by choice, I'd like to hear why, there are good reasons to stay there for certain workflows, and I don't think auto mode is a universal answer yet.

If this was useful, a like helps more people find it before the August 14 rollout actually lands. Next up in this series: a deeper look at writing your own `allow`/`ask`/`deny` rules so the classifier has less guessing to do in the first place.

---

## Post assets

| File | Use |
|------|-----|
| [blog-hero.svg](./blog-hero.svg) | Hashnode cover image (SVG, 1600×900) |
| [03-banner-prompt.md](./03-banner-prompt.md) | Prompt to regenerate with Midjourney / DALL·E / Ideogram |
| [02-title-options.md](./02-title-options.md) | All title options — edit frontmatter above to switch |
