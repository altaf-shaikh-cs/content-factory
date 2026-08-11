# Claude Code's Auto Mode: How the Safety Classifier Replaces Permission Prompts

## Context

Anthropic is rolling out a major default-behavior change to Claude Code: starting **August 14, 2026**, `auto` becomes the default permission mode for new sessions on Pro, Max, and Team plans (announced August 7, 2026; widely covered by 9to5Mac, The Register, Help Net Security, and others). This replaces the old pattern of Claude stopping and asking "yes/no/yes don't ask again" before every file edit, shell command, or network call.

## The core problem: permission fatigue

Claude Code's classic permission system prompts before file edits, most Bash commands, and other side-effecting actions. Anthropic ran a study of 1,053 paid testers measuring how well humans actually catch dangerous commands when reviewing these prompts manually:

- **Humans caught only 13.6%** of a planted dangerous command when reviewing permission prompts manually.
- **Human catch rate fell to about 5% after 50 prompts** in a session — i.e., reviewers get worse, not better, as fatigue sets in.
- **Auto mode's classifier caught 89%** of the same planted dangerous command in the same study.

This is the "permission fatigue" problem: the more prompts a human has to click through, the less signal each one carries, and eventually people rubber-stamp everything just to keep working.

## What Auto Mode actually is

Auto mode doesn't remove safety checks — it moves them from a human clicking "yes" to a **separate classifier model** that reviews each action before it runs.

