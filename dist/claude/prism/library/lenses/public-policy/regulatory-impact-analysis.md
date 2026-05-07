---
name: regulatory-impact-analysis
display_name: Regulatory Impact Analysis (OECD RIA)
class: lens
underlying_class: native
domain: public-policy
source: OECD, Regulatory Policy Committee; standardized across member states since 2008
best_for:
  - Comparing policy options on net welfare and distributional effects
  - Building evidence-based policy recommendations with quantified trade-offs
  - Identifying unintended consequences and regressive impacts before implementation
one_liner: "Compare policy options on cost-benefit and distributional impact, quantify trade-offs, and recommend with confidence."
---

# Regulatory Impact Analysis (OECD RIA)

## Overview
Regulatory Impact Analysis is a structured method for evaluating policy options by comparing their costs, benefits, and distributional effects across affected populations. Rather than defending a preferred option, RIA forces comparison across at least two alternatives (including the status quo) using a common evidence standard. Practitioners use it before enacting regulation to avoid costly mistakes, to make distributional inequities visible, and to build political consensus by showing whose interests are served.

## Analytical Procedure

### Phase 1 — Problem Definition and Option Scoping

1. **State the policy problem in one sentence.** Define the market failure, externality, or social objective that justifies intervention. Example: "Insufficient disclosure of mortgage terms leads borrowers to underestimate default risk."

2. **Identify the affected population(s).** List groups who will bear costs or receive benefits. Include: consumers, businesses (by size/sector), workers, taxpayers, vulnerable populations (elderly, low-income, rural).

3. **Define the baseline (status quo).** Describe the current regulatory and market state. If the baseline is already changing (e.g., technology adoption, demographic shift), state the counterfactual scenario you are comparing against.

4. **List at least three policy options** including:
   - Option A: No further intervention (status quo)
   - Option B: Your preferred or most ambitious option
   - Option C: A lighter-touch alternative (e.g., voluntary standard, targeted subsidy, public information campaign)
   - Optional: Option D if there is a fundamentally different approach (e.g., tax vs. regulation)
   Each option must be concrete enough to cost.

### Phase 2 — Cost-Benefit Analysis

5. **For each option, enumerate all costs and benefits.** Use this table structure:

| Affected Party | Benefit / Cost | Category | Timing | Magnitude (est.) | Confidence |
|---|---|---|---|---|---|
| Borrowers | Reduced default risk (benefit) | Avoided loss | Year 1–5 | $X per person | Low/Med/High |
| Lenders | Reduced compliance cost (benefit) | Operational | Year 1+ | $Y per firm | Med |
| Lenders | Loan origination delay (cost) | Operational | Year 1 | Z days, $K per loan | High |

   - **Category:** Operational, Compliance, Avoided harm, Distributional, Macroeconomic, Environmental, Social (e.g., trust, health, safety)
   - **Timing:** When does this effect appear? Immediate, gradual, one-time, recurring?
   - **Magnitude:** Monetize where possible. If non-monetary, describe the unit and direction.
   - **Confidence:** High = market data or empirical study; Medium = reasonable extrapolation from analogous cases; Low = expert judgment or assumption.

6. **Calculate net cost-benefit for each option.** Sum benefits minus costs. If you cannot monetize, state it separately as a "qualitative finding." Example: "Option B prevents estimated 500 defaults per year (high confidence), avoiding ~$50M in borrower losses. Compliance cost to lenders is ~$30M (medium confidence, based on similar UK disclosure rule). Net benefit: ~$20M annually."

7. **Compute the benefit-cost ratio** for each option (B/C). If B/C > 1, the option passes the efficiency test. If B/C < 1, the option is net negative for society (though it may still be chosen for distributional reasons).

### Phase 3 — Distributional Analysis

8. **For each option, show who wins and who loses.** Create a distributional matrix:

| Population | Option A (Status Quo) | Option B (Preferred) | Option C (Light) | Net Change from Status Quo |
|---|---|---|---|---|
| Low-income households | $0 cost, X% default rate | $Y compliance cost, 0.5X% default rate | No cost, 0.8X% default rate | Win / Lose / Neutral |
| High-income households | $0 cost, 0.1X% default rate | $Y cost, 0.05X% default rate | No cost, 0.1X% default rate | Win / Lose / Neutral |
| Small lenders | $0, normal profit | $Z operating cost, Y% margin compression | $W cost, Z% margin change | |
| Large banks | $0, high profit | $Z cost (absorb), margin stable | $W cost, stable margin | |

   - Enter quantified impacts (cost, rate, margin, access) or qualitative direction (improves/worsens).
   - Highlight regressive effects (i.e., costs fall disproportionately on low-income groups).

9. **Assess fairness and equity.** For regressive or ambiguous impacts, state why the distributional outcome is justified (e.g., "compliance cost is regressive but affects <5% of affected households and overall welfare gain is large," or "option is inequitable and should be paired with a subsidy for vulnerable groups").

### Phase 4 — Scenario and Sensitivity Testing

10. **Run each option under three scenarios:** base case (your best estimate), optimistic (benefits larger, costs smaller), and pessimistic (benefits smaller, costs larger). Shade confidence ranges. Example:
    - Base: B/C = 1.8 (medium confidence)
    - Optimistic: B/C = 2.5 (if take-up is 80% instead of 60%)
    - Pessimistic: B/C = 0.9 (if compliance cost is 2× estimate)

11. **Test sensitivity to key assumptions.** For each major input (discount rate, take-up rate, lender response, behavioral assumption), vary it ±20% and recompute. Flag inputs where ±20% swing flips the recommendation (high sensitivity = high risk if assumption is wrong).

### Phase 5 — Risk, Unintended Consequences, and Alternatives

