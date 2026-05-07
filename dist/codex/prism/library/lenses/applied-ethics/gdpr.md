---
name: gdpr
display_name: GDPR Compliance Audit
class: lens
underlying_class: native
domain: applied-ethics
source: EU Regulation 2016/679 (General Data Protection Regulation), effective May 25, 2018
best_for:
  - Auditing data processing activities for regulatory compliance
  - Identifying gaps in consent, transparency, and data subject rights
  - Assessing necessity and proportionality of personal data collection
one_liner: "Map personal data flows, verify lawful basis under Article 6, confirm data subject rights implementation, and evaluate Data Protection Impact Assessment necessity."
---

# GDPR Compliance Audit

## Overview
GDPR is the EU's baseline standard for lawful personal data processing. Rather than a checklist of features, it is a constraint-based framework: every processing activity must satisfy four irreducible requirements — lawful basis, transparency, data subject rights, and proportionality. Practitioners use this lens when designing data systems, auditing existing workflows, or preparing for regulatory review. The discipline is tracing each data flow from source to deletion and confirming that every touch point satisfies the regulation.

## Analytical Procedure

### Phase 1 — Map the Processing Activity

1. **Name the processing activity in plain language.** Examples: "user authentication," "marketing email sending," "fraud detection," "analytics reporting." Avoid jargon; be specific about *what data is touched* and *what decision or action results*.

2. **For this activity, identify all personal data involved.** Personal data is any information relating to an identified or identifiable natural person. Itemize:
   - Direct identifiers (name, email, phone, ID number)
   - Quasi-identifiers (age + location + employer — combination that re-identifies)
   - Sensitive categories (racial/ethnic origin, political opinion, religious belief, genetic data, biometric data for ID, health, sex life, trade union membership)
   - Inferred or derived data (scores, segments, predictions about the person)
   - Metadata (timestamps, IP addresses, device IDs, cookie IDs if linkable to a person)

3. **Identify all parties involved:**
   - **Controller** — the entity (you, your company) that decides what data is collected and why.
   - **Processor** — any third party (vendor, cloud provider, analytics platform) that processes data on the controller's instructions.
   - **Joint controller** — a partner that shares decision-making authority over processing purposes or means.
   - **Data subject** — the person whose data is collected.

4. **Document the data lifecycle:** Where does the data come from? Where is it stored? Who accesses it? How long is it retained? Where does it go when deleted or transferred? Draw a flow diagram if processing involves multiple systems or parties.

### Phase 2 — Verify Lawful Basis (Article 6)

Every processing activity must rest on at least one lawful basis from Article 6. If none applies, the processing is unlawful.

5. **For the processing activity identified in Phase 1, determine which basis (if any) applies:**

   - **Consent (6.1.a):** The data subject has *freely* given *specific* and *informed* consent. Consent is not passive (pre-ticked boxes, silence, inactivity). Consent must be withholdable without penalty. If the person cannot refuse without losing access to an essential service, it is not free consent.
     - **Check:** Is consent explicit, separate from other terms, and can it be withdrawn? Is there a record of when and how consent was obtained?
   
   - **Contract (6.1.b):** Processing is necessary to perform a contract the data subject has entered. "Necessary" means the data would not serve its stated purpose without that data.
     - **Check:** Would the contract still function if this data were removed? Is collection proportional to contract performance?
   
   - **Legal obligation (6.1.c):** Processing is required by law (tax filing, AML, financial regulation, criminal justice, etc.).
     - **Check:** Name the specific statute or directive. Is the retention period dictated by law?
   
   - **Vital interests (6.1.d):** Processing is necessary to protect the vital interests (life, bodily integrity, health) of the data subject or another person.
     - **Check:** Is this a one-off emergency situation? If routine, this basis usually fails — use another.
   
   - **Public task (6.1.e):** Processing is necessary for a task in the public interest or official authority (government agencies, public health, law enforcement).
     - **Check:** Is the processing mandate statutory? Is the processing published or transparent?
   
   - **Legitimate interests (6.1.f):** Processing is necessary for legitimate interests pursued by the controller or a third party, *except where data subject interests or fundamental rights override* (balancing test).
     - **Check:** Have you documented the legitimate interest (not just "marketing")? Have you weighed it against the data subject's interest in privacy? Would the data subject reasonably expect this use? Is there a less intrusive alternative?

