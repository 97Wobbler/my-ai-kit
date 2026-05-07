---
name: eu-ai-act
display_name: EU AI Act Risk Tier Classification
class: lens
underlying_class: native
domain: applied-ethics
source: European Union (Regulation 2024/1689); implemented April 2024
best_for:
  - Classifying AI systems by regulatory risk tier
  - Identifying mandatory compliance obligations
  - Assessing high-risk AI system requirements
one_liner: "Classify AI system into risk tier (unacceptable/high/limited/minimal), then verify tier-specific obligations are met."
---

# EU AI Act Risk Tier Classification

## Overview

The EU AI Act establishes a tiered risk framework for AI systems: unacceptable risk (prohibited), high risk (extensive requirements), limited risk (transparency obligations), and minimal risk (voluntary best practices). Practitioners use this lens to determine which regulatory requirements bind a given AI system and to audit whether a deployed or proposed system satisfies its tier's obligations. The discipline is accurate tier classification — misclassification leads to either over-compliance costs or regulatory violations.

## Analytical Procedure

### Phase 1 — System Definition

1. **Document the AI system's purpose and scope.** Write in one sentence: What is the system designed to do? Who uses it? What decisions or actions does it influence?

2. **Identify the primary use case(s).** List the 2–4 most important applications of the system. Each may fall into a different tier; you will classify each separately.

3. **Map inputs, processing, and outputs.** What data enters? What transformation occurs? What decision, recommendation, or prediction leaves the system? This clarity prevents misclassification due to feature creep or hidden use cases later.

### Phase 2 — Unacceptable Risk Classification

4. **Check against prohibited practices.** The EU AI Act bans certain uses outright, regardless of safeguards:
   - Real-time biometric identification systems in public spaces (with narrow exceptions for law enforcement under strict conditions)
   - Social credit scoring that causes social disadvantage
   - Manipulative AI designed to exploit vulnerable groups (children, disabled persons)
   - Emotion recognition in critical contexts (law enforcement, border control, employment)
   
   **If any use case matches, classify it as Unacceptable Risk. STOP. This use case cannot proceed under EU AI Act unless an exception explicitly applies.** Document the exception and verify it holds.

5. **If no unacceptable use is present, proceed to Phase 3.**

### Phase 3 — High-Risk Classification

6. **Check against Annex III categories.** High-risk AI systems fall into one of these categories:
   
   **Biometric and identification:**
   - Biometric classification, categorization, or identification (except emotion recognition, which is unacceptable)
   
   **Critical infrastructure and safety:**
   - Operation of critical infrastructure (power grids, water, transport, gas)
   - Safety components in machinery, vehicles, or aviation
   
   **Employment and education:**
   - Recruitment filtering, candidate evaluation, or performance monitoring
   - Educational assessment, placement, or eligibility determination
   
   **Law enforcement and judicial:**
   - Police investigation assistance or suspect evaluation
   - Predicting criminal behavior or reoffending risk
   - Determining guilt, innocence, or sentence severity
   - Detecting or classifying evidence
   
   **Migration, asylum, border control:**
   - Border crossing assessment, visa decisions, deportation decisions
   
   **Credit and financial:**
   - Creditworthiness or loan approval
   - Insurance premium or eligibility determination
   - Benefits eligibility determination
   
   **Health and safety:**
   - Real-time disease diagnosis or treatment recommendation
   - Triage or patient prioritization in critical scenarios
   - Allocation of scarce medical resources
   
   **Benefits determination:**
   - Eligibility for public assistance (unemployment, housing, child benefits, disability)
   - Fraud detection in public benefits
   
   **Law enforcement biometrics:**
   - Mass screening via facial recognition, gait recognition, or voice identification
   
   For each use case, ask: **Does this system perform a function listed above?** If yes, classify as High Risk and proceed to Phase 4. If no, proceed to Phase 3b.

7. **Check for modified or augmented versions of high-risk categories.** Systems that refine, build upon, or augment a high-risk function are also high-risk. Example: a recruitment system that uses high-risk biometric inputs is high-risk even if the final decision is not biometric-based.

### Phase 3b — Limited and Minimal Risk

8. **Check for transparency-sensitive use cases.** Limited-risk systems require transparency but not the extensive controls of high-risk. They include:
   - General-purpose language models or foundation models (unless fine-tuned for a high-risk function)
   - Deepfakes or synthetic media systems
   - AI systems that influence significant decisions about individuals (but are not in the high-risk categories)
   - Chatbots and conversational AI
   
   If the system falls here, classify as Limited Risk.

9. **If none of the above apply, classify as Minimal Risk.** This includes most analytical, generative, and optimization AI systems that do not directly influence consequential human decisions.

### Phase 4 — Obligation Mapping

10. **For High-Risk systems, verify these mandatory requirements:**
    - Risk assessment documentation (before deployment)
    - Data quality and governance (training data must be "adequate and relevant")
    - Technical documentation and RAIC (Register of AI Conformity)
    - Logging and record-keeping (6 months of AI system operation logs)
    - Human oversight procedure (meaningful human control before critical decisions)
    - Transparency and information provision (user must know they interact with AI)
    - Cybersecurity and robustness testing (including adversarial testing)
    - Performance monitoring post-deployment
    - Conformity assessment (internal or by third-party notified body)
    - CE marking and EU Declaration of Conformity
    
    For each requirement, document: (a) Is it implemented? (b) Is it sufficient? (c) Is evidence retained and audit-able?

11. **For Limited-Risk systems, verify these obligations:**
    - Disclosure that an AI system is being used
    - Clear information about system capabilities and limitations
    - For synthetic media (deepfakes): clear disclosure that the content is AI-generated

12. **For Minimal-Risk systems, best practices are encouraged but not mandatory.**
    - NIST AI RMF, ISO 42001, or similar frameworks are voluntary.

