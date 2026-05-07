---
name: argument-mapping
display_name: Argument Mapping
class: lens
underlying_class: native
domain: information-analysis
source: Stephen Toulmin (The Uses of Argument, 1958); popularized in critical thinking by David Siegel and others
best_for:
  - Untangling complex written or spoken arguments into their structural components
  - Identifying unstated assumptions and logical gaps in reasoning
  - Evaluating strength of evidence chains before making decisions
one_liner: "Decompose claims, evidence, and rebuttals into a visual tree to expose logical gaps."
---

# Argument Mapping

## Overview
Argument mapping externalizes the logical structure of a reasoning chain—breaking a claim into its supporting premises, evidence, and assumptions—so gaps, circular reasoning, and unsupported jumps become visible. Instead of reading an argument linearly, you build a diagram: the main claim sits at the apex; below it sit the direct premises it depends on; below those sit the evidence and sub-premises; rebuttals and counter-evidence branch to the side. Practitioners use this when evaluating proposals, research papers, or policy arguments where missing or weak links could be costly.

## Analytical Procedure

### Phase 1 — Extraction

1. **Identify the main claim.** Read or listen to the full argument. In one sentence, state what the author is trying to convince you of. This is the apex of your map. If multiple competing claims exist, map them separately.

2. **Extract direct premises.** For each claim, ask: "What reasons does the author give to support this?" List each reason as a separate box. These are the premises that directly support the apex. Write them in the author's own terms, not interpreted or paraphrased—this prevents you from "fixing" weak reasoning unconsciously.

3. **For each direct premise, ask: "Is this asserted as true, or is it itself argued for?"** If asserted (no evidence given), tag it `ASSERTED`. If argued for, continue decomposing downward. If evidence is given, tag it `EVIDENCED`.

4. **Extract evidence and sub-premises.** Repeat the process one level down. For every evidenced premise, write out the specific data points, studies, examples, or logical steps offered. Again, use the author's language.

5. **Mark the type of each lowest-level item:**
   - `DATA` — a concrete fact, statistic, or observation (e.g., "unemployment is 3.5%")
   - `AUTHORITY` — "X says so" (e.g., "the WHO reports...")
   - `DEFINITION` — a conceptual or definitional claim (e.g., "inflation means rising prices")
   - `LOGICAL` — a rule or inference pattern (e.g., "if A and B, then C")
   - `ASSUMED` — unstated, inferred from gaps in the chain

### Phase 2 — Gap Identification

6. **Identify implicit premises.** Where does the chain have a jump—where the conclusion doesn't obviously follow from what's stated? Write down what would need to be true (but isn't explicitly said) to bridge that gap. These are assumed premises.

7. **Spot missing evidence.** For each `ASSERTED` premise, note: "Is evidence available for this? If not, why is the author asserting without support?" (Sometimes there's a good reason; often there isn't.)

8. **Check for circular reasoning.** Does any premise depend on the conclusion, or does a sub-premise depend on another premise further up the chain in a loop? Mark any cycles found.

### Phase 3 — Rebuttal Layer

9. **List known rebuttals to the main claim.** What are the strongest counter-arguments? Write each as a separate branch off the main claim. For each rebuttal, mark whether the author addresses it:
   - `ADDRESSED` — the author acknowledges and responds to it
   - `IGNORED` — a known counter-argument that the argument makes no room for
   - `UNKNOWN` — the author may not be aware of this counter-argument

10. **For each addressed rebuttal, trace its refutation.** Did the author actually dismantle the counter-argument, or just assert it's wrong? Use the same extraction process from Phase 1 on the refutation itself.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Main claim is stated in one sentence | Y/N |
| Every direct premise is extracted in author's own words | Y/N |
| Every evidenced premise is decomposed at least one level deeper | Y/N |
| Lowest-level items are typed (DATA / AUTHORITY / DEFINITION / LOGICAL / ASSUMED) | Y/N |
| At least 3 implicit premises are identified and marked | Y/N |
| All known rebuttals are listed and marked (ADDRESSED / IGNORED / UNKNOWN) | Y/N |
| No unsupported claims remain in the primary chain | Y/N |

## Red Flags

- The map is shallower than 3 levels. The author asserted almost everything without support, or you stopped decomposing too early.
- Every lowest-level item is typed as `ASSUMED`. Either the argument has no real evidence or you haven't dug deep enough to find where evidence actually appears.
- No rebuttals are marked `IGNORED`. Either the argument is airtight (rare) or you haven't identified genuine counter-arguments.
- The same source is cited multiple times at the bottom level as if it confirms independent claims. That's one piece of evidence, not three.
- Implicit premises are vague ("people believe this" instead of "the author assumes younger people are more digital-native"). Imprecise assumed premises defeat the purpose of mapping.
- The map is asymmetrical: one branch of the argument is mapped to 4 levels deep, another to 1 level. This suggests selective scrutiny.

## Output Format

```
## Argument Map

**Main Claim:**
<one sentence>

### Direct Premises
1. [ASSERTED | EVIDENCED] <premise in author's words>
2. [ASSERTED | EVIDENCED] <premise>
...

### Evidence and Sub-Premises
**For Premise 1:**
- [DATA | AUTHORITY | DEFINITION | LOGICAL | ASSUMED] <supporting item>
- [TYPE] <supporting item>

**For Premise 2:**
...

### Implicit Premises (Bridging Gaps)
1. <assumption required for gap between Premise 1 and Conclusion>
2. <assumption required for gap between Evidence A and Premise 2>
...

### Identified Rebuttals
| Counter-claim | Status | Author's Response |
|---|---|---|
| <strongest rebuttal> | ADDRESSED / IGNORED / UNKNOWN | <refutation or "none"> |
| <second rebuttal> | <status> | <refutation or "none"> |

### Structural Issues
- Circular reasoning: <yes/no; if yes, describe the loop>
- Unsupported assertions in main chain: <count and list>
- Asymmetry in decomposition: <yes/no; if yes, which branches>

### Confidence
<high/medium/low> — <justification: evidence quality, rebuttal coverage, depth of decomposition, implicit assumptions>
```
---
