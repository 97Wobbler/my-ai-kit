---
name: kernighans-law
display_name: Kernighan's Law
class: heuristic
underlying_class: native
domain: agile
source: Brian Kernighan, The Elements of Programming Style, 1978 (with P. J. Plauger)
best_for:
  - code review and readability standards
  - debugging strategy
  - mentoring junior developers
  - architecture decisions
one_liner: "Debugging is twice as hard as writing code; so if you write code as cleverly as possible, you are, by definition, not smart enough to debug it."
---

# Kernighan's Law

## The Rule

Write code at roughly half your maximum cleverness. Prioritize clarity and simplicity over demonstrating technical prowess or minimizing lines of code.

The corollary: if you write the most intricate, clever code you can conjure, debugging and maintaining it will exceed your cognitive capacity, and the cost falls on the team.

## When It Applies

- Code style decisions: choosing between a one-liner that flattens 10 levels of logic vs. a 10-line explicit version. The explicit version wins.
- Architectural choices: using a straightforward three-tier architecture vs. an ingenious but obscure pattern. Straightforward is better.
- Variable naming: using `x` and `y` vs. `user_id` and `velocity`. The latter leaves less room for misunderstanding.
- Test readability: when a test is hard to understand because it's "clever," it becomes hard to maintain and debug.
- Knowledge transfer: when explaining code to a junior, "clever" code requires them to reverse-engineer your thinking; "clear" code lets them learn the intent directly.

## When It Misleads

- Treating "simple" and "naive" as synonyms. The simplest O(n²) algorithm is not always better than a less obvious O(n log n) algorithm if the latter is well-understood and well-tested.
- Over-applying simplicity to the point of inefficiency. You should not write slow, verbose code for core loops that run millions of times per second; at that point, the goal changes and some "cleverness" (in the form of careful optimization) is warranted.
- Confusing the law with "never use advanced language features." Rust's trait system, Lisp macros, or Python's metaclasses are complex but essential in their domains. The law warns against *unnecessary* complexity, not all complexity.
- Using clarity as cover for laziness. "I didn't refactor because Kernighan's Law says simple is better" is a rationalization if the code is unmaintainably messy.

## Common Misuse

Citing Kernighan's Law to argue that any code optimization or architectural sophistication is bad. Some teams use the law to justify avoiding learning advanced concepts, yielding a codebase that is "simple" but rigid and inefficient. The law applies to the engineer's *awareness* of their own limits, not a ban on all technical depth.

Another misuse: applying the law uniformly across a codebase. Core utilities, libraries, and performance-critical paths may warrant more sophistication; outer layers and user-facing code should be simpler. Context matters.

## How Agents Use It

- **Embedded**: in code review lenses, as a step to ask: "Is this code clear to someone unfamiliar with it? Can you explain the intent in one sentence, or is it buried in cleverness?" If the latter, request simplification.
- **Sanity-gate**: when evaluating code submissions, apply a "cognitive load" check: Does the code require the reader to understand 3+ layers of indirection? Is there a simpler way to express the same logic? If yes on both counts, it fails the heuristic.
- **Mentoring**:
  - When a junior writes clever code, praise the technical skill but coach toward simplicity: "I see what you did here. It's clever. Now, let's rewrite it so someone else can understand it immediately."
  - When a senior writes complex code, ask: "Why not use X simpler approach?" Often, the answer is "because of [constraint]," which is valuable. If no constraint exists, simplify.
- **Architecture guidance**:
  - When choosing between approaches, explicitly ask: "Which one can a mid-level engineer debug in 30 minutes?" That is often the right choice.
  - For critical systems, the standard should be even simpler: code that can be debugged and modified by the on-call engineer at 3 AM.
- **Measurement**:
  - Track cyclomatic complexity in code reviews; high complexity correlates with bug rates and maintenance cost.
  - Monitor the time required to onboard new engineers to a codebase; clearer code has lower onboarding time.
  - Measure defect density in "clever" vs. "simple" subsystems; the heuristic predicts that simple code has fewer bugs.

**Historical note**: Kernighan was writing in 1978, when debugging tools were primitive. The law is even more relevant today because code is often reviewed and debugged by different people, in async, distributed teams. The person who wrote the code is not available at 2 AM when the bug manifests in production.
