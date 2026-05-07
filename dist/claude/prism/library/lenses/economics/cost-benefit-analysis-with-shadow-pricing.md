---
name: cost-benefit-analysis-with-shadow-pricing
display_name: Cost-Benefit Analysis with Shadow Pricing
class: lens
underlying_class: native
domain: economics
source: A.C. Pigou (The Economics of Welfare, 1920); formalized in UNEP cost-benefit guidance and applied in infrastructure appraisal (HM Treasury Green Book)
best_for:
  - Valuing non-market goods (environmental, social, health impacts)
  - Infrastructure and policy decisions where market prices don't exist or are distorted
  - Comparing projects across sectors with heterogeneous externalities
one_liner: "Monetize non-market values via shadow prices to strengthen social welfare evaluation."
---

# Cost-Benefit Analysis with Shadow Pricing

## Overview
Standard cost-benefit analysis compares monetized costs and benefits; shadow pricing extends this to non-market goods by inferring their implicit economic value from revealed or stated preferences. When a decision involves environmental degradation, health impacts, or social outcomes with no price tag, shadow pricing estimates what those goods are "worth" in the same currency as the marketed inputs. Practitioners use this when a project's true economic impact cannot be captured by market transactions alone — and when ignoring the unmeasured benefit or cost would bias the decision badly.

## Analytical Procedure

### Phase 1 — Scope the Decision and Identify Non-Market Impacts

1. **State the decision in one sentence.** Example: "Should we build a dam in this river valley?" Avoid embedding the answer.

2. **List all costs and benefits of the project** — both market (e.g., construction materials, labor, electricity revenue) and non-market (e.g., habitat loss, flood risk reduction, cultural site impact, air quality change).

3. **Flag every impact with no observed market price.** Common categories:
   - Environmental: species habitat, water quality, carbon sequestration, air pollutants
   - Health: mortality risk reduction, morbidity, occupational injury prevention
   - Social: cultural heritage, recreation access, community cohesion, equity
   - Option value: value of preserving choice for future generations

4. **For each non-market impact, write a unit of measurement.** Not "carbon is important" but "10,000 metric tons of CO₂ avoided annually" or "habitat loss of 50 hectares." Quantification comes before pricing.

### Phase 2 — Choose Shadow Pricing Method

5. **For each non-market impact, select a pricing method based on the data available.** No single method works for all. Document your choice and why:

   - **Revealed Preference (Market Analogs)**
     - Use when: Similar goods are traded in related markets
     - Example: Hedonic pricing (house price variation with air quality reveals air quality's value)
     - Example: Travel cost method (spending on trips to a recreation site reveals value of that site)
     - Strength: Grounded in actual choices
     - Weakness: Market may be thin, biased, or far removed from the good in question

   - **Stated Preference (Contingent Valuation / Choice Experiment)**
     - Use when: No market analog exists and you can survey the affected population
     - Example: Willingness-to-pay surveys for preserving a forest
     - Strength: Directly asks people what they'd sacrifice
     - Weakness: Hypothetical bias; respondents may strategically misstate preferences

   - **Benefit Transfer**
     - Use when: A similar non-market good was priced in another study or location
     - Example: Apply per-hectare wetland values from published studies to your wetland loss
     - Strength: Fast, low-cost
     - Weakness: Context specificity is high; transfer error is common and often unquantified

   - **Production Function Approach**
     - Use when: The non-market good is an input to market production
     - Example: Pollinator loss reduces crop yield; value crop yield loss
     - Strength: Chains to observable market outcomes
     - Weakness: Requires knowing the ecological/physical relationship precisely

   - **Replacement Cost / Damage Avoidance**
     - Use when: You can estimate the cost to replicate or prevent the loss
     - Example: Cost of treating water to remove a pollutant now present = value of water quality lost
     - Strength: Conservative; grounds valuation in real expenditure
     - Weakness: Replacement cost ≠ actual willingness-to-pay (may overstate or understate)

6. **For each method chosen, list the data sources and assumptions:**
   - What study, market, or survey is being used?
   - What population's preferences is this value derived from? (local users, national public, global?)
   - What time period or conditions?
   - What adjustments were made for inflation, distribution, or scope?

7. **Sensitivity analysis: price each impact using two methods if possible.** The range between them bounds your confidence in the shadow price.

### Phase 3 — Monetize and Integrate

8. **Multiply each non-market quantity by its shadow price.** Create a line-item table:
   | Impact | Unit | Quantity | Shadow Price ($/unit) | Total Value ($) | Method |
   |---|---|---|---|---|---|
   | CO₂ avoided | metric ton | 10,000 | 50 | 500,000 | Damage cost (IPCC SCC) |
   | Habitat loss | hectare | 50 | 25,000 | 1,250,000 | Benefit transfer (published studies) |
   | Health benefits | Life-years saved | 3 | 100,000 | 300,000 | Stated preference (VSL) |

9. **Add shadow-priced impacts to the standard CBA table:**
   | Category | Market (Net) | Non-Market (Net) | Total |
   |---|---|---|---|
   | Costs | -$5M | -$2M | -$7M |
   | Benefits | $8M | $2M | $10M |
   | **NPV** | **+$3M** | **0** | **+$3M** |

10. **Recalculate the decision metric** (NPV, IRR, benefit-cost ratio) with shadow prices included. Compare it to the market-only metric; if the ranking or sign flips, the non-market impacts are decision-critical.

### Phase 4 — Document and Interrogate

11. **For each shadow price used, fill in a single source-justification row:**
    - What is the source document or study?
    - What population does it represent?
    - How transferable is it to your context? (geography, time, preferences)
    - What is the plausible range (low / central / high estimate)?
    - If the price was adjusted (e.g., inflation, scaling), show the calculation.

12. **Test for incoherence:** If you have priced the same outcome using two methods, do the values diverge wildly (more than 2×)? If yes, investigate why. If the methods are equally defensible, report both and note the decision is sensitive to method choice.

13. **Check for double-counting:** Ensure the same benefit or cost isn't captured twice under different names (e.g., "health benefit from pollution reduction" should not also appear as "increased productivity from less sick days" unless you've carefully isolated the non-overlapping part).

