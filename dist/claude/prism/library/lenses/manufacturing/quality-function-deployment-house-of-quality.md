---
name: quality-function-deployment-house-of-quality
display_name: Quality Function Deployment / House of Quality
class: lens
underlying_class: native
domain: manufacturing
source: Yoji Akao (1966, Japan); adapted for product development in the US by ASI and GOAL/QPC in the 1980s
best_for:
  - Translating customer needs into engineering specifications without loss or distortion
  - Preventing misalignment between marketing claims and what the design can deliver
  - Prioritizing engineering effort where customer value is highest
one_liner: "QFD House of Quality — map the voice of the customer into engineering language."
---

# Quality Function Deployment / House of Quality

## Overview
Quality Function Deployment (QFD), operationalized through the "House of Quality" matrix, captures what customers need, translates it into how the product must perform, and traces each engineering specification back to customer value. The discipline is *completeness of the mapping* — most teams build partial matrices or skip the correlation step, leaving hidden gaps between customer intent and design. Practitioners use this when launching a new product, redesigning an existing one, or when field failures suggest the design missed something the customer actually cared about.

## Analytical Procedure

### Phase 1 — Gather Customer Needs ("What")

1. **Conduct Voice of Customer (VoC) interviews or surveys.** Speak to 10–30 actual users or end customers, not just sales or product managers. Ask open-ended questions: "What frustrates you about the current product?" "What would make this easier?" "When did this last fail you?" Record verbatim statements.

2. **Cluster the statements into need categories.** Group similar complaints or wishes. Examples: "starts up too slowly," "takes forever to boot," "laggy on startup" → cluster as "Startup speed."

3. **Write each need in the customer's language, not engineering language.**
   - Bad: "Reduce latency to <100ms."
   - Good: "Loads results fast enough to not make me wait."

4. **Assign a priority weight to each need.** Use customer frequency, business impact, or competitive importance. Common scale: 1–5 or 1–10. Record the weighting method (e.g., "number of customers who mentioned this").

### Phase 2 — Translate to Engineering Specifications ("How")

5. **For each customer need, generate 2–4 measurable engineering specifications** that would satisfy it. Avoid one-to-one pairing; most needs require multiple specs to be fully met.
   - Customer need: "Loads results fast."
   - Specs: (a) Query response time ≤50ms, (b) UI render time ≤30ms, (c) Image pre-caching enabled by default.

6. **Make each spec quantifiable and testable.** It must be something you can measure in a lab or field trial. Vague specs ("good performance," "intuitive interface") are red flags.

7. **Record the *direction* of each spec:** "more is better" (e.g., battery life in hours), "less is better" (e.g., error rate %), "target is X ± Y" (e.g., operating temperature 20–25°C).

### Phase 3 — Build the Relationship Matrix

8. **Create a table (or the "roof" of the House):** rows are customer needs, columns are engineering specs. At each intersection, mark the *strength* of the relationship:
   - **Strong** (●●● or 9 points) — The spec directly and substantially satisfies the need.
   - **Medium** (●● or 3 points) — The spec contributes but other specs also matter.
   - **Weak** (● or 1 point) — The spec has minor influence.
   - **Empty** — No relationship.

9. **Check for orphan needs:** If a row has no strong relationships, the team missed a spec or the need cannot be met by design alone (e.g., "it's cheap" might require process improvements, not just design). Flag these.

10. **Check for orphan specs:** If a column has no strong relationships, either it's a solution in search of a problem (wasteful) or it serves a different goal (reliability, manufacturability). Document its rationale or consider dropping it.

### Phase 4 — Identify Correlations and Trade-offs

11. **In the "roof" section above the specs row, mark correlations between specs:**
   - **Positive** (↑ or ✓) — Improving one helps the other. Example: reducing circuit complexity reduces power consumption.
   - **Negative** (↓ or ✗) — Improving one hurts the other. Example: increasing screen brightness increases power drain.
   - **None** — Independent.

12. **For each negative correlation, document the trade-off.** Which need wins in the priority? Who makes that call? This surfaces decision authority and risk.

### Phase 5 — Prioritize and Benchmark

13. **Calculate a weighted importance score for each spec:**
   - For each spec, multiply the priority weight of each customer need by the relationship strength (9, 3, or 1), then sum.
   - This tells you which specs have the highest customer-value leverage.

