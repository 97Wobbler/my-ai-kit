---
name: moscow
display_name: MoSCoW Prioritization
class: frame
underlying_class: native
domain: product-management
source: Dai Clegg, Oracle, 1994
best_for:
  - Sorting product requirements or features by delivery urgency and business impact
  - Breaking a roadmap into delivery tiers that align with stakeholder expectations
one_liner: "Classify requirements as Must / Should / Could / Won't to set release scope and priority."
---

# MoSCoW Prioritization

## Overview

MoSCoW is a prioritization frame that sorts product requirements into four
delivery tiers based on the **consequence of exclusion** and the **urgency
of delivery**. Its core claim is that different tiers demand **structurally
different scope and release decisions** — conflating Must-haves with
Could-haves in the same release leads to missed deadlines and broken
promises to both users and stakeholders. By explicitly sorting requirements,
teams align on what will ship when, prevent scope creep, and make honest
trade-off conversations possible when time or budget constrains the plan.

## Categories

1. **Must have**
   - The feature or fix is **non-negotiable** for the release to be viable.
   - Absence makes the release unshippable or violates a critical business
     constraint (legal, security, contractual, or core product promise).
   - Discriminating criterion: if this requirement is dropped, the release
     is cancelled or delayed, not shipped as-is.
   - Example: GDPR compliance controls before a European launch; fixing a
     security vulnerability in production; the core transaction flow in a
     financial product.

2. **Should have**
   - The feature adds **significant value** and is expected by stakeholders,
     but the release is still viable without it.
   - Absence is **disappointing but not catastrophic**; users or business
     can adapt for one release cycle.
   - Discriminating criterion: if dropped, the release proceeds with known
     compromises acknowledged by stakeholders; the feature re-enters scope
     in the next cycle.
   - Example: a performance improvement that halves load time but the
     product is already usable; a convenience feature that power users
     expect.

3. **Could have**
   - The feature is **nice-to-have** and adds polish or covers an edge
     case, but is not on the critical path.
   - Absence does **not affect core functionality** or user perception of
     success.
   - Discriminating criterion: if time runs short, this is the first class
     of work to defer without stakeholder objection.
   - Example: a cosmetic UI refinement; support for an uncommon file
     format; an optimization that only benefits a small user segment.

4. **Won't have** (this time)
   - The requirement is **explicitly out of scope** for this release, often
     deferred to a future cycle.
   - Absence is **known and accepted** by stakeholders, either because
     there is insufficient priority or because the feature conflicts with
     other Must/Should commitments.
   - Discriminating criterion: the requirement is not dropped by accident;
     it is a **deliberate decision documented in writing**.
   - Example: a feature backlog item that competes for time with a higher
     priority; a capability that depends on a dependency not yet available.

## Classification Procedure

1. List each candidate requirement as a single line item. Include the user
   need, the business benefit, and any known constraints (e.g., "breaks if
   XYZ is not complete").

2. For each requirement, answer: **"If we ship the release *without* this,
   is it still a viable product?"**
   - If **no** → Must have. Stop.
   - If **yes** → go to step 3.

3. Ask: **"Will stakeholders accept its absence, or will we face
   significant pushback or contractual breach?"**
   - If **unacceptable absence** → Should have. Stop.
   - If **acceptable absence** → go to step 4.

4. Ask: **"Is this in the current roadmap for this release, or do we need
   to actively choose to defer it?"**
   - If **in the roadmap, but nice-to-have** → Could have. Stop.
   - If **explicitly deferred or out of scope** → Won't have. Stop.

5. Review the full list. Count Must/Should/Could/Won't. If Must + Should
   exceeds planned team capacity for the release, escalate to stakeholders
   — something currently classified as Should or Must must move to Could or
   Won't, or the deadline must move.

6. Document the classification in writing; circulate to stakeholders for
   agreement. A disagreement signals misalignment on scope.

## Implications per Category

| Category | Release decision | What the team should do |
|---|---|---|
| **Must have** | **Commit.** Ship date depends on Must completion. | Build first. Do not trade for time or cost. De-risk early via design review or prototype. If at-risk, escalate immediately. |
| **Should have** | **Prioritize, but conditionally.** Plan for completion, but accept deferral if Must + Could overrun. | Build second. Commit to a target, but pre-agree with stakeholders: "if we are slipping on Must, we will cut this." |
| **Could have** | **Include if time remains; defer guilt-free if not.** | Build last, or in parallel if low-risk. First candidate to cut when schedule tightens. Never trade Must/Should delivery for Could completion. |
| **Won't have** | **Actively defer.** Not in this release; document why (e.g., "target for Q3"). | Do not start work. Do not let stakeholders request it as a "small add-on." Revisit prioritization in the next cycle. |

For roadmap communication: **"We commit to Must and Should. Could ships if budget remains. Won't is explicitly deferred."** This is more honest than a flat feature list and makes trade-offs visible.

## Common Misclassifications

- **Everything classified as Must.** The most common failure mode. Result:
  scope explodes, deadlines slip, and the team's commitment becomes
  worthless. The tell is that you have more Must work than time. Escalate
  and re-classify; something is not truly Must.

- **Should mistaken for Must due to stakeholder pressure.** A stakeholder
  says "we need X" without understanding the timeline impact. Ask: "If X
  is not in this release, do we not ship at all, or do we ship with a
  known gap?" The answer reveals the true tier.

- **Could classified as Should "because it's in the product."** Existing
  features are assumed-Must by users; new features are Could unless they
  are core to the release value proposition. The tell is: "Is the user
  comparing us to competitors on this axis?" If no, it's probably Could
  or Won't.

- **Won't classified without stakeholder agreement.** A feature is cut
  unilaterally by the team without telling stakeholders until late in the
  cycle. The tell is a surprised stakeholder two weeks before launch. Always
  document and review Won't items with decision-makers upfront.

- **Treating MoSCoW as a ranking, not a tier.** Items within a category are
  not ordered; all Must items have equal standing for the release. If you
  need to rank within Must, that's a sign the Must set is too large or you
  have not understood the constraints.
