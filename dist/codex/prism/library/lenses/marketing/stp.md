---
name: stp
display_name: Segmentation, Targeting, Positioning
class: lens
underlying_class: native
domain: marketing
source: Wendell Smith (1956); foundational in modern marketing strategy
best_for:
  - Clarifying market structure and competitive position
  - Validating product-market fit before scaling
  - Identifying gaps between intended and actual positioning
one_liner: "Three-step strategic framework — Segment, Target, Position — to sharpen differentiation."
---

# Segmentation, Targeting, Positioning

## Overview
STP decomposes market strategy into three sequential, measurable decisions: (1) dividing the market into distinct groups by shared characteristics, (2) choosing which groups to serve, and (3) defining how your offering will be perceived relative to competitors within that group. Practitioners use it to move from vague market ambitions ("we're for everyone who needs software") to concrete competitive claims that can be tested and defended. The discipline is the rigor of each layer — most strategies collapse because one layer was skipped or remained abstract.

## Analytical Procedure

### Phase 1 — Segmentation

1. **Define the addressable market.** State the broadest category of customer need or use case your offering could theoretically serve. Example: "People who need to track their personal finances" not "software users."

2. **Identify segmentation variables.** Choose one primary dimension and 1–2 secondary dimensions. Acceptable variables include:
   - **Demographic:** age, income, education, location, company size
   - **Behavioral:** purchase frequency, usage intensity, price sensitivity, switching cost
   - **Psychographic:** values, decision criteria, lifestyle, risk tolerance
   - **Firmographic:** industry, company stage, growth rate, revenue
   - **Needs-based:** specific problem statement, desired outcome, pain point ranking

3. **Map distinct segments.** For each variable, identify 3–5 segments that satisfy these criteria:
   - Internally homogeneous (members behave similarly)
   - Externally heterogeneous (different from other segments)
   - Measurable (you can identify members through observable traits)
   - Accessible (you can reach them with marketing and sales effort)
   - Substantial (large enough to justify targeted effort)

4. **Characterize each segment.** For the top 3 candidates, write:
   - Size estimate (number of addressable customers, TAM for that segment)
   - Willingness to pay (price tolerance or budget range)
   - Primary decision criterion (what drives purchase choice)
   - Current solution and dissatisfaction (what they use now and why it fails them)

### Phase 2 — Targeting

5. **Evaluate each segment against your constraints.** Create a scoring matrix:
   | Segment | Size | Profitability | Go-to-market feasibility | Strategic fit | Total score |
   |---|---|---|---|---|---|
   | | 1–5 | 1–5 | 1–5 | 1–5 | |

   Profitability = price willingness × gross margin potential.
   Go-to-market feasibility = can you afford to reach and convert this segment?
   Strategic fit = does this segment align with your core competency and product roadmap?

6. **Apply elimination filters.** Remove segments that:
   - Have clearly superior competitors with moat (entrenched and hard to displace)
   - Require product capabilities you cannot build in 12–24 months
   - Operate in regulatory jurisdictions you cannot serve
   - Are declining in size or consolidating (shrinking TAM)

7. **Rank the remaining candidates.** Order by total score and validate the top 2 manually. The manual step: spend 1–2 hours researching the target segment (5–10 customer interviews, analyst reports, competitor positioning) and verify the size and willingness-to-pay assumptions. Recalibrate scores if reality deviates.

8. **Make the targeting decision.** Commit to your primary target segment in writing. Identify 1 secondary segment for future expansion. Say explicitly: "We are targeting [segment name] first because [reason from evaluation]."

### Phase 3 — Positioning

9. **Identify the competitive set.** List 4–6 offerings (products, vendors, or alternatives including "do nothing") that your target segment currently uses or considers. Include indirect competitors (if targeting small-business accountants, Quickbooks, Excel, outsourced bookkeepers, and pen-and-paper all compete).

