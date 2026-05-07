---
name: fair
display_name: FAIR (Factor Analysis of Information Risk)
class: model
underlying_class: native
domain: security
source: Jack A. Jones, "Factors Analysis of Information Risk," Risk Management Insight, 2005; formalized in FAIR standard (Open Group) 2018
best_for:
  - Quantifying information risk in monetary terms by decomposing it into frequency, loss magnitude, and control effectiveness
  - Comparing and prioritizing security investments across heterogeneous assets and threat scenarios
  - Communicating risk to non-technical stakeholders using a transparent, auditable factor model
one_liner: "Factor Analysis of Information Risk — decompose risk into frequency × magnitude for quantitative measurement."
---

# FAIR (Factor Analysis of Information Risk)

## Overview

FAIR claims that information risk can be expressed as a transparent, quantifiable equation: **Risk = Probability of Loss Event × Magnitude of Loss**. Unlike qualitative risk scoring (High/Medium/Low) that conflates frequency and severity and hides assumptions, FAIR decomposes risk into measurable or estimable sub-factors that an organization can observe, validate, and improve. The model is both descriptive — it reveals what drives current risk — and actionable — it shows which control investments will reduce risk most efficiently. FAIR is especially powerful for comparing disparate risks (a data breach vs. a systems outage vs. intellectual property theft) on a common scale, and for communicating risk to executives and boards in business terms (dollars per year) rather than categorical ratings.

## Core Variables and Relationships

FAIR models risk through a hierarchical decomposition:

1. **Risk (R)** — the primary quantity, expressed in dollars of expected loss per time period (usually annualized).
   - **Drivers:** Probability of Loss Event × Magnitude of Loss Event
   - **Equation:** R = Freq × Mag, where Freq is annualized frequency and Mag is financial impact per incident.

2. **Probability of Loss Event** — the chance that a threat will actually cause harm within the period.
   - **Threat Event Frequency (TEF):** How often does the threat actor / condition occur? (e.g., intrusion attempts per year, insider departure events per year)
   - **Threat Capability (TC):** Given a threat event, can the actor succeed? Depends on attack sophistication vs. asset defensibility.
   - **Vulnerability (V):** Does the asset have security gaps the threat can exploit? Measured qualitatively or as a control-gap map.
   - **Control Strength:** How effectively do deployed controls reduce TEF (by deterring or detecting threats) or reduce TC (by raising attack cost)?
   - **Relationship:** Probability of Loss = (TEF × TC) − impact of controls, or more formally, adjusted loss probability factors in control effectiveness.

3. **Magnitude of Loss Event** — the financial damage if a loss event occurs.
   - **Primary Loss:**
     - Confidentiality loss: Cost of breach notification, regulatory fines, lost customer trust, IP theft value
     - Integrity loss: Cost of data correction, system rebuild, remediation, customer notification
     - Availability loss: Lost revenue during downtime, SLA penalties, reputational damage
   - **Secondary Loss:** Downstream business impact (lost contracts, market share erosion, reduced valuation)
   - **Relationship:** Total Magnitude = Primary + Secondary; varies by asset and loss type.

4. **Controls and their effectiveness:**
   - **Preventive controls** reduce Threat Event Frequency (deter attackers, reduce exploit surface)
   - **Detective controls** reduce Threat Capability (alerts enable faster response, limiting damage)
   - **Corrective controls** reduce Magnitude (backup/restore reduces data loss, incident response limits secondary impact)
   - Control effectiveness is not binary; it is typically modeled as a % reduction in frequency or magnitude.

5. **Uncertainty and distribution:**
   - FAIR does not assume point estimates. Frequency and magnitude are expressed as probability distributions (triangular, lognormal, etc.).
   - **Range:** Model risk as low / medium / high estimates, then aggregate to a distribution and read off percentiles (median, 90th percentile) for decision-making.

## Key Predictions

- **Risk is non-linear in controls.** A 50% reduction in threat frequency and a 50% reduction in loss magnitude do *not* both reduce risk equally: the first reduces Risk by 50%, but the second also reduces it by 50%, so combined they reduce it by 75%. Prioritize whichever factor is larger.

- **High-frequency, low-magnitude risks are often over-controlled relative to their cost.** A phishing attack happens 100 times/year but 99% are stopped by email filtering; residual frequency is 1 × $50K = $50K risk. A single ransomware attack at 0.1/year might be $2M, yielding 0.1 × $2M = $200K risk. Yet organizations often spend more defending against phishing than ransomware.

