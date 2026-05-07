---
name: fab
display_name: Features, Advantages, Benefits
class: lens
underlying_class: native
domain: marketing
source: origin uncertain
best_for:
  - Translating product specs into customer-facing value propositions
  - Aligning sales messaging with buyer pain points
  - Stress-testing claims about competitive differentiation
one_liner: "Translate product features into advantages and benefits aligned with customer needs."
---

# Features, Advantages, Benefits

## Overview
FAB translates a product's raw attributes into a narrative hierarchy that speaks to buyers. A **Feature** is what the product is or does (specifications, technical properties). An **Advantage** is why that feature matters in isolation (what capability it unlocks). A **Benefit** is what the advantage means for the customer's concrete situation (the outcome or pain relief the buyer actually cares about). Practitioners use this lens when product documentation is strong but sales messaging is generic, or when a pitch feels feature-heavy and lands nowhere.

## Analytical Procedure

### Step 1 — Extract Features
1. **List all features of the product.** Write 8–15 discrete, testable attributes. Include technical specs (e.g., "API rate limit: 1000 requests/min"), functional capabilities (e.g., "integrates with Salesforce via OAuth"), and structural properties (e.g., "deployed on 3 continents").
2. **For each feature, state it as objectively as possible.** Remove marketing language. If you wrote "lightning-fast," rewrite it as "sub-200ms response time at 95th percentile."

### Step 2 — Identify Advantages
3. **For each feature, ask: "What becomes possible or easier because of this?"** Write the immediate capability or relief, divorced from any particular customer type. Write 1–2 advantages per feature.
   - Feature: "OAuth 2.0 integration with Salesforce"
   - Advantage: "Eliminates manual credential entry and sync tasks; users authenticate once and are always in sync."

4. **Check that each advantage is **not** customer-specific.** If you write "sales teams love that they...", you are writing a benefit, not an advantage. Rewrite it as "eliminates the need for..." or "reduces time to..." or "makes possible..."

### Step 3 — Map Benefits to Buyer Personas
5. **Define 3–5 buyer personas relevant to the product.** For each, list their primary pain point or goal (e.g., "VP of Sales wants to close deals faster"; "Data Engineer needs to avoid manual pipelines").
6. **For each persona + pain point pair, go through your advantages and ask: "Does this advantage directly address this pain point?"** If yes, write the benefit — the specific relief or outcome that buyer will experience.
   - Persona: VP of Sales, pain: "My team spends 3 hours/week syncing CRM with external data."
   - Advantage: "Eliminates manual sync tasks."
   - Benefit: "Your team recovers 12+ hours/month and can focus on actual deal work instead of data hygiene."

7. **Write each benefit in the customer's language, not engineering language.** Use outcomes, time/money saved, or risk reduced. Quantify if possible.

### Step 4 — Validate the Chain
8. **For each Benefit you wrote, trace backward:** Does it follow logically from the Advantage? Does the Advantage flow from the Feature? If any link breaks, revise or drop the claim.
9. **Check for orphaned features.** Are there 3+ features with no mapped Advantage? If yes, they may be:
   - Real but immaterial to customer value (keep for completeness, don't emphasize).
   - Misidentified as features (perhaps they are implementation details).
   - Valuable but you haven't found the right buyer segment yet.

10. **Check for competing benefits.** If two benefits contradict (e.g., "for experienced users" vs. "for beginners"), note the conflict and decide which persona gets priority messaging.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Features are stated without marketing language or hedging | Y/N |
| Each feature has ≥1 advantage; advantages are not customer-specific | Y/N |
| Buyer personas are named and their pain points are explicit | Y/N |
| Each benefit is tied to a named persona and a specific pain point | Y/N |
| At least 50% of features have mapped benefits | Y/N |
| Benefits use outcome language (time saved, risk reduced, revenue gained) | Y/N |
| At least two features map to the same benefit (no 1:1 bloat) | Y/N |

## Red Flags

- Features and Advantages read identically (e.g., "Feature: scalable" and "Advantage: it scales"). You have not moved up the hierarchy.
- Benefits are written in product terms, not customer terms (e.g., "distributed architecture" instead of "your pipeline never goes down").
- A persona is listed but no benefits are mapped to it. Either the product does not serve that persona, or the mapping work was skipped.
- Every feature maps to a unique benefit. This suggests either feature bloat or that the differentiation story is scattered rather than clustered.
- No quantification in benefits (no time, cost, or risk numbers). The benefit feels abstract and unmemorable.
- Orphaned features outnumber mapped features. The product has a coherence problem: its advertised strengths don't align with buyer pain.

## Output Format

```
## FAB Analysis

### Features
| # | Feature | Language check |
|---|---|---|
| 1 | <objective specification> | ✓ |

### Advantages
| Feature # | Advantage | Customer-agnostic? |
|---|---|---|
| 1 | <capability or relief, not persona-specific> | ✓ |

### Buyer Personas & Pain Points
| Persona | Primary Pain / Goal |
|---|---|
| <name> | <explicit pain point> |

### Benefits Mapped
| Feature # | Advantage | Persona | Benefit | Outcome language |
|---|---|---|---|---|
| 1 | <...> | <...> | <...> | ✓ |

### Validation
- Orphaned features (no mapped benefit): <count>
- Competing benefits: <list or "none">
- Feature-Advantage-Benefit chains intact: <count>

### Messaging Priority
1. <Primary benefit for primary persona>
2. <Secondary benefit for secondary persona>
3. ...

### Confidence
<high/medium/low> — <justification: e.g., "high — buyer personas validated with sales team; 7/9 features mapped; benefits quantified with customer research" or "medium — personas inferred; time-based benefits speculative pending customer interviews">
```
