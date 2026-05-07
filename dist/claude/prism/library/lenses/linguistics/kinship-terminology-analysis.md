---
name: kinship-terminology-analysis
display_name: Kinship Terminology Analysis
class: lens
underlying_class: native
domain: linguistics
source: Lewis Henry Morgan (1871); systematized in structural anthropology by Claude Lévi-Strauss (1949)
best_for:
  - Inferring social structure and kinship norms from terminology patterns
  - Identifying marriage rules, residence patterns, and descent systems
  - Cross-cultural comparison of family organization
one_liner: "Derive social structure and marriage rules from kinship term systems."
---

# Kinship Terminology Analysis

## Overview
Kinship terminology—the words a language uses to name family relations—encodes a culture's marriage rules, descent system, and residential patterns. Rather than assuming kinship terms map directly to biological relationships, this lens decodes the social logic embedded in the terminology itself. A single term applied to both mother and mother's sister signals something different about lineage than a unique term for each. Practitioners use this to infer hidden social structures, validate or challenge ethnographic claims, and compare family systems across cultures without imposing their own categories.

## Analytical Procedure

### Phase 1 — Collect and Normalize the Terminology

1. **Obtain a complete kinship term list for the language or culture under study.** Ideally from a primary ethnographic source or native speaker documentation. The list must include terms for: grandparents, parents, siblings, aunts, uncles, cousins (patrilateral and matrilateral), spouses, children, and in-laws. Record the terms phonetically and note any gender distinctions (e.g., brother vs. sister, paternal vs. maternal uncle).

2. **Create a kin-type matrix.** For each term, list the genealogical positions (biological relationships) it covers. Use standard notation:
   - F = father, M = mother, B = brother, S = son, D = daughter, Z = sister, H = husband, W = wife
   - Prefix P, M, or F for paternal, maternal, father's, or mother's line (e.g., MZS = mother's sister's son)
   - Use arrows for generation (↑ = ascending, ↓ = descending)

   Example:
   | Term | Covers | Kin Types |
   |---|---|---|
   | uncle | father's brothers and mother's brothers | FB, MB |
   | mamá | mother and mother's sisters | M, MZ |

3. **Identify if the language has separate terms for lineal vs. collateral kin.** Lineal = direct line (parents, children). Collateral = siblings of parents, their children. Mark each term as L (lineal) or C (collateral) or both.

4. **Check for gender marking.** Note whether the language distinguishes by gender of the relative (e.g., brother vs. sister) and by gender of the speaker (some languages use different terms if the speaker is male vs. female). Record these patterns in a separate column.

### Phase 2 — Identify Merging and Splitting Patterns

5. **List all cases where a single term covers multiple distinct kin types.** These are "mergings." Classify each merging by pattern:
   - **Generational**: Same term for adjacent generations (e.g., grandfather and father called by same term).
   - **Siblingship**: Same term for siblings and cousins (e.g., brother and parallel cousin lumped together).
   - **Affinal collapse**: Same term for blood relatives and married-in relatives (e.g., mother and stepmother).
   - **Cross-sibling merging**: Same term for brother and sister (rare in most systems; signals unusual gender organization).

6. **List all cases where distinct kin types have different terms.** These are "splittings." Note:
   - Is the splitting based on generation, gender, lineality, or side of family (paternal vs. maternal)?
   - Are some categories split while others are merged? (E.g., mother's side heavily split; father's side lumped together.)

7. **Check for reciprocal asymmetry.** If A calls B by term X, does B call A by the reciprocal term? Or the same term? Or a term for a different category? Record these asymmetries — they often point to hierarchies or age-based distinctions.

### Phase 3 — Infer Social Rules

8. **Apply the Omaha/Iroquois/Crow/Hawaiian/Sudanese/Eskimo decision tree** (the six main kinship systems). Compare your merging/splitting patterns to the templates:
   - **Hawaiian**: Merges heavily across generations and collaterality; minimal gender marking. (Signals: bilateral descent, classificatory system, no name-inheritance rules.)
   - **Iroquois**: Separates parallel cousins (treated as siblings) from cross cousins (treated differently). (Signals: descent rule exists; cross-cousin marriage may be preferred.)
   - **Crow**: Merges mother's side across generations but splits father's side. (Signals: matrilineal descent.)
   - **Omaha**: Mirrors Crow but favors patrilateral side. (Signals: patrilineal descent.)
   - **Eskimo**: Separates nuclear family (unique terms) from all collateral kin (lumped as "cousins," "aunts," "uncles"). (Signals: bilateral descent, nuclear family emphasis, limited clan structure.)
   - **Sudanese**: Every relative has a distinct term. (Signals: little social merging; descriptive rather than classificatory system.)

   Not every system fits perfectly — note where it deviates.

