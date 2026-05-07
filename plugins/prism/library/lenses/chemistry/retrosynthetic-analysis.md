---
name: retrosynthetic-analysis
display_name: Retrosynthetic Analysis
class: lens
underlying_class: native
domain: chemistry
source: Elias James Corey (Harvard University, 1967)
best_for:
  - Planning multi-step organic syntheses by working backward from target
  - Identifying key bond disconnections and synthetic bottlenecks
  - Teaching strategic thinking in organic chemistry
one_liner: "Design synthetic routes by working backward from target to precursors."
---

# Retrosynthetic Analysis

## Overview
Instead of asking "What reactions can I run on what I have?" (forward synthesis), work backward from the target molecule: "What precursor would I need to make this bond?" Retrosynthesis decomposes a complex molecule into progressively simpler, more available building blocks by systematically breaking bonds and asking "Where did this come from?" Practitioners use it to plan economical routes, spot which bonds are expensive or risky to form, and avoid synthetic dead ends before committing reagents and time.

## Analytical Procedure

### Phase 1 — Target Analysis and Bond Selection

1. **Draw the target molecule clearly.** Use standard structural notation. Label all stereocenters, functional groups, and any bonds of special interest (strain, heteroatoms, quaternary centers).

2. **Identify all non-trivial bonds.** Trivial bonds are those that form easily and inexpensively in forward synthesis (e.g., simple C—C coupling under standard conditions). Highlight bonds that are:
   - Between complex carbon scaffolds
   - Involving stereocenters (forming or adjacent to one)
   - To electron-poor or hindered positions
   - Between heteroatoms and carbon
   - That would create ring strain or ring closure
   These are "disconnection candidates."

3. **For each candidate bond, ask: "If I break this bond, do I get two precursors that are easier to make than the target?"** Write yes or no. If yes, this is a valid disconnection to explore.

4. **Rank candidate disconnections by strategic value:**
   - High: Breaking reduces target complexity the most (molecule splits into two very different pieces) AND precursors are known/commercial/easy.
   - Medium: Breaking is chemically reasonable but precursors are not obviously easier.
   - Low: Breaking creates precursors that are nearly as complex as the target.

### Phase 2 — Retrosynthetic Step Execution

5. **Choose the highest-ranked disconnection.** Draw the bond break with a curved arrow notation (or simply cross it out and write the two precursors).

6. **For the break you chose, identify the synthetic reaction that would form that bond in the forward direction.** Write the reaction name (e.g., "Grignard addition," "Wittig olefination," "Suzuki coupling"). Be specific about which fragment is electrophile and which is nucleophile/organometallic.

7. **State the synthetic requirements for this reaction:**
   - Functional groups needed on each precursor (e.g., "Left fragment must be an aldehyde; right fragment must be a Grignard or phosphonium ylide")
   - Any protecting groups or functional group manipulations required before or after the bond-forming step
   - Selectivity issues (regio-, stereo-, chemo-) and how they are managed
   - Scalability and cost of the reaction (laboratory scale vs. process scale)

8. **If precursors do not already have the correct functional groups, add synthetic steps.** This is a sub-problem: how do you prepare the electrophile or nucleophile from a simpler starting material? If the sub-problem is small, solve it. If it is large, defer it and continue retrosynthesis from the simpler precursor.

### Phase 3 — Iteration and Convergence

9. **Repeat steps 5–8 on each new precursor.** Stop when all precursors are:
   - Commercially available (cost-check against budget)
   - Known in the literature (can be looked up)
   - Easily prepared from common starting materials in ≤2 steps

10. **Draw the complete synthesis tree.** Root = target. Leaves = starting materials. Edges = reactions. Annotate each edge with reaction name and a brief note on yield or hazards if known.

11. **Count the number of synthetic steps and potential bottlenecks:**
    - How many convergence points are there (places where two syntheses meet)? Convergent syntheses are less wasteful.
    - Which step is most likely to fail (lowest yield, longest time, hazardous, expensive reagent)? Mark this as the bottleneck.
    - Are any building blocks obtained from the same source? Parallel synthesis could reduce time.

