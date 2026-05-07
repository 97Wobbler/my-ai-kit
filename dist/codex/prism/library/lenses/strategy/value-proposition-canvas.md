---
name: value-proposition-canvas
display_name: Value Proposition Canvas
class: lens
underlying_class: native
domain: strategy
source: Osterwalder, Pigneur, Bernarda, Smith; "Value Proposition Design" (2014)
best_for:
  - Validating product-market fit by stress-testing alignment between customer needs and solution offerings
  - Identifying gaps between what customers actually need and what you're building
  - Designing or pivoting a value proposition with evidence rather than intuition
one_liner: "Explicitly match customer jobs/pains/gains to product features/pain-relievers/gain-creators."
---

# Value Proposition Canvas

## Overview

The Value Proposition Canvas maps a customer's actual Jobs, Pains, and Gains against a product's Features, Pain Relievers, and Gain Creators. The discipline is the *specificity* of each element and the rigor of the alignment check — most teams write vague platitudes (e.g., "saves time") instead of concrete, measurable customer needs and measurable product responses. Practitioners use this when a product feels misaligned with its market or when they need to prioritize which customer needs to address first.

## Analytical Procedure

### Phase 1 — Map the Customer Profile

1. **Name the customer segment.** Be specific: "B2B SaaS product managers at Series A startups" beats "business customers."

2. **List the customer's Jobs.** A job is a task the customer is trying to accomplish or a problem they're trying to solve. Jobs can be functional (complete a report), emotional (feel respected), or social (establish status). Write 5–10 jobs. For each, note: Is this a recurring job or a one-time job? Who initiates it?
   - Bad: "Manage their workflow"
   - Good: "Review pull requests without context-switching to GitHub"

3. **List the Pains associated with each job.** Pains are obstacles, frustrations, or costs that arise while doing the job or that prevent the job from being done well. For each pain, estimate its frequency and severity (high/medium/low). Ask: Does the customer currently tolerate this pain or actively avoid the job because of it?

4. **List the Gains the customer desires.** Gains are the outcomes or benefits the customer would get if the pain were removed or if the job were made easier. Be concrete: "save 2 hours per week," "reduce error rate below 1%," "make this repeatable without expert judgment." Distinguish between nice-to-haves and must-haves.

### Phase 2 — Map the Value Proposition

5. **List the product's Features.** Features are the tangible elements of your solution — the buttons, workflows, data models, integrations. Write them as the customer would perceive them, not as engineering describes them. For each feature, write which job(s) it serves.
   - Bad: "RESTful API with 99.9% uptime"
   - Good: "Automated report generation without leaving Slack"

6. **List the Pain Relievers.** For each customer pain from Phase 1, write how the product removes, reduces, or sidesteps that pain. If a pain has no corresponding reliever, flag it as a gap. Conversely, if a feature has no pain to relieve, question whether it's solving a real problem or solving for a different segment.

7. **List the Gain Creators.** For each desired gain from Phase 1, write how the product enables or delivers that gain. Again, look for orphaned gain creators (features that create value the customer didn't ask for) and orphaned gains (benefits the customer wants that your product doesn't create).

### Phase 3 — Align and Validate

8. **Draw alignment lines.** On the canvas (or in a table), connect each customer job/pain/gain to its corresponding feature/reliever/creator. If a customer need has no corresponding product element, mark it as a **gap**. If a product element serves no customer need, mark it as **waste**.

9. **Rate the alignment for each job.** For the customer jobs identified in Phase 1, score each as:
   - **Well-aligned** — Multiple features/relievers/creators address it, gaps are minor
   - **Partially aligned** — Some support exists but key gaps remain
   - **Misaligned** — Little or no support; customer would need to work around the product

10. **Identify the critical path.** Which 2–3 jobs are most important to your target customer? Which of those are best-addressed by your product? This is where you own the market. Focus on jobs where you have material advantage over alternatives.

11. **Pressure-test each alignment claim.** For each feature marked as a pain reliever or gain creator, ask:
    - How would the customer measure that this pain is actually relieved?
    - Is the relief proportional to the effort the customer invests in using the feature?
    - Does the customer have an alternative (manual process, competitor, status quo) that already relieves this pain? If so, how is your product better?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Customer segment is named specifically (not "users" or "businesses") | Y/N |
