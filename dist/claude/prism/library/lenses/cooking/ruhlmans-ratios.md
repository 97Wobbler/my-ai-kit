---
name: ruhlmans-ratios
display_name: Ruhlman's Ratios
class: lens
underlying_class: native
domain: cooking
source: Michael Ruhlman, *Ratio: The Simple Codes Behind the Craft of Everyday Cooking* (2009)
best_for:
  - Designing reproducible dishes without memorizing recipes
  - Scaling recipes up or down while maintaining proportions
  - Debugging a failed dish by understanding what went wrong in the ratio
one_liner: "Ratio-driven cooking that frees recipes from rigid instructions."
---

# Ruhlman's Ratios

## Overview
Rather than treating recipes as fixed ingredient lists, Ruhlman's Ratios isolates the core numerical relationships (by weight) that produce a category of dish—paste, dough, sauce, custard, etc. Once you know the ratio, you can build the dish at any scale and with any flavor variations while preserving structure. Practitioners use this lens when they need to understand *why* a recipe works, troubleshoot failures, or adapt dishes to available ingredients without losing the essential character.

## Analytical Procedure

### Phase 1 — Identify the Dish Category

1. **Name the dish and its category.** Is it a dough (bread, pasta, pastry)? A batter (cake, pancake, crepe)? A sauce (béchamel, vinaigrette, emulsion)? A custard (crème anglaise, flan)? A paste (compound butter, forcemeat)? Write the category; it determines which ratios apply.

2. **List the canonical ingredient list.** Use a reliable published recipe (not multiple sources yet). Weigh each ingredient in grams. Include water, fat, eggs, flour, and binders — omit garnish and optional flavorings for now.

3. **Identify the primary structure-building ingredient.** In bread, it's flour. In custard, it's egg. In vinaigrette, it's oil. This ingredient becomes your reference weight (the denominator). Write it down.

### Phase 2 — Derive the Ratio

4. **Divide each ingredient weight by the reference weight.** If your reference is 100g (flour in bread), then:
   - Flour: 100g ÷ 100g = 1 part
   - Water: 60g ÷ 100g = 0.6 parts
   - Salt: 2g ÷ 100g = 0.02 parts
   - Yeast: 0.5g ÷ 100g = 0.005 parts
   
   Write these as a simple ratio: **1 flour : 0.6 water : 0.02 salt : 0.005 yeast** (or scale to whole numbers if cleaner: **100 flour : 60 water : 2 salt : 0.5 yeast**).

5. **Cross-reference against known ratios in the category.** Consult Ruhlman's table or other culinary science sources (e.g., Stella Parks' *BraveTart* for pastry ratios). Write down what the canonical ratio says your dish should be. If your derived ratio differs by more than 10%, investigate why — you may have missed an ingredient, used the wrong reference, or discovered a variant.

6. **Annotate which ingredients are structural (non-negotiable) and which are flavor/texture (variable).** Flour, water, and binder in dough are structural. Salt, spice, and herbs are variable. Mark each ingredient in your ratio with one of these labels.

### Phase 3 — Apply the Ratio

7. **Scale the recipe to your target batch size.** Decide how much of the reference ingredient you need (e.g., 500g flour for a large batch). Multiply every ingredient by the same scale factor. The ratio stays identical; only the absolute weights change.

8. **Make the dish using the scaled ratio.** Follow standard technique for your category (knead, whip, emulsify, etc.) — the ratio alone does not replace method, only the ingredient quantities.

9. **Evaluate the result against the expected outcome for that category.** Does it have the right texture, crumb, gloss, set? Record any deviations. If the dish failed, note which structural ingredient you suspect is off (too much/little flour? Too little fat?).

### Phase 4 — Troubleshoot via Ratio Drift

10. **If the dish failed, ask: "Which ratio component is most likely out of balance?"** Use the evaluation criteria table below to diagnose. For example:
    - Bread is dense and heavy → flour-to-water ratio is likely too dry (lower water %).
    - Sauce breaks and curdles → fat-to-egg ratio is likely too high (too much fat per egg).
    - Custard is grainy → egg-to-liquid ratio is likely too high (overcoagulated).

11. **Make a single-ingredient adjustment.** Change only one ingredient weight (usually add or subtract the suspected culprit by 5–10%), re-derive the ratio, and test again. Document the change. Do not adjust multiple ingredients simultaneously — you will not learn which one mattered.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Dish category is explicitly named | Y/N |
| Reference ingredient (denominator) is identified | Y/N |
| All structural ingredients are weighted and ratioed | Y/N |
| Derived ratio is cross-checked against a known source | Y/N |
| Structural and variable ingredients are labeled | Y/N |
| Scaled recipe uses consistent multiplier across all ingredients | Y/N |
| Troubleshooting, if needed, adjusts only one ingredient at a time | Y/N |

## Red Flags

- Reference ingredient is ambiguous or changes between recipes (e.g., sometimes flour by weight, sometimes by volume). This breaks the ratio entirely.
- The ratio includes optional ingredients or garnishes as if they were structural. Ratios are for structure; flavor variations belong outside the ratio.
- A failed dish is troubleshot by guessing multiple adjustments at once. You will not know which ingredient fixed it — and the next batch will fail again under slightly different conditions.
- The derived ratio differs drastically from the canonical ratio for that category, but no investigation was done. Either the reference is wrong or the methodology was — you need to know which.
- The dish succeeded but the ratio was never recorded or verified. Ratios have power only when they are explicit and repeatable.

## Output Format

```
## Ruhlman's Ratios Assessment

**Dish Name & Category:**
<name> | <category: dough/batter/sauce/custard/paste/etc.>

### Phase 1 — Ingredient List (by weight, grams)
| Ingredient | Weight (g) | Structural? |
|---|---|---|
| <reference ingredient> | <weight> | Yes |
| <ingredient 2> | <weight> | Yes/No |
| ... | ... | ... |

### Phase 2 — Derived Ratio
**Reference Ingredient:** <name> at <weight>g

**Ratio:**
<ingredient 1> : <ratio> | <ingredient 2> : <ratio> | ...

**Canonical Ratio (cross-check):**
<source and canonical ratio>

**Variance:** <+/- percent from canonical, with brief note if >10%>

### Phase 3 — Scaled Recipe (target batch)
**Target reference weight:** <weight>g

| Ingredient | Scaled weight (g) |
|---|---|
| ... | ... |

### Phase 4 — Outcome & Troubleshooting
**Result:** <description of dish outcome>

**Matches expected?** <Yes/No>

**If no, suspected ratio drift:**
- <Ingredient name>: <too high/too low/diagnosis>
- <Adjustment made>: <old ratio → new ratio>

### Confidence
<high | medium | low> — <justification: is the ratio well-sourced? Did the dish succeed? Has the ratio been tested more than once?>
```
---
