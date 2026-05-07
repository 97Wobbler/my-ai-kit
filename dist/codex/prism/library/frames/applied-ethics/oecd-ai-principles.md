---
name: oecd-ai-principles
display_name: OECD AI Principles
class: frame
underlying_class: native
domain: applied-ethics
source: OECD, 2019 ("Recommendation of the Council on Artificial Intelligence")
best_for:
  - Classifying an AI system or policy decision against five normative principles
  - Sorting an ethical concern into a principle to determine which stakeholder accountability applies
  - Auditing AI governance for coverage across all five principle domains
one_liner: "Classify an AI system or decision against 5 principles—inclusive growth, human-centered fairness, transparency, robustness, accountability—to determine which governance and mitigation controls apply."
---

# OECD AI Principles

## Overview

The OECD AI Principles frame sorts an AI system, feature, or governance decision against five normative principles that emerged from consensus among OECD member states. Its core claim is that responsible AI requires **simultaneous attention to all five domains**—and that each principle demands structurally different controls and stakeholder involvement. A system may be technically robust but exclude vulnerable populations (violating inclusive growth), or be transparent but unaccountable (violating accountability). The frame does not prescribe a solution; it identifies which principle(s) are at stake in a given decision, which then determines which mitigation strategies and actors are appropriate.

## Categories

1. **Inclusive Growth**
   - AI systems should create broad economic and social benefits and not exacerbate inequality or disadvantage specific groups.
   - The principle addresses distribution: who benefits, who bears risk, whether vulnerable populations are included in value capture.
   - Discriminating criterion: the decision or system design explicitly considers differential impact across income, geography, or demographic groups, and is defensible on grounds of inclusive benefit.
   - Example: a hiring AI that actively tests for and removes bias against underrepresented candidates; a lending algorithm that expands credit access to underserved communities without predatory terms.

2. **Human-Centered Fairness**
   - AI systems should respect human rights, core democratic values, and human agency; decisions must not unjustly discriminate or strip humans of meaningful control.
   - The principle addresses dignity and agency: freedom from unfair treatment, the right to contest decisions, preservation of human autonomy in high-stakes domains.
   - Discriminating criterion: the system design includes mechanisms for human review in consequential decisions, tests for and mitigates discriminatory outcomes, and preserves user agency.
   - Example: a credit-denial AI that offers a human review path and explanation; a criminal-risk assessment that flags uncertainty and requires human judgment in borderline cases.

3. **Transparency**
   - AI systems and their impacts should be explainable and documented to stakeholders—developers, users, regulators, and affected publics.
   - The principle addresses information asymmetry: stakeholders need to understand what the system does, how it makes decisions, and what risks it poses.
   - Discriminating criterion: the system's logic, training data sources, known failure modes, and impact on stakeholders are documented and disclosed at a level appropriate to the stakeholder's need to understand and contest decisions.
   - Example: a content-moderation AI that publishes its enforcement guidelines and weekly transparency reports; a predictive-policing system that discloses its historical data sources and documented disparities.

4. **Robustness and Security**
   - AI systems should be technically sound, resilient to adversarial input, and protected against misuse; failures should be detectable and correctable.
   - The principle addresses safety and reliability: the system performs as intended, resists deliberate attack, can be audited, and failures do not cascade silently.
   - Discriminating criterion: the system has been tested for robustness, has fail-safes and monitoring, and can be corrected or shut down without widespread harm.
   - Example: a healthcare diagnostic AI that includes uncertainty estimates and alerts clinicians to low-confidence cases; a financial model audited for adversarial examples and monitored for drift.

5. **Accountability**
   - AI systems should have clear lines of responsibility: someone is responsible for the system's impacts, stakeholders know whom to turn to, and there are mechanisms for redress.
   - The principle addresses answerability: actors cannot hide behind technical complexity; there is a path for harmed parties to contest and seek remedy.
   - Discriminating criterion: the organization deploying the AI clearly owns its impacts, has documented the chain of custody from data to decision, and provides a mechanism (complaint, audit, court) by which affected parties can seek recourse.
   - Example: a hiring AI deployed with explicit vendor accountability for disparate-impact liability; a loan-denial AI with a clear human appeal process and a responsible party named.