- **Asset criticality determines risk prioritization more than threat intensity.** A skilled attacker targeting a non-critical asset may pose lower risk than an amateur against a critical asset, because the denominator (magnitude of loss) is smaller. The same threat, hitting a bigger asset, is a bigger risk.

- **Control ROI is calculable.** If a control costs $100K/year and reduces risk by $500K/year, the net benefit is $400K/year. This discipline cuts through arguments about "best practices" disconnected from actual business impact.

- **Operational risk (frequency) dominates in mature security environments.** Once detective and preventive controls reach high effectiveness, further spending yields small returns; the remaining risk is driven by low-probability but high-impact events, which often need only acceptance or insurance rather than additional controls.

- **Secondary loss often exceeds primary loss** for high-profile incidents (e.g., a $1M data breach may trigger $50M in lost market value or customer churn). Magnitude estimates that miss secondary loss understate risk by an order of magnitude.

## Application Procedure

Instantiate FAIR against a specific asset, threat, or control investment decision.

1. **Define the asset and loss scenario precisely.**
   - What asset is at risk? (e.g., customer database, payment processing system, email system)
   - What is the loss type? (confidentiality, integrity, availability, or hybrid)
   - What is the scope of impact? (e.g., 10K customers, $100M/day revenue, intellectual property valued at $10M)
   - Write this in one sentence: "Risk to: [asset], loss type: [C/I/A], scope: [unit of harm]."

2. **Enumerate credible threat scenarios.**
   - What actors could cause loss? (external attacker, insider, system failure, third-party risk)
   - For each, estimate Threat Event Frequency (TEF): How often does this threat event occur in your operational context? Use historical data, industry benchmarks, or expert elicitation.
   - Example: External intrusion attempts to retail payment system: 100,000 attempts/year (from honeypot or external telemetry).

3. **Assess Threat Capability and Vulnerability.**
   - If a threat event occurs (attacker gains access to network perimeter, insider logs in), what is the probability they succeed in causing the loss?
   - Threat Capability (TC): depends on attacker skill, resources, and specificity of targeting.
   - Vulnerability (V): does the asset have security gaps the threat can exploit? (missing patches, weak authentication, no encryption, no segmentation)
   - Estimate TC × V as a % probability. Example: An insider with read access to a database; Prob of exfiltration = 80% (they know SQL, network is not monitored for egress).

4. **Inventory and model controls.**
   - What controls exist (preventive, detective, corrective)?
   - For each, estimate % reduction in TEF or % reduction in Magnitude.
   - Example: Multi-factor authentication reduces insider exfiltration success by 60% (some insiders will not attempt if MFA is required). Email filtering stops 99% of phishing, so TEF of phishing is reduced from 100,000/year to 100/year.

5. **Estimate Loss Magnitude per incident.**
   - Primary loss: Quantify confidentiality loss (breach notification cost, regulatory fines per record, IP value), integrity loss (cost to detect and correct), or availability loss (lost revenue per hour × expected downtime).
   - Consult incident data (your own past incidents, public disclosures, insurance studies) for anchors.
   - Secondary loss: Model business impact (customer churn, stock price impact, brand erosion, lost contracts). Use scenario analysis or customer surveys if available.
   - Estimate as a range (low / medium / high); do not force a point estimate.
   - Example: Data breach of 100K customer records: $50/record notification + fines + credit monitoring = $5M primary. Secondary (lost customers, reputational damage) estimated at $10M–$50M; use $20M as median.

6. **Compute Residual Risk (after controls).**
   - Residual Loss Probability = (TEF × TC) − control impact, capped at 0 and 1.
   - Residual Risk = Residual Loss Probability × Magnitude.
   - Example: Insider exfiltration, 1000 insiders/year × 80% success × 60% reduction from MFA = 320/year chance. $20M magnitude. Risk = 320 × $20M = $6.4B annualized (before capping at number of insiders). Recalculate with correct denominator: 1000 insiders, 80% intrusion success = 800/year; 60% MFA reduction → 320/year; cap at 1000 total. Prob = min(320/1000, 1.0) = 0.32. Risk = 0.32 × $20M = $6.4M/year.

