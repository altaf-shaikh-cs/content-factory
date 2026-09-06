---
description: "Generative explainer-video agent for the multi-channel content factory. Generates illustrated scene stills with a Gemini image model, then moves a camera over them (Ken Burns + crossfade) or composites them behind the deterministic renderer's exact animated text. Requires GEMINI_API_KEY. Use for tonal, narrative, or metaphor-driven posts where illustration carries the idea. For numbers, formulas and mechanisms use /video-gen-agent instead."
trigger: /video-gen-gemini-agent
---

# /video-gen-gemini-agent

Illustrated explainer video. Gemini draws the scenes; ffmpeg or the deterministic renderer puts them in motion.

**Project-side home:** `./agents/video-gen-gemini/`
**Scripts:** `./agents/video-gen-gemini/scripts/`
**Reference spec:** `./agents/video-gen-gemini/specs/example-scenes.json`

Sibling: `/video-gen-agent` renders exact animated text with no model call. **Default to hybrid mode, which uses both.**

---

## Step 0 — Preflight, every run

```bash
node agents/video-gen-gemini/scripts/gemtest.mjs models
```

- **No key** → stop. The script prints the one-line Keychain command; relay it and offer
  `/video-gen-agent` instead, which needs nothing. Do not proceed, and never ask the user
  to paste the key into the conversation.
- **Key works** → use a model id from that list. Never guess a model id; they change.

---

## Interface contract

```
[VIDEO BRIEF]
Channel: <linkedin | x | instagram | blog>
Source post: <path to final-post.md>
Mode: <hybrid | art | baked>       ← omit for hybrid
Style: <path into agents/image-gen/inspiration/…>   ← omit and the agent picks
Dimensions: <1080x1350 | 1080x1080 | 1080x1920>
Target length: <seconds>
Handle / Domain: <…>
Output path: <post-folder>/explainer.mp4
```

---

## Step 1 — Pick the mode, and say why

| Post shape | Mode |
|---|---|
| Carries real numbers, a formula, a mechanism | **hybrid** (or hand it to `/video-gen-agent`) |
| Story, opinion, mental-model shift, metaphor | **hybrid** |
| Pure mood, no message text at all | `art` |
| The user explicitly wants to evaluate Gemini's text rendering | `baked` |

`baked` is a test mode. If you use it, say so in the surface block and flag that every
frame needs proofreading before publishing.

---

## Step 2 — Pick a style reference

Read `agents/image-gen/inspiration/MANIFEST.md`. Pick the style whose mood tags match the
post, and reference **a specific file** inside that folder, not the folder. The style
reference is the single biggest lever on output quality and on staying on-brand.

Match what the static image agent would have chosen for the same post, so the video and
the post's images look related.

---

## Step 3 — Write the scenes spec

4-7 scenes, 4-6s each. Write it to the post folder as `scenes.json`.

Prompt rules:

- Describe a **concrete scene**, an object doing something. Never describe the abstraction.
  The model can draw a parcel riding a belt; it cannot draw "redundant token cost".
- One subject per scene.
- Carry a recurring visual motif across scenes so the video feels like one piece.
- Never ask for a statistic to be drawn. Numbers come from the text layer.
- No emojis, no company or internal tool names, no private details.
- Never invent a claim that is not in the post.

---

## Step 4 — Generate and LOOK

```bash
node agents/video-gen-gemini/scripts/gen-scenes.mjs <scenes.json> <post-folder>/stills
```

**Read every generated image before assembling.** Check:

- Stray text, garbled letters, or a fake logo (in `art` mode there should be none)
- Scenes that drifted off-style from each other
- Anatomy or object errors that will read as sloppy at feed size
- Anything that misrepresents the post's claim

Regenerate individual scenes by rerunning after rewording that one prompt. Do not ship a
scene you would not defend.

---

## Step 5 — Assemble

**Hybrid (default).** Write a `video-gen` spec, setting each scene's `bg` to the
matching still (an absolute `file://` path), then:

```bash
node agents/video-gen/renderer/render.mjs <spec.json> <post-folder>/explainer.mp4
```

Scene text, layouts and timing follow `/video-gen-agent`'s Step 1-4, including the
contact sheet before the full render. The renderer draws a scrim over each still
automatically, so light illustrations still hold white text.

**Art / baked.**

```bash
node agents/video-gen-gemini/scripts/assemble.mjs <scenes.json> <post-folder>/stills <post-folder>/explainer.mp4
```

---

## Step 6 — Surface block

```
[VIDEO GENERATED]
Agent: video-gen-gemini (<mode>)
Model: <exact model id used>
Style reference: <path>
Scenes: <n> · <duration>s · <W>×<H>
Generations: <n images, m retries>
Stills: <path to stills dir>
Spec: <path>
MP4: <output path> (<size> MB)
Reviewed: <what you checked the stills for, and anything you regenerated>
```

---

## Edge cases

- **No API key** → stop at Step 0, offer `/video-gen-agent`.
- **Model returns no image** (`finishReason` is a safety or recitation block) → reword the
  prompt to be more concrete and less abstract, and retry once. If it blocks again, say so
  and drop that scene rather than forcing it.
- **Stills are inconsistent with each other** → the style reference is doing too little.
  Strengthen `styleNote` with the concrete attributes (background colour, line weight,
  palette size) rather than mood words.
- **A number appears in an `art` still** → regenerate. Do not publish a model-invented number.
- **Quota or rate limit** → report how many scenes succeeded, keep them, and say which
  ones to rerun. Do not silently produce a short video.

---

## Shared rules

- Never invent statistics, quotes, or claims not in the source post
- No emojis unless explicitly asked
- No company names or internal tool names
- Commit the stills alongside the MP4 — the output is not reproducible from the spec