10. **Map the competitive landscape.** Choose 2 attributes that matter most to your target segment (from their stated decision criteria). Plot each competitor on a 2D grid:
    - X-axis: attribute A (e.g., "ease of use")
    - Y-axis: attribute B (e.g., "total cost of ownership")
    Populate with your knowledge of each competitor's strengths. Note the empty spaces (whitespace) and crowded regions (commoditized).

11. **Formulate a differentiation claim.** Write a single statement that:
    - Is specific to your target segment (not universal)
    - Occupies a defensible position on the map (whitespace or a gap)
    - Reflects a real strength you possess or can credibly build
    - Directly addresses the target's primary decision criterion

    Bad: "We are the best CRM."
    Good: "We are the only CRM built for 2–5 person sales teams with no IT support, so it takes 30 minutes to set up instead of 4 weeks."

12. **Test the positioning against the target.** Conduct 3–5 conversations with target customers (or lookalike prospects). Present your differentiation claim (not your name, not your product, just the claim). Record:
    - Do they immediately understand what you're claiming to be different at?
    - Does the difference matter to them (would it influence a decision)?
    - Do they find it credible given the competitive set?

    If fewer than 3 out of 5 answer "yes" to all three questions, revise the claim.

13. **Anchor the positioning operationally.** Translate the positioning statement into:
    - **Messaging priority:** the 1–2 phrases that appear first in marketing materials
    - **Feature emphasis:** which product capabilities get highlighted; which are de-emphasized
    - **Proof points:** pricing, case studies, customer testimonials that reinforce the claim
    - **Go-to-market channels:** which sales and marketing tactics will credibly reach and convert the target

## Evaluation Criteria

| Check | Pass |
|---|---|
| Segmentation uses consistent variable(s) and produces 3–5 distinct segments | Y/N |
| Each segment has size estimate, willingness-to-pay, and dissatisfaction statement | Y/N |
| Targeting evaluation matrix scores all candidates consistently | Y/N |
| Primary and secondary targets are named explicitly | Y/N |
| Competitive set includes 4–6 options including indirect competitors | Y/N |
| Positioning claim is specific, defensible, and addresses primary decision criterion | Y/N |
| Positioning claim was tested with ≥3 target customers and passes ≥60% | Y/N |
| Positioning is translated into messaging, features, proof points, and channels | Y/N |

## Red Flags

- Segmentation produces identical descriptions across segments ("they all value quality and low cost"). Segments are not internally homogeneous — the variable chosen was too coarse.
- Targeting evaluation scores all segments highly. Either constraints were not applied or the evaluation was lenient. Remove candidates more aggressively.
- Positioning claim is generic ("best value," "most innovative," "customer-focused"). It does not differentiate from the competitive set or lives in a crowded region of the map.
- Positioning has not been tested with target customers. You are guessing that they care about your claimed difference.
- Primary target is described as "everyone who could benefit" or "multiple segments equally." You have not committed to a target.
- The segmentation, targeting, and positioning are disconnected — the target doesn't align with the segments chosen, or the positioning doesn't address the target's decision criteria.

## Output Format

```
## STP Strategy

### Segmentation
| Segment | Size | Willingness-to-pay | Primary dissatisfaction | 
|---|---|---|---|
| | | | |

### Targeting Evaluation
| Segment | Size | Profitability | Go-to-market | Strategic fit | Score |
|---|---|---|---|---|---|

**Primary target:** <name and justification>
**Secondary target:** <name and justification>

### Competitive Landscape
**Attributes:** <X-axis> vs <Y-axis>

| Competitor | X position | Y position | Strength |
|---|---|---|---|

**Whitespace identified:** <position on map where target's needs are unmet>

### Positioning
**Differentiation claim:**
> <specific, testable statement addressing target's primary decision criterion>

**Validation (target feedback):**
- Understanding: _ / 5
- Relevance: _ / 5
- Credibility: _ / 5

### Operationalization
- **Messaging:** <primary phrases>
- **Feature priority:** <features to emphasize>
- **Proof points:** <pricing, case studies, testimonials>
- **Channels:** <go-to-market tactics>

### Confidence
<high | medium | low> — <justification based on validation testing and competitive research depth>
```
