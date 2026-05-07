---
name: flavor-pairing
display_name: Flavor Pairing
class: lens
underlying_class: native
domain: cooking
source: Karen Page and Andrew Dornenburg, The Flavor Bible (2008)
best_for:
  - Discovering unexpected ingredient combinations grounded in shared flavor compounds
  - Breaking monotony in menu design or recipe development
  - Validating or challenging intuitive pairings with chemical evidence
one_liner: "Ingredient affinity database built on shared flavor compounds."
---

# Flavor Pairing

## Overview
Ingredients pair well when they share underlying flavor compounds — not merely because tradition says so or because they appear together in canonical recipes. The Flavor Bible catalogs these molecular commonalities across thousands of ingredients, allowing chefs and recipe developers to discover non-obvious pairings (e.g., white chocolate + miso, watermelon + basil) that feel surprising but taste coherent. Practitioners use this when conventional pairings feel stale, when designing dishes across unfamiliar cuisines, or when validating whether a creative combination will work before plating.

## Analytical Procedure

1. **Identify your anchor ingredient.** Choose a single ingredient you want to build a pairing around — the dish's foundation or focal point. Write its name exactly.

2. **Look up the anchor ingredient in the Flavor Bible or equivalent reference** (Karen Page/Dornenburg, or a digital flavor-compound database such as FlavorDB or FoodPairing.com). Record the top 8–12 ingredients listed as affinity matches. Do not filter or pre-judge; copy them as given.

3. **For each affinity match, classify it by relationship type:**
   - **Direct pairing** — the two ingredients are commonly eaten together in cuisine(s) you're familiar with
   - **Flavor-compound match** — they share aromatic volatiles but are not traditionally paired
   - **Textural complement** — different mouthfeel or structure but overlapping flavor profile
   - **Culinary context bridge** — they belong to different cuisines but could work in a hybrid context

4. **Filter by constraint.** Remove any pairing that fails your non-negotiable constraints (e.g., vegetarian, no tree nuts, seasonal availability, cost). Record which pairings you removed and why. Do not remove pairings simply because they "sound weird."

5. **Select 2–4 candidate pairings** from the remaining list. Prefer at least one "Flavor-compound match" (the high-novelty option) and at least one from another category. Justify your selection in one sentence per pairing.

6. **For each candidate, map the shared flavor compounds** (if accessible). The compounds should be specific — e.g., "both high in linalool and geraniol" rather than "both floral." If a database is unavailable, consult culinary literature or conduct a sensory test: taste a small amount of each ingredient in sequence and note common flavor notes (citrus, earthy, anise, umami, etc.).

7. **Prototype at minimal scale.** Prepare a tiny tasting: 1 tsp or 1 small bite of the anchor + each candidate. Evaluate alone, not in a full dish yet. Record:
   - Does the pairing taste coherent (compounds working together) or disjointed?
   - What is the dominant flavor in the combination?
   - Does it need a bridge ingredient to work (e.g., acid, fat, salt)?

8. **Scale up to a simple preparation** if the minimal tasting was coherent. Pair the anchor and candidate in a neutral vehicle — a sauce, a simple braise, a fresh salad dressing — that does not introduce competing flavors. Cook or assemble. Taste. Does the pairing hold up at volume? Does it suggest a specific dish direction?

9. **Document the winning pairing(s).** Record the anchor, the partner ingredient(s), the shared flavor compound(s) if known, the preparation context, and a one-line tasting note.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Anchor ingredient is clearly named and singular | Y/N |
| At least 8 affinity matches from reference consulted | Y/N |
| Each affinity match is classified by relationship type | Y/N |
| Constraint-filtered pairings are documented with reasons | Y/N |
| At least one candidate is a Flavor-compound match (non-traditional) | Y/N |
| Shared flavor compounds are named specifically, not generically | Y/N |
| Minimal-scale tasting was conducted and recorded | Y/N |
| Scaled preparation tasting was conducted | Y/N |
| Final pairing(s) include compound basis and tasting note | Y/N |

## Red Flags

- The affinity matches are all Direct pairings (traditionally paired). The lens was applied to validate received wisdom, not to discover. Run again with a filter: ignore traditional pairings and focus only on Flavor-compound matches.
- Shared flavor compounds are described as "floral," "fruity," or "savory" without specificity. These are culinary descriptors, not chemical compounds. Return to the reference and name the actual volatile (linalool, ester family, glutamate, etc.) or acknowledge the database is inaccessible.
- Constraint filtering removed almost all candidates. Either your anchor ingredient has very narrow affinity (rare) or your constraints are too tight. Loosen one constraint and re-run.
- The minimal tasting was skipped. "It sounds like it should work" is not evidence. No pairing is validated until tasted.
- The scaled preparation tasted of only one ingredient; the pairing collapsed. The compounds may be shared but not in proportion. Adjust ratios or add a bridge ingredient before abandoning the pairing.

## Output Format

```
## Flavor Pairing Analysis

**Anchor ingredient:**
<name>

**Affinity matches (from reference):**
1. <ingredient> — [Direct pairing | Flavor-compound match | Textural complement | Culinary context bridge]
2. <ingredient> — [type]
...

**Constraints applied:**
- <constraint 1>
- <constraint 2>

**Filtered pairings (removed and why):**
- <ingredient>: <reason>
- <ingredient>: <reason>

**Candidate pairings (selected for testing):**
1. **<ingredient>** — <one-sentence justification>
   - Shared compounds: <specific volatiles or descriptors>
   - Minimal tasting result: <coherent/disjointed; dominant note>
   - Bridge ingredient needed: <yes/no; if yes, what>
   - Scaled preparation: <brief description>
   - Scaled tasting result: <outcome and one-line note>

2. **<ingredient>** — <...>
   - ...

**Winning pairing(s):**
| Anchor | Partner | Shared Compounds | Preparation | Tasting Note |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

**Confidence:**
<high/medium/low> — <justification based on: reference authority, shared compound specificity, number of tastings conducted, consensus across scaled preparations>
```
---
