# `runs/` — the factory heartbeat

**Every channel agent writes one line here on every run, including runs that produce nothing.**

## Why this exists

Channel agents exit quietly when there is nothing to do. A quiet exit is byte-identical to a routine that never fired, crashed, or was never created. That ambiguity is not theoretical: between 2026-06-30 and 2026-08-15 the X and Instagram channels produced nothing and opened zero PRs, while `CLAUDE.md` still advertised them as running daily. Nobody noticed for seven weeks.

A run log removes the ambiguity. "Ran and had nothing to do" and "did not run" now look different on disk.

## The contract

One file per channel: `runs/<channel>.md`, where `<channel>` is `linkedin` | `x` | `instagram` | `blog`.

Each file is an **append-only** markdown table. Newest row at the bottom. A channel agent writes ONLY its own file, so concurrent routines can never conflict.

| Column | Meaning |
|---|---|
| `Date` | UTC date of the run, `YYYY-MM-DD` |
| `Outcome` | one of `produced` · `skipped` · `blocked` · `error` |
| `Detail` | one short line, why this outcome. No trailing period |
| `Output` | link to the post/reel folder, or `—` |

### Outcome vocabulary

| Outcome | When |
|---|---|
| `produced` | The run generated content and opened a PR |
| `skipped` | The run worked correctly and decided there was nothing to make (empty queue, every candidate already in flight, fit gate said no) |
| `blocked` | A gate stopped generation on purpose. Today the only one is the LinkedIn ship gate (unshipped inventory at or above threshold) |
| `error` | The run failed. Put the failure in `Detail` |

`skipped` is a healthy outcome. `blocked` is a healthy outcome. Absence of any row is the unhealthy one.

## When and how to write the row

Writing the row is the **last action of every run**, before the agent reports back. It happens on all paths, including early exits.

**If the run produced content** (there is already a `claude/<channel>-<slug>` branch and a PR):
include the run-log row in that same branch and commit. No extra push.

**If the run produced nothing** (`skipped`, `blocked`, or a recoverable `error`, so no branch and no PR):
commit just this one line and push it straight to the fork's `main`.

```bash
git add runs/<channel>.md
git commit -m "runs: <channel> <YYYY-MM-DD> <outcome>"
git pull --rebase origin main && git push origin main
```

This is the **one and only** exception to "never push to main directly." It is safe because the change is a single appended line in a file that exactly one agent writes, and `--rebase` absorbs any interleaving. It must never carry any other file. If the push fails, report the failure and move on. A missing heartbeat row is a nuisance; a routine that dies trying to write one is worse.

## Who reads it

`/factory-health` (see `.claude/skills/factory-health/SKILL.md`) reads every file here weekly and reports channels that have gone dark. It distinguishes:

- **No row in > 2 days** → the routine is broken, disabled, or was never created. Check https://claude.ai/code/routines
- **Rows present but no `produced` in > 14 days** → the routine is alive and the channel is starved or gated. Check the queue and the ship gate

## What this is not

Not state. The queue, the ledger, and what has been consumed still live in each channel's `TODO.md`, which stays the source of truth. This is an append-only log of agent activity and nothing reads it to make a production decision.
