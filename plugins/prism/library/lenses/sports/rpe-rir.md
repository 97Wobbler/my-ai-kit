---
name: rpe-rir
display_name: RPE/RIR (Rate of Perceived Exertion / Reps in Reserve)
class: lens
underlying_class: native
domain: sports
source: Borg (perceived exertion scale, 1962); RIR framework modernized by Helms, Cronin, Storey (strength & conditioning, 2016–present)
best_for:
  - Autoregulating training load without technology
  - Translating subjective feel into actionable training decisions
  - Bridging the gap between planned intensity and actual capacity on a given day
one_liner: "Autoregulation framework that adjusts daily training volume via perceived exertion / reps in reserve."
---

# RPE/RIR (Rate of Perceived Exertion / Reps in Reserve)

## Overview

RPE/RIR is a two-axis system for quantifying training intensity without external devices. RPE (1–10 scale) measures how hard a set *feels* relative to maximum effort; RIR (0–10 scale) estimates how many additional reps could be performed before mechanical failure. Together, they allow lifters and coaches to adjust volume and intensity on the fly, accounting for fatigue, recovery, stress, and day-to-day variance. Practitioners use this when periodized targets (e.g., "3 × 5 at 80% 1RM") are too rigid for real bodies, or when access to load-testing equipment is limited.

## Analytical Procedure

### Phase 1 — Establish Baseline RPE/RIR Anchors

1. **Define a maximal-effort set for your exercise.** Perform or recall a set taken to *mechanical failure* — the point at which one more rep in good form is impossible. This is RPE 10, RIR 0.

2. **Work backward and assign RPE/RIR pairs to intermediate intensities.** Using the same exercise, perform or recall sets at these nominal loads:
   - RPE 6–7: feels easy, 3–4 reps left in tank (RIR 3–4)
   - RPE 7–8: feels moderate, 2–3 reps left (RIR 2–3)
   - RPE 8–9: feels hard, 0–1 reps left (RIR 0–1)
   - RPE 9–10: feels maximal, 0 reps left (RIR 0)

   Do NOT use external load as reference; use only feel and estimated remaining capacity. Record these anchors in a table for the exercise.

3. **Test your calibration against a known load.** Take a weight you expect to be ~RPE 8 and perform a set. Count actual reps before failure. Compare to your anchor estimate. If your actual RIR was 3 but you predicted 1, recalibrate your anchors — you underestimated perceived exertion or overestimated reserve.

### Phase 2 — Rate the Working Set

4. **Perform the prescribed set.** Complete the target reps (e.g., 5 reps, 8 reps, 20 reps) and **immediately** assess:
   - How many additional reps in good form could you perform right now?
   - On a scale of 1–10, how hard did that set feel?

5. **Record both RPE and RIR**, plus any contextual notes: sleep, stress, time of day, previous exercise(s) that session.

6. **Apply a confidence modifier** if conditions deviate from baseline:
   - **Fatigue accumulation in the session:** Add +0.5 to perceived RPE (a set might feel RPE 8.5 instead of 8, even at the same load).
   - **Reduced sleep (<6 hours prior night):** Add +1 to perceived RPE.
   - **High ambient stress (work/life):** Add +0.5 to perceived RPE.
   - **Uncommon exercise or equipment:** Reduce confidence in your RIR estimate by one full rep (e.g., if you think RIR 2, assume RIR 1–3 range).

### Phase 3 — Make Autoregulation Decisions

7. **Compare actual RPE/RIR to the prescribed target.** Your prescription is usually given as "3 × 5 @ RPE 8" or "4 sets @ RIR 2."

