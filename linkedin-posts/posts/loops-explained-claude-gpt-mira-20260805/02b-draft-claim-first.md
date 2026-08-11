Most engineers who say they are building AI loops are running expensive spinners.

Not because loops are complicated. Because they skip the one part that makes them work.

The Verify step.

A loop has five parts: Discover, Plan, Execute, Verify, Iterate.

Verify is the heart. Without a gate that can actually fail the work, the agent grades its own homework. The model that wrote the output is far too generous a reviewer. It iterates in circles and the bill grows the entire time.

Here is how the cost compounds, and why most people miss it.

Every iteration, the agent re-reads its full context: the goal, everything it produced, every failure. That pile grows each pass. Ten iterations is not ten prompts. It is ten prompts that each keep getting bigger.

The metric that matters is not tokens spent. It is cost per accepted change. Below 50% acceptance, the loop costs more than doing it manually.

Four questions before building one:

Does this task repeat at least weekly?
Can something automatically reject bad output?
Can the agent do the work end to end?
Is "done" objective, not a judgment call?

One no: keep it as a prompt. Most engineers who burn money on loops fail criterion 2.

If all four are yes, build in this exact order. Get one manual run working reliably. Save those instructions as a reusable file. Add a gate and a stop condition. Then automate.

Automate last. Not first.

Scheduling something you have not made reliable by hand is how loops blow up while you sleep.

What loop have you built, or what stopped you from building one?

#AIEngineering #AgentDesign #SoftwareEngineering #BuildingWithAI

---
Angle: Bold claim-first
Hook: Most engineers who say they are building AI loops are running expensive spinners.
Word count: 265
