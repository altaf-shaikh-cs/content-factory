# CLAUDE.md — Instagram Reels channel

Briefs any Claude session that opens work inside `./instagram-reels/`. Read this AND the [parent CLAUDE.md](../CLAUDE.md) before acting.

---

## What this folder is

The Instagram Reels channel of the multi-channel content factory. It consumes ideas from `../raw-ideas/` (shared, immutable) and produces **reel suggestions + publish-ready shooting scripts + cover frames** here.

Channel overview: [`README.md`](./README.md).
Craft baseline: [`PLAYBOOK.md`](./PLAYBOOK.md) — Reels best-practices, read every run (this channel's substitute for an analytics loop).
Living menu of reel ideas: [`reel-map.md`](./reel-map.md).
Loop prompt: [`../instagram.agent.md`](../instagram.agent.md).
Full skill: `.claude/skills/instagram-reels-agent/SKILL.md`.

---

## The one thing that makes this channel different

**Instagram does NOT drain one idea per run like LinkedIn and X do.** It **mines the whole library** and proposes reels of three kinds:

- **Direct** — 1 raw idea → 1 reel.
- **Combo** — several related ideas summarised into one reel.
- **Pattern** — a NEW reel angle derived from patterns ACROSS ideas (grounded in ≥2 source files, present in none alone).

Because one idea can fuel many reels and a reel can use many ideas, **ideas are never "used up."** There is no subtractive queue. We track **produced reels** (each listing its source ideas) and **coverage** instead.

---

## Hard rules (Instagram-specific)

1. **`../raw-ideas/` is read-only here.** Never move, rename, or delete files there. Shared with other channels.
2. **All WRITES stay inside `./instagram-reels/`.** **Read-only access to `../linkedin-posts/` and `../x-posts/` is allowed** for cross-channel signal (what topics resonated) — never write there.
3. **Mine the whole library; don't drain a queue.** Selection is by **reel-worthiness score** in `reel-map.md`, not filename order.
4. **Hook lands in the first 1-2 seconds.** No "hey guys", no logo intro, no slow build. On-screen text + spoken line + a visual.
5. **Every reel names a STYLE** — `FACELESS` (text + VO + B-roll) or `ON-CAMERA` (talking head). The Strategist decides per reel.
6. **Every reel is a timed shooting script** — beats with timestamp, on-screen text, spoken/VO line, and visual cue. Not a paragraph.
7. **Length serves retention.** 7-15s for reach, 20-40s talking-head, up to ~90s tutorial. State the target.
8. **3-5 relevant hashtags** in the caption — niche over broad. Never spammy. (IG differs from X here — tags aid discovery.)
9. **Name an audio approach** — trending-audio (reach) vs original voiceover (evergreen).
10. **Never invent statistics, quotes, or claims** not in the source idea(s). Pattern reels must be grounded in real source files.
11. **Strip company names, internal tool names, private details.** Keep the lesson.
12. **CTA must be public-shareable.** No "DM me to try the internal tool". Prefer follow/save/comment reasons.
13. **One reel scripted per production run.** The map can list many; script exactly one.
14. **Every handoff is BOTH printed AND saved** to the per-reel folder. Never one without the other.
15. **No emojis** unless the user explicitly asks. (Hashtags are allowed; emojis are not.)
16. **Respect `channels:` frontmatter.** If a raw idea declares `channels: [...]` without `instagram` (or `reels`), skip it silently.

---

## Decision shortcuts

| User says...                                          | Do this                                                                 |
|-------------------------------------------------------|-------------------------------------------------------------------------|
| "suggest reels" / "what reels can I make"             | Trigger `instagram-reels-agent` in **map-only** mode (refresh `reel-map.md`, print it). |
| "process my reels" / "/instagram-reels-agent"         | Trigger the skill in **map + script** mode (refresh map, script top pick). |
| "script a reel about X" / "/instagram-reels-agent X"  | Trigger the skill in **Mode C** (script that candidate / topic).        |
| "run the loop" inside this folder                     | Use `../instagram.agent.md` prompt.                                      |
| Drops a new file in `../raw-ideas/`                   | "Queued for the next map refresh — or run `/instagram-reels-agent` now." |
| Edit a shipped reel script                            | Edit `reels/<reel-slug>-<date>/reel-script.md` directly. Don't re-run the pipeline unless asked. |
| Re-make a reel                                        | Remove its line from `TODO.md` Produced. Then trigger the skill.        |
| "why didn't you suggest X?"                           | Check `reel-map.md` Coverage gaps / Parked in `TODO.md`.                |
| `../raw-ideas/` empty                                 | Print "No raw ideas to mine for reels." Stop.                          |
| "what are the rules?" / "Reels best practices"        | Read / update [`PLAYBOOK.md`](./PLAYBOOK.md).                          |

---

## Pipeline contract (quick reference)

```
[refresh reel-map over the WHOLE library]   → reel-map.md  (Scout/Pattern-Miner; reads LinkedIn+X signal read-only)
     map-only mode → stop here (print the board)
     map+script    → pick top unproduced candidate ↓

00-reel-brief.md      ← chosen candidate + type + source idea list + cross-channel signal
  → Reel Strategist            → 01-reel-plan.md  (STYLE faceless|on-camera · FORMAT · beats · angles)
  → Scriptwriters × N parallel → 02a-script-demo, 02b-script-hottake, 02c-script-story
  → Editor                     → 03-editor-verdict.json  (hard-fails weak hook / no payoff / non-shareable CTA)
  → [revision loop, max 2 rounds]
  → Cover Designer (/image-gen-agent) → cover-1.svg (9:16) + cover-2.svg (4:5)
                                      → exports/cover-1.png + cover-2.png
  → reel-script.md   ← THE DELIVERABLE
  → TODO.md: In Progress → Produced (list sources); refresh reel-map coverage
```

**Default N=3 scriptwriter angles:** Demo/how-to · Hot-take/POV · Story/build-in-public. Override with `/instagram-reels-agent 2` to drop the story angle.

---

## Image defaults (Instagram)

- **Cover frames:** 2 per reel — `cover-1.svg` (1080×1920, 9:16 reel cover) and `cover-2.svg` (1080×1350, 4:5 grid-safe). Different style each.
- **PNGs:** auto-converted into `exports/`.
- **No emojis, no logos, no company names** unless explicitly requested.

---

## When to push back

- Asked to add stats not in the source idea → ask for the source.
- Asked to ship a reel with no clear payoff or a 5-second intro before the hook → refuse, fix the hook.
- Asked to spam 15+ hashtags → push back, 3-5 relevant tags.
- Asked to skip the Editor → push back, it catches weak hooks and missing payoffs.
- Asked to move a file out of `../raw-ideas/` → refuse, shared and immutable.
- Asked to write into another channel's folder → refuse, read-only across channels.

---

## What NOT to do

- Don't drain ideas one-by-one in filename order — this channel mines the whole library and ranks by reel-worthiness.
- Don't treat an idea as "used up" after one reel — it can fuel a Direct AND a Combo AND a Pattern reel.
- Don't write into `../raw-ideas/` (except Mode C may add ONE new file for an ad-hoc topic).
- Don't write outside `./instagram-reels/`.
- Don't auto-commit or auto-push.
- Don't fold Instagram into another channel's folder.
