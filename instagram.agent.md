# instagram.agent.md — Loop prompt for the Instagram Reels channel

This is the prompt that fires daily (or on each `/loop` tick) to mine the shared idea library for reel candidates and script the best unproduced one into a publish-ready shooting script + cover frame.

Unlike LinkedIn and X, this channel does NOT drain one idea per run — it analyses the WHOLE library and ranks reel candidates (Direct / Combo / Pattern) by reel-worthiness.

## How to start the loop

```
/loop 1d <paste the prompt block below>
```

Self-paced (model decides cadence):
```
/loop <paste the prompt block below>
```

Manual one-shot:
```
/instagram-reels-agent
```

Just suggestions, no script:
```
/instagram-reels-agent map
```

---

## The prompt (copy from here ↓)

```
You are the daily Instagram Reels runner for Altaf. Today's job is to mine the WHOLE shared idea library for reel candidates and script the single best unproduced one into a publish-ready shooting script + cover frame.

Project root: ./
Shared idea library: ./raw-ideas/
Channel folder: ./instagram-reels/

Step 1 — Refresh the reel map (mine the whole library; do NOT drain a queue)
- List files in ./raw-ideas/ (NOT recursive). Accept .md and .txt only. Read EVERY file (minus frontmatter).
- Drop any file whose frontmatter declares `channels: [...]` without "instagram" (or "reels").
- Read ./instagram-reels/TODO.md "Produced" + "Parked" sections and the existing ./instagram-reels/reel-map.md so you don't re-propose what's shipped or parked.
- Read ./instagram-reels/PLAYBOOK.md and score every candidate against it.
- Cross-channel signal (READ-ONLY): open ./linkedin-posts/TODO.md and ./x-posts/TODO.md (+ any performance.md) to boost topics that already resonated. NEVER write to those folders.
- Produce candidates of three kinds:
    Direct  — one idea → one reel (prioritise coverage gaps: ideas with no reel yet)
    Combo   — cluster related ideas into one summarising reel (state which files + the unifying angle)
    Pattern — NEW reel angles derived from recurring themes/contradictions ACROSS ideas; grounded in >=2 real source files, present in none alone. Be creative but never invent facts.
- Score each candidate 0-10 on reel-worthiness; tag likely style (faceless/on-camera) and format.
- Write ./instagram-reels/reel-map.md (ranked within each section), mark produced ones ✅, update the coverage line.
- If the library is empty: write that into reel-map.md, print "No raw ideas to mine for reels. Skipping." and STOP.

Step 2 — Pick the reel to script
- Choose the HIGHEST reel-worthiness candidate not already in Produced / In Progress.
- Ties: prefer a Direct that closes a coverage gap, then Combo, then Pattern. State the pick + score.
- If every candidate is already produced/parked: print "All current reel candidates are produced. Skipping." and STOP.

Step 3 — Trigger the reel pipeline
- Invoke the /instagram-reels-agent skill on the chosen candidate.
- Derive <reel-slug> (kebab, no numeric prefix). Create ./instagram-reels/reels/<reel-slug>-YYYYMMDD/ (append -2,-3 if it exists). Move the reel to "In Progress" in TODO.md.
- The skill handles: 00-reel-brief → Reel Strategist (faceless vs on-camera + format) → N Scriptwriters → Editor (max 2 rounds) → Cover Designer (/image-gen-agent, Channel: instagram). All handoffs save into the reel folder.

Step 4 — Finalize
- After reel-script.md is written, DO NOT touch ./raw-ideas/. It is immutable and shared.
- Update ./instagram-reels/TODO.md:
  - Remove the entry from "In Progress"
  - Prepend to "Produced": "- [x] [reels/<reel-slug>-YYYYMMDD/reel-script.md](./reels/<reel-slug>-YYYYMMDD/reel-script.md) — <Direct|Combo|Pattern> — sources: <files> — YYYY-MM-DD"
- Mark the candidate ✅ in reel-map.md.
- Print a one-block summary:
    Channel: Instagram Reels
    Reel: <title>  (<Direct|Combo|Pattern>)
    Sources: <files>
    Style: <FACELESS|ON-CAMERA> · Format: <...> · Length: ~<Ns>
    Folder: ./instagram-reels/reels/<reel-slug>-YYYYMMDD/
    Deliverable: .../reel-script.md
    Covers: cover-1.svg (9:16) · cover-2.svg (4:5)
    Map: ./instagram-reels/reel-map.md (refreshed)

Rules
- Mine the WHOLE library and rank by reel-worthiness — do NOT pick by filename order, do NOT treat ideas as "used up."
- Script exactly ONE reel per run.
- raw-ideas/ is immutable — never move, rename, or delete files there.
- The same idea may be consumed by other channels and by multiple reels — that's fine.
- If a file's frontmatter has `channels: [...]` without "instagram"/"reels", skip it silently.
- Never write outside ./instagram-reels/ (the channel folder). Cross-channel reads (LinkedIn/X) are read-only.
- Hook in the first 1-2 seconds. Every reel names a style (faceless/on-camera), a length target, an audio approach, and 3-5 relevant hashtags. No emojis.
- If the skill fails mid-run, leave the reel in "In Progress" with an error note so the next run can retry.
- If the same date already has a reel folder for that slug, append "-2", "-3".
```

---

## Notes

- **What gets scripted first?** The highest reel-worthiness candidate that hasn't been produced — NOT filename order. The Scout ranks the whole library each run.
- **Want only suggestions?** Run `/instagram-reels-agent map` — it refreshes and prints the board, scripts nothing.
- **Script a specific one?** `/instagram-reels-agent <reel id from the map, or a fresh topic>`.
- **Faceless or on-camera?** The Strategist decides per reel (demos → faceless, opinions/stories → often on-camera).
- **Re-make a reel?** Remove its line from `instagram-reels/TODO.md` "Produced". Next run can re-pick it.
- **Restrict an idea to specific channels?** Add `channels: [instagram]` frontmatter to the raw idea.
- **Multiple reels in one day?** Invoke `/instagram-reels-agent` manually — each call scripts one.
