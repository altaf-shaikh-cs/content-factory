#!/usr/bin/env python3
"""
Builds the 8-slide LinkedIn document carousel for the five-rung-ai-automation-ladder post.

Style: blend of `diagram-explainer` (layout structure, pastel blocks, annotation callouts)
and `bold-editorial-type` (cream ground, giant bold type, orange/blue accents, mono captions,
hairline footer with signature dots).

Outputs slide-1.svg .. slide-8.svg into the post folder.
"""
import os

W, H = 1080, 1350
M = 88                      # outer margin
RIGHT = W - M               # 992
COL = RIGHT - M             # 904 usable width

# --- palette (from bold-editorial-type sample) ---
CREAM   = "#EDEAE3"
CREAM_2 = "#E4E0D6"
INK     = "#1A1A18"
ORANGE  = "#E14B16"
BLUE    = "#1668D6"
GREY    = "#8A8578"
HAIR    = "#D2CEC4"
PEACH   = "#F6C9A8"

# pastel block fills (from diagram-explainer sample)
PASTELS = ["#DDD9CF", "#C3D8EF", "#C9DCC2", "#F6D6B8", "#D5C4EC"]

SANS = "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', Menlo, 'DejaVu Sans Mono', monospace"

TAGLINE = ["A rung only holds if the", "one below it is reliable."]