8. **Apply these rules:**

   | Scenario | Action | Example |
   |---|---|---|
   | Actual RPE < Prescribed RPE by ≥1 point | Add 1 rep to remaining sets or increase load by 2.5–5% next session | Prescribed RPE 8, actual RPE 6 → Add 1 rep or 5% load next week |
   | Actual RPE = Prescribed RPE (±0.5) | Keep load and reps constant | Prescribed RPE 8, actual RPE 7.8 → Repeat same load next session |
   | Actual RPE > Prescribed RPE by ≥1 point | Reduce reps on remaining sets by 1–2, or reduce load by 2.5–5% | Prescribed RPE 8, actual RPE 9.5 → Drop to 3 reps or 5% less load |
   | RIR is consistently 0 when target is RIR 1–2 | Increase caution in next session; reduce load or reps further | Training hard sessions in a row; drop to RIR 2–3 target |
   | RIR is consistently ≥2 when target is RIR 0–1 | You have room to push; add reps or 2.5–5% load next session | Feeling strong and overshooting RIR targets regularly |

9. **Do NOT ignore contextual notes.** If RPE is higher than usual but sleep was poor, rest before increasing load. If RPE is lower and you haven't skipped workouts, confidence in the autoregulation decision is high — proceed.

### Phase 4 — Track and Iterate

10. **Keep a session log** with: date, exercise, reps performed, actual RPE, actual RIR, decision made, contextual notes (sleep, stress, etc.). After 3–4 weeks, review the log.

11. **Check for calibration drift.** If actual RIR consistently misses your estimate by >1 rep, recalibrate your anchors (return to Phase 1, step 2). This is normal; body awareness improves with practice.

12. **Assess progression rate.** If you are increasing load or reps every session, autoregulation is working and stress accumulation is controlled. If you plateau for ≥2 weeks despite adequate recovery, suspect fatigue or miscalibration.

## Evaluation Criteria

| Check | Pass |
|---|---|
| RPE/RIR anchors established for the exercise with at least 3 reference points | Y/N |
| Baseline anchors tested against a known load and calibration error estimated | Y/N |
| RPE and RIR recorded for every working set, with no estimates guessed post-hoc | Y/N |
| Contextual modifiers (sleep, stress, fatigue) noted for sets with unexpected RPE/RIR | Y/N |
| Autoregulation decisions follow the rules table without exception or override | Y/N |
| Session log maintained for ≥3 weeks before iteration | Y/N |

## Red Flags

- RPE and RIR are not correlated. (A set at RPE 9 should have RIR 0–1, not RIR 3.) This signals calibration failure or inconsistent rating — return to Phase 1.
- RIR is always estimated as 0, even on lighter sets. You are likely conflating RPE with RIR or pushing to failure on every set, defeating the purpose of autoregulation.
- Contextual notes are absent. Without sleep/stress/fatigue data, you cannot distinguish a true inability to progress from a temporary dip in recovery.
- Autoregulation rules are overridden because "you felt like it." The system only works if decisions follow the rules. Ad-hoc adjustments introduce bias and stall progress.
- Baseline anchors are set once and never revisited. After 6–12 weeks of training, your capacity changes and anchors should be recalibrated.

## Output Format

```
## RPE/RIR Autoregulation Log

**Exercise:** <name>
**Session date:** <date>
**Sleep (hours prior night):** <number>
**Stress level (1–5):** <rating>

### Set Ratings
| Set | Target Reps | Actual Reps | RPE | RIR | Notes |
|---|---|---|---|---|---|
| 1 | <n> | <n> | <x.x> | <n> | <any > |
| 2 | <n> | <n> | <x.x> | <n> | <anomalies noted> |
| 3 | <n> | <n> | <x.x> | <n> | |

### Decision & Next Session Plan
- **Prescribed target:** <e.g., "3 × 5 @ RPE 8">
- **Actual average RPE:** <x.x>
- **Actual average RIR:** <x.x>
- **Decision:** <Keep load | Add reps | Increase load | Reduce load>
- **Justification:** <one sentence citing the rule applied>
- **Next session plan:** <e.g., "4 × 5 @ RPE 8" or "5% load increase, target RIR 2">

### Calibration Check
- **RIR estimate error (actual − predicted):** <±n reps>
- **Recalibration needed?:** <Yes/No>

### Confidence
<high | medium | low> — <Rationale: e.g., "high — contextual notes stable, RIR estimates within ±1 rep, no sleep deficit" or "medium — poor sleep may have inflated RPE by ~0.5 points; next session will clarify">
```
---