6. **If no lawful basis exists, processing is non-compliant.** Flag this. If a basis exists, confirm it is documented and communicated to data subjects (via privacy notice).

### Phase 3 — Confirm Data Subject Rights Implementation

7. **The regulation grants data subjects the following rights. For each, ask whether your system honors it:**

   - **Right of access (Art. 15):** Can the data subject request and receive a copy of all data you hold about them in machine-readable form within 30 days (extendable by 2 months)?
   
   - **Right to rectification (Art. 16):** Can the data subject correct inaccurate data? Do you have a process to update records when asked?
   
   - **Right to erasure (Art. 17):** Can the data subject demand deletion ("right to be forgotten") when the lawful basis no longer applies, consent is withdrawn, or data is no longer necessary? Exception: if legal obligation or legitimate interests override, you may retain with justification.
   
   - **Right to restrict processing (Art. 18):** Can the data subject ask you to stop using their data (without deleting it) while disputing accuracy or basis?
   
   - **Right to data portability (Art. 20):** Can the data subject get their data in a structured, commonly-used, machine-readable format (e.g., CSV, JSON) and have it transmitted to another controller?
   
   - **Right to object (Art. 21):** Can the data subject object to processing based on legitimate interests, direct marketing, or profiling? You must stop unless you prove overriding interests.
   
   - **Rights related to automated decision-making (Art. 22):** If a decision with significant legal or practical effect (credit denial, hiring, benefit eligibility) is made wholly by algorithm without human review, the data subject has the right to explanation and human intervention.

8. **For each right, document:**
   - Is there a mechanism to exercise it (email, web form, API)?
   - What is the response time (usually 30 days)?
   - Is the process free of cost?
   - Are exceptions (legal obligation, competing rights) clearly documented?

### Phase 4 — Assess Data Protection Impact Assessment (DPIA) Necessity (Article 35)

9. **A DPIA is a formal risk analysis required for high-risk processing. Processing is likely high-risk if it involves:**

   - Large-scale systematic collection or monitoring (especially of children, employees, or vulnerable groups)
   - Automated decision-making or profiling with significant effects (credit, employment, criminal justice, insurance)
   - Sensitive categories (health, race, religion, sexual orientation, genetic/biometric data for ID, criminal records)
   - Data combining multiple sources, allowing re-identification or behavioral analysis
   - Data shared with third parties outside the EEA (transfers outside the EU/EEA require legal adequacy or contractual safeguards)
   - New technologies (AI, biometrics, surveillance) that create novel privacy risks

10. **If processing matches one or more above criteria, a DPIA is required.** The DPIA must document:
    - Purpose and necessity of processing
    - Data subject risks (likelihood and severity of privacy harm — unauthorized access, discrimination, loss of control, etc.)
    - Mitigations (encryption, access controls, audit logs, training, data minimization)
    - Residual risks after mitigations
    - Stakeholder consultation (data subjects, employees, external experts)

11. **If DPIA identifies residual high risks, you must consult your Data Protection Authority before processing begins.** Failure to do so is non-compliance.

### Phase 5 — Proportionality and Data Minimization (Article 5)

12. **For the processing activity, apply the data minimization principle:**
    - Is the data collected adequate (enough to achieve the stated purpose)?
    - Is it relevant (does it actually serve the purpose)?
    - Is it limited to what is necessary (no surplus data collected "just in case")?
    - Is retention time bounded (not kept forever when a shorter period suffices)?
    
    If you collect name, email, phone, and purchase history but the purpose is one-time product delivery, this fails proportionality — surplus data should not be collected.

13. **Document the retention schedule:**
    - When is data deleted or anonymized?
    - Is deletion automatic or manual?
    - Are there legal holds (litigation, audit) that extend retention?

## Evaluation Criteria

