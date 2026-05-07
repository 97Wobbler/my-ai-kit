---
name: linus-law
display_name: Linus's Law
class: heuristic
underlying_class: native
domain: agile
source: Eric S. Raymond, The Cathedral and the Bazaar, 1999 (named after Linus Torvalds)
best_for:
  - code review practices
  - open-source governance
  - quality assurance strategy
  - distributed development teams
one_liner: "With enough eyeballs, all bugs are shallow."
---

# Linus's Law

## The Rule

Given sufficient visibility and number of reviewers, any defect—whether a logic error, security vulnerability, or performance bottleneck—can be found and understood quickly, because the bug becomes obvious to someone with the right expertise.

## When It Applies

- Justifying code review culture in distributed teams: asynchronous reviews by multiple developers often catch issues that no single reviewer would miss.
- Open-source projects: thousands of users and contributors examining the code in production create a powerful quality filter.
- Security analysis: "many eyeballs" over a specification or codebase can discover subtle cryptographic or access-control flaws.
- Incident response: asking the team to review a log or error trace often surfaces the root cause faster than the on-call engineer investigating alone.
- Design reviews: presenting an architecture to a broad group of engineers with different specialties increases the chance that someone will spot a flaw.

## When It Misleads

- Assuming that *any* number of eyeballs suffices. A codebase reviewed only by people unfamiliar with the domain (e.g., JavaScript developers reviewing a Kubernetes operator) will miss domain-specific bugs no matter how many eyeballs are present.
- Treating visibility as automatically creating quality. A code review process where reviewers are tired, under time pressure, or not empowered to block merges will not catch bugs despite many eyes on the code.
- Confusing "many eyeballs" with "many comments." A PR with 50 comments is not the same as 50 separate quality reviews; some comments are nitpicks, others contradict each other, and few may focus on correctness.
- Ignoring the incentive structure. In open-source, many developers review because they care about the project. In a corporate setting, reviewers may be distracted or motivated to rubber-stamp code to unblock their own work.

## Common Misuse

Using the law as cover for insufficient automated testing or static analysis. "We have code review; bugs are shallow" is false confidence if the team lacks unit tests, integration tests, or linters that catch entire classes of errors before human review. Eyeballs are good at finding logic errors but terrible at spotting missing edge cases or performance regressions across an entire codebase.

Another misuse: treating code review as a bottleneck that slows down feature delivery. Some teams minimize review to ship faster, arguing that post-release feedback provides "more eyeballs." This ignores that catching bugs *before* merge is far cheaper than incident response in production.

## How Agents Use It

- **Embedded**: in code review lenses, as a step to document: "Route this code review to reviewers with domain expertise in: [X], [Y], [Z]. Ensure at least N reviewers sign off before merge." Link reviewer selection to the specific domains touched by the change.
- **Sanity-gate**: when evaluating a codebase or process, ask: "What is the code review participation rate? Are reviewers sufficiently expert in the domains they review?" If many merges happen with 1 or 0 reviews, or if reviews are performed by people unfamiliar with the code, flag a quality risk.
- **Scaling practices**:
  - In small teams (< 5), every engineer reviews; ensure each review is substantive.
  - In medium teams (5-20), establish a code review standard (e.g., "2 reviews for data-touching code") and rotate reviewers to spread knowledge.
  - In large teams (> 20), create reviewer pools by subsystem; each subsystem has a set of 3-5 experts who handle reviews.
- **Tool support**:
  - Use CODEOWNERS files to route reviews automatically based on file paths.
  - Encourage threaded discussions in PRs to surface disagreement early.
  - Measure review time and lag; optimize asynchronous practices (e.g., overnight reviews in distributed teams).
  - Use automated checks (tests, linters, static analysis) to reduce the cognitive load on human reviewers.

**Key insight**: The law does not promise that bugs will disappear; it promises that *with the right people*, bugs become *obvious*. The skill is in assembling the right eyeballs and creating conditions for them to focus.
