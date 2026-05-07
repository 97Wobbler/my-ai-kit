---
name: Kano Model
domain: general
source: Noriaki Kano, Tokyo University of Science, 1984 ("Attractive Quality and Must-Be Quality")
best_for: Classifying product features or quality attributes by the non-linear relationship between their presence and customer satisfaction
one_liner: "Classify product features as Must-be / Performance / Attractive / Indifferent / Reverse to judge investment priority."
---

# Kano Model

## Overview

The Kano Model sorts product attributes along two axes — **level of
implementation** (none → fully delivered) and **level of customer
satisfaction** (frustration → delight) — and observes that the
relationship between them is **not linear and not the same** across
attributes. The same investment yields very different satisfaction returns
depending on the attribute's category. Sorting features into Kano
categories before prioritizing work prevents two common errors:
over-investing in basics that only prevent dissatisfaction, and
under-investing in delighters that are the actual source of enthusiasm.

## Categories

1. **Must-be (기본)**
   - Presence is taken for granted; **absence causes sharp
     dissatisfaction**, but presence creates no positive satisfaction.
   - Satisfaction curve: flat near zero when present, plunges when absent.
   - Discriminating criterion: the user would never list this as a reason
     they love the product, but would immediately complain if it were
     missing.
   - Example: the brakes on a car work; a banking app shows an accurate
     balance.

2. **One-dimensional / Performance (성과)**
   - Satisfaction is **proportional** to implementation level.
   - More is better; less is worse; the user can articulate the tradeoff.
   - Discriminating criterion: users readily compare competitors on this
     axis ("yours is faster/cheaper/more accurate than theirs").
   - Example: fuel efficiency, battery life, page-load speed.

3. **Attractive / Delighter (매력)**
   - Absence causes **no dissatisfaction** (users don't expect it), but
     presence causes **disproportionate satisfaction**.
   - Discriminating criterion: users cannot articulate this as a desire
     before seeing it, but react strongly once they do.
   - Example: AirDrop when it was new; a surprising thoughtful detail in
     an onboarding flow.
   - Note: delighters erode over time into Performance or Must-be
     attributes as expectations rise.

4. **Indifferent (무관심)**
   - Neither presence nor absence meaningfully affects satisfaction.
   - Discriminating criterion: users do not notice or care regardless of
     implementation level.
   - Example: an internal configuration option that end users never
     interact with; an obscure edge-case flag.

5. **Reverse (역효과)**
   - Presence actively **decreases** satisfaction for some or all users.
   - Discriminating criterion: a segment of users prefers *less* of the
     attribute, or its absence entirely.
   - Example: an assistive "suggestions" popup that power users find
     intrusive; an animated splash screen.

## Classification Procedure

Kano's original method uses a **two-question survey** per attribute —
functional ("How do you feel if feature X is present?") and dysfunctional
("How do you feel if feature X is absent?") — with a 5-point scale:
*I like it / I expect it / I am neutral / I can tolerate it / I dislike
it*. The pair of answers maps to a Kano category via a standard grid.

Agent-usable lightweight procedure:

1. List each candidate feature or quality attribute one per row.
2. For each, answer both functional and dysfunctional questions from the
   perspective of the target user segment. Name the segment explicitly —
   a feature can be a delighter for one segment and Indifferent for
   another.
3. Apply the classification grid:
   - **Like if present, dislike if absent** → Performance.
   - **Expect if present, dislike if absent** → Must-be.
   - **Like if present, tolerate if absent** → Attractive.
   - **Neutral in both directions** → Indifferent.
   - **Dislike if present** → Reverse.
4. If the two-question answers are self-contradictory ("like it present,
   like it absent"), re-examine — usually the feature is Indifferent to
   that segment, or the segment is mis-scoped.
5. Record the classification *and the segment it applies to*; Kano is
   segment-relative, not universal.

## Implications per Category

| Category | What to do |
|---|---|
| **Must-be** | Invest until the bar is met; further investment yields no return. These are a table-stakes floor, not a growth lever. |
| **Performance** | Invest in proportion to how competitively differentiating the axis is — these are the axes users actively compare on. |
| **Attractive** | Invest **selectively and visibly** — one well-executed delighter usually outweighs several mediocre ones. Expect erosion over 1–3 years. |
| **Indifferent** | Cut or defer; free up budget. |
| **Reverse** | Remove, or make optional — never force on users who experience it negatively. |

Implicit prioritization rule: **Must-be baselines first, Performance
investments sized by competitive gap, Attractive items selected rarely but
made excellent, Indifferent eliminated, Reverse removed or gated.**

## Common Misclassifications

- **Treating all features as Performance.** The dominant failure mode in
  roadmap work; it leads to flat satisfaction curves because Must-be gaps
  poison everything above them and Attractive surprises never appear.
- **Mistaking a Delighter for Performance after launch.** A delighter
  that's been in the product for a year is now a Must-be — continuing to
  treat it as a differentiator overestimates its return.
- **Classifying without naming the segment.** A feature that is a
  delighter to power users may be Reverse to novices. Segment-agnostic
  Kano classification is a common source of invalid prioritization.
- **Using Kano on a single-user sample.** Individual opinion is not
  Kano data; the categorization needs enough coverage of the segment to
  survive one loud outlier.
- **Collapsing Indifferent into Must-be "to be safe".** Inflates the
  roadmap and hides the fact that no one will notice the investment.