9. **Infer descent and marriage rules from the pattern:**
   - **Parallel cousin merging with siblings** → likely patrilineal or matrilineal descent with unilineal kinship.
   - **Cross-cousin distinction** → cross-cousin marriage may be permitted or preferred (check ethnographic sources to confirm).
   - **Heavy maternal-side splitting** → matrilineal emphasis.
   - **Reciprocal term asymmetry** → possible age-ranking, spousal inequality, or inherited status.
   - **Lack of in-law terms** → affinal relatives incorporated into lineal categories (signals weak affinal boundaries).

10. **Check for residence pattern clues.** If terms distinguish paternal and maternal relatives sharply, ask: Which side stays nearby? Which side is "outside"? These often align with patrilocal (wife joins husband's family) or matrilocal (husband joins wife's family) residence.

### Phase 4 — Validate Against Ethnographic Data

11. **Cross-check inferences.** If you inferred patrilineal descent, does the ethnographic record say so? If you inferred cross-cousin marriage preference, do the marriage records confirm it? List confirmations and contradictions explicitly.

12. **Note what the terminology cannot tell you.** Kinship terms encode social categories, not practices. A term may allow cross-cousin marriage without anyone actually practicing it. Record this caveat in your output.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Complete kinship term list obtained (min. 15-20 terms across generations) | Y/N |
| Kin-type matrix accurate (every term's coverage recorded) | Y/N |
| All mergings and splittings identified and classified | Y/N |
| System matched to one of six templates with deviations noted | Y/N |
| At least 3 inferences about descent/marriage/residence drawn from patterns | Y/N |
| Inferences cross-checked against ethnographic record | Y/N |
| Caveats noted (what terminology cannot determine) | Y/N |

## Red Flags

- Kin-type matrix incomplete or includes only nuclear family terms. Terminology systems are not universal — full collection is mandatory.
- All terms are treated as equivalent; no merging or splitting patterns identified. If no mergings exist, the system is unusually descriptive — flag this as a finding, not a failure.
- Inferred descent system does not match the primary ethnographic source. Either the terminology data is corrupted, or the inference logic is wrong — investigate both.
- No reciprocal asymmetries noted. Real kinship systems often have them (e.g., grandchild and grandparent terms are not reciprocals); missing them suggests shallow reading.
- Conclusions stated with certainty despite ethnographic record contradicting inferences. Terminology is one source; it does not override direct observation of actual marriage or residence patterns.
- No caveats about the gap between category and practice. Terminology encodes norms, not behavior — conflating the two is a common error.

## Output Format

```
## Kinship Terminology Assessment

**Language/Culture:**
<name and source of data>

**Kinship System Type:**
<Hawaiian/Iroquois/Crow/Omaha/Eskimo/Sudanese/mixed>

### Kin-Type Matrix
| Term | Genealogical Coverage | Lineal/Collateral | Gender Marked |
|---|---|---|---|
| <...> | <...> | <...> | Yes/No |

### Key Mergings
1. <pattern> — <kin types merged> — **Implication:** <...>
2. ...

### Key Splittings
1. <pattern> — <kin types distinguished> — **Implication:** <...>
2. ...

### Inferred Social Structure
- **Descent system:** <patrilineal/matrilineal/bilateral/double/unclear>
- **Marriage rule (if inferable):** <cross-cousin preferred/parallel cousin prohibited/exogamous/other>
- **Residence pattern (if inferable):** <patrilocal/matrilocal/ambilocal/other>
- **In-law integration:** <affinal kin incorporated/distinguished>

### Validation Against Ethnographic Record
| Inference | Ethnographic Confirmation | Status |
|---|---|---|
| <...> | <...> | Confirmed / Contradicted / No data |

### Caveats and Limitations
- <What terminology alone cannot determine>
- <Gaps between category and actual practice>

### Confidence
<high/medium/low> — <justification based on completeness of data, internal consistency, and ethnographic corroboration>
```
