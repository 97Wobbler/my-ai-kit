---
name: bakers-percentage
display_name: Baker's Percentage
class: lens
underlying_class: native
domain: cooking
source: Origin uncertain; formalized in professional baking by mid-20th century
best_for:
  - Scaling bread and pastry recipes consistently across batch sizes
  - Diagnosing balance problems in dough composition
  - Communicating precise ingredient ratios across kitchens and teams
one_liner: "Express every ingredient as a weight ratio relative to flour for scalable, reproducible recipes."
---

# Baker's Percentage

## Overview
Baker's Percentage expresses all ingredients in a formula as a percentage of flour weight, with flour always set to 100%. Instead of scaling by total batch weight (which obscures ingredient relationships), it anchors to the binding agent and builds ratios around it. Practitioners use it when they need to scale recipes reliably, diagnose why a dough is too wet or dry, or communicate a formula across kitchens where ingredient sourcing or batch sizes differ.

## Analytical Procedure

### Phase 1 — Convert to Baker's Percentage

1. **Weigh all ingredients by mass, not volume.** Use grams or ounces consistently. If a recipe lists volume (cups, tablespoons), convert using density:
   - All-purpose flour: 1 cup ≈ 125g
   - Water: 1 cup ≈ 240g
   - Salt: 1 tablespoon ≈ 18g
   - Yeast (instant dry): 1 tablespoon ≈ 9g
   Record all weights in the same unit.

2. **Identify the flour weight.** This is your 100% baseline. If the recipe uses multiple flours (whole wheat, rye, etc.), sum them — the total flour weight is always 100%.

3. **Calculate each ingredient's percentage:**
   ```
   Ingredient % = (Ingredient weight ÷ Total flour weight) × 100
   ```

4. **Create a baker's percentage table:**
   | Ingredient | Weight (g) | Baker's % |
   |---|---|---|
   | Flour (total) | X | 100% |
   | Water | Y | (Y÷X)×100 |
   | Salt | Z | (Z÷X)×100 |
   | (etc.) | | |

5. **Verify the formula makes sense.** Typical ranges:
   - Water: 55–75% (too low = tough dough, too high = slack dough)
   - Salt: 1.5–2.5% (less = bland, more = tough, inhibits fermentation)
   - Fresh yeast: 0.5–3% (less = slow fermentation, more = off-flavors)
   - Instant dry yeast: 0.3–1.5%
   - Fat (oil/butter): 0–10% (affects crumb softness and shelf life)

### Phase 2 — Diagnose Dough Balance

6. **Calculate the hydration percentage.** This is water ÷ flour and is the most critical ratio:
   - <60% hydration: stiff dough (bagels, pasta)
   - 60–65%: standard bread (sandwich loaves)
   - 65–75%: wetter dough (ciabatta, sourdough)
   - >75%: very wet dough (batter-like, requires high-skill handling)

7. **Compare ratios to category benchmarks.** If your hydration is 80% but you're making sandwich bread (benchmark 62%), that's your problem — the dough will be sticky and loose.

8. **Check for missing or imbalanced ingredients:**
   - No salt? The dough will ferment too fast and taste flat.
   - Salt >2.5%? Fermentation will slow dramatically or stall.
   - Fat <0.5% in enriched dough (brioche, croissant)? It will be dry.
   - Yeast <0.2%? Fermentation will be impractically slow.

### Phase 3 — Scale the Recipe

9. **Decide your target flour weight.** For 1 kg flour batch, use the baker's percentages directly (100g water from 100% flour = 100g water, etc.). For 500g flour, multiply all percentages by 5 to get grams; for 2 kg flour, multiply by 20.

10. **Recalculate ingredient weights using the percentages:**
    ```
    Ingredient weight = (Baker's % ÷ 100) × Target flour weight
    ```

11. **List the scaled recipe.** Include the target flour weight in the header:
    ```
    Recipe: Sourdough for 1 kg flour
    - Flour: 1000g
    - Water: 650g (65%)
    - Salt: 20g (2%)
    - Starter: 50g (5%)
    ```

## Evaluation Criteria

| Check | Pass |
|---|---|
| All ingredients converted to baker's percentage based on flour = 100% | Y/N |
| Hydration percentage calculated and compared to dough-type benchmarks | Y/N |
| Salt, yeast, and fat percentages checked against typical ranges | Y/N |
| If scaling, target flour weight is explicit and all ingredients recalculated | Y/N |
| Scaled recipe lists weights in consistent units (grams or ounces) | Y/N |
| Any out-of-range percentages are flagged with a diagnosis | Y/N |

## Red Flags

- Hydration calculated by total weight (flour + water + other ingredients) instead of flour weight alone. This distorts diagnosis.
- Salt percentage >3% or yeast >2%. Either a typo in the original recipe or it will behave unexpectedly.
- Recipe scaled by volume (cups) without converting to weight first. Scaling accuracy is lost.
- Multiple flours used but not summed to a single 100% baseline. The percentages will be incoherent.
- Hydration is reasonable (62%) but the dough behaves wet in practice. Suspect the flour brand or protein content — baker's percentage assumes standard flour.
- No salt or yeast percentage listed. The formula is incomplete or the step was skipped.

## Output Format

```
## Baker's Percentage Analysis

**Original recipe:**
- <list ingredients and amounts as given>

### Phase 1 — Conversion to Baker's Percentage
| Ingredient | Weight | Baker's % |
|---|---|---|
| Flour (total) | _g | 100% |
| ... | ... | ...% |

**Flour weight baseline:** _g

### Phase 2 — Diagnosis
| Metric | Value | Benchmark | Status |
|---|---|---|---|
| Hydration | ___% | 60–65% (standard) | ✓ In range / ⚠ Out of range |
| Salt | ___% | 1.5–2.5% | ✓ / ⚠ |
| Yeast | ___% | 0.3–1.5% (instant) | ✓ / ⚠ |
| Fat | ___% | 0–10% | ✓ / ⚠ |

**Diagnosis:**
<If out of range, explain the expected behavior and what to adjust.>

### Phase 3 — Scaled Recipe (if applicable)
**Target flour weight:** _g

- Flour: _g (100%)
- Water: _g (___%)
- [other ingredients]: _g (___%)

### Confidence
<high/medium/low> — <justification. High confidence if all ingredients are accounted for and conversion verified. Medium if recipe uses volume units and conversion relied on standard density assumptions. Low if ingredient list is incomplete or flour protein content is unknown (affects hydration behavior).>
```