| At least 5 distinct jobs are identified and each is stated concretely | Y/N |
| Each job has 1–3 associated pains with frequency/severity noted | Y/N |
| Each pain has a measurable quality (time, error rate, cost, etc.) | Y/N |
| Gains are stated as concrete outcomes, not vague benefits | Y/N |
| At least 5 features are listed with customer-facing language | Y/N |
| Every pain has a corresponding pain reliever OR is flagged as a gap | Y/N |
| Every gain has a corresponding gain creator OR is flagged as a gap | Y/N |
| Gaps and waste elements are documented and prioritized | Y/N |
| At least one alignment claim was pressure-tested with a customer alternative | Y/N |

## Red Flags

- Customer jobs are generic or abstract ("improve efficiency," "manage better"). These are symptoms, not jobs. Dig deeper: What specific activity is the customer performing when they need efficiency?
- All pains and gains lack measurement. "Reduces friction" and "improves experience" are not falsifiable. Without metrics, you cannot know if the product actually solves the problem.
- The product has more features than the customer has jobs. This is feature bloat masquerading as flexibility.
- Every feature is marked as a pain reliever or gain creator. No product solves everything. If all features are essential, the scoping is dishonest.
- Alignment was drawn without customer validation. Your job is not the customer's job. Your pain relief may not feel like relief to them. Pressure-test with real customers.
- Gaps are identified but not ranked. You cannot address every gap. Make the strategic choice: Which unsolved pains are worth solving, and which are acceptable costs of focusing elsewhere?

## Output Format

```
## Value Proposition Canvas Assessment

**Customer Segment:**
<Name and specifics: role, industry, company size, etc.>

### Customer Profile

#### Jobs
| Job | Type (Functional/Emotional/Social) | Frequency | Initiated by |
|---|---|---|---|
| <e.g., "Review pull requests in under 5 min without switching context"> | Functional | Daily | Developer (self) |

#### Pains
| Pain | Associated Job | Severity | Frequency | Current handling |
|---|---|---|---|---|
| <e.g., "Context-switching to GitHub breaks flow; takes 3 min per review"> | Review PRs | High | 10x/day | Tolerated |

#### Gains
| Desired Gain | Measurable outcome | Associated Job | Priority |
|---|---|---|---|
| <e.g., "Complete 15 reviews in 30 min without context-switch"> | 2 min per review | Review PRs | Must-have |

### Value Proposition

#### Features
| Feature | Customer language | Job(s) served |
|---|---|---|
| <e.g., "Slack bot reviews and summarizes code"> | See PR diff without leaving Slack | Review PRs |

#### Pain Relievers
| Pain | Reliever (feature) | Adequacy |
|---|---|---|
| <pain from above> | <feature from above> | Partial / Full / None |

#### Gain Creators
| Desired Gain | Creator (feature) | Adequacy |
|---|---|---|
| <gain from above> | <feature from above> | Partial / Full / None |

### Alignment Matrix
| Job | Well-aligned | Partially | Misaligned | Gaps | Waste |
|---|---|---|---|---|---|
| <...> | X |   |   | <none> | <none> |

### Critical Path
1. **Most important job:** <job> — Alignment: <rating> — Competitive advantage: <brief assessment>
2. ...

### Pressure-test Results
| Feature claim | Customer alternative | How is your product better? | Confidence |
|---|---|---|---|
| <e.g., "Slack bot relieves context-switch pain"> | Manual GitHub + context-switch | Faster and keeps dev in Slack | Medium — needs user testing |

### Gaps & Waste
**Gaps (unmet needs):**
- <e.g., "No support for async code review; reviews pile up when author is offline">
  - Priority: High | Effort to fix: Medium

**Waste (unsupported features):**
- <e.g., "Mobile app notifications no one uses">
  - Recommendation: Deprecate in next release

### Confidence
<high/medium/low> — <justification, e.g., "High: validated against 8 target customers; Partial gaps are known trade-offs. Medium: alignment on emotional gains untested.">
```
