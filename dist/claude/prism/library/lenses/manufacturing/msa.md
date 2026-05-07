---
name: msa
display_name: Measurement System Analysis
class: lens
underlying_class: native
domain: manufacturing
source: AIAG (Automotive Industry Action Group); Minitab; origin formalized in quality engineering circa 1990s
best_for:
  - Quantifying whether measurement variation is acceptable or is masking real process variation
  - Deciding if a gauge or measurement protocol is fit for purpose before process improvement
  - Identifying which measurement sources (operator, instrument, environmental) contribute most to total variation
one_liner: "Measurement system analysis — quantify repeatability and reproducibility to judge measurement trust."
---

# Measurement System Analysis

## Overview
Measurement System Analysis (MSA) quantifies how much of the observed variation in a process comes from the measurement system itself versus the actual process. When measurement error is large relative to process tolerance or process variation, you cannot trust the data — control charts will be false alarms, capability indices will be wrong, and process improvement efforts will chase measurement noise. Practitioners use MSA before launching control charts, before making process decisions, and whenever a measurement method is new or suspected to be unstable.

## Analytical Procedure

### Phase 1 — Design and Data Collection

1. **Define the measurement characteristic.** Write down exactly what is being measured, the units, and the tolerance or specification limits. Example: "Bolt hole diameter, tolerance 10.00 ± 0.10 mm."

2. **Identify all sources of measurement variation.** List:
   - Repeatability: variation when the same operator measures the same part repeatedly with the same instrument.
   - Reproducibility: variation when different operators measure the same part(s) with the same instrument.
   - Environmental factors: temperature, humidity, vibration, lighting (if these affect the measurement).
   - Part-to-part: the actual variation in the process you are trying to measure.

3. **Select parts for the study.** Choose 10 parts that span the full range of process output (smallest, largest, and typical parts). These parts must be measurable by the system and representative of normal production.

4. **Designate operators.** Use 2–3 operators who will perform the measurements. These should be the people who actually use the measurement system, or trained to the same standard.

5. **Run the measurement replication.** Each operator measures each part 2–3 times in random order (re-randomize between replicates to avoid memory bias). Record all results in a structured table with columns: Part ID, Operator, Replicate 1, Replicate 2, [Replicate 3]. Use the actual measurement instrument(s) as they are used in production.

6. **Record environmental conditions if relevant.** If temperature, humidity, or other factors are suspected to affect the measurement, log them during the study.

### Phase 2 — Calculate Repeatability and Reproducibility

7. **Calculate the range for each part–operator combination.** For each operator–part pair, subtract the minimum replicate from the maximum replicate. These ranges measure repeatability (instrument + operator technique variation on that part).

8. **Calculate the average range across all measurements (R̄).** Sum all ranges, divide by the number of part–operator combinations.

9. **Estimate repeatability (Equipment Variation, EV).**
   - EV = R̄ × K₁
   - K₁ = 2.66 for 2 replicates, K₁ = 3.05 for 3 replicates (constants from control chart theory).
   - This is the inherent precision of the instrument.

10. **For each part, calculate the average of all measurements (X̄ₚ).** Then calculate the range of the part averages across all operators (R_Xbar = max(X̄ₚ) − min(X̄ₚ)).

