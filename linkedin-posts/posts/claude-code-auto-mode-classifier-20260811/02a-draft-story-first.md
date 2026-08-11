[HANDOFF: COPYWRITER — Story-first]

By prompt 50, you catch 5% of dangerous commands.

Not because you're careless.
Because that's how attention works.

Anthropic ran a study of 1,053 paid testers. They measured how often people actually catch a dangerous command embedded in Claude Code's permission prompts.

Humans caught it 13.6% of the time at the start of a session.
By prompt 50: 5%.

The reviewers got worse as the session went on. Not because they were careless — because fatigue is structural, not personal.

Starting August 14, 2026, auto mode becomes the default for Claude Code on Pro, Max, and Team plans.

The permission prompt isn't removed.
The human clicking "yes" is replaced by a classifier.

A dedicated model (Sonnet 5 by default) reviews every action before it runs.
The same study: 89% catch rate on the same planted dangerous command.

Not fewer checks. A different reviewer.

The classifier sees your messages, tool calls, and CLAUDE.md. Tool results are stripped from what it reads — so injected content in a file or webpage can't manipulate it directly.

Two things still apply:
Your explicit allow/deny rules in settings.json run first. Deterministic. Absolute.
Everything you didn't write a rule for goes to the classifier.

What it blocks without being asked: curl | bash, production deploys, force-push, terraform destroy, IAM changes, live credentials in the transcript, hard resets on uncommitted work.

What's allowed without a prompt: local file ops, installing from your lockfile, pushing to the repo you're working in, read-only HTTP.

If the classifier blocks something 3 times in a row or 20 times in a session, auto mode pauses and manual prompting resumes.

89% vs 13.6%.

What's the one action you'd want to keep under manual review even in auto mode?

---
Angle: Story-first
Hook: By prompt 50, you catch 5% of dangerous commands.
Word count: 238
