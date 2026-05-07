---
name: nist-ai-rmf
display_name: NIST AI Risk Management Framework
class: lens
underlying_class: native
domain: applied-ethics
source: National Institute of Standards and Technology (2023)
best_for:
  - Mapping AI system risks across governance, design, and operation
  - Scoring risk severity and determining mitigation priorities
  - Aligning risk management with organizational tolerance
one_liner: "Walk Govern / Map / Measure / Manage functions to identify and score AI risks across intent, development, and deployment."
---

# NIST AI Risk Management Framework

## Overview

The NIST AI RMF structures risk identification and response through four core functions: Govern (establish oversight), Map (identify risks by lifecycle stage), Measure (assess severity and likelihood), and Manage (select and implement controls). Practitioners use it to build institutional AI risk programs, create risk registers tied to business outcomes, and communicate risk decisions to leadership and stakeholders. The discipline is granularity — vague "AI risk" becomes specific, bounded, scored, and actionable.

## Analytical Procedure

### Phase 1 — Govern: Establish Institutional Context

1. **Define the organization's AI risk tolerance.** Write a 2-3 sentence statement answering: What harms is your organization willing to accept in order to deploy AI? What harms are unacceptable? Examples: "We accept ±2% accuracy variance in fraud detection but will not deploy if false-positive rate exceeds 5%. We accept training-data bias if mitigated; we do not accept using protected characteristics in the decision logic."

2. **Inventory the decision authority.** Name the role that owns AI risk acceptance (CISO, Chief AI Officer, Product VP, etc.). Document what they need from risk assessment to make decisions (quantified severity? stakeholder sign-off? cost-benefit analysis?).

3. **Map organizational context to the framework's stakeholders.** Identify:
   - **AI actors**: teams building, deploying, maintaining the system
   - **Deployers**: teams operating the system in production
   - **Subjects**: end-users or individuals affected by the AI decision
   - **Regulators/Auditors**: external parties with authority over the system
   For each group, note their primary concern (accuracy, fairness, compliance, safety, etc.).

### Phase 2 — Map: Identify Risks by Lifecycle Stage

4. **Decompose the AI system by lifecycle stage.** For each stage below, list the specific technical or organizational practice:
   - **Planning & Design**: What is the system intended to do? Who decided? What proxies or approximations are being used for the true goal?
   - **Data**: What data is collected, labeled, and used for training? Who collected it? Under what conditions? Are there known gaps or biases?
   - **Model Development**: What model architecture, training procedure, and validation method are being used? What trade-offs were made (accuracy vs. interpretability, speed vs. robustness)?
   - **Deployment**: How is the model integrated into a production system? What happens if the model fails? How is it monitored? Who can override it?
   - **Use & Monitoring**: Who uses the system? What decisions do they make with its outputs? How frequently is the model retrained? What triggers an update?

5. **For each stage, brainstorm failure modes.** Use the NIST risk categories as prompts:
   - **Fairness**: Does the system treat individuals or groups unequally due to training data, design choice, or deployment context?
   - **Security**: Can the model be adversarially attacked, poisoned, or extracted? Can the system be misused or accessed by unauthorized parties?
   - **Resilience**: How does the system behave on out-of-distribution inputs? Does it gracefully degrade or fail catastrophically?
   - **Transparency**: Can the system's decision be explained to subjects and regulators? Is the explanation accurate?
   - **Accountability**: If the system causes harm, who is responsible? Are there logs, audits, and human oversight mechanisms?
   - **Privacy**: Does the system expose or infer private information about individuals?

   Write each failure mode as: "<Stage>: <specific condition> could lead to <observable harm>."
   Example: "Data: Training data collected only from urban users could lead to poor performance and biased recommendations for rural users."

6. **Assign each failure mode to a risk category.** If it spans multiple categories (e.g., fairness + transparency), list all.

### Phase 3 — Measure: Assess Severity and Likelihood

7. **For each failure mode, estimate impact severity.** Use a scale (Negligible / Minor / Moderate / Severe / Critical) and specify the harm:
   - **Negligible**: System output ignored; user can easily correct; no measurable harm.
   - **Minor**: User must invest time to work around; low financial loss; affects one individual or small cohort.
   - **Moderate**: Affects significant cohort; correctable but resource-intensive; measurable financial loss or reputational damage.
   - **Severe**: Affects large population; non-trivial cost to remediate; regulatory scrutiny; material reputational or financial harm.
   - **Critical**: Violates law; causes injury; catastrophic financial loss; irreversible harm to subjects or organization.

8. **Estimate likelihood.** For each failure mode, answer: Under what conditions would this occur? How frequently? Assign a likelihood (Rare / Unlikely / Possible / Likely / Certain):
   - **Rare**: Would require multiple simultaneous failures or adversarial effort; not expected in 5+ years.
   - **Unlikely**: Could occur but would require unusual circumstances; expected once in 1–5 years.
   - **Possible**: Could occur under plausible conditions; expected multiple times in 1 year.
   - **Likely**: Expected to occur regularly; difficult to prevent without intervention.
   - **Certain**: Occurs reliably or is already known to occur.

