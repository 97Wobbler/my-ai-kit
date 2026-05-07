---
name: ice-scoring
display_name: ICE Scoring
class: lens
underlying_class: native
domain: product-management
source: Sean Ellis (GrowthHackers); popularized by Intercom, Mixpanel
best_for:
  - Prioritizing features, initiatives, or experiments when velocity matters more than perfect prediction
  - Comparing disparate opportunities on a shared numerical scale
  - Making trade-offs between high-impact, high-confidence, but hard items versus easy wins
one_liner: "Quantify prioritization via Impact × Confidence × Ease."
---

# ICE Scoring

## Overview
ICE Scoring reduces prioritization to three dimensions — Impact (how much does this move the metric?), Confidence (how sure are we?), and Ease (how fast can we ship?) — multiplied together to yield a single comparable score. Teams use it to arbitrate between competing initiatives when consensus fails or to surface which bets offer the best return per unit of effort. The discipline is in scoring honestly; most teams score carelessly and end up ranking by gut feeling dressed as mathematics.

## Analytical Procedure

### Phase 1 — Establish Scoring Parameters

1. **Define the target metric.** What single outcome matters most to your business right now? User signups, revenue, retention, engagement, cost-per-acquisition? Write it down. All Impact scores must be justified against this metric, not against secondary signals like "team morale" or "code quality."

2. **Define the time horizon.** Over what period do you expect to see the impact? One quarter? Six months? One year? Impact and Confidence estimates are meaningless if the horizon is ambiguous.

3. **Calibrate the scale.** Standard ICE uses 1–10 for each dimension, but define what each score means concretely:
   - **Impact 10:** Moves the target metric by >50% in the time horizon.
   - **Impact 5:** Moves the metric by 10–25%.
   - **Impact 1:** Moves the metric by <5%.
   - **Confidence 10:** You have direct data (A/B test, customer research, historical precedent) backing the estimate.
   - **Confidence 5:** You have indirect signals (competitor moves, team intuition from similar work).
   - **Confidence 1:** This is a guess.
   - **Ease 10:** Can ship in one sprint with existing tools; no major technical unknowns.
   - **Ease 5:** Needs 2–4 sprints; some technical or design unknowns.
   - **Ease 1:** Needs >4 sprints; multiple dependencies or unknowns.

### Phase 2 — Score Each Initiative

4. **For each initiative, score Impact independently.** Do not glance at Confidence or Ease yet. Estimate: "If this works as intended, how much does it move the target metric?" Use the calibrated scale. Write a one-sentence justification for every score ≥7 or ≤3; middle scores can be justified with a phrase.

5. **Score Confidence independently.** Do not adjust based on Ease. Ask: "What is our actual certainty that the Impact will materialize?" Sources of confidence:
   - Direct evidence: prior A/B test on similar change (+5 points).
   - Customer research: interviews or surveys showing strong signal (+3 points).
   - Industry precedent: direct competitors or adjacent domains achieved this (+2 points).
   - Team experience: team has shipped similar work before (+1 point).
   - Untested assumption: guessing (-0 to -3 points; cap at Confidence 1).

6. **Score Ease independently.** Ask: "How long until we can measure results?" Factor in:
   - Build and QA time (can be estimated from sprints or story points).
   - Dependency risk (if blocked on another team, deduct 2–3 points).
   - Technical debt or unknowns in the implementation path (deduct 1–2 points per major unknown).

7. **Multiply: ICE = Impact × Confidence × Ease.** Enter all three scores and the product into a table (see Output Format).

### Phase 3 — Sanity-Check and Rank

8. **Review high-scoring items.** If a 10-10-10 scores 1000 and an 8-8-8 scores 512, the ranking is obvious. Look instead at the cluster around the median score. A 9-6-8 (432) versus a 7-9-6 (378) — which matters more? Re-read the justifications.

9. **Spot-check for recency bias.** High-confidence scores often cluster around recent wins or current crises. Ask: "Are we scoring this high because it's fresh, or because the evidence is actually strong?" Adjust down by 1–2 confidence points if you catch yourself over-weighting a recent event.

10. **Check for Ease manipulation.** Teams often score Ease high on pet projects. If an item you've been advocating for scores 9 on Ease, ask a skeptic to re-score it. Ease consensus is a good sanity check.

11. **Rank by ICE score, highest first.** This is your prioritized backlog.

### Phase 4 — Validate the Ranking

12. **Trace the top-3 items to a concrete next step.** If the #1 item is "Improve onboarding," that's too vague. The next step should be "Run 5 customer interviews about onboarding friction — two weeks, one researcher." If you can't name the next step, the Confidence score was probably too high.

13. **Run one full cycle (ship, measure, learn).** After launching the top initiatives, revisit the scores for the ones that shipped. What was the actual Impact versus predicted? Adjust future Confidence scores based on your track record. If Impact predictions are consistently 2x too high, your team is overconfident; apply a systematic 0.5× discount to future Confidence scores.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Target metric is named and time horizon is explicit | Y/N |
| Impact/Confidence/Ease scale is calibrated with concrete thresholds | Y/N |
| Every item ≥7 or ≤3 on any dimension has a written justification | Y/N |
| No Confidence score was inflated to favor Ease (or vice versa) | Y/N |
| Top-3 items have explicit next steps | Y/N |
| At least one prior ranking was revisited and updated based on results | Y/N |

## Red Flags

- All items score between 5–7 on all dimensions. Either the estimation was lazy or the initiatives are genuinely interchangeable. Run again, this time forced to give at least 2 items a ≥8 or ≤3 on some dimension.
- Confidence and Ease are highly correlated (high-Ease items also score high-Confidence). Teams often conflate "easy to build" with "sure to work." Separate them explicitly: re-score Confidence based only on evidence, not effort.
- The top-scoring item is vague ("improve user experience") or owned by an absent stakeholder. ICE is a tool for making trade-offs; if an item can't be scoped or shipped, it doesn't belong on the list.
- Ease scores never go below 4. If everything is "easy," you're either very good at estimation (unlikely) or you're scoring conservatively to avoid hard projects. Pressure-test the 7+ Ease scores by asking "what's the biggest unknown here?"
- The ranking has not changed in two quarters. ICE is a learning tool. If the same three items stay at the top indefinitely, either your initiatives never ship (red flag) or the scores are stale and should be revisited (required behavior).

## Output Format

```
## ICE Prioritization

**Target metric:** <name and definition>
**Time horizon:** <duration, e.g., "one quarter">

### Calibration
| Dimension | 10 | 5 | 1 |
|---|---|---|---|
| Impact | <threshold> | <threshold> | <threshold> |
| Confidence | <threshold> | <threshold> | <threshold> |
| Ease | <threshold> | <threshold> | <threshold> |

### Scored Initiatives
| Initiative | Impact | Confidence | Ease | ICE | Justification |
|---|---|---|---|---|---|
| <name> | <1–10> | <1–10> | <1–10> | <product> | <one sentence> |

### Ranking (by ICE score)
1. <name> — <ICE score> (I:<X>, C:<X>, E:<X>)
2. ...
3. ...

### Top-3 Next Steps
1. <initiative> → <concrete first action>
2. <initiative> → <concrete first action>
3. <initiative> → <concrete first action>

### Learning from Prior Cycles
**Last cycle's prediction vs. actual:**
| Initiative | Predicted Impact | Actual Impact | Adjustment |
|---|---|---|---|
| <name> | <1–10> | <1–10> | Confidence ×0.X in future |

### Confidence
<high | medium | low> — <justification: quality of evidence, track record accuracy, unresolved dependencies, or estimation maturity>
```
