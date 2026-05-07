---
name: morphological-analysis
display_name: Morphological Analysis (Zwicky)
class: lens
underlying_class: native
domain: brainstorming
source: Fritz Zwicky (Astrophysics Institute, 1969); "Discovery, Invention, Research Through the Morphological Approach"
best_for:
  - Systematically generating solution variants when the design space feels constrained
  - Identifying overlooked combinations in complex multi-variable problems
  - Breaking out of incremental thinking by forcing exploration of all quadrants
one_liner: "Systematically explore the full combinatorial space across dimensions and values."
---

# Morphological Analysis (Zwicky)

## Overview
Morphological Analysis structures a problem by its key dimensions, lists the possible values (variants) for each dimension, and then systematically explores the combinatorial grid. Instead of relying on intuition or habit to pick one value per dimension, you generate and evaluate many combinations — including unlikely ones. Practitioners use this when the solution space is large, when existing solutions dominate discussion, or when they suspect novel combinations have been overlooked.

## Analytical Procedure

### Phase 1 — Define the Morphological Space

1. **State the design problem in one sentence.** What are you trying to solve or design? Be specific enough to bound the problem but broad enough that multiple solution approaches exist.

2. **Identify 3–6 key dimensions.** These are the fundamental variables that define any solution in this space. Dimensions must be:
   - **Independent** — changing one should not force you to change another (though values may interact)
   - **Comprehensive** — together they should cover all major aspects of a solution
   - **Non-overlapping** — no dimension should be a subset of another
   
   Examples: For "sustainable transportation," dimensions might be (Propulsion, Energy source, Capacity, Route type, Ownership model). For "meeting scheduling," dimensions might be (Format, Location, Participant pre-work, Duration, Decision mechanism).

3. **For each dimension, list 4–8 possible values or variants.** Values must be:
   - **Concrete** — not abstract concepts, but things you could actually build or test
   - **Mutually exclusive** — a solution picks one value per dimension (or explicitly none, which counts as a variant)
   - **Non-evaluative** — list "Combustion engine" and "Electric motor," not "Outdated engine" and "Superior motor"
   
   Do not restrict this list to what currently exists. If you list only commercial variants, you will bias the grid toward the status quo.

4. **Build the morphological matrix.** Draw a table with dimensions as rows and values as columns. This is the grid you will explore.

### Phase 2 — Systematic Exploration

5. **Generate combination candidates.** Choose a systematic rule for sampling the grid:
   - **Exhaustive** (for small grids): Generate all combinations. With 3 dimensions of 4 values each, that is 64 combinations. Beyond ~100, exhaustive becomes impractical.
   - **Random sampling** (for large grids): Randomly select 30–50 combinations across the full grid. Record the seed so the sample is reproducible.
   - **Boundary exploration** (for directed search): Pick extreme values (e.g., cheapest + fastest, most niche + most mass-market) and combinations near those extremes.
   - **Constraint satisfaction** (for feasibility-aware search): If certain combinations are infeasible (e.g., "solar + submarine" is nonsense), mark them and skip, but still explore the remaining grid systematically.

6. **For each candidate combination, write a brief description.** 2–3 sentences. Describe what the solution would look like if you actually built it. Do not evaluate it yet. Examples:
   - "Electric motor + shared fleet + subway routes + autonomous driving" → A fleet of small autonomous electric vehicles that move continuously on fixed subway corridors, booked on-demand.
   - "Combustion engine + owner-operated + any road + manual" → A privately owned car with a gas engine that you drive yourself.

7. **Evaluate each combination against your problem goals.** Use a fixed rubric:
   - **Feasibility** (can this actually exist with current or near-term technology?): Y/N
   - **Goal alignment** (does this solve the stated problem?): Y/N
   - **Novelty** (is this significantly different from existing solutions?): Y/N
   - **Viability signal** (does this seem worth investigating further?): Strong / Weak / None

   Tag each combination with these four signals. Do not discard combinations marked "Weak" or "None" — they often yield insights.

### Phase 3 — Synthesis and Insight

8. **Cluster the combinations by viability signal.** Separate Strong, Weak, and None into three groups.

9. **Extract insights from weak and null combinations.** Why does a combination fail to align with your goals? Common answers:
   - A dimension value itself is infeasible (the problem is with that value, not the combination)
   - The combination exposes a hidden constraint (e.g., "solar + always-on" fails because solar is intermittent — revealing that "availability" is a hidden dimension you didn't list)
   - The combination is unviable because the dimensions interact (e.g., "manual control + 1000-person capacity" doesn't work because humans can't manually coordinate that scale)

10. **Identify promising combinations** — those marked Strong or combinations with interesting weak signals (revealing a hidden dimension or interaction). For each, note:
    - What makes this combination novel relative to current solutions?
    - What would have to be true for this to work?
    - What is the smallest experiment you could run to test one aspect of it?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Design problem stated as a single, bounded sentence | Y/N |
| 3–6 dimensions identified; each is independent and non-overlapping | Y/N |
| Each dimension has 4–8 concrete, mutually exclusive values | Y/N |
| At least 30 combinations were generated and briefly described | Y/N |
| Each combination evaluated with all four signals (Feasibility, Goal alignment, Novelty, Viability) | Y/N |
| Weak/None combinations analyzed for hidden dimensions or interactions | Y/N |
| At least 3 combinations marked Strong or with actionable insights | Y/N |

## Red Flags

- The matrix contains only existing commercial solutions. You are exploring the past, not the design space.
- All combinations cluster into one viability band (all Strong or all None). Either the problem is trivial or the dimensions are not truly independent.
- A dimension has only 2 values. Dimensions with 2 values are binary choices; expand or split into finer dimensions.
- Combinations are evaluated using intuition only ("this feels wrong"). Use the rubric; intuition biases toward the familiar.
- No Weak or None combinations are analyzed. These often contain the most novel insights.
- The evaluation rubric is fuzzy ("seems viable"). Define each signal concretely: What counts as feasible? What is the time horizon? What are your goal metrics?

## Output Format

```
## Morphological Analysis Report

**Design Problem:**
<one sentence>

### Morphological Matrix

| Dimension | Value 1 | Value 2 | Value 3 | ... |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | |
| <...> | <...> | <...> | <...> | |

### Combination Candidates

#### Combination 1: [Dimension1=Value, Dimension2=Value, ...]
Description: <2–3 sentences>
- Feasibility: Y/N
- Goal alignment: Y/N
- Novelty: Y/N
- Viability signal: Strong / Weak / None

#### Combination 2: ...

### Insights from Weak/None Combinations

| Combination | Why it failed | Hidden dimension or interaction revealed |
|---|---|---|
| <...> | <...> | <...> |

### Promising Combinations (Strong + High-Signal Weak)

1. **[Combination X]**
   - Novel relative to status quo: <...>
   - What must be true: <...>
   - Smallest testable experiment: <...>

2. ...

### Confidence
<high/medium/low> — <justification>
```
---