14. **Benchmark:** Research what competitors or best-in-class products achieve on each spec. Record as a column adjacent to your target.

15. **Set targets:** For each spec, decide your target value. Use the benchmark to set realistic targets — aiming for "best in class" on every spec is expensive and often impossible.

### Phase 6 — Validate and Hand Off

16. **Review the completed House with both customer advocates and engineering leads.** Test the claim: "If we hit all these specs, will customers be happy?" If the answer is hedged or uncertain, the mapping is incomplete.

17. **Assign ownership.** Each spec should have a named engineer or subsystem owner responsible for hitting the target.

18. **Document assumptions and risks.** Note any spec where hitting the target requires new technology, long lead times, or manufacturing changes. These are execution risks.

## Evaluation Criteria

| Check | Pass |
|---|---|
| VoC gathered from ≥10 actual customers or end users (not secondhand) | Y/N |
| Every customer need is stated in plain language (no jargon) | Y/N |
| Every customer need has ≥2 engineering specs linked to it | Y/N |
| Every engineering spec is quantifiable and measurable | Y/N |
| All relationship cells in the matrix are filled (no guessing) | Y/N |
| Orphan needs and orphan specs are explicitly flagged and justified | Y/N |
| Negative correlations in the roof are documented with trade-off owners | Y/N |
| Weighted importance scores calculated for every spec | Y/N |
| Engineering leads agree the target specs will satisfy customer needs | Y/N |
| Each spec has a named owner | Y/N |

## Red Flags

- The customer needs were gathered secondhand (from sales, marketing, or past studies). Direct VoC is non-negotiable; you will misinterpret what customers care about.
- Multiple customer needs map to zero or one spec. This guarantees the design will miss customer intent. Expand the spec list or re-examine needs.
- The relationship matrix is sparse (many empty cells). Either the specs and needs are misaligned or the team didn't interrogate the relationships thoroughly.
- Specs use adjectives instead of numbers ("fast," "reliable," "user-friendly"). These cannot be tested and will cause disputes at design review.
- Negative correlations in the roof are ignored. Trade-offs not named become surprises during design; you end up with a product that fails at one thing because you over-optimized another.
- The same engineer targets multiple high-priority specs with no dependency or phasing plan. Overload and missed targets follow.
- No benchmark data. You have no way to know if your targets are achievable or competitive.
- Engineering pushback on targets is noted but the target doesn't change. If engineering says "we can't hit 50ms response time," the need ("loads fast") is real but the spec is wrong. Iterate.

## Output Format

```
## Quality Function Deployment Report

### Voice of Customer
| Priority | Customer Need | Frequency | Source |
|---|---|---|---|
| <1-5> | <plain language> | <count/ratio> | <method> |

### Engineering Specifications
| Spec ID | Specification | Direction | Target | Benchmark | Owner |
|---|---|---|---|---|---|
| <S1> | <quantified, measurable> | more/less/target ± range | <value> | <competitor value> | <name> |

### Relationship Matrix (House Body)
```
                  [S1]  [S2]  [S3]  ...
Customer Need 1    ●●●   ●●    —
Customer Need 2    ●●    —     ●●●
...
```

### Correlation Matrix (House Roof)
```
        [S1-S2]  [S1-S3]  [S2-S3]  ...
       ↑ / ↓ / —
```

### Weighted Importance Score
| Spec | Calc: Σ(need priority × relationship strength) | Score |
|---|---|---|
| S1 | (5×9) + (3×3) + (4×1) | 54 |

### Trade-off Analysis
| Negative Correlation | Specs Involved | Decision | Owner |
|---|---|---|---|
| <...> | <...> | <which spec wins> | <authority> |

### Orphan Analysis
**Needs with no strong spec link:** <list or "none">
**Specs with no need link:** <list or "none">

### Validation Checkpoint
Engineering sign-off: "Meeting these specs will satisfy customer needs." [Yes/No/Conditional]
Conditional note: <if applicable>

### Confidence
<high | medium | low> — <justification. High if: VoC is direct, specs are testable, matrix is complete, no orphans, engineering agrees. Medium if: one element weak (e.g., small sample VoC, one orphaned need, weak benchmark). Low if: multiple gaps or no engineering alignment.>
```
