---
name: confirmation-bias
display_name: Confirmation Bias
class: heuristic
underlying_class: native
domain: general
source: Peter Wason (1960); Ray Nickerson (1998)
best_for:
  - hypothesis testing and evidence evaluation
  - investigation and diagnosis
  - design review and architectural decisions
one_liner: "seek disconfirming evidence as actively as confirming evidence, or you will miss what breaks your theory."
---

# Confirmation Bias

## The Rule
Once you hold a hypothesis, you will naturally seek evidence that supports it and overlook or discount evidence that contradicts it; the only remedy is to actively search for disconfirming cases.

## When It Applies
- Testing a hypothesis or proposed root cause: you've narrowed it down to "the bug is in the auth layer," then all signals get read through that lens.
- Incident post-mortems where a leading theory emerges early and subsequent investigation becomes a hunt for supporting details.
- Design reviews where the default option is the one being proposed, and reviewers unconsciously soften objections.
- Evaluating candidates, solutions, or proposals where first impressions set the direction of inquiry.

## When It Misleads
- When the hypothesis is actually correct and disconfirming evidence is genuinely rare or absent. Forcing yourself to hunt for counterevidence does not make a sound theory unsound.
- In time-constrained contexts where actively searching for refutation consumes resources needed for execution. Confirmation bias is a real cost; so is paralysis by over-skepticism.
- When the evidence set is truly one-sided (e.g., a law of physics, an implementation detail you've verified exhaustively). The heuristic applies to judgment calls under uncertainty, not to settled facts.

## Common Misuse
Treating confirmation bias as a reason to never commit to a hypothesis. The point is not radical skepticism — it is that you must *actively* construct the opposing case, not wait for disconfirming evidence to appear. Many people cite the bias as an excuse to second-guess conclusions without doing the work of building a real alternative.

Another failure mode: demanding equal time for disconfirming evidence when the evidence distribution is genuinely skewed. Confirmation bias is about your *search behavior*, not about enforcing statistical parity in the evidence you find.

## How Agents Use It
- **Embedded**: in hypothesis-testing or root-cause analysis lenses, as a mandatory step after a leading hypothesis emerges — explicitly enumerate what would falsify it, then hunt for those cases before deepening confidence.
- **Sanity-gate**: on each top finding framed as a conclusion, ask: "What evidence would prove this wrong, and did we actively look for it, or did we just not find it?" Flag findings where disconfirming evidence was not explicitly searched.
