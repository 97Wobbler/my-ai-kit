---
name: dfss
display_name: Design for Six Sigma (DMADV)
class: lens
underlying_class: native
domain: manufacturing
source: Mikel Harry and Richard Schroeder (Motorola/GE); formalized 2000s
best_for:
  - New product design with tight tolerance and defect-rate targets
  - Translating customer voice into hard specifications before prototyping
  - Eliminating design-stage rework by front-loading variation analysis
one_liner: "Design for Six Sigma — translate customer needs into strict specifications and remove variability up front."
---

# Design for Six Sigma (DMADV)

## Overview
DMADV (Define, Measure, Analyze, Design, Verify) is a structured methodology for designing new products or services to meet customer requirements with minimal defect rates from the start. Unlike DMAIC (which improves existing processes), DMADV targets the design phase itself—translating voice-of-customer data into measurable specifications, analyzing failure modes before tooling, and verifying the design meets targets before production release. Practitioners use this when the cost of design rework or field defects is high, and when customer expectations are tight enough that iteration is expensive.

## Analytical Procedure

### Phase 1 — Define

1. **Articulate the project charter.** State the business case in one sentence: what problem does this product solve, for whom, and what is the financial impact of failure?

2. **Collect voice-of-customer (VOC) data.** Conduct interviews, surveys, or observational studies with ≥20 representatives of the target user population. Record verbatim customer statements about what matters to them. Document context: who said it, under what conditions, how many customers echoed it.

3. **Translate VOC into critical-to-quality (CTQ) characteristics.** For each customer need, identify the measurable attribute that matters. Example:
   - VOC: "This widget doesn't jam in the summer."
   - CTQ: "Operational temperature range −10°C to +60°C without malfunction."
   - Measurable: Binary pass/fail after thermal cycling test.

4. **Prioritize CTQs by impact and difficulty.** Use a 2×2 matrix: plot each CTQ by (customer impact: high/low) and (our ability to design for it: high/low). Focus on high-impact, high-difficulty CTQs first.

5. **Write a process SIPOC** (Supplier, Input, Process, Output, Customer):
   - What inputs does the design require?
   - Who provides them, and at what specification?
   - What does the design output, and who receives it?
   - This forces clarity on handoffs and dependencies.

### Phase 2 — Measure

6. **Define measurement systems for each CTQ.** For each critical-to-quality characteristic, specify:
   - Exact measurement method (instrument, procedure, acceptance criteria).
   - Repeatability: Can the same person get the same result twice? (Run the measurement twice, calculate variation.)
   - Reproducibility: Do different people get the same result? (Have 2–3 people run the measurement independently, compare.)
   - If R&R (repeatability and reproducibility) exceeds 10% of tolerance, the measurement is unreliable — improve the method before proceeding.

7. **Establish baseline data.** If a legacy product or competitor product exists, measure it against the CTQs. This defines what "normal" looks like and what improvement margin exists.

8. **Set target specifications.** For each CTQ, define:
   - Nominal (ideal) value.
   - Upper and lower specification limits (USL, LSL).
   - Justification: customer need, physics, regulatory, manufacturing capability, or cost-trade.
   Example: "Target nominal 25mm, USL 25.5mm, LSL 24.5mm because tighter tolerance adds $0.50/unit and customer testing shows ±0.5mm is imperceptible."

### Phase 3 — Analyze

9. **Conduct Failure Mode and Effects Analysis (FMEA) on the conceptual design.** For each component or subsystem:
   - List potential failure modes (ways it could fail to meet CTQ).
   - For each failure mode, assign Severity (1–10: how bad if it happens), Occurrence (1–10: how likely), and Detection (1–10: how hard to catch before shipment).
   - Calculate Risk Priority Number (RPN) = Severity × Occurrence × Detection.
   - Focus on failure modes with RPN > 100 or Severity ≥ 8.

10. **Analyze design sensitivity to variation.** Use design of experiments (DOE) or simulation to test how small changes in input parameters affect CTQ output. Example:
    - Vary wall thickness ±10% and measure impact on strength and weight.
    - Vary material supplier and measure impact on thermal stability.
    - Identify which parameters are "critical" (small changes → big CTQ impact) and which are "robust" (variation is absorbed).

