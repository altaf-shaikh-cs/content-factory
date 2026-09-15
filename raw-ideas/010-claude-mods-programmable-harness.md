# Claude Mods, the Tetris proof, and the 23-day churn post

Captured 2026-09-15 from the X trending page "Claude Code Launches Mods for Cust..."
Source is a single screenshot: two posts stacked, both roughly 23 hours old.

## Post 1 — Boris Cherny (@bcherny)

> Claude Mods are landing now. Someone already built a Tetris-in-Claude mod
> See issue for the latest community update, technical details, and more cool demos

Links to github.com/anthropics/cla... (truncated in capture).

Engagement at capture: 274 replies · 254 reposts · 2.5K likes · 508K views.

### The embedded screenshot of the mod source

A file listing of the arcade mod:

- `snake.ts` — steer a growing snake eating food (+1 each); hitting a wall or your own body ends it, filling the board also ends it
- `tetris.ts` — drop the seven tetrominoes, rotate and shift them to fill rows; full rows clear for 100/300/500/800 points, gravity speeds up every 10 lines, hard drops add 2 points per row, game ends when a new piece can't spawn
- `twenty48.ts` — slide a 4x4 grid in one of four directions; equal neighbours merge once per move for points, a new 2 (90%) or 4 appears after any move that changed something, 2048 wins, no legal move loses
- `mines.ts` — reveal tiles on a minefield where the first click is always safe and zeroes flood-open their area; flag suspected mines, hit one and you lose, open every safe tile and you win
- `flappy.ts` — flap a bird against constant gravity through gaps in scrolling pipes (gap = a third of the board height), scoring 1 per pipe passed; the ceiling just stops you, the floor or a pipe ends the run
- `invaders.ts` — move a ship along the bottom row and fire one shot at a time at an 8x3 alien formation that steps sideways and drops a row at the edges; aliens are 10 points each, their bombs cost one of 3 lives, a cleared wave respawns lower and faster
- `pong.ts` — volley the ball past a CPU paddle that tracks it at 0.6 rows/tick; where the ball hits your paddle sets its angle, first side to 5 points wins
- `typing.ts` — retype one randomly chosen code or prose line exactly; wrong characters count as errors until backspaced, scored on WPM (5 chars = a word) plus accuracy

**Shared logic (not games):**

- `pet.ts` — a virtual pet fed by your actual work: passing tests/commits/edits grant XP and mood, failing tests cost mood, idling drains it; level = sqrt(xp/10), advancing egg -> baby -> kid -> adult -> legend
- `auto.ts` — picker for `/arcade random` and `/arcade auto`: recent test failure -> pet, long running turn -> a longer game, short turn -> a quick one, idle -> a put-down-anytime game, always avoiding a repeat of the last game
- `best.ts` — high-score rule: lower wins for Minesweeper (fastest clear), higher elsewhere, and scores <= 0 never count

Terminal strip visible in the capture, with Tetris running live above the prompt:

```
Claude is done · tetris · paused · score 48 · p resumes · best 74
Crunched for 27s · done 5:53 PM
manual mode on · ? for shortcuts
```

## Post 2 — Yuchen Jin (@Yuchenj_UW), directly below

> It's been 23 days since I last opened Claude Code.
>
> It used to be one of my favorite products, but I think I prefer Codex now.
>
> Codex just works better with OSS models. And among OSS models, Kimi K3 is still unbeatable at coding.

## Verified context (web, 2026-09-15)

- Claude Mods are discoverable, shareable, installable modifications to Claude Code: skills, MCP servers, agents, harnesses.
- The arcade mod is `github.com/sezaakgun/cc-arcade`. Eight games run in the strip above the prompt while Claude works. **Playing costs no tokens: the plugin answers every click and command itself.**

## Why this is worth a post

The two posts look like opposites and are the same observation. Neither is an argument
about model quality.

- The leaver is leaving over the harness: which models it will run, how it fits his setup.
- The builder stayed because the harness became programmable, and used it to ship a game engine on day one.

The model is the commodity. The harness is the product, and it is the only part a user
can change.

The transferable engineering point, and the reason the zero-token detail matters: a falling
block is deterministic code and never needed a model. Every piece of work you can move out
of the model call and into ordinary code gets faster, cheaper and exact. Most teams are
still choosing a model; fewer are asking how much of the product needs one at all.

First-person anchor available: the same call was already made in this content pipeline,
where the video step is deterministic code rather than a generative model, because a model
cannot reliably spell a statistic and the statistic is the whole point of the video.
