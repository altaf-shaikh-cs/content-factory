[HANDOFF: COPYWRITER — Bold claim-first]

Anthropic just put an AI in charge of reviewing Claude Code's actions.

The data says humans were doing it badly.

In a study of 1,053 paid testers: humans caught only 13.6% of a planted dangerous command when reviewing permission prompts. By prompt 50 in a session, that fell to 5%.

The classifier that replaces them: 89%.

Starting August 14, 2026, auto mode becomes the default on Pro, Max, and Team plans.

The review doesn't go away. The reviewer changes.

A dedicated Sonnet 5 model runs before every action executes. It sees your conversation, your tool calls, your CLAUDE.md. Not your tool results — those are stripped so content injected into a file can't reach the classifier directly.

Two layers, evaluated in order:
1. Your explicit allow/deny rules in settings.json. Deterministic. First. Absolute.
2. The classifier. Covers everything you didn't write a rule for.

What it blocks by default: curl | bash, production deploys, force-push, terraform destroy, IAM changes, printing live credentials, hard resets on uncommitted work.

What it allows without a prompt: local file operations, installing from your lockfile, pushing to the repo you're working in, read-only HTTP requests.

Explicit "ask" rules you've written still force a manual prompt in auto mode. The classifier doesn't override your rules.

If the classifier blocks 20 times in a session or 3 in a row, auto mode pauses and falls back to manual prompting.

One consistent AI reviewer doing 89%. 1,053 humans averaging 13.6%.

What's the one action you'd want to keep under manual review even in auto mode?

---
Angle: Bold claim-first
Hook: Anthropic just put an AI in charge of reviewing Claude Code's actions.
Word count: 240
