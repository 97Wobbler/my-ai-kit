---
name: millers-law
display_name: Miller's Law (7±2)
class: model
underlying_class: native
domain: ux
source: George A. Miller, "The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information," Psychological Review, 1956
best_for:
  - Predicting when information presentation will exceed working memory limits
  - Explaining why users struggle with complex interfaces or dense content chunks
  - Designing chunking strategies for menus, forms, and information hierarchies
one_liner: "Working-memory capacity constraint that predicts cognitive load."
---

# Miller's Law (7±2)

## Overview

Miller's Law claims that the human working memory can hold and process approximately 7±2 discrete items (chunks) simultaneously, and that this capacity limit is relatively invariant across domains and individuals. The model is **descriptive**: it describes an empirically observed bottleneck in cognition, not how memory works mechanistically. Applied to user interface design, Miller's Law predicts that when an interface presents more than roughly 5–9 information items at once without clear chunking or hierarchy, cognitive overload will occur — users will fail to retain, process, or accurately recall the full set. The model is particularly useful for diagnosing why flat, undifferentiated lists or menus feel overwhelming, and for predicting the effectiveness of hierarchical vs. flat designs.

## Core Variables and Relationships

1. **Working memory capacity (WMC)** — the number of discrete chunks an agent can hold in focus simultaneously.
   - Baseline: ~7 items, with observed range 5–9 across individuals and contexts.
   - Does not increase with intelligence or expertise for arbitrary items.
   - Degraded by time pressure, competing cognitive tasks, and stress.
   - Expands slightly (but does not double) with meaningful chunking — a chess player recognizes familiar board patterns as single chunks rather than individual pieces.

2. **Chunk definition** — what counts as a discrete item.
   - A chunk is a meaningful unit: a word, a digit, a recognizable pattern, a category label.
   - Chunks are *learned*: familiar patterns compress into smaller chunks; unfamiliar items consume more.
   - Example: "2-6-4-9-1-9-5-6" is 8 items for most people; "264-1956" might be 2 for someone who recognizes a date and a number.
   - Reordering or adding unfamiliar structure increases perceived chunk count even if the information is identical.

3. **Presentation load** — the number of distinct, separable items presented to the user in a single view.
   - Includes: menu items, form fields, list entries, button choices, categories, instructions, or any cognitively distinct element.
   - Not tied to visual complexity or page size — two dense pages of text can present far fewer *chunks* than a list of 10 one-word labels.
   - Increases with lack of visual or semantic grouping (flat presentation → higher load).

4. **Cognitive overload threshold** — the point at which performance degrades.
   - Occurs reliably when presented chunks exceed ~9 items (roughly mean + 1 SD).
   - Manifests as: longer task completion time, higher error rates, abandonment, reduced recall of later items (recency effect worsens).
   - Overload is nonlinear: crossing from 7 → 9 items has less impact than 9 → 12.

5. **Chunking and hierarchy** — the mechanism by which designers reduce *effective* chunk count.
   - Grouping semantically related items under a category label reduces presentation load (e.g., "Colors: Red, Blue, Green" is 1 chunk with 3 sub-items, not 4 separate chunks).
   - Hierarchy allows deeper exploration of subsets without loading the whole tree at once.
   - Labeling and visual separation reinforce chunk boundaries.

## Key Predictions

- **Flat menus with 10+ items will produce higher error rates, longer task completion, and lower menu item recall compared to hierarchically organized menus with 5–7 top-level items**, even if total item count is identical.

- **Adding a 10th item to an interface that already presents 7–8 items will produce a disproportionate drop in task performance** — the last item added is both harder to retain and suffers recency interference from earlier items.

- **Reordering the same 7 items into semantic groups (e.g., "Colors," "Sizes," "Prices") will reduce perceived cognitive load and error rates compared to alphabetical or arbitrary ordering**, because grouped items compress into fewer effective chunks.

- **Expert users (e.g., pilots using a familiar cockpit) will tolerate more than 7±2 items *in a known, practiced context***, because expertise compresses familiar patterns into single chunks — but this does not invalidate the 7±2 limit for novel information or untrained users.

- **Form fields presented all at once on a single page will show higher abandonment and lower completion rates as field count exceeds 7–9**, compared to multi-step forms that present 5–7 fields per screen.

- **Interfaces that violate Miller's Law (presenting 15+ items flat) will have a "forgotten end" effect**, where later items are recalled or acted upon at rates below chance — not because they are harder to encode but because they exceed WMC.

## Application Procedure

Instantiate the model against a specific interface, list, menu, or information presentation.

1. **Define the interface scope.** What is the user's task, and what single view or interaction are you evaluating? (E.g., "The 'Categories' dropdown in the mobile app," not "the entire product," which is too broad.)