- The classifier runs on **Claude Sonnet 5 by default** (not whatever model you're chatting with), unless Anthropic configures a different server-side model, or your session model is Sonnet 4.6 / uses Fable 5, in which case it falls back accordingly.
- It sees **user messages, tool calls, and CLAUDE.md content** — but tool *results* are stripped from what it reviews, specifically so that hostile content embedded in a file or web page (prompt injection) can't manipulate the classifier directly. A separate server-side probe scans incoming tool results for suspicious content before Claude even reads them.
- It blocks actions that are **irreversible, destructive, or aimed outside your environment**, or that escalate beyond what you asked for.
- Explicit `ask` permission rules still force a manual prompt even in auto mode — the classifier doesn't override rules you've set.

## The "dual-layer" architecture (rules + classifier)

Auto mode sits on top of Claude Code's existing tiered permission system, not instead of it. The evaluation order for any action is:

1. **Your explicit allow/ask/deny rules** (in `settings.json`) resolve first. Deny beats ask beats allow, and rule specificity doesn't matter — a broad `Bash(aws *)` deny blocks a narrower `Bash(aws s3 ls)` allow.
2. **Read-only actions and file edits inside your working directory** are auto-approved (except writes to a small set of "protected paths" like `.git`, `.claude`, `.ssh`-adjacent config, shell rc files — those always route to the classifier or a prompt, even in auto mode).
3. **Everything else goes to the classifier** — this is Layer 2, the "background safety check."
4. **If the classifier blocks**, Claude gets the reason (usually just the fixed string "Blocked by classifier" rather than a detailed explanation) and tries an alternative approach.

So: Layer 1 is deterministic, user-authored rules (fast, no model call, absolute). Layer 2 is a probabilistic safety net for the long tail of actions nobody wrote a rule for.

## What's blocked by default (the classifier's judgment calls)

Concrete categories the classifier is designed to block without being told, drawn directly from Claude Code's documentation:

- Downloading and executing code (`curl | bash`)
- Sending sensitive data to external endpoints
- Production deploys and database migrations
- Mass deletion on cloud storage
- Granting IAM or repo permissions; modifying shared infrastructure
- Irreversibly destroying files that existed before the session started
- Force push
- `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop` (anything presumed to discard uncommitted work)
- Amending a commit that wasn't created in the current session, or that's already been pushed
- `terraform destroy` / `pulumi destroy` / `cdk destroy` and similar infra-teardown commands
- Merging a PR no human approved, approving Claude's own PR, or disabling CI checks
- Writing to a secrets manager, or changing DNS/TLS records
- Toggling or deleting a production feature flag
- Opening a reverse shell or a tunnel exposing a local service to the internet
- Printing a live credential or token into the transcript
- Routing a package install around an internal registry to a public one
- Running a command with a flag that disarms a safety guard (e.g. `--insecure`)
- `rm -rf /` or `rm -rf ~` (and their command-substitution disguised forms) — routed to the classifier as of recent versions, previously always a hard prompt

Notably, the classifier also treats **plain-English boundaries stated in conversation** as binding: if you tell Claude "don't push" or "wait for my review before deploying," it will block matching actions even if the default rules would normally allow them. That boundary isn't stored as a rule though — it's re-read from the transcript each time, so it can be lost if context gets compacted out.

## What's allowed by default (no prompt, no classifier round-trip)

- Local file operations inside the working directory
- Installing dependencies already declared in lockfiles/manifests
- Reading `.env` and sending those credentials to their matching API
- Read-only HTTP requests
- Pushing to any branch of the repo you're already working in, including the default branch (some exceptions for branches that look like deploy targets, e.g. `production` or `gh-pages`)
- Messages between agents collaborating in the same multi-agent/sub-agent session

## Guardrails on auto mode itself

- If the classifier blocks an action **3 times in a row, or 20 times total** in a session, auto mode pauses itself and Claude Code falls back to manual prompting. These thresholds aren't configurable.
- Entering auto mode **drops broad allow rules that grant arbitrary code execution** — e.g. a blanket `Bash(*)` — specifically so a pre-existing "yes to everything" rule can't neutralize the classifier. Narrow rules like `Bash(npm test)` still carry over.
- Sub-agents get checked at three separate points: before they're spawned (task description is evaluated), continuously while they run (their actions go through the same classifier), and after they finish (a full-history review that can prepend a security warning to their results if something looks off).
- Auto mode requires specific models (Opus 4.6+, Sonnet 4.6+, or Fable 5 on the Anthropic API — narrower still on Bedrock/Vertex/Foundry) and can be disabled org-wide by administrators via `permissions.disableAutoMode` in managed settings.
- Anthropic is explicit that this is risk-reduction, not risk-elimination: "Auto mode reduces permission prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations."

## Other permission modes for context

Auto mode is one of six: `default`/Manual (prompts on everything), `acceptEdits` (auto-approves file edits + safe filesystem commands only), `plan` (research/propose without editing), `auto` (the classifier-driven mode above), `dontAsk` (auto-denies anything not pre-approved — for locked-down CI), and `bypassPermissions` (skips all checks — isolated containers/VMs only, explicitly warned against for anything with internet access).

## Sources

- [Choose a permission mode — Claude Code Docs](https://code.claude.com/docs/en/permission-modes)
- [Configure permissions — Claude Code Docs](https://code.claude.com/docs/en/permissions)
- [PSA: Claude Code enabling auto mode as default next week — 9to5Mac](https://9to5mac.com/2026/08/07/psa-claude-code-enabling-auto-mode-as-default-next-week-anthropic-says/)
- [Claude Code puts auto mode in the driver's seat — The Register](https://www.theregister.com/ai-and-ml/2026/08/10/claude-code-puts-auto-mode-in-the-drivers-seat/5285326)
- [Anthropic to put AI in charge of reviewing Claude Code actions by default — Help Net Security](https://www.helpnetsecurity.com/2026/08/10/anthropic-claude-code-auto-mode/)
- [Claude Auto Mode: 89% vs 13.6% Human Catch Rate — explainx.ai](https://explainx.ai/blog/claude-code-auto-mode-default-pro-max-team-august-2026)

## Angle note for channels

This is timely (rollout is 3 days out from today) and technical enough for a developer/DevOps audience. Good fit for blog (deep dive on the dual-layer architecture + what's allowed/blocked) and LinkedIn/X (the 89% vs 13.6% stat is a strong hook on its own). Strip nothing here — this is public Anthropic product documentation, not an internal tool or company detail.