7. **Test control ROI and prioritize.**
   - For each control under consideration, compute the risk reduction it would achieve.
   - Compare to cost (capital + operational).
   - ROI (annual risk reduction $) / (annual control cost $) > 1 suggests control is worthwhile.
   - Rank controls by risk reduction per $ invested and prioritize accordingly.

8. **Check boundary conditions** (below). Flag if any apply; if so, note complementary analysis needed.

9. **Communicate the result** using the Output Format below — include ranges, not point estimates, and flag assumptions.

## Boundary Conditions

FAIR's quantitative model assumes certain conditions that often break down:

- **Rare, novel threat types with no historical data.** A 0-day attack or novel insider threat pattern has no empirical TEF. FAIR works best when frequency can be anchored to observables (past incidents, red team tests, threat intelligence reports). For Black Swan scenarios, FAIR gives only a rough range; supplement with scenario analysis or tail-risk methods.

- **Tight feedback loops between risk and control adaptation.** FAIR models a snapshot: it assumes TEF, TC, and control effectiveness are stable during the horizon. In fast-moving threat environments (active adversary campaigns, rapid attacker adaptation), the model becomes outdated quickly; recompute quarterly or use dynamic models (e.g., game theory) if adversary adaptation is rapid.

- **Unmeasurable secondary losses.** FAIR can quantify primary loss (breach notification) but secondary loss (brand erosion, market share loss) is highly subjective and forward-looking. If secondary loss dominates and is hard to estimate, FAIR's precision is illusory. Use qualitative scenarios or executive judgment in parallel.

- **Systemic / correlated risks.** FAIR models individual loss scenarios (one breach, one outage). It does not natively capture correlated risks (a single attacker causing multiple simultaneous breaches, or a single control failure that affects many assets). Supplement with dependency analysis or systemic risk modeling.

- **Regulatory or compliance-driven controls.** Many controls are mandated by regulation (e.g., PCI-DSS, HIPAA), not chosen via ROI. FAIR can quantify their value, but regulatory constraints may override economic logic. Flag when compliance, not economics, drives control selection.

- **Controls with detection-only or response-dependent impact.** A detective control (SIEM alert) only reduces risk if the organization *responds quickly*. FAIR must then model response time, response accuracy, and incident containment effectiveness — all of which vary organizationally. If response maturity is low or inconsistent, detective control effectiveness is much lower than a generic estimate suggests.

## Output Format

```
## FAIR Analysis: <asset> — <threat scenario>

**Asset:** <name and criticality>
**Loss type:** <C/I/A / hybrid>
**Scope:** <unit of harm, e.g., customers affected, revenue lost>
**Time horizon:** <e.g., 1 year, annualized>

### Threat and Probability Estimation
| Threat | TEF (events/year) | TC (% success) | TEF × TC | Controls | Residual Prob |
|---|---|---|---|---|---|
| <threat 1> | <#> | <#%> | <#> | <control(s) + effectiveness %> | <#%> |
| ... | ... | ... | ... | ... | ... |

### Loss Magnitude Estimation (per incident)
| Loss Type | Low | Median | High | Notes |
|---|---|---|---|---|
| Primary (notification, fines, remediation) | $X | $Y | $Z | <assumption> |
| Secondary (churn, market value, brand) | $X | $Y | $Z | <assumption> |
| **Total Magnitude** | **$X** | **$Y** | **$Z** | |

### Residual Risk Calculation
| Scenario | Probability | Magnitude (Median) | Annual Risk |
|---|---|---|---|
| <threat 1> | <#%> | $Y | $Z |
| <threat 2> | <#%> | $Y | $Z |
| **Aggregate Annual Risk** | | | **$Z** |

### Control ROI (if evaluating new controls)
| Control | Cost/year | Risk Reduction | Net Benefit | ROI |
|---|---|---|---|---|
| <control A> | $X | $Y | $Y − $X | ($Y − $X) / $X |
| ... | ... | ... | ... | ... |

### Boundary Conditions and Caveats
- <which boundary conditions apply>
- <data quality / frequency source>
- <assumptions that, if wrong, significantly shift the risk estimate>
- <complementary analyses needed>

### Confidence: high | medium | low
<reasoning: observability and quality of TEF estimates + confidence in magnitude estimates + control effectiveness assumptions + whether rare/novel threats dominate + organizational response maturity>
```
---
