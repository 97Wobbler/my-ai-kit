---
name: lewis-structures-formal-charge
display_name: Lewis Structures + Formal Charge
class: lens
underlying_class: native
domain: chemistry
source: Gilbert N. Lewis (1916); formal charge notation standardized in general chemistry pedagogy (mid-20th century)
best_for:
  - Evaluating which resonance structure contributes most to molecular ground state
  - Predicting site reactivity and nucleophile/electrophile character
  - Diagnosing errors in Lewis structure drawing
one_liner: "Judge resonance structure stability via formal charge."
---

# Lewis Structures + Formal Charge

## Overview
Lewis structures show valence electrons and bonding in a molecule; formal charge (FC) assigns charge to individual atoms within a structure to predict which resonance form dominates and where reactive sites concentrate. Practitioners use this framework when multiple valid Lewis structures exist for a molecule (resonance) and must decide which is the major contributor to the actual structure, or when predicting where nucleophiles or electrophiles will attack. The discipline is applying FC consistently and recognizing that the structure with the lowest formal charges (and negative FC on the most electronegative atoms) is usually the dominant resonance form.

## Analytical Procedure

### Step 1 — Draw all valid Lewis structures for the molecule

1. **Count valence electrons.** Use the periodic table to find valence electrons for each atom. For ions, add (anion) or subtract (cation) electrons equal to the charge.

2. **Connect atoms with single bonds.** Place the least electronegative atom (usually not H or F) at the center. Use the octet rule as a guide (8 electrons for main-group atoms; 2 for H).

3. **Distribute remaining electrons as lone pairs** on atoms until the octet is satisfied.

4. **If the octet is not satisfied, form double or triple bonds** by moving lone pairs into bonding regions.

5. **Generate all valid structures.** Do not skip structures that satisfy the octet rule, even if they look unstable. The goal here is to find every possibility before evaluating.

### Step 2 — Calculate formal charge for each atom in each structure

**Formula:**
```
FC = V - L - (B/2)
```
where:
- **V** = number of valence electrons in the free atom
- **L** = number of non-bonding electrons (lone pairs) on the atom in the structure
- **B** = number of bonding electrons (total in all bonds connected to the atom)

6. **For each atom in each structure, apply the formula above.** Write the FC as a superscript next to the atom symbol in the structure (e.g., N⁺, O⁻).

7. **Verify the sum of all FCs equals the net charge of the molecule.** If it doesn't, recalculate.

### Step 3 — Evaluate dominance of each structure

8. **Score each structure on the following criteria (lower score = more dominant):**

   | Criterion | Score | Rule |
   |-----------|-------|------|
   | Sum of absolute FCs | Count of non-zero FCs | Structures with more atoms at FC = 0 are more stable. |
   | Negative FC location | 0 if on most electronegative atom(s); +2 per mismatch | Negative formal charges should sit on atoms that want electrons (O, N, S, halogens). Positive FCs on these atoms is penalized. |
   | Positive FC location | 0 if on least electronegative atom; +2 per mismatch | Positive formal charges should sit on atoms that resist electron gain (C, H). Positive FC on O or N is strongly disfavored. |
   | Hypervalency | 0 if octet satisfied; +5 if any atom exceeds octet | Main-group atoms beyond period 2 (P, S, Cl, etc.) may exceed 8 electrons if the structure requires it; this is acceptable but less preferred than octet-obeying forms. |

9. **Compare total scores across all structures.** The structure with the lowest total score is the major (most stable) resonance form.

### Step 4 — Identify reactive sites

10. **Locate atoms bearing negative formal charge** in the dominant structure. These sites are nucleophilic (electron-rich) and will preferentially attack electrophiles.

11. **Locate atoms bearing positive formal charge** in the dominant structure. These sites are electrophilic (electron-poor) and will preferentially attack nucleophiles.

12. **Cross-check with electronegativity.** A C⁻ (negative carbon, rare but possible in carbanions) is very nucleophilic despite being less electronegative than N or O, because it has excess electron density. Note any exceptions where FC and electronegativity diverge.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All valid Lewis structures generated (octet rule satisfied in each) | Y/N |
| Valence electron count verified for the molecule | Y/N |
| Formal charge calculated for every atom in every structure | Y/N |
| Sum of FCs in each structure equals net molecular charge | Y/N |
| Each structure scored on all four criteria | Y/N |
| Dominant structure identified and justified | Y/N |
| Nucleophilic and electrophilic sites identified from FC | Y/N |

## Red Flags

- Only one Lewis structure is shown. If the molecule has multiple atoms or unsaturation, resonance almost always exists — the analysis is incomplete.
- Formal charges are calculated correctly but then ignored in the final judgment (e.g., "this structure has lower FC, but I chose the other one because it looks more symmetric"). FC calculation exists to guide structure selection, not decorate it.
- An atom exceeds 8 electrons in a period-2 element (C, N, O, F). These atoms cannot expand their octet. Redraw.
- Negative formal charge on a hydrogen or halogen in the dominant form (e.g., H⁻ as a lone species, not bonded to a metal; Cl⁻ in a covalent molecule). This is a red flag unless explicitly justified (e.g., a strongly polarized C—Cl bond in a carbocation context).
- The sum of formal charges does not equal the net charge of the molecule. Recalculate; there is an arithmetic error.
- Nucleophilic and electrophilic sites are not identified, or are identified without reference to formal charge. The reactivity prediction is disconnected from the structure.

## Output Format

```
## Lewis Structure + Formal Charge Analysis

**Molecular formula:** <e.g., NO₂>
**Net charge:** <0, +1, -1, etc.>
**Valence electron count:** <total>

### All Valid Lewis Structures

**Structure 1:**
```
[ASCII or plain-text Lewis structure with FC labels]
```

Formal charges:
| Atom | FC |
|------|-----|
| <e.g., N> | <e.g., +1> |

**Structure 2:** [repeat]

### Structure Scoring

| Structure | Non-zero FCs | Charge location score | Hypervalency | Total score |
|-----------|---------------|-----------------------|---------------|-------------|
| 1 | <count> | <0–4> | <0 or 5> | <sum> |
| 2 | <count> | <0–4> | <0 or 5> | <sum> |

**Dominant structure:** Structure <number> (lowest score: <score>)

### Reactive Sites

| Site | Formal Charge | Character | Reactivity |
|------|-------------------|-----------|------------|
| <atom, e.g., O in C=O> | <e.g., δ−> | Nucleophilic | Attacked by electrophiles (e.g., H⁺, alkyl halides) |
| <atom, e.g., C in C=O> | <e.g., δ+> | Electrophilic | Attacked by nucleophiles (e.g., OH⁻, RO⁻) |

### Confidence
<high | medium | low> — <justification, e.g., "high: all structures follow octet rule and FC assignments are unambiguous; medium: hypervalency possible in one structure requiring periodic-table-specific knowledge; low: multiple structures score identically and experiment or additional theory required to choose">
```
---
