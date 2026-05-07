---
name: research-ethics
display_name: Research Ethics (Belmont Report)
class: lens
underlying_class: native
domain: applied-ethics
source: Belmont Report (U.S. Department of Health, Education, and Welfare, 1979); codified in 45 CFR 46 and ICH-GCP
best_for:
  - Reviewing human subjects research protocols for ethical compliance
  - Identifying risks to participant welfare and autonomy
  - Evaluating whether vulnerable populations receive adequate protections
one_liner: "Evaluate human subjects research against three principles — respect for persons, beneficence, and justice — via informed consent, risk-benefit analysis, and vulnerable population safeguards."
---

# Research Ethics (Belmont Report)

## Overview

The Belmont Report establishes three foundational principles for ethical human subjects research: (1) respect for persons (autonomous agents deserve informed consent; those with diminished autonomy require extra protections), (2) beneficence (maximize benefits, minimize harms), and (3) justice (fair distribution of research burdens and benefits across populations). Practitioners use this lens to audit research protocols, consent forms, and participant selection before IRB submission or to identify ethical gaps in ongoing studies.

## Analytical Procedure

### Phase 1 — Extract the Protocol Elements

1. **State the research question and primary outcome in one sentence.** No jargon. What is the study trying to find or prove?

2. **List the population:** age, health status, decision-making capacity, any group-defining characteristic (e.g., "pregnant women," "incarcerated individuals," "children with autism").

3. **Enumerate the procedures:** every intervention, measurement, specimen collection, or data access. Include duration, frequency, and invasiveness (blood draw, survey, brain imaging, deception, etc.).

4. **Document the risks:** probability and severity of physical harm, psychological distress, loss of privacy, social/economic harm, loss of autonomy. Distinguish individual risks from group-level stigma or discrimination risks.

5. **Identify the benefits:** to the participant directly, to participants with the same condition, to science/society generally. Be honest about speculative benefits.

6. **Record the consent process:** written or oral? how is comprehension verified? who delivers consent? what can participants withdraw from without penalty?

### Phase 2 — Apply the Three Principles

#### Principle 1: Respect for Persons

7. **Is informed consent present?** Check these components:
   - **Disclosure:** Does the consent document or process reveal purpose, procedures, risks, benefits, alternatives, and limits on confidentiality? Read it as a lay person — jargon is a red flag.
   - **Comprehension:** How will the researcher verify that participants understand? (e.g., teach-back, comprehension questions, readability grade level <6th grade for general audiences.)
   - **Voluntariness:** Are there coercive elements (mandatory participation, withdrawal penalties, undue inducement)? Are power differentials flagged (e.g., student-professor, patient-clinician, prisoner-guard)?

8. **For diminished autonomy populations, are protections added?** Check:
   - Children: is there parental/guardian consent AND child assent (age-appropriate)? Is a pediatric or child welfare ethics expert consulted?
   - Cognitively impaired: is there a legally authorized representative? Is the person's own preference still sought when possible?
   - Prisoners: is there independent ethics oversight (not just IRB)? Are alternatives to prison participation incentivized?
   - Institutionalized persons (hospital, nursing home, military): is there an advocate outside the institution?

#### Principle 2: Beneficence (Maximize benefit, minimize harm)

9. **Risk-benefit analysis:** For each identified risk, ask:
   - Is the risk necessary to answer the research question? (If not, redesign to eliminate it.)
   - Does a direct benefit to the participant offset the risk? (Therapeutic research vs. non-therapeutic.)
   - If non-therapeutic, is the risk minimal? (Risk no greater than in daily life or routine clinical care.)
   - Are there less risky alternatives that would answer the question equally?

10. **Probability and severity matrix:** Map each risk:
    - **Low probability, low severity:** acceptable with disclosure.
    - **Low probability, high severity:** needs strong justification and explicit consent.
    - **High probability, any severity:** serious concern; protocol redesign needed.
    - **High probability, high severity:** likely unethical; redesign or stop.

11. **Monitoring plan:** Will researchers actively monitor for harms? Who stops the study if harms emerge? Is there a stopping rule?

#### Principle 3: Justice (Fair distribution of burdens and benefits)