def esc(s):
    """Escape for XML and normalise typography to entities."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("'", "&#8217;").replace("·", "&#183;")
    s = s.replace("->", "&#8594;").replace("→", "&#8594;")
    return s


def txt(x, y, s, size=30, weight=400, fill=INK, font=SANS, anchor="start", ls=None, op=None):
    a = [f'x="{x}"', f'y="{y}"', f'font-family="{font}"', f'font-size="{size}"',
         f'font-weight="{weight}"', f'fill="{fill}"']
    if anchor != "start":
        a.append(f'text-anchor="{anchor}"')
    if ls is not None:
        a.append(f'letter-spacing="{ls}"')
    if op is not None:
        a.append(f'opacity="{op}"')
    return f'  <text {" ".join(a)}>{esc(s)}</text>'


def rect(x, y, w, h, fill, r=0, op=None, stroke=None, sw=None):
    a = [f'x="{x}"', f'y="{y}"', f'width="{w}"', f'height="{h}"', f'fill="{fill}"']
    if r:
        a.append(f'rx="{r}"')
    if op is not None:
        a.append(f'opacity="{op}"')
    if stroke:
        a += [f'stroke="{stroke}"', f'stroke-width="{sw or 2}"']
    return f'  <rect {" ".join(a)}/>'


def line(x1, y1, x2, y2, stroke=HAIR, sw=2, op=None):
    a = [f'x1="{x1}"', f'y1="{y1}"', f'x2="{x2}"', f'y2="{y2}"',
         f'stroke="{stroke}"', f'stroke-width="{sw}"']
    if op is not None:
        a.append(f'opacity="{op}"')
    return f'  <line {" ".join(a)}/>'


def eyebrow(label, y=148):
    """Short rule + spaced mono caps label, as in the inspiration sample."""
    return [line(M, y - 10, M + 46, y - 10, GREY, 3),
            txt(M + 66, y, label.upper(), size=23, weight=700, fill=GREY, font=MONO, ls=6)]


def slide_no(n):
    return [txt(RIGHT, 148, f"{n} / 8", size=22, weight=400, fill=GREY, font=MONO, anchor="end")]


def footer():
    """Hairline, byline left, prominent handle + tagline right, signature dots."""
    y = 1196
    o = [line(M, y, RIGHT, y, HAIR, 2)]
    o += [txt(M, y + 52, "Altaf Shaikh", size=27, weight=700, fill=INK)]
    o += [txt(M, y + 86, "// AI Engineering", size=20, weight=400, fill=GREY, font=MONO)]
    o += [txt(RIGHT - 46, y + 48, "@teachmebro", size=30, weight=700, fill=ORANGE,
              font=MONO, anchor="end")]
    o += [txt(RIGHT - 46, y + 82, TAGLINE[0], size=18, weight=400, fill=GREY,
              font=MONO, anchor="end")]
    o += [txt(RIGHT - 46, y + 106, TAGLINE[1], size=18, weight=400, fill=GREY,
              font=MONO, anchor="end")]
    o += [f'  <circle cx="{RIGHT - 26}" cy="{y + 40}" r="11" fill="{ORANGE}"/>',
          f'  <circle cx="{RIGHT - 2}" cy="{y + 40}" r="11" fill="{BLUE}"/>']
    return o


def frame(body, n):
    """Assemble a full slide."""
    head = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
            '  <defs>',
            f'    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">',
            f'      <stop offset="0%" stop-color="{CREAM}"/>',
            f'      <stop offset="100%" stop-color="{CREAM_2}"/>',
            '    </linearGradient>',
            '  </defs>',
            f'  <rect width="{W}" height="{H}" fill="url(#ground)"/>']
    return "\n".join(head + slide_no(n) + body + footer() + ['</svg>', ''])


# ---------------------------------------------------------------- slide 1: hook
def slide1():
    b = eyebrow("the five-rung ladder")
    y = 330
    for ln in ["Your AI", "automation", "didn't fail."]:
        b.append(txt(M, y, ln, size=104, weight=900, fill=INK))
        y += 122
    # highlighter swipe behind the turn, as in the sample's "Harness."
    b.append(rect(M - 10, 748, 700, 74, PEACH, r=4, op=0.95))
    b.append(txt(M, 806, "You skipped a rung.", size=72, weight=900, fill=INK))
    b.append(rect(M, 892, 6, 96, ORANGE, r=3))
    b.append(txt(M + 34, 934, "Five rungs. Most people jump.", size=34, weight=400, fill=INK))
    b.append(txt(M + 34, 976, "The rung you skipped is the work you kept.", size=34, weight=400, fill=INK))
    b.append(txt(M, 1080, "prompt  ·  skill  ·  loop  ·  routine  ·  agent team",
                 size=22, weight=700, fill=GREY, font=MONO, ls=2))
    # sparse constellation in the negative space, top right
    pts = [(742, 300), (860, 246), (952, 322), (884, 404), (790, 386)]
    for i in range(len(pts) - 1):
        b.append(line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], GREY, 2, op=0.4))
    for i, (px, py) in enumerate(pts):
        c = BLUE if i % 2 else ORANGE
        b.append(f'  <circle cx="{px}" cy="{py}" r="7" fill="{c}" opacity="0.8"/>')
    return frame(b, 1)


# -------------------------------------------------------- slide 2: the ladder
RUNGS = [
    ("01", "PROMPT",     "you are the checker"),
    ("02", "SKILL",      "saved once, reused"),
    ("03", "LOOP",       "something else checks"),
    ("04", "ROUTINE",    "the trigger is not you"),
    ("05", "AGENT TEAM", "maker split from checker"),
]


def slide2():
    b = eyebrow("the ladder")
    b.append(txt(M, 262, "Five rungs. Each one is", size=56, weight=900, fill=INK))
    b.append(txt(M, 324, "work you stopped doing.", size=56, weight=900, fill=INK))
    # bar width grows with the rung: the encoding IS the amount handed over
    for i, (num, name, sub) in enumerate(RUNGS):
        n = i + 1
        y = 1136 - n * 150
        w = 420 + (n - 1) * 121
        b.append(rect(M, y, w, 122, PASTELS[i], r=14))
        b.append(rect(M, y, 8, 122, ORANGE if n >= 3 else GREY, r=4))
        b.append(txt(M + 34, y + 56, num, size=30, weight=900, fill=GREY, font=MONO))
        b.append(txt(M + 96, y + 58, name, size=38, weight=900, fill=INK))
        b.append(txt(M + 96, y + 96, sub, size=21, weight=400, fill=GREY, font=MONO))
    b.append(txt(RIGHT, 1160, "more handed over  →", size=21, weight=700,
                 fill=GREY, font=MONO, anchor="end"))
    return frame(b, 2)


# ------------------------------------------------- slide 3 / 5: paired rungs
def pair_slide(n, eb, h1, h2, cards):
    b = eyebrow(eb)
    b.append(txt(M, 268, h1, size=60, weight=900, fill=INK))
    b.append(txt(M, 336, h2, size=60, weight=900, fill=INK))
    y = 452
    for idx, (num, name, tint, body, note) in enumerate(cards):
        b.append(rect(M, y, COL, 316, tint, r=18))
        b.append(txt(M + 44, y + 78, num, size=44, weight=900, fill=GREY, font=MONO))
        b.append(txt(M + 128, y + 80, name, size=44, weight=900, fill=INK))
        yy = y + 152
        for ln in body:
            b.append(txt(M + 44, yy, ln, size=33, weight=400, fill=INK))
            yy += 44
        b.append(rect(M + 44, y + 246, 5, 44, ORANGE, r=3))
        b.append(txt(M + 70, y + 278, note, size=22, weight=400, fill=GREY, font=MONO))
        y += 356
    return frame(b, n)


def slide3():
    return pair_slide(
        3, "rungs 1 and 2", "Typed every time,", "then saved once.",
        [("01", "PROMPT", PASTELS[0],
          ["You are the memory, the planner", "and the checker. All of it."],
          "close the tab and it is gone"),
         ("02", "SKILL", PASTELS[1],
          ["Your rules written down once,", "picked up every time they fit."],
          "no re-explaining it every Monday")])


def slide5():
    return pair_slide(
        5, "rungs 4 and 5", "Off your machine.", "Then split in two.",
        [("04", "ROUTINE", PASTELS[3],
          ["It runs on a schedule.", "The trigger stops being you."],
          "close the laptop, it keeps going"),
         ("05", "AGENT TEAM", PASTELS[4],
          ["Roles, not one worker. The maker", "is split from the checker."],
          "one agent grading itself is still rung 4")])


# ------------------------------------------------------- slide 4: rung 3, loop
def slide4():
    b = eyebrow("rung 3, where most people stop")
    b.append(txt(M, 268, "A loop is not a prompt", size=60, weight=900, fill=INK))
    b.append(txt(M, 336, "that repeats.", size=60, weight=900, fill=INK))
    b.append(txt(M, 400, "It has three parts a prompt does not.", size=30, weight=400, fill=GREY))
    parts = [("VERIFIER", PASTELS[2], ["Something other than the model", "can reject bad output."]),
             ("STATE",    PASTELS[1], ["What is done, what failed,", "what is next. Tomorrow resumes."]),
             ("STOP",     PASTELS[3], ["Two exits: it succeeded,", "or eight tries and report."])]
    y = 456
    for name, tint, body in parts:
        b.append(rect(M, y, COL, 148, tint, r=16))
        b.append(txt(M + 36, y + 62, name, size=26, weight=900, fill=INK, font=MONO, ls=4))
        yy = y + 62
        for ln in body:
            b.append(txt(M + 330, yy, ln, size=28, weight=400, fill=INK))
            yy += 40
        y += 168
    # annotation callout, borrowed from diagram-explainer
    b.append(rect(M, 972, COL, 178, "#FFFFFF", r=16, op=0.55))
    b.append(rect(M, 972, 6, 178, ORANGE, r=3))
    b.append(txt(M + 40, 1030, "Without a real check you do not", size=34, weight=700, fill=INK))
    b.append(txt(M + 40, 1076, "have a loop. You have an agent", size=34, weight=700, fill=INK))
    b.append(txt(M + 40, 1122, "agreeing with itself on repeat.", size=34, weight=700, fill=ORANGE))
    return frame(b, 4)


# ---------------------------------------------------------- slide 6: the rule
def slide6():
    b = eyebrow("the rule")
    y = 316
    for ln in ["A rung only holds", "if the one below it", "is reliable."]:
        b.append(txt(M, y, ln, size=76, weight=900, fill=INK if "reliable" not in ln else ORANGE))
        y += 92
    b.append(txt(M, 660, "So the order is not negotiable:", size=30, weight=400, fill=GREY))
    steps = ["one manual run you trust", "save it as a skill",
             "wrap it in a loop with a gate", "then put it on a schedule"]
    y = 716
    for i, s in enumerate(steps):
        b.append(rect(M, y, 58, 58, PASTELS[i + 1], r=29))
        b.append(txt(M + 29, y + 39, str(i + 1), size=28, weight=900, fill=INK,
                     font=MONO, anchor="middle"))
        b.append(txt(M + 88, y + 40, s, size=34, weight=700, fill=INK))
        if i < len(steps) - 1:
            b.append(line(M + 29, y + 58, M + 29, y + 88, GREY, 3, op=0.6))
        y += 88
    b.append(rect(M, 1076, 6, 76, ORANGE, r=3))
    b.append(txt(M + 34, 1108, "Scheduling what you never made reliable by hand",
                 size=26, weight=400, fill=GREY, font=MONO))
    b.append(txt(M + 34, 1142, "is how automations burn money overnight.",
                 size=26, weight=400, fill=GREY, font=MONO))
    return frame(b, 6)


# -------------------------------------------------------- slide 7: diagnostic
DIAG = [
    ("RUNG 1", PASTELS[0], "You retype the same context every session",
     "save it as a skill, not an agent team"),
    ("RUNG 2", PASTELS[1], "Rules are saved, you still read every output",
     "add a verifier, not a bigger model"),
    ("RUNG 3", PASTELS[2], "Bad output gets rejected, you still press go",
     "put it on a schedule"),
    ("RUNG 4", PASTELS[3], "Runs without you, one agent grades itself",
     "split the maker from the checker"),
    ("NOT 5",  PASTELS[4], "You jumped straight to a team of agents",
     "go back and earn rung 3 first"),
]


def slide7():
    b = eyebrow("find your rung")
    b.append(txt(M, 262, "One symptom.", size=58, weight=900, fill=INK))
    b.append(txt(M, 326, "One next move.", size=58, weight=900, fill=INK))
    y = 400
    for chip, tint, symptom, move in DIAG:
        b.append(rect(M, y + 14, 152, 58, tint, r=10))
        b.append(txt(M + 76, y + 52, chip, size=23, weight=900, fill=INK,
                     font=MONO, anchor="middle", ls=1))
        b.append(txt(M + 182, y + 42, symptom, size=29, weight=700, fill=INK))
        b.append(txt(M + 182, y + 84, "→  " + move, size=24, weight=400,
                     fill=ORANGE, font=MONO))
        if chip != "NOT 5":
            b.append(line(M, y + 128, RIGHT, y + 128, HAIR, 2))
        y += 152
    return frame(b, 7)


# ------------------------------------------------------- slide 8: cost + CTA
def slide8():
    b = eyebrow("before you climb")
    b.append(txt(M, 258, "Every rung you climb is", size=54, weight=900, fill=INK))
    b.append(txt(M, 320, "maintenance you cannot", size=54, weight=900, fill=INK))
    b.append(txt(M, 382, "walk away from.", size=54, weight=900, fill=ORANGE))
    b.append(txt(M, 456, "A program returns the same output forever.", size=31, weight=400, fill=INK))
    b.append(txt(M, 498, "An agent does not.", size=31, weight=400, fill=INK))
    b.append(rect(M, 556, COL, 336, "#FFFFFF", r=18, op=0.5))
    b.append(txt(M + 40, 616, "CLIMB PAST RUNG 2 ONLY IF ALL FOUR ARE TRUE",
                 size=21, weight=900, fill=GREY, font=MONO, ls=2))
    checks = ["the task repeats at least weekly",
              "something can reject bad output on its own",
              "the agent can do the work end to end",
              "done is objective, not a judgment call"]
    y = 668
    for c in checks:
        b.append(rect(M + 40, y - 22, 26, 26, "none", r=6, stroke=GREY, sw=3))
        b.append(txt(M + 84, y, c, size=28, weight=400, fill=INK))
        y += 52
    b.append(txt(M + 40, 872, "Miss one and stay on the rung you are on.",
                 size=24, weight=700, fill=ORANGE, font=MONO))
    b.append(rect(M, 952, 6, 152, ORANGE, r=3))
    b.append(txt(M + 34, 1008, "Be honest about the rung you", size=44, weight=900, fill=INK))
    b.append(txt(M + 34, 1058, "are on, not the one you talk about.", size=44, weight=900, fill=INK))
    b.append(txt(M + 34, 1120, "Which one did you try to skip?", size=40, weight=900, fill=ORANGE))
    return frame(b, 8)


BUILDERS = [slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8]

if __name__ == "__main__":
    out = os.environ["OUT_DIR"]
    for i, fn in enumerate(BUILDERS, start=1):
        p = os.path.join(out, f"slide-{i}.svg")
        with open(p, "w") as f:
            f.write(fn())
        print(f"wrote {p} ({os.path.getsize(p)} bytes)")