### Phase 5 — Confidence and Gaps

13. **Identify classification confidence.** Is the tier classification certain, or does the system straddle boundaries?
    - **High confidence:** System clearly matches one category with no ambiguity.
    - **Medium confidence:** System matches a category but has edge cases or unclear secondary functions.
    - **Low confidence:** System could plausibly fit multiple tiers depending on interpretation of intent, data use, or context.
    
    If confidence is low, escalate to legal/compliance review before deployment.

14. **Document any known gaps or delegated responsibility.** For instance: "This system is classified as High Risk; human oversight is delegated to the end-user organization. Evidence that users understand their oversight obligation must be retained."

## Evaluation Criteria

| Check | Pass |
|---|---|
| System purpose and primary use case(s) clearly documented | Y/N |
| Unacceptable risk categories explicitly checked; exceptions (if any) documented | Y/N |
| All applicable Annex III high-risk categories checked | Y/N |
| Final tier classification (Unacceptable/High/Limited/Minimal) is defensible | Y/N |
| For High-Risk: all 11 obligations have implementation status (Yes/No/Partial) | Y/N |
| Confidence level (High/Medium/Low) and justification recorded | Y/N |
| If confidence is Low, escalation documented | Y/N |

## Red Flags

- System's purpose is vague ("general AI assistant"). Restate it concretely or reclassify as Limited Risk.
- Unacceptable risk categories are checked but exceptions are claimed without legal citation. Verify the exception is real and narrow.
- High-Risk classification but only 2–3 of 11 obligations are addressed. The system is not compliant; deployment is premature.
- Classification changed after discovering secondary use cases. Document all use cases upfront or implement governance to prevent drift.
- Human oversight obligation is listed as "future responsibility of deployer." Without written contract and audit trail, this is a compliance failure waiting to happen.
- Confidence is reported as "High" but the system is new or operates in novel legal jurisdiction. Historical case law or regulatory guidance may be absent.
- Foundation model or general-purpose system is classified as Minimal Risk without checking whether fine-tuning brings it into High Risk.

## Output Format

```
## EU AI Act Risk Tier Assessment

**System name and version:**
<...>

**Primary use case(s):**
1. <...>
2. <...>

### Phase 1 — System Definition
**Purpose (one sentence):**
<...>

**Inputs → Processing → Outputs:**
- Input: <...>
- Processing: <...>
- Output: <...>

### Phase 2 — Unacceptable Risk Check
| Prohibited practice | Applies? | Exception claimed? | Verified? |
|---|---|---|---|
| Real-time biometric ID in public spaces | Y/N | Y/N | Y/N |
| Social credit scoring | Y/N | Y/N | Y/N |
| Manipulative AI on vulnerable groups | Y/N | Y/N | Y/N |
| Emotion recognition in critical context | Y/N | Y/N | Y/N |

**Verdict:** Proceed / PROHIBITED

### Phase 3 — High-Risk Classification
| Annex III category | Applies? | Notes |
|---|---|---|
| Biometric classification/identification | Y/N | <...> |
| Critical infrastructure operation | Y/N | <...> |
| Employment/education assessment | Y/N | <...> |
| Law enforcement/judicial | Y/N | <...> |
| Migration/asylum/border control | Y/N | <...> |
| Credit/financial decisions | Y/N | <...> |
| Health/safety diagnosis or triage | Y/N | <...> |
| Public benefits determination | Y/N | <...> |
| Law enforcement biometric mass screening | Y/N | <...> |

**Any matches:** HIGH RISK (proceed to Phase 4) / NO MATCHES (check Phase 3b)

### Phase 3b — Limited Risk Check
- Transparency-sensitive (e.g., foundation model, deepfake, significant decision influence)? Y/N
- Result: LIMITED RISK / MINIMAL RISK

### Phase 4 — High-Risk Obligations (if applicable)
| Obligation | Implemented? | Sufficient? | Evidence retained? |
|---|---|---|---|
| Risk assessment (pre-deployment) | Y/N/Partial | Y/N | Y/N |
| Data quality and governance | Y/N/Partial | Y/N | Y/N |
| Technical documentation and RAIC | Y/N/Partial | Y/N | Y/N |
| Logging and record-keeping (6 months) | Y/N/Partial | Y/N | Y/N |
| Human oversight procedure | Y/N/Partial | Y/N | Y/N |
| Transparency/disclosure to users | Y/N/Partial | Y/N | Y/N |
| Cybersecurity and robustness testing | Y/N/Partial | Y/N | Y/N |
| Performance monitoring (post-deployment) | Y/N/Partial | Y/N | Y/N |
| Conformity assessment | Y/N/Partial | Y/N | Y/N |
| CE marking and Declaration | Y/N/Partial | Y/N | Y/N |
| Cybersecurity/adversarial robustness | Y/N/Partial | Y/N | Y/N |

**Compliance status:** Compliant / Gaps identified (list below)

### Phase 4b — Limited-Risk Obligations (if applicable)
| Obligation | Implemented? |
|---|---|
| User disclosure (AI in use) | Y/N |
| Capabilities/limitations transparency | Y/N |
| Synthetic media disclosure (if applicable) | Y/N |

### Gaps or Deferred Responsibilities
<List any obligations marked "N" or "Partial", and who is responsible for closing the gap.>

### Classification Summary
**Final tier:** Unacceptable Risk / High Risk / Limited Risk / Minimal Risk
**Confidence:** High / Medium / Low
**Justification:** <2–3 sentences on why this tier applies and any classification uncertainties.>

### Confidence
<high/medium/low> — <Confidence reflects clarity of tier classification, completeness of Annex III assessment, and presence of secondary use cases or jurisdictional ambiguity.>
```
