---
name: boy-scout-rule
display_name: Boy Scout Rule
class: heuristic
underlying_class: native
domain: agile
source: Robert C. Martin, Clean Code, 2008; rooted in scouting principle "Leave the campground cleaner than you found it"
best_for:
  - code review feedback
  - refactoring strategy
  - technical debt prevention
  - developer culture and standards
one_liner: "Leave the code in a better state than you found it, even if you didn't create the mess."
---

# Boy Scout Rule

## The Rule

Whenever you touch a file or module, make a small, deliberate improvement before you commit. The improvement should be orthogonal to the main task—not part of the feature or fix you're implementing—but a genuine step toward higher quality.

## When It Applies

- Fixing a bug in a function with unclear variable names: rename `x` and `y` to `user_id` and `score` while you're there.
- Adding a feature to a module with weak test coverage: write one new unit test for an untested code path while implementing your feature.
- Reviewing a PR: suggest a small follow-up improvement (simplify a conditional, extract a helper function, add a comment) in addition to approving the core logic.
- Incident response: after fixing an outage, add a monitoring alert or a comment explaining why the bug wasn't caught earlier.
- Long-lived codebases: every commit is an opportunity to nudge code quality in the right direction.

## When It Misleads

- Using the Boy Scout Rule as cover for unbounded scope creep. "While I'm here, I'll refactor the entire module" is not the rule; it is the Broken Windows theory taken to extremes. The improvement should be small—on the order of one or two commits, not a full refactoring.
- Applying it to code you don't understand. Renaming variables in code you barely grasped introduces risk. Make sure your small improvement doesn't introduce a subtle bug.
- Over-applying the rule to reviewers and blockers. If every reviewer adds a follow-up improvement request, the PR gets blocked and the developer loses momentum. Small improvements should be encouraged, not mandated.
- Confusing it with perfectionism. The goal is not to leave the code perfect, but incrementally better. A function with four issues might see one improved per pass.

## Common Misuse

Using the rule as justification for a reviewer to request unrelated changes. "While you're in this file, refactor the error handling" sounds helpful but violates the spirit of the rule: it should be the *author* who does small improvements, not the reviewer. A reviewer's job is to flag issues and approve; if the reviewer spots a valuable improvement, they should either: (1) make it themselves in a separate commit, or (2) mention it as a lower-priority suggestion ("nice to have, not blocking").

Another misuse: applying it inconsistently. If only senior developers follow the rule and juniors are told "just implement your feature," the codebase quality doesn't improve evenly. The rule works best when it's a team practice, not an individual discipline.

## How Agents Use It

- **Embedded**: in code review lenses, as a step to encourage: "Author: before submitting, ask yourself: 'Is there one small improvement I can make to code quality while I'm here?'" Suggest reviewers look for opportunities to praise small improvements.
- **Sanity-gate**: when a codebase has accumulated high technical debt, apply the heuristic as a check on refactoring PRs: "Is the improvement incremental and orthogonal to the main task, or is this attempting to fix everything at once?" If the latter, ask the author to split the work.
- **Culture signal**:
  - In retrospectives, celebrate small improvements that were made in regular work.
  - In PR feedback, acknowledge and praise when an author makes a small improvement orthogonal to their feature.
  - Contrast with the Broken Windows theory: don't tolerate accumulated neglect, but do improve in steady increments.
- **Measurement**:
  - Track average test coverage gain per commit (small improvements add up).
  - Monitor comment density and clarity over time.
  - Measure the number of code smells eliminated per sprint (aim for slow, steady reduction).

**Connection to Broken Windows theory**: The Boy Scout Rule is the preventive side of the same coin. Broken Windows warns against allowing problems to fester; the Boy Scout Rule actively combats festering by making incremental improvements routine. Together, they establish a culture where code quality is nobody's sole responsibility and everybody's shared practice.