## Evaluation Criteria

| Check | Pass |
|---|---|
| All non-market impacts identified and quantified in physical units | Y/N |
| Each shadow price has a named method and data source | Y/N |
| No shadow price is used without a plausible range (low/central/high) | Y/N |
| Benefit transfer (if used) includes a statement of transferability risk | Y/N |
| Double-counting check completed; no outcome priced twice | Y/N |
| Sensitivity analysis shows decision reversal risk (if any) | Y/N |
| Discount rate and time horizon chosen and justified | Y/N |

## Red Flags

- A non-market impact is left unpriced on grounds of "immeasurable" without attempting any method. All valuation methods have limits, but giving up abandons the analysis.
- Shadow prices are borrowed wholesale from a textbook or prior study with no discussion of context fit. Benefit transfer requires explicit transferability reasoning.
- The monetized total for a large impact (e.g., habitat loss or health effect) is presented without showing the underlying quantity × price calculation. The reader cannot reverse-engineer it.
- Two shadow price methods give contradictory results (e.g., stated preference: $5K/hectare; benefit transfer: $50K/hectare) and the divergence is not investigated or explained in the final report.
- The discount rate applied to future non-market benefits is not stated. This is often the largest lever on NPV; omitting it hides a major assumption.
- Willingness-to-pay estimates come from a population far removed from the affected community (e.g., national survey for a local health impact) without discussing whether preferences should be weighted.

## Output Format

```
## Cost-Benefit Analysis with Shadow Pricing

**Decision:**
<one sentence: what are we evaluating?>

### Phase 1 — Non-Market Impacts Identified
| Impact | Unit | Quantity | Market Price Available? | Y/N |
|---|---|---|---|---|
| <...> | <...> | <...> | |

### Phase 2 — Shadow Pricing Methods
| Impact | Method | Data Source | Transferability / Justification |
|---|---|---|---|
| <...> | Revealed/Stated/Benefit Transfer/Production Function/Damage Avoidance | <...> | <...> |

### Shadow Price Detail (for each impact)
**Impact: <name>**
- Method: <name>
- Source: <citation>
- Base value: $<X> per <unit>
- Adjustment applied (if any): <inflation, scope, etc.>
- Plausible range: $<low> to $<high>
- Reasoning for range: <what drives uncertainty?>

### Phase 3 — Monetized Impacts
| Impact | Unit | Qty | Shadow Price $/unit | Total $ | Method |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <...> |
| **Subtotal Non-Market** | | | | <$X> | |

### Full Cost-Benefit Table
| Category | Market Value | Non-Market Value | Total |
|---|---|---|---|
| **Costs** | <$X> | <$Y> | <$X+Y> |
| **Benefits** | <$X> | <$Y> | <$X+Y> |
| **Net Present Value** | <$> | <$> | <$> |

### Sensitivity Analysis
| Scenario | CBA Result (Market Only) | CBA Result (with Shadow Prices) | Decision Impact |
|---|---|---|---|
| Central | <NPV> | <NPV> | <same/reversed> |
| Shadow prices at low end | — | <NPV> | <same/reversed> |
| Shadow prices at high end | — | <NPV> | <same/reversed> |

### Double-Count Check
- Outcomes priced once and only once: Y/N
- Overlapping benefits identified and resolved: Y/N

### Confidence
<high | medium | low> — <justification: which shadow prices have reliable methods? which rely on transfer or extrapolation? does decision reverse under plausible ranges?> 
```