### Phase 4 — Feasibility and Refinement

12. **For the most critical 2–3 reactions, consult literature or run a quick desk check:**
    - Has this exact transformation been reported? If yes, note yield, scale, conditions.
    - If not, is it a variant of a known reaction? Estimate probability of success (high/medium/low).
    - Are any reagents/solvents hazardous, restricted, or expensive? Flag for process safety review.

13. **Identify alternative disconnections for any bottleneck step.** Repeat Phase 1–2 on just that bond to see if a different disconnection leads to a smoother forward route.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Target molecule is drawn clearly with all stereocenters and functional groups marked | Y/N |
| All non-trivial bonds were identified as candidates | Y/N |
| Disconnections chosen reduce target complexity materially (target splits, or precursors are known simpler) | Y/N |
| Each disconnection is paired with a specific forward reaction name and mechanism class | Y/N |
| Functional group requirements for each precursor are stated | Y/N |
| Synthesis tree is complete (all leaves are commercial/simple) | Y/N |
| At least one bottleneck and one alternative disconnection are identified | Y/N |

## Red Flags

- Disconnections proposed without naming the forward reaction. "I break this bond because it looks breakable" is not retrosynthesis — it's guessing.
- Precursors from a disconnection are nearly as complex as the target. The problem was not decomposed; it was split.
- No stereoselective strategy is mentioned, but target has stereocenters. Stereochemistry must be addressed in each step or the synthesis will fail.
- Synthesis tree has > 15 steps with no convergence. Linear, stepwise syntheses are inefficient. Consider whether two subtrees can be assembled in parallel.
- A reaction is proposed for which no precedent or mechanism is sketched. "We could do a nucleophilic aromatic substitution here" without checking if the aromatic ring is activated is a red flag.
- Bottleneck is identified but no alternative route is explored. Retrosynthesis is not done until you have at least two routes and have picked the better one.

## Output Format

```
## Retrosynthetic Analysis

**Target Molecule:**
[STRUCTURE and description]

### Phase 1 — Bond Candidates and Ranking
| Bond | Breaks into | Complexity reduction | Precursor ease | Rank |
|---|---|---|---|---|
| C1—C2 | Aldehyde + Grignard-ready alkene | High (ester → two distinct pieces) | Medium (Grignard is standard) | High |
| C5—N | Aryl bromide + amine nucleophile | Medium (aromatic swing) | High (both commercial) | High |

### Phase 2 — Lead Disconnection
**Selected bond:** C1—C2 (Grignard addition to aldehyde)

**Forward reaction:** Grignard addition; R-MgX + R'CHO → R-CH(OH)-R'

**Functional group requirements:**
- Left fragment: Grignard-ready (C1 must be a good leaving group or C-H on a position alpha to electron-withdrawing group)
- Right fragment: Aldehyde or equivalent electrophile
- Post-reaction: Reduce/oxidize as needed or use protecting groups if OH is temporary

**Literature check:** Grignard addition to aldehydes, yields typically 60–90%, scale-up feasible.

### Phase 3 — Iteration
[Complete precursor-by-precursor breakdown, including any sub-problems and how they are solved]

### Phase 4 — Synthesis Tree and Bottleneck Analysis
**Tree structure:**
```
Target
├─ Precursor A (Aldehyde)
│  └─ Simple aldehyde (commercial or 1-step prep)
└─ Precursor B (Grignard parent)
   └─ Alkyl halide (commercial)
```

**Bottleneck:** Grignard formation (moisture-sensitive, requires anhydrous conditions and inert atmosphere). Alternative: Use organolithium or organoboron coupling instead.

**Alternative disconnection explored:** Suzuki coupling (C-Ar coupling) — requires Ar-B(OH)₂ and Ar-Br/I. More robust to moisture but requires catalyst and may be costlier.

### Confidence
<high/medium/low> — <Grignard route is high confidence if literature precedent is strong; medium if precursors require additional synthesis steps; low if target has multiple stereocenters and no selectivity strategy is outlined>
```