## Classification Procedure

1. **Identify the decision or system** in one or two sentences. Name the stakeholders most directly affected.

2. **For each principle, ask the diagnostic question:**
   - **Inclusive Growth:** Does the system or decision explicitly address whether its benefits and risks are distributed fairly across all populations, or could it systematically exclude or harm specific groups?
   - **Human-Centered Fairness:** Does the system or decision respect human autonomy, dignity, and freedom from unjust discrimination? Is there a human override or review path?
   - **Transparency:** Can the affected stakeholders understand how and why the decision was made, what data was used, and what risks exist?
   - **Robustness:** Has the system been tested for failure modes, adversarial inputs, and monitored for silent drift? Can it be corrected or safely disabled?
   - **Accountability:** Is there a clear, named owner responsible for the system's impacts, and a mechanism for redress if harm occurs?

3. **Mark each principle as:**
   - ✓ **Addressed:** the system design or decision explicitly satisfies the principle.
   - ✗ **Absent or weak:** the principle is not meaningfully considered or a significant control is missing.
   - ? **Unclear:** the principle is partially addressed but with gaps or ambiguities.

4. **If all five are addressed**, the system passes the frame and is defensible on OECD grounds. If any are absent or weak, proceed to step 5.

5. **For each absent or weak principle, determine the required mitigation:**
   - Identify which actor (developer, deployer, regulator, user) must own the gap.
   - Identify the structural control needed (testing, disclosure, governance, human review, etc.).
   - Assign remediation priority based on stakeholder exposure to harm.

## Implications per Category

| Principle | What it demands | If violated, risks |
|---|---|---|
| **Inclusive Growth** | Intentional design for equitable benefit distribution; testing for disparate impact across demographics or regions. | Exacerbates existing inequalities; erodes public trust in AI; triggers regulatory backlash; harms vulnerable groups. |
| **Human-Centered Fairness** | Human review in high-stakes decisions; transparent reasoning; contestability; explicit bias testing. | Unjust discrimination; loss of human dignity; public perception of fairness violations; legal liability under anti-discrimination law. |
| **Transparency** | Documented model logic, training data provenance, known failure modes, and stakeholder-appropriate disclosure. | Stakeholders cannot evaluate or contest decisions; regulators cannot audit; affected parties lack grounds to seek redress. |
| **Robustness and Security** | Adversarial testing, monitoring for drift, graceful degradation, recovery mechanisms. | Silent failures; cascading harm; susceptibility to manipulation; loss of stakeholder confidence in system reliability. |
| **Accountability** | Named responsible actor; clear liability; documented decision chain; accessible redress mechanism. | Diffusion of responsibility; affected parties have no recourse; regulators cannot enforce; system continues causing harm unchecked. |

## Common Misclassifications

- **Transparency mistaken for Accountability.** Publishing a model card does not assign responsibility for harms. A transparent-but-unaccountable system allows stakeholders to see the problem but offers no path to redress. The tell: "We disclosed everything" does not answer "Who fixes it?"
- **Robustness mistaken for Fairness.** A technically robust system that performs consistently can still discriminate consistently. The tell: the system is reliable but produces disparate impact on protected groups.
- **Inclusive Growth mistaken for Human-Centered Fairness.** A system can be equitable in aggregate benefit distribution but unfair to individuals within the winning group. The tell: benefits are broadly shared but some individuals are denied autonomy or dignity in how decisions are made.
- **Addressing one principle while neglecting others.** A system that is highly transparent but lacks accountability is partially compliant. OECD principles are interdependent; a gap in any one weakens the others. The tell: strong performance on one dimension masks serious weakness in another.
- **Classifying the system's intention rather than its implementation.** The developer's stated intent to be inclusive does not satisfy the Inclusive Growth principle if the deployed system causes harm. Classification must be based on actual design, testing, and impact—not aspiration.