11. **Map tolerance stack-up.** If the CTQ depends on multiple components stacked together, calculate:
    - Worst-case stack: Σ(upper deviations) − Σ(lower deviations). Does it exceed CTQ tolerance?
    - Statistical stack: √(Σ(component tolerances)²). More realistic for normal distribution.
    - If stack-up exceeds CTQ tolerance, tighten component tolerances (costly) or redesign (rethink assembly).

### Phase 4 — Design

12. **Generate design alternatives.** Working from CTQs and the FMEA results, sketch ≥3 materially different approaches to meet the specification. Do not converge on one design yet. Use brainstorm rules: defer judgment, build on others' ideas, encourage wild ideas.

13. **Score each design against CTQs and manufacturability.** Create a matrix:
    - Rows: CTQs and secondary criteria (cost, tooling time, supply chain risk, repairability).
    - Columns: Each design alternative.
    - Score each cell (e.g., 1–5 or qualitative). Weight rows by importance.
    - Select the design with highest weighted score, not by gut feel.

14. **Prototype and test the selected design.** Build a prototype and run tests against each CTQ:
    - Does it pass? Record the margin (how far from limit?).
    - Does it fail? Why? Document the failure mode and trigger.
    - If margin is < 30% on any CTQ, revisit the design now. Field designs with razor-thin margins become expensive problems in production.

15. **Design for manufacturing (DFM) review.** Bring manufacturing, supply chain, and quality engineers into the room:
    - Can this be made repeatably with current tooling, or is new tooling needed (cost/lead time impact)?
    - Are material sources secure? Any single-source risk?
    - Are tolerances achievable with standard processes, or do they demand special techniques (cost)?
    - Are there assembly steps that are error-prone?
    Write a DFM report identifying cost and risk drivers.

### Phase 5 — Verify

16. **Conduct design verification testing (DVT).** Build ≥10 units (or the first production run if cost permits) and run ≥500 hours / ≥1000 cycles of real-world testing:
    - Measure all CTQs under stress (temperature extremes, humidity, vibration, user abuse scenarios).
    - Document failure: when, how, under what conditions.
    - Measure capability: calculate process capability index (Cpk). Target Cpk ≥ 1.33 (Six Sigma quality).
      - Cpk = min((USL − mean) / (3 × stdev), (mean − LSL) / (3 × stdev)).
      - Cpk < 1.0: unacceptable. Cpk 1.0–1.33: marginal. Cpk > 1.33: acceptable.

17. **Validate design against customer needs.** If possible, put the prototype in the hands of 5–10 real end users for 2–4 weeks. Collect feedback:
    - Do the CTQs we chose actually matter to them?
    - Are there unstated needs we missed?
    - Is the product fit for purpose under real conditions?

18. **Generate design documentation (design history file / DHF):**
    - Customer requirements and CTQ mapping.
    - Design FMEA results and mitigations.
    - Design specifications and tolerance justifications.
    - DVT test results and capability indices.
    - DFM report and production readiness assessment.
    - Any design changes made post-verification and their rationale.
    This becomes the baseline for future changes and audits.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Every customer need was captured in ≥1 CTQ | Y/N |
| CTQ measurement systems have R&R < 10% of tolerance | Y/N |
| FMEA completed with RPN calculations for all high-risk failure modes | Y/N |
| Tolerance stack-up (worst-case and statistical) was calculated | Y/N |
| ≥3 design alternatives were generated and scored objectively | Y/N |
| Prototype was built and tested against all CTQs before DVT | Y/N |
| DVT included ≥10 units under stress (thermal, vibration, user scenarios) | Y/N |
| Cpk calculated from DVT data; Cpk ≥ 1.33 on all CTQs or deviations documented | Y/N |
| Design History File completed with traceability to customer needs | Y/N |

## Red Flags