12. **Selection of participants:** Is the population justified, or is it chosen only for convenience?
    - **Justified inclusion:** study cannot answer the question without this population (e.g., hypertension research needs hypertensive participants).
    - **Unjustified inclusion:** population is chosen because they are easy to access or less likely to object (e.g., prisoners studied not because they are essential to the question, but because they cannot refuse).
    - **Burden concentration:** Are all burdens falling on one group (e.g., all low-income, all racial minorities)? Is benefit distribution skewed?

13. **Allocation of benefits:** If the research produces a successful treatment, who gets access?
    - Post-trial access: Do participants in successful trials continue to receive the beneficial intervention? Can they afford it?
    - Broader access: Does the protocol or institution commit to making results available to the studied population if effective?
    - Exploitation check: Are participants from resource-poor populations bearing risk to develop treatments for wealthy populations?

### Phase 3 — Synthesize the Ethical Assessment

14. **Assign a governance level:** Does this protocol require only standard IRB review (expedited or full)? Does it need:
    - Vulnerable populations subcommittee?
    - External ethics consultation?
    - Special regulatory oversight (FDA, DHHS)?
    - Community advisory board?

15. **List required revisions or mandatory safeguards** before approval is recommended.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All six protocol elements (Q1–Q6) are documented | Y/N |
| Informed consent has all three components (disclosure, comprehension, voluntariness) | Y/N |
| Diminished autonomy protections are present if population warrants | Y/N |
| Risk-benefit analysis includes a probability/severity matrix | Y/N |
| Participant selection is explicitly justified (not just convenient) | Y/N |
| Post-trial access or broader benefit distribution is addressed | Y/N |
| Governance level and required safeguards are specified | Y/N |

## Red Flags

- Consent document uses technical jargon (e.g., "protocol," "randomization," "endpoints") without plain-language definition.
- Risks are minimized or omitted (e.g., "minimal risk" claimed without justification).
- No real benefit to participants, yet the study enrolls vulnerable populations (prisoners, children, cognitively impaired).
- Withdrawal process is vague or carries implied penalties (e.g., "you can withdraw but we may exclude you from future studies").
- Participants are selected solely because they are "readily available" (recruitment convenience, not scientific necessity).
- No plan for handling incidental findings (e.g., researcher discovers a health problem unrelated to the study).
- Power imbalance unaddressed (e.g., student enrolls classmates, clinician enrolls patients, professor enrolls advisees) with no external recruitment or oversight.
- Study design could answer the question without the identified high-risk procedure, but the risky procedure is included anyway.

## Output Format

```
## Research Ethics Assessment

**Research Question:**
<one plain-language sentence>

**Population:** <age, health status, capacity, group characteristics>

### Protocol Elements
| Element | Description |
|---|---|
| Procedures | <all interventions and measurements> |
| Individual Risks | <probability, severity, each risk> |
| Group-Level Risks | <stigma, discrimination, etc.> |
| Direct Benefits | <to participant> |
| Indirect Benefits | <to others or science> |
| Consent Process | <written/oral, verification method, withdrawal terms> |

### Principle 1: Respect for Persons
**Informed Consent Components:**
- Disclosure: [Present / Incomplete / Absent]
- Comprehension verification: [Method / None specified]
- Voluntariness: [Coercive elements / None identified]

**Diminished Autonomy Protections:**
- Population: <if applicable>
- Safeguards in place: [List or N/A]

### Principle 2: Beneficence
**Risk-Benefit Matrix:**
| Risk | Probability | Severity | Justification | Alternative Exists? |
|---|---|---|---|---|
| <...> | [High/Low] | [High/Low] | <...> | [Y/N] |

**Monitoring Plan:** <stopping rules, oversight mechanism, harm reporting>

### Principle 3: Justice
**Participant Selection Justification:**
- Is this population scientifically necessary? [Y/N]
- Burden concentration: [Present / Absent]
- Exploitation risk: [High / Medium / Low] — <justification>

**Benefit Distribution:**
- Post-trial access: [Specified / Absent]
- Broader access commitment: [Present / Absent]

### Required Governance & Safeguards
- Oversight level: [Standard IRB / Vulnerable populations subcommittee / External ethics / Other]
- Mandatory revisions: <list>

### Critical Gaps (if any)
<describe any ethical concerns not addressed in protocol>

### Confidence
<high/medium/low> — <justification. High: all three principles adequately addressed with detailed plans. Medium: major principles covered but gaps remain. Low: significant risks unaddressed or consent structure deficient.>
```