9. **Calculate risk score.** Create a matrix:

   | | Negligible | Minor | Moderate | Severe | Critical |
   |---|---|---|---|---|---|
   | **Rare** | 1 | 2 | 3 | 4 | 5 |
   | **Unlikely** | 2 | 4 | 6 | 8 | 10 |
   | **Possible** | 3 | 6 | 9 | 12 | 15 |
   | **Likely** | 4 | 8 | 12 | 16 | 20 |
   | **Certain** | 5 | 10 | 15 | 20 | 25 |

   Assign each failure mode a score. Scores ≥12 require explicit mitigation; scores <6 can be accepted as-is.

### Phase 4 — Manage: Design and Implement Controls

10. **For each high-risk failure mode (score ≥12), design a control.** A control is a specific, measurable action:
    - **Prevent**: Make the failure impossible or extremely unlikely. Example: "Exclude protected characteristics from feature set and add a technical audit to verify none are reconstructible."
    - **Detect**: Identify the failure if it occurs. Example: "Monitor prediction distribution by demographic group monthly; alert if Demographic Parity Index falls below 0.8."
    - **Respond**: Limit harm once the failure is detected. Example: "If fairness metric breaches threshold, halt automated decisions and route to human review until model is retrained."

11. **Assign ownership and timeline.** For each control, name the responsible team and a deadline. Controls with tight deadlines or high dependencies should be tracked in a risk register.

12. **Define success criteria.** For each control, write a testable condition:
    - Bad: "Improve model fairness."
    - Good: "No demographic group has false-positive rate > 5% above the overall baseline, verified quarterly."

## Evaluation Criteria

| Check | Pass |
|---|---|
| AI risk tolerance is written as a specific statement, not generic | Y/N |
| Decision authority and stakeholders are named, not generic "leadership" | Y/N |
| All five lifecycle stages (Planning, Data, Model, Deployment, Use) were mapped | Y/N |
| At least one failure mode was identified per stage | Y/N |
| Each failure mode is assigned severity *and* likelihood, not just severity | Y/N |
| At least one failure mode scored ≥12 and has a designed control | Y/N |
| Controls specify prevent/detect/respond and have ownership + deadline | Y/N |
| Success criteria are measurable (e.g., a threshold or metric), not aspirational | Y/N |

## Red Flags

- Failure modes are generic ("bias," "unfairness," "security risk"). They must reference the specific system, data, or decision.
- Likelihood is estimated without naming the conditions or adversary that would trigger it. "Possible" without justification is guessing.
- Risk score is calculated but controls are not designed for high-scoring risks. Scoring without mitigation is administrative theater.
- Controls are named without ownership or deadline. "Implement monitoring" is not a control; "Analytics team will deploy demographic parity check to production by Q2 2024" is.
- Success criteria are absent or unmeasurable. You cannot verify a control is working without a quantified target.
- Only Govern phase is completed; Map/Measure/Manage are skipped. The framework is iterative — all four phases must be touched.
- All risks score as Negligible or Critical with no middle ground. Extreme risk distributions suggest bias in severity/likelihood estimation.

## Output Format

```
## NIST AI RMF Assessment

### Govern
**Risk Tolerance Statement:**
<2-3 sentences describing what harms are acceptable and unacceptable.>

**Decision Authority:**
Role: <title>
Decision criteria: <what they need to decide>

**Stakeholders:**
- AI Actors: <team(s)>
- Deployers: <team(s)>
- Subjects: <who is affected>
- Regulators: <external parties>

### Map
**Lifecycle Stages & Failure Modes:**

| Stage | Practice | Failure Mode | Risk Category |
|---|---|---|---|
| Planning & Design | <...> | <...> | <Fairness/Security/Resilience/Transparency/Accountability/Privacy> |
| Data | <...> | <...> | <...> |
| ... | ... | ... | ... |

### Measure
**Risk Scores:**

| Failure Mode | Severity | Likelihood | Score | Priority |
|---|---|---|---|---|
| <...> | <Negligible/Minor/Moderate/Severe/Critical> | <Rare/Unlikely/Possible/Likely/Certain> | <1-25> | High/Medium/Low |

### Manage
**Controls for High-Risk Failures (score ≥12):**

| Failure Mode | Control Type | Control Description | Owner | Deadline | Success Criteria |
|---|---|---|---|---|---|
| <...> | Prevent/Detect/Respond | <specific, measurable action> | <team/role> | <date> | <testable condition> |

**Confidence**
<high/medium/low> — <justification. E.g., "High — stakeholders validated risk tolerance and controls are already in place with monitoring; Medium — likelihood estimates are based on industry benchmarks, not this organization's data; Low — failure modes depend on future regulatory changes that are not finalized.">
```
---