- CTQs are vague or not measurable ("reliable," "durable," "user-friendly"). Vague CTQs guarantee rework.
- FMEA exists but RPN > 100 failure modes have no documented mitigation or design change.
- Tolerance stack-up was never calculated. You will discover this problem in production, not now.
- Only one design alternative was generated. Single-solution design is driven by habit, not analysis.
- Prototype testing showed failures, but the design was released anyway with a "we'll fix it post-launch" note. Post-launch fixes are 10× more expensive.
- DVT sample size is < 5 units or test duration is < 100 hours. You have no statistical confidence in Cpk.
- Cpk < 1.33 on any CTQ but production proceeds. Six Sigma target exists for a reason: field defect rates spike below 1.33.
- No design change log. If you can't trace which part of the design came from which customer need or FMEA, you have no control over variants.

## Output Format

```
## DMADV Design Verification Report

**Product / Project:**
<name and business case>

### Phase 1 — Define
**Voice-of-Customer Summary:**
- Customer need 1: <verbatim quote> [n= respondents]
- Customer need 2: ...

**Critical-to-Quality (CTQ) Map:**
| Customer Need | CTQ Characteristic | Measurable Attribute | Justification |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

**CTQ Prioritization (2×2 Matrix):**
- High impact, high difficulty: <list>
- High impact, low difficulty: <list>
- Low impact, high difficulty: <list>

**Process SIPOC:**
| Element | Description |
|---|---|
| Supplier | <...> |
| Input | <...> |
| Process | <...> |
| Output | <...> |
| Customer | <...> |

### Phase 2 — Measure
**CTQ Measurement Systems:**
| CTQ | Method | R&R | Pass |
|---|---|---|---|
| <...> | <...> | <...>% | Y/N |

**Target Specifications:**
| CTQ | Nominal | LSL | USL | Justification |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### Phase 3 — Analyze
**Failure Mode and Effects Analysis (FMEA) — High RPN Modes:**
| Failure Mode | Severity | Occurrence | Detection | RPN | Mitigation |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <...> |

**Design Sensitivity Analysis:**
- Critical parameters (variation → large CTQ impact): <list>
- Robust parameters (variation absorbed): <list>

**Tolerance Stack-up (Example: CTQ A):**
- Worst-case: ±<value> (exceeds/within spec)
- Statistical: ±<value> (exceeds/within spec)
- Action: <adjust tolerances / redesign / accept>

### Phase 4 — Design
**Design Alternatives Scored:**
| Criterion | Weight | Alt 1 Score | Alt 2 Score | Alt 3 Score |
|---|---|---|---|---|
| <...> | <...>% | <...> | <...> | <...> |
| **Total** | **100%** | **<...>** | **<...>** | **<...>** |

**Selected Design:** <name> (reason: highest score, or <reason>)

**Prototype Test Results:**
| CTQ | Target | Result | Margin % | Status |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | Pass/Fail |

**Design for Manufacturing (DFM) Summary:**
- Tooling required: <yes/no; lead time; cost>
- Supply chain risk: <critical materials; single-source items>
- Process capability: <achievable tolerances; special techniques needed>
- Assembly risk: <high-error-rate steps; mitigation>

### Phase 5 — Verify
**Design Verification Test (DVT) Plan:**
- Sample size: <N units>
- Test duration / cycles: <...>
- Stress conditions: <thermal, vibration, user scenarios>
- Capability index target: Cpk ≥ 1.33

**DVT Results:**
| CTQ | Mean | StDev | Cpk | Margin % | Status |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | Pass/Fail |

**Customer Validation:**
- End-user feedback period: <...> weeks, <N users>
- Unmet needs discovered: <list or "none">
- CTQ confirmation: <all met / some questioned / major rework needed>

**Design History File Status:**
- [ ] Customer requirements mapped to CTQs
- [ ] FMEA and mitigations documented
- [ ] Design specifications and tolerances justified
- [ ] DVT test results and Cpk recorded
- [ ] DFM report and production readiness assessment completed
- [ ] Design changes (post-verification) logged with rationale

### Confidence
<high | medium | low> — <justification: e.g., "High: DVT sample n=12, Cpk ≥ 1.5 on all CTQs, customer validation complete. Medium: Cpk borderline on CTQ-3 (1.32), supply chain risk on material source. Low: Limited real-world use data; DVT did not include long-term aging scenario.">
```