12. **Identify foreseeable unintended consequences.** For each option, list second-order effects:
    - **Behavioral response:** Will regulated parties evade, adapt, or exit? Example: "If mortgage disclosure is too burdensome, lenders may tighten credit, reducing access for marginal borrowers."
    - **Competitive effects:** Does the rule favor some firms over others (e.g., hurts small lenders disproportionately)?
    - **Systemic risk:** Could the rule amplify financial instability, sectoral concentration, or moral hazard?
    - **Political risk:** Is the rule durable or at high risk of repeal if costs materialize?

13. **Compare options on:
    - Effectiveness (does it solve the stated problem?)
    - Efficiency (lowest cost per unit of problem solved?)
    - Distributional fairness (who bears the burden?)
    - Administrability (can regulators enforce it?)
    - Durability (can it be sustained politically and technically?)

### Phase 6 — Recommendation and Confidence

14. **Rank the options.** Use a decision matrix:

| Criterion | Weight | Option A | Option B | Option C |
|---|---|---|---|---|
| Net benefit (B/C ratio) | 40% | 0.8 | 1.8 | 1.2 |
| Equity (avoids regressivity) | 30% | 0 (no change) | −2 (costs low-income more) | 0 (neutral) |
| Administrability | 20% | 5 | 2 | 5 |
| Durability | 10% | 5 | 3 | 4 |
| **Weighted score** | | **2.3** | **1.9** | **2.5** |

   Adjust weights based on political and ethical priorities (efficiency vs. equity trade-off).

15. **State your recommendation.** Recommend the option with the highest weighted score or the best trade-off if scores are close. If no option has B/C > 1, recommend status quo unless equity or non-economic criteria dominate.

16. **Justify the recommendation.** Example: "Option C is recommended because it achieves 67% of Option B's net benefit at 60% of the cost, imposes no distributional burden, and is more durable politically. Option B should be revisited if future evidence shows take-up rates exceed 70%."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem statement is a single, specific sentence (not vague or multi-part) | Y/N |
| At least three distinct policy options are defined and costed | Y/N |
| All major costs and benefits across affected parties are enumerated | Y/N |
| Benefits and costs are monetized or quantified with confidence tags | Y/N |
| Distributional analysis shows impact by income, firm size, or other relevant axis | Y/N |
| Sensitivity testing varies ≥3 key assumptions and flags reversals | Y/N |
| Unintended consequences are named (behavioral, competitive, systemic, political) | Y/N |
| Recommendation is justified by comparison, not preference | Y/N |

## Red Flags

- Only two options analyzed (status quo and preferred option). Missing a middle ground or alternative approach.
- All costs and benefits are "medium confidence" or lower. This signals the analysis is speculative; stronger evidence is needed before implementation.
- No distributional analysis. The analysis ignores who loses and assumes aggregate net benefit is sufficient.
- Unintended consequences section is empty or generic ("unintended impacts may occur"). Real implementation always surfaces real surprises; missing them means the analysis wasn't adversarial.
- Recommendation is stated as a preference ("we believe Option B is best") rather than derived from evidence comparison. The analysis is advocacy, not analysis.
- Sensitivity analysis shows recommendation reverses under plausible scenarios (e.g., if take-up is 20% lower). Analysis is too fragile to act on.
- Baseline/counterfactual is vague or assumed stable. If the status quo is already changing, comparison is misleading.

## Output Format

```
## Regulatory Impact Analysis

**Policy Problem:**
<one sentence defining the market failure or objective>

**Baseline (Status Quo):**
<current regulatory and market state; counterfactual if baseline is dynamic>

### Policy Options
1. **Option A:** <concrete description, e.g., status quo with no new regulation>
2. **Option B:** <preferred or ambitious option>
3. **Option C:** <lighter-touch alternative>

### Cost-Benefit Analysis

| Option | Total Benefits | Total Costs | Net Benefit | B/C Ratio | Confidence |
|---|---|---|---|---|---|
| A | $X | $Y | $X−Y | X/Y | Med/High |
| B | $X' | $Y' | $X'−Y' | X'/Y' | Med |
| C | $X'' | $Y'' | $X''−Y'' | X''/Y'' | Low/Med |

### Distributional Impact

| Population | Option A | Option B | Option C | Fairness Assessment |
|---|---|---|---|---|
| Low-income | <cost/benefit> | <cost/benefit> | <cost/benefit> | Regressive / Neutral / Progressive |
| Mid-income | <...> | <...> | <...> | |
| High-income | <...> | <...> | <...> | |
| Small firms | <...> | <...> | <...> | |
| Large firms | <...> | <...> | <...> | |

### Sensitivity Analysis
- **Base case:** Option B, B/C = 1.8
- **Optimistic:** B/C = 2.5 (if take-up is 80%)
- **Pessimistic:** B/C = 0.9 (if compliance cost is 2×)
- **Reversals:** Recommendation flips if <key assumption changes by >X%>

### Unintended Consequences
1. **Behavioral response:** <e.g., lenders tighten credit>
2. **Competitive effects:** <e.g., hurts small firms>
3. **Systemic risk:** <e.g., concentration effects>
4. **Political durability:** <e.g., rule at risk of repeal>

### Recommendation
**Recommended option:** Option [A/B/C]

**Justification:**
<Ranked comparison on effectiveness, efficiency, equity, administrability, durability. Why this option trades off benefits and costs best.>

**Conditions for revision:**
<If X evidence emerges, reconsider Option Y. If cost estimates exceed $Z, implement Phase 2 monitoring.>

### Confidence
<high/medium/low> — <Justify confidence in recommendation: evidence quality, distributional certainty, unintended consequence risk, political durability risk>
```