11. **Estimate reproducibility (Operator/Setup Variation, OV).**
    - Average of operator averages: X̄_operator (average of each operator's grand mean across all parts and replicates).
    - Range of operator averages: R_op = max(X̄_operator) − min(X̄_operator).
    - OV = (R_op × K₂ − (EV / (n × r))) where K₂ = 3.65 for 2 operators, K₂ = 2.70 for 3 operators; n = number of parts; r = number of replicates.
    - If this calculation yields a negative number, set OV = 0 (variation is within noise).

12. **Calculate repeatability and reproducibility combined (R&R).**
    - R&R = √(EV² + OV²)

13. **Calculate part-to-part variation (PV).**
    - Range of part averages: R_parts = max(part average) − min(part average).
    - PV = R_parts × K₃ (where K₃ = 4.56 for 10 parts).

14. **Calculate total variation (TV).**
    - TV = √(R&R² + PV²)

### Phase 3 — Evaluate Acceptability

15. **Calculate % Contribution metrics.**
    - % EV = (EV / R&R) × 100 — what fraction of R&R is the instrument?
    - % OV = (OV / R&R) × 100 — what fraction is the operator/setup?
    - % R&R = (R&R / TV) × 100 — what fraction of total variation is measurement system?
    - % R&R vs. Tolerance = (R&R / Tolerance) × 100 — if you have a specification, compare R&R to it instead of TV.

16. **Apply acceptance thresholds (AIAG standard):**
    - **% R&R < 10%:** System is acceptable.
    - **10% ≤ % R&R < 30%:** System is acceptable if there is no alternative; improvement is recommended.
    - **% R&R ≥ 30%:** System is not acceptable; corrective action is required.
    - Separately, if % EV > 90% of R&R, the instrument itself is the problem. If % OV > 90% of R&R, training or setup standardization is the problem.

17. **Perform discrimination check.** Calculate the Number of Distinct Categories (NDC) = 1.41 × (PV / R&R), rounded down. If NDC ≥ 5, the system can distinguish between process variation. If NDC < 2, the system cannot distinguish anything meaningful.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All 10+ parts span full range of process output | Y/N |
| 2–3 operators used; each measured each part 2–3 times | Y/N |
| No part has zero variation (replicate measurements are not identical) | Y/N |
| EV, OV, R&R, PV, and TV all calculated and recorded | Y/N |
| % EV and % OV breakdowns are clear and sum to 100% | Y/N |
| Acceptance decision made using stated thresholds (10%, 30%) | Y/N |
| NDC is reported and interpreted (acceptable if ≥ 5) | Y/N |

## Red Flags

- All replicates for a part–operator are identical. This is physically implausible and usually indicates measurement resolution is too coarse, or the operator is copying rather than re-measuring.
- % R&R is borderline (24–29%) but no mention of which source (EV or OV) dominates. Without this breakdown, you cannot recommend corrective action.
- The study used only one operator. Reproducibility cannot be assessed; the R&R value is incomplete.
- Parts chosen do not span the tolerance or process range. The R&R estimate will be artificially low because variation was not fully captured.
- Tolerance is unknown or not mentioned. If % R&R is being compared to tolerance, that tolerance must be explicit and correct.
- NDC < 2 but the system is being accepted anyway. If the system cannot distinguish categories, it should not be used for acceptance sampling or control charting.

## Output Format

```
## Measurement System Analysis Report

**Measurement Characteristic:**
<name, units, tolerance/spec limits>

**Study Parameters:**
- Parts: <count> (range of values: <min> to <max>)
- Operators: <count> [names/identifiers]
- Replicates per part–operator: <count>
- Study date: <date>

### Phase 1 — Repeatability (Equipment Variation)
- Average range (R̄): <value>
- Equipment Variation (EV): <value>
- % EV: <percentage>%

### Phase 2 — Reproducibility (Operator/Setup Variation)
- Operator/Setup Variation (OV): <value>
- % OV: <percentage>%

### Phase 3 — Combined R&R
- Repeatability & Reproducibility (R&R): <value>
- % R&R of Total Variation: <percentage>%
- % R&R of Tolerance: <percentage>% [if applicable]

### Phase 4 — Part-to-Part Variation
- Part Variation (PV): <value>
- % PV of Total: <percentage>%

### Total Variation
- Total Variation (TV): <value>

### Acceptability Assessment
| Criterion | Value | Status |
|---|---|---|
| % R&R | <percentage>% | Acceptable / Marginal / Not Acceptable |
| NDC (Number of Distinct Categories) | <count> | Acceptable (≥5) / Marginal (2–4) / Inadequate (<2) |
| Dominant source of variation | EV / OV | <corrective action recommended> |

### Interpretation
<1–2 sentences: whether the system is fit for purpose, and what the next step is (use as-is, improve operator training, upgrade instrument, etc.)>

### Confidence
<high | medium | low> — <justification: e.g., "high — adequate sample size, stable environmental conditions, clear separation of sources"; "medium — borderline % R&R, single environmental condition not controlled"; "low — very small sample, high EV suggests instrument drift">
```
---
