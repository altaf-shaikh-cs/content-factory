# Post plan

**Source idea:** `../../../raw-ideas/claude-autoclassifier.md`
**Primary source:** https://www.anthropic.com/engineering/claude-code-auto-mode (followed closely, per direct instruction)
**Generated:** 2026-08-26
**Supersedes:** an earlier draft this same day that was rejected for being a feature dump. Diagnosis of that failure is below, because it drives every choice here.

## Why the first attempt failed

It inventoried the system: the decision order, the block list, the protected paths, the circuit breakers, the thresholds. All true, all sourced, and all of it made the reader's job harder rather than easier. A list of twenty things a system blocks does not reduce fear. It reads as twenty things that could go wrong. Coverage is not clarity.

The fix is not a shorter list. It is one idea with a spine.

## The spine

The engineering article's own argument, which is better than any summary of its feature set:

The threat it was built for is **not malice, it is eagerness**. "The agent understands the user's goal, and is genuinely trying to help, but takes initiative beyond what the user would approve."

That single reframe does the whole job the brief asked for:
- **Astonishment**: the reader assumed the guard exists to stop a rogue AI. It exists to stop a helpful one. That is a genuinely surprising inversion.
- **Fear reduction**: eagerness is a failure the reader has personally had and already understands. It is mundane. Mundane threats are not frightening.
- **Self-directed decision**: it explains why the system's known weakness sits exactly where it does, which hands the reader the rule instead of a recommendation.

## The one idea to teach

**Authorization is not transitive.** With the article's own two examples, which are perfect and need no improvement:

- "Clean up my branches" does not authorize deleting them in bulk
- "Can we fix this?" is a question, not a directive

The classifier's question is not "is this dangerous", it is "did the human authorize *this*". Everything else in the article is downstream of that.

## Two mechanisms, kept because each answers a fear rather than describing a feature

| Reader's fear | The design choice | Why it lands |
|---|---|---|
| "It will rationalize its way past the check" | Assistant reasoning is stripped before the reviewer sees the call | It judges **actions, not arguments**. Four words the reader keeps |
| "A poisoned file or web page will hijack it" | Tool results are stripped | Carried by the article's own example: the reviewer never sees the malicious file and does not need to, because credentials leaving for a stranger fails against intent regardless of what suggested it |

Everything else the article covers (two-stage cost design, the tiered allowlist, subagent checkpoints, the fallback thresholds) is cut. Correct, uninteresting to a reader deciding whether to be afraid.

## The honest number, used as a tool and not a caveat

Not the raw 17%. The *reason* for it, which is far more useful:

> "The classifier finds approval-shaped evidence and stops short of checking whether it's consent for the blast radius of the action."

That converts a scary statistic into an actionable boundary. A precise weakness yields a precise rule, and the rule is the payoff:

**Small blast radius and you are watching: let it run. Large blast radius or nobody watching: write a deny rule instead of hoping.**

This is also exactly Altaf's own two-month practice (classifier for interactive work, guardrails for unattended agents), so the recommendation and the lived experience are the same sentence rather than two claims stacked on each other.

## Closing

Article's own line, which is more generous than anything written for it: "The classifier doesn't need to be flawless to be valuable." Turn it on the reader's setup, then ask which half their current task is in.

## Compliance

No emojis. No em dashes. No company names. Every claim traces to the linked engineering article. The 89% vs 13.6% comparison stays excluded: not first-party verifiable. Raw percentages omitted entirely this time, because the *reason* for the miss is the useful part and numbers were part of what made the last draft feel like a dump.
