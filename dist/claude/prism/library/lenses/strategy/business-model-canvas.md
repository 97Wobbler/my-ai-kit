---
name: business-model-canvas
display_name: Business Model Canvas
class: lens
underlying_class: native
domain: strategy
source: Alexander Osterwalder and Yves Pigneur, 2010
best_for:
  - Visualizing how a business creates, delivers, and captures value
  - Stress-testing business assumptions across nine interdependent components
  - Communicating a business model to diverse stakeholders in a single artifact
one_liner: "Visualize and validate value flow via nine business-model blocks."
---

# Business Model Canvas

## Overview
The Business Model Canvas is a one-page strategic template that maps how a business operates across nine components: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, and Cost Structure. Rather than building a 50-page business plan, practitioners use this lens to externalize their assumptions about how the business works, identify hidden dependencies, and pressure-test the model before execution. The nine blocks form an interconnected system — changes in one block cascade to others, which is exactly the point.

## Analytical Procedure

### Phase 1 — Fill the Canvas

1. **Identify your primary Customer Segment.** Who is paying for your product or service? Write one specific segment; ignore adjacencies for now. Examples: "SMB accountants in US markets with <$50M revenue," not "businesses."

2. **Define the Value Proposition for that segment.** What problem does your product solve, or what outcome does it enable? Write it as a benefit, not a feature. Bad: "real-time dashboard." Good: "accountants can detect cash flow gaps within 24 hours and reforecast weekly without manual labor."

3. **Map Channels.** Through what media do you reach and deliver to this customer segment? List: awareness (how they find you), evaluation (how they learn it works), purchase (how they buy), delivery (how they get it), support (how you help post-sale). Distinguish owned, partner, and paid channels.

4. **Specify Customer Relationship.** What ongoing interaction model do you maintain? Personal assistance, self-service, automated (e.g., email), community, etc. Be explicit about who is engaged — the buyer, the user, or both.

5. **List Revenue Streams.** How do you extract money from the customer? Subscription, per-use, licensing, marketplace take, freemium upgrade, etc. For each stream, name the pricing model (fixed, variable, tiered) and estimated price point or volume assumption.

6. **Name Key Resources.** What assets must you own, control, or access to execute the model? Physical (factories, servers), intellectual (patents, data), human (engineering talent, domain experts), financial (cash, credit lines). Be specific — "technology" is not a resource.

7. **List Key Activities.** What work must you do repeatedly to deliver the value proposition? Production, problem-solving, platform/network operations, marketing, customer success. Avoid copying generic activity lists; write what *you* must do.

8. **Map Key Partnerships.** What external organizations are essential to your model? Suppliers, complementors, strategic partners, outsourced functions. For each, write why they are essential (what do they provide that you cannot build fast or cheaper?).

9. **Build Cost Structure.** Identify fixed costs (salaries, rent, infrastructure) and variable costs (COGS, payment processing, support labor). Estimate the largest cost drivers and their percentage of revenue. Revenue - Costs = Unit Economics or burn rate.

### Phase 2 — Pressure-test Dependencies

10. **For each Revenue Stream, trace backward.** Does it require something in Key Resources or Key Activities that you don't have? Does it depend on a Partnership that is not yet secured? Write the dependency chain.

11. **For each Key Activity, ask: "What fails if we don't do this?"** If the answer is "nothing" or "it's nice to have," move it out of Key Activities — it's a nice-to-have. If the answer is "customers don't get the core value," it stays.

12. **For each Key Partnership, check: "Have we signed a term sheet, LOI, or contract?"** If no, write it as a risk. If yes, note the term length and renewal date. Unsigned partnerships are assumptions, not facts.

13. **Check the Channel-to-Segment fit.** Are the channels where your customer segment actually buys, or where you hope they will? For B2B, is a direct sales team the model or wishful thinking? For B2C, if you're betting on organic social, do you have evidence that segment uses that platform?

14. **Examine Cost Structure against Revenue.** Calculate months-to-breakeven or annual burn. If the canvas shows $50K monthly burn but Revenue Streams are "freemium with 2% conversion," does the math work? Where is the path to profitability?

15. **Identify circular dependencies.** Does Customer Relationship depend on a Key Activity that depends on a Partnership that depends on a Channel decision? Trace and write the dependency cycle — these are your risk nodes.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All nine blocks are filled with specific entries (not generic) | Y/N |
| Value Proposition is stated as an outcome, not a feature | Y/N |
| Revenue Streams include pricing model and assumed price/volume | Y/N |
| Key Resources list at least one asset you do not yet own | Y/N |
| Every Key Partnership has a status: signed / unsigned / risk | Y/N |
| Cost Structure is estimated within an order of magnitude | Y/N |
| At least one dependency cycle has been identified and written | Y/N |
| Customer Segment is narrow enough to fit on one line | Y/N |

## Red Flags

- All nine blocks are filled but they read like a generic template ("we will use online and offline channels," "we will build strong customer relationships"). The canvas is aspirational fiction, not a model.
- Revenue Streams and Cost Structure do not intersect with unit economics — no attempt to estimate breakeven or profitability. The model is untested.
- Key Partnerships are all unsigned or conditional. The business depends on handshake agreements or hoped-for integrations that have not been negotiated.
- Value Proposition is stated as a feature or technology ("AI-powered," "blockchain-based"), not an outcome. The customer's problem is not addressed.
- Customer Segment is too broad ("businesses," "enterprises"). The model is trying to serve everyone and actually serves no one.
- Circular dependencies exist but are not acknowledged. When asked, "If Partner X backs out, what happens to Revenue Stream Y," the answer is vague.
- Channel strategy and actual customer buying behavior are misaligned — the canvas shows aspirational go-to-market, not empirical fit.

## Output Format

```
## Business Model Canvas Assessment

### Canvas Summary
| Block | Entry |
|---|---|
| **Customer Segment** | <...> |
| **Value Proposition** | <...> |
| **Channels** | <...> |
| **Customer Relationship** | <...> |
| **Revenue Streams** | <...> |
| **Key Resources** | <...> |
| **Key Activities** | <...> |
| **Key Partnerships** | <...> |
| **Cost Structure** | <...> |

### Dependency Analysis
| Dependency | Status | Risk Level |
|---|---|---|
| <Resource requirement for Revenue Stream X> | <Available / At-risk / Missing> | <High / Medium / Low> |
| <Partnership requirement for Key Activity Y> | <Signed / Unsigned / Uncertain> | <...> |

### Unit Economics
- **Monthly Revenue (estimated):** <$...>
- **Monthly Cost (estimated):** <$...>
- **Burn/Surplus:** <$...>
- **Months to Breakeven:** <...> or <not profitable in current model>

### Key Risks
1. <Unsigned partnership / Misaligned channel / Unproven assumption>
2. <...>

### Pressure-Test Findings
- **Channel-Segment Fit:** <Aligned / Misaligned / Untested>
- **Revenue-Cost Alignment:** <Viable path / Uncertain / Unprofitable>
- **Circular Dependencies:** <None / Present at: ...>

### Confidence
<high | medium | low> — <justification: based on completeness of research, realism of estimates, status of partnerships, and empirical validation>
```
---