2. **Identify and count chunks presented to the user in that view.**
   - List every visually or semantically distinct item the user must process: menu items, buttons, form fields, list entries, instructions, icons with labels, etc.
   - Count based on the user's actual task and expertise level, not your internal categorization. (A novice sees "File, Edit, View" as 3 chunks; a power user may see "File (with 12 subcommands)" as 1 chunk if the structure is automatic.)
   - If items are grouped or hierarchical, count the top-level chunks only for a first pass.

3. **Assess chunking and grouping quality.**
   - Are items grouped under meaningful category labels?
   - Are visual separations (spacing, borders, color) used to reinforce groupings?
   - Is the ordering (alphabetical, by frequency, by category) helping or hindering perception?
   - Is there unnecessary variety in item length or format that would increase perceived chunk count?

4. **Map to the 7±2 band.**
   - If chunk count is ≤5: load is well below capacity; no overload prediction.
   - If 5–7: comfortable; low error rates expected.
   - If 7–9: at capacity; performance is stable but fragile — adding items will degrade rapidly.
   - If 9–12: overload zone; error rates and completion time will rise noticeably.
   - If >12: severe overload; high abandonment, low recall of later items.

5. **Identify overload mechanisms if present.**
   - Lack of visual grouping (all items the same size, spacing, color)?
   - Poor labeling or semantic relation between items?
   - Unfamiliar domain (items are not chunks to this user)?
   - Time pressure or divided attention (user is multitasking)?

6. **Generate the prediction.**
   - Will users succeed at the task within this interface, or will they exceed WMC and show degraded performance?
   - Which items will be forgotten, misclicked, or skipped?
   - What is the remediation: reduce items, add hierarchy, improve labels, or train the user on chunking?

7. **Check boundary conditions** (below). If any apply, note that the 7±2 limit may not be the binding constraint.

## Boundary Conditions

Miller's Law applies to the *perception and retention* of discrete items under working memory constraints. It breaks down or becomes secondary under:

- **Very familiar, highly practiced contexts.** Expert pilots or radiologists facing familiar information structures can exceed 7±2 items because expertise compresses patterns into single chunks. The limit still applies to *novel* information within their domain. Designers cannot assume all users are experts.

- **Spatial or visual layout that creates sub-groups the user naturally scans in isolation.** If a 15-item list is visually arranged in a 3×5 grid with clear cell boundaries, users may process it as 3 groups of 5 rather than 15 flat items — the effective chunk count depends on how the layout invites chunking. The limit is not violated, only masked by good layout.

- **Procedural or sequential tasks where items are revealed gradually over time.** Miller's Law applies to items held simultaneously in working memory. A wizard form that reveals 3 fields, then hides them and reveals 3 more does not violate the limit, even if the total form has 20 fields. Time separates the chunks.

- **Semantic or meaningful tasks where items are deeply integrated (low distinctness).** Miller's Law assumes items are discrete. A novel's 200 pages do not violate 7±2 because the information is integrated into a coherent narrative, not a list of unrelated chunks. Measure chunk count based on *functional distinctness* in the user's task, not physical item count.

- **High cognitive load from other sources (mental math, instruction complexity, stress).** The 7±2 limit is not fixed; it can degrade to 4±1 under divided attention. If a user is already cognitively taxed, the effective WMC for your interface drops, and even 6 items may overload. Measure the user's baseline load.

- **Cross-cultural or linguistic variation.** The 7±2 limit is observed across cultures, but the perception of what constitutes a "chunk" is language- and culture-dependent. A label that is a single recognizable chunk in English may be multiple chunks in another language. Test with actual users, not assumptions.

## Output Format

```
## Miller's Law Analysis: <interface or presentation name>

**Scope:** <user task, view, or interaction being evaluated>
**User type:** <novice / intermediate / expert, and familiarity with this domain>
**Presentation mode:** <menu, form, list, dropdown, sidebar, etc.>

### Chunk inventory
| Item or group | Chunk count | Reasoning |
|---|---|---|
| ... | ... | ... |

**Total chunks presented:** <n>
**Assessment:** <within 7±2 / above / well above>

### Grouping and hierarchy
- Visual grouping: <present / absent, effectiveness>
- Category labels or semantic relation: <clear / unclear / missing>
- Labeling clarity: <users will recognize chunks as distinct / ambiguous / confusing>

### Overload risk and performance prediction
- Predicted error rate: <low / moderate / high>
- Predicted task completion rate: <high / moderate / low>
- Predicted items at risk of being skipped or forgotten: <which ones, why>
- Completion time impact: <no impact / noticeable slowdown / severe slowdown>

### Remediation (if overload detected)
- Reduce total chunks: <e.g., combine related items, hide advanced options>
- Improve chunking: <add category labels, visual separation, reorder>
- Use hierarchy: <convert flat list to dropdown, accordion, or wizard>
- Other: <domain-specific suggestions>

### Boundary-condition check
<which of the above boundary conditions apply; does WMC remain the binding constraint or is another factor (expertise, layout, time separation) dominant>

### Confidence: high | medium | low
<reasoning: data quality on user expertise + whether the presentation is novel or practiced + layout effectiveness + whether competing cognitive load is controlled>
```