| Check | Pass |
|---|---|
| All personal data in the processing activity identified, including quasi-identifiers and metadata | Y/N |
| Controller, processor, and joint controller roles clearly assigned | Y/N |
| Data lifecycle (source, storage, access, deletion) documented | Y/N |
| At least one Article 6 lawful basis found and documented | Y/N |
| Lawful basis is justified (not merely asserted; balancing test completed for legitimate interests) | Y/N |
| Data subject rights mechanisms are in place for all applicable rights | Y/N |
| DPIA completed if processing is high-risk; or documented reasoning why processing is low-risk | Y/N |
| Data minimization principle applied; surplus data identified and removal plan created | Y/N |
| Privacy notice provided to data subjects explaining basis, rights, and recipients | Y/N |

## Red Flags

- Lawful basis is "consent" but consent mechanism allows pre-ticked boxes, silence, or bundled consent (all non-compliant under GDPR).
- Lawful basis is "legitimate interests" but no balancing test is documented — only the controller's interest is mentioned.
- Data retention policy is missing or states "indefinite" retention.
- Data subject rights requests have no documented response SLA; or responses exceed 30 days without extension justification.
- Processor (third-party vendor) is used without a written Data Processing Agreement (DPA).
- Processing involves sensitive data or automated decision-making but no DPIA is documented.
- Privacy notice is not provided to data subjects, or provided only in opaque legal language.
- Data is transferred outside the EEA without adequacy decision or Standard Contractual Clauses (SCCs).
- Deletion/erasure mechanism does not exist; data is never purged from backups or archives.

## Output Format

```
## GDPR Compliance Audit

**Processing Activity:**
<plain-language description of what data is collected, for what purpose, and what happens as a result>

### Phase 1 — Processing Map
- **Data categories:** <list of personal data types>
- **Sensitive categories (if any):** <list>
- **Controller:** <entity making decisions>
- **Processor(s):** <third parties handling data on instructions>
- **Data subjects:** <who the data is about>
- **Retention period:** <how long data is kept>

### Phase 2 — Lawful Basis
- **Basis applied:** <Article 6.1.a/b/c/d/e/f>
- **Justification:** <explanation of why basis applies; for legitimate interests, include balancing test>
- **Documentation:** <evidence that basis is recorded and communicated to data subjects>
- **Compliance: PASS / FLAG**

### Phase 3 — Data Subject Rights
| Right | Mechanism | Response time | Free of cost? | Status |
|---|---|---|---|---|
| Access (Art. 15) | <process> | <days> | Y/N | PASS / PARTIAL / MISSING |
| Rectification (Art. 16) | <...> | <...> | <...> | <...> |
| Erasure (Art. 17) | <...> | <...> | <...> | <...> |
| Restrict (Art. 18) | <...> | <...> | <...> | <...> |
| Portability (Art. 20) | <...> | <...> | <...> | <...> |
| Object (Art. 21) | <...> | <...> | <...> | <...> |
| Automated decision-making (Art. 22) | <...> | <...> | <...> | <...> |

### Phase 4 — Data Protection Impact Assessment
- **High-risk factors present:** <list criteria from Phase 4, step 9>
- **DPIA required:** Y/N
- **If yes, DPIA status:** <completed | in progress | planned>
- **Residual risks:** <list unresolved risks after mitigations>
- **Authority consultation required:** Y/N

### Phase 5 — Data Minimization & Retention
- **Adequate:** <data covers stated purpose with no surplus>
- **Relevant:** <data actually serves purpose>
- **Limited to necessity:** <no bloat; only essential data collected>
- **Retention bounded:** <deletion schedule documented and automatic if possible>
- **Compliance: PASS / FLAG**

### Gaps & Remediation
| Gap | Severity | Remediation | Owner | Due |
|---|---|---|---|---|
| <...> | High/Medium/Low | <...> | <...> | <...> |

### Overall Compliance
- **Status:** COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT
- **Critical blockers:** <list any blockers to compliance>

### Confidence
<high | medium | low> — <justification based on completeness of documentation, clarity of lawful basis, and presence/absence of mitigating controls>
```
---
