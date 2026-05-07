---
name: yagni
display_name: YAGNI
class: heuristic
underlying_class: native
domain: agile
source: Ron Jeffries, Extreme Programming, late 1990s
best_for:
  - feature prioritization
  - scope management
  - architecture decisions
  - codebase complexity control
one_liner: "You Aren't Gonna Need It — don't add features until they are actually required."
---

# YAGNI

## The Rule

Do not implement functionality in advance of actual need. Build only what is required for the current iteration or release; refactor and extend later when new requirements arrive.

The corollary: YAGNI is safe and practical only when you have high test coverage, fast CI, and a refactoring-ready codebase. Without those safety nets, YAGNI becomes recklessness.

## When It Applies

- Feature flags and future exporters: when a customer might need JSON export "someday," implement JSON now; but XML, YAML, and CSV exports can wait for actual requests. Once JSON is requested, extending to XML is a small refactor.
- Configuration options: resist adding flags for every possible behavior variant. Add them when a customer or test case actually needs them.
- Generalization: when writing a function to handle user uploads, don't pre-emptively support video, audio, and documents if only images are needed today. Build image upload, then extend.
- Database schema: do not create columns for future analytics or features that may never ship. Add them when the feature is green-lit.
- Caching and optimization: do not pre-optimize for scale before you have actual performance data. Add caching when monitoring shows a bottleneck.

## When It Misleads

- Applying YAGNI to foundational decisions. Whether to use a relational or document database, whether to adopt async messaging, or whether the system will handle distributed transactions—these are *architectural* choices that are expensive to reverse. These should be decided based on anticipated needs, not current code alone.
- Using YAGNI to justify poor initial design. "We'll refactor later" is false confidence if "later" never comes due to technical debt, budget constraints, or the original architects leaving.
- Ignoring patterns that emerge across requirements. If three different customers ask for similar features, YAGNI doesn't mean waiting for the fourth; it means recognizing the pattern and building a general solution.
- Treating refactoring capacity as infinite. YAGNI assumes that the team can quickly and safely refactor when new features arrive. If the codebase is brittle, test coverage is poor, or the team is stretched, YAGNI becomes dangerous.

## Common Misuse

Using YAGNI to justify delaying crucial infrastructure. "We don't have a logging system yet because we don't strictly need it" is false economy if debugging in production is painful. Infrastructure that serves all code should be built early.

Another misuse: applying YAGNI to cross-cutting concerns like security, performance monitoring, or error handling. These need foundational support; adding them later is far more expensive than designing them in initially.

A third misuse: confusing YAGNI with "don't refactor." YAGNI says "don't add features speculatively," but once you *do* add a feature, you should refactor ruthlessly to keep the code clean. Without refactoring, YAGNI leads to accidental complexity.

## How Agents Use It

- **Embedded**: in backlog prioritization and scope lenses, as a step to ask: "Is this feature actively requested, or are we assuming customers will want it?" Rate features by actual demand vs. speculation, and defer speculative features.
- **Sanity-gate**: when reviewing a feature PR, check: "Does this add capability beyond what was requested?" If yes, ask: "Can we defer this and deliver the MVP, then refactor/extend based on real feedback?" If the answer is "it's too hard to refactor later," that is a red flag—it means the architecture is brittle or test coverage is weak.
- **Architecture decision**:
  - Use YAGNI to choose simpler designs for *features* and *options* (e.g., JSON export today, XML later).
  - Do *not* use YAGNI to choose brittle architectures (e.g., no logging, no observability, no distributed transaction support) unless you are genuinely confident those concerns won't arise.
- **Refactoring discipline**:
  - YAGNI is only safe with strong safety nets. Measure:
    - Test coverage (aim for >80% for business logic).
    - CI/CD cycle time (can you deploy safely in < 10 minutes?).
    - Code review throughput (can refactoring PRs be merged quickly?).
  - If any of these are weak, YAGNI becomes risky; either strengthen them or add conservative speculation to architecture.
- **Measurement**:
  - Track features that were built speculatively but never used (aim for < 20%).
  - Track refactoring velocity (features added per sprint should remain steady; if it drops, technical debt is accumulating).
  - Monitor production incidents caused by "we didn't think of that"; use these as evidence that some architectural decisions should have been made earlier.

**Key distinction**: YAGNI applies to *features and user-facing code*. Foundational architecture, testing infrastructure, observability, and security need forward-thinking because they are expensive to retrofit. The wisdom lies in knowing which category you are in.

**Complementary heuristic**: Premature Optimization warns against over-optimizing code before profiling. YAGNI warns against over-generalizing architecture before requirements are clear. Together, they counsel: implement cleanly for current needs; refactor decisively when new needs emerge.
