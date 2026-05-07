---
name: xy-problem
display_name: XY Problem
class: heuristic
underlying_class: native
domain: general
source: comp.unix.shell folklore (Eric S. Raymond, "How To Ask Questions The Smart Way", 2001); popularized via xyproblem.info
best_for:
  - debugging help requests and support tickets
  - code review of "how do I do X?" questions
  - requirement intake and stakeholder interviews
  - PR descriptions that justify a solution but not a problem
one_liner: "The Y the user asks about is not the real problem X — dig into motive before solution."
---

# XY Problem

## The Rule

When someone asks how to accomplish Y, suspect that Y is their attempted *solution* to an unstated underlying problem X. Refuse to answer Y in isolation until X is on the table; the best help for Y is often a different solution to X entirely.

## When It Applies

- A question begins with "How do I…" and prescribes a specific mechanism, tool, or syntax (regex, shell trick, config flag) without naming the goal.
- A bug report describes a fix attempt that failed, not the original symptom.
- A PR proposes implementation details before the issue describing the user need exists.
- A stakeholder requests a feature shaped exactly like one specific UI element ("add a dropdown here") rather than describing the workflow they are trying to enable.
- A debugging session is stuck because every fix to Y produces a new failure of Y, suggesting Y is the wrong frame.

## When It Misleads

- When Y is genuinely the right question and the asker has already done the X→Y translation themselves. Aggressive "but what is your *real* problem?" interrogation is then condescending and wastes everyone's time.
- In well-scoped technical questions where the X is obvious from context (e.g., "how do I escape a quote in this JSON string?" — the X is "produce valid JSON," and demanding it be stated explicitly is pedantic).
- In time-pressured incident response, where forcing a re-derivation of the problem from first principles can block a working tactical fix.
- When the asker is exploring or learning, and Y itself is the object of interest regardless of whether it solves any X.

## Common Misuse

Using "that's an XY problem" as a rhetorical dismissal — a way to refuse to engage with the question as asked while signaling superior insight. The heuristic is meant to *expand* the conversation by surfacing X, not to *terminate* it by refusing to discuss Y. A second misuse is stacking infinite "but why?" layers (the 5-Whys failure mode), turning every concrete request into an open-ended philosophy session about ultimate goals. The fix is to ask for X exactly *once*, then proceed with whichever framing — X or Y — actually unblocks the asker.

## How Agents Use It

- **Embedded**: in requirement-gathering, debugging, and code-review lenses, as a mandatory clarification step before recommending an implementation. The agent must restate (or explicitly flag as unknown) the underlying goal X that the requested Y is meant to serve, and check whether a different Y' would serve X better.
- **Sanity-gate**: on each "do Y" recommendation in synthesis, force the agent to name the X it solves and the alternative solutions to X that were considered and rejected. If X cannot be articulated, downgrade the recommendation's confidence and surface the gap to the user.
