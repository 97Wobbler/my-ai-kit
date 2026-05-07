---
name: apqp-ppap
display_name: APQP / PPAP
class: lens
underlying_class: native
domain: manufacturing
source: AIAG (Automotive Industry Action Group), 1997
best_for:
  - Validating supplier process capability before production launch
  - Structuring product and process design reviews with OEMs
  - Documenting design intent and manufacturing feasibility trade-offs
one_liner: "Prove supplier process capability to OEM standards before new-part production."
---

# APQP / PPAP

## Overview
Advanced Product Quality Planning (APQP) is a structured five-phase process for developing a new part or assembly before production intent. Production Part Approval Process (PPAP) is the submission and evidence package the supplier delivers at the end of APQP to prove the design, process, and controls are ready. Together, they enforce that process capability (Cpk ≥ 1.33) and design robustness are demonstrated *before* the first production run, not discovered during it. Practitioners use this when launching new parts into regulated or safety-critical applications, or when an OEM contractually requires evidence that a supplier has done the planning work.

## Analytical Procedure

### Phase 1 — Gather APQP inputs and establish the program structure (APQP)

1. **Collect the contract and design intent from the OEM.** Obtain:
   - Purchase order or engineering release with part number, revision level, and key performance indicators (dimensions, material, surface finish, electrical properties if applicable).
   - Design specification (CAD, 2D drawings, or material datasheet).
   - OEM's PPAP submission level requirement (see Step 6 below).
   - Any OEM-imposed design freeze dates and sampling windows.

2. **Hold a launch meeting with Design, Process Engineering, Quality, and Production.** Confirm:
   - Who owns each part of the APQP plan (design verification, process capability, tooling procurement, control plan).
   - Timeline: design freeze date, first article inspection (FAI) date, production release date.
   - Resource constraints (equipment availability, measurement system availability, raw material lead time).
   - Any known process risks (e.g., tight tolerance stack-up, novel material, new supplier for a critical sub-component).

3. **Create or update a control plan.** Document:
   - Each critical product characteristic (CPK) and critical process parameter (CPP).
   - Inspection / test method for each characteristic (100% inline, sampling plan, or attribute test).
   - Accept/reject criteria (upper/lower spec limits, surface finish standards, hardness ranges).
   - Who is responsible for each check (in-process, at-gate, by customer).
   Do NOT leave a characteristic unmapped. Every dimension and property must have a measurement method and ownership.

### Phase 2 — Design and process validation (APQP)

4. **Run Failure Mode and Effects Analysis (FMEA) on the part design and manufacturing process.** For each failure mode:
   - Estimate severity (1–10 scale, where 10 = safety-critical, 1 = cosmetic).
   - Estimate current occurrence probability (1–10, where 10 = will definitely happen without controls).
   - Estimate current detection capability (1–10, where 10 = we will definitely miss it in test).
   - Calculate Risk Priority Number (RPN) = Severity × Occurrence × Detection.
   - For RPN > 100 or Severity ≥ 8, define a mitigation action (design change, process control, 100% inspection).
   - Record the action owner and target completion date.
   Do NOT declare the FMEA complete until all high-RPN items have been assigned a mitigation.

5. **Verify design changes close the FMEA gaps.** Once a mitigation is implemented:
   - Confirm the change reduces Occurrence or Detection (or both).
   - Recalculate RPN. Target: RPN < 100 for all items, and Severity × Occurrence < 8 for safety-critical modes.
   - If RPN is still high, add a redundant control (e.g., 100% inline inspection + final audit).

6. **Plan and execute process capability studies.** For each critical process parameter (CPP):
   - Run at least 30 consecutive parts or subassemblies under production-intent conditions (same equipment, same operator shift, same material lot, same environmental conditions).
   - Measure each part using the same inspection method and gauge that will be used in production.
   - Calculate the process capability index (Cpk) and process performance index (Ppk).
   - Acceptance criterion: **Cpk ≥ 1.33** for each CPP. If Cpk < 1.33, adjust the process (tool offsets, coolant, speed, pressure) and re-run the study until the target is hit.
   - Document the raw data, control charts (X-bar/R or I-MR), and the final Cpk values in a traceable file.

### Phase 3 — PPAP submission preparation

7. **Prepare the PPAP submission level.** OEMs typically demand one of five levels:
   - **Level 1:** Part number/change notice only (lowest rigor, used for minor changes to existing parts).
   - **Level 2:** Part number + control plan + supporting data for critical characteristics.
   - **Level 3:** Level 2 + dimensional layout (CAD / 2D drawings with GD&T callouts), first article inspection report (FAI).
   - **Level 4:** Level 3 + process capability studies, FMEA, material certifications, tooling photos.
   - **Level 5:** Level 4 + pre-production run (typically 300–1000 units) inspected and sorted, design history file (DHF), production history file (PHF).
   Confirm your OEM's requirement early. Most automotive OEMs demand Level 3, 4, or 5 for new parts.

8. **Compile the PPAP package.** Organize the submission into a folder or bound document with:
   - Cover sheet: part number, revision, supplier name, submission date, OEM contact.
   - Dimensional layout with GD&T (CAD extract or formal drawing).
   - Material certifications (mill certs, third-party test reports if metal).
   - Process capability study reports (Cpk values, control charts, raw data).
   - Control plan (hard copy or PDF).
   - FMEA summary (design and process FMEAs, with mitigation actions and current RPN).
   - First article inspection report (CMM report, hardness test results, material analysis if applicable).
   - Design verification summary (simulation results, bench testing, if applicable).
   - Tooling photos and serial numbers (so the OEM can audit the actual tools later if needed).
   - Production trial run data (if Level 5): sample size, number of parts produced, number of defects, lot certifications.

9. **Perform an internal audit of the PPAP package before sending.** Checklist:
   - All critical characteristics have a process capability study showing Cpk ≥ 1.33.
   - All high-severity failure modes (from FMEA) have a documented mitigation and updated RPN.
   - Material certifications match the specification in the design.
   - Control plan lists an owner and acceptance method for every critical characteristic.
   - Dimensional data is complete: no missing dimensions, no conflicting tolerances.
   - Signature and approval lines are filled in by Design, Manufacturing, and Quality.
   Do NOT skip the internal audit. It catches 80% of OEM rejections.

### Phase 4 — Submit and obtain OEM approval

10. **Submit the PPAP package to the OEM quality engineer assigned to your part.** Include:
    - A cover letter stating the submission level, part number, and a summary of any changes from the previous revision.
    - A checklist of included documents.
    - Contact information for clarifications.

11. **Expect the OEM to respond within 2–4 weeks with one of:**
    - **Approved (Green):** Part is released to production. Begin scheduling first-off parts and ramping production volume.
    - **Conditional approval (Yellow):** Approved pending minor documentation updates or a small design change. Supplier must address and resubmit.
    - **Rejected (Red):** One or more critical requirements are not met (e.g., Cpk < 1.33, FMEA incomplete, material mismatch). Supplier must investigate root cause, make changes, and resubmit.

### Phase 5 — Maintain process control and traceability (APQP)

12. **Implement ongoing control during production ramp.** For the first 1000 units (or first production month):
    - Run a control chart for each CPP: plot each sample on an X-bar/R chart with control limits from the capability study.
    - If any point falls outside the control limits, stop the line, investigate the cause, adjust the process, and take corrective action on affected parts.
    - Record the data and corrective actions in a traceable log.

13. **Maintain design history and production history files (DHF/PHF) as part of ongoing records.**
    - DHF: All design documents, CAD, simulation results, design reviews, design changes, and approval records.
    - PHF: All PPAP submissions, process capability studies, control charts, FMEA updates, tooling changes, corrective actions, and customer complaints related to the part.
    - These files are the supplier's proof that the process is under control and traceable. OEMs audit DHF/PHF periodically (usually annually).

## Evaluation Criteria

| Check | Pass |
|---|---|
| OEM's PPAP submission level is documented and resources allocated | Y/N |
| FMEA identifies all high-severity failure modes (Severity ≥ 8) and documents mitigation for each | Y/N |
| Process capability studies are complete for all CPPs, with Cpk ≥ 1.33 for each | Y/N |
| Capability study data includes at least 30 consecutive parts, measured with production-intent equipment | Y/N |
| Control plan lists an owner and acceptance criterion for every critical characteristic | Y/N |
| PPAP package is complete: dimensional layout, capability data, FMEA, FAI report, material certs, control plan | Y/N |
| Internal audit of PPAP package completed before OEM submission | Y/N |
| Ongoing control plan (X-bar/R chart, corrective action log) is in place before production ramp | Y/N |

## Red Flags

- Cpk is calculated from a single production run (e.g., one shift, one tool setting, one material lot). Capability studies must span multiple shifts/tools/lots to be valid.
- FMEA has no high-severity failure modes. Either the part is trivial (unlikely) or the FMEA was filled out at a shallow level without cross-functional input.
- Control plan lists "inspect all parts" for every critical characteristic. This is a symptom that the process is not capable or controls are not in place; it's expensive and not sustainable in high-volume production.
- PPAP submission has no capability study or only old data from a previous revision. A new Cpk study is required whenever the process, equipment, tooling, or raw material changes.
- Material certificates are generic or missing. OEMs require third-party test reports for metals and other critical materials; self-signed supplier certs are rejected.
- Dimensional layout is a redline or informal sketch. PPAP requires formal CAD extract or a released 2D drawing with GD&T; hand-drawn tolerances are not acceptable.
- No design freeze date or no confirmation that design is locked before Cpk studies begin. If the part design changes during the capability study, the study is invalidated.

## Output Format

```
## APQP / PPAP Assessment

**Part number and revision:**
<part number, revision>

**OEM and PPAP submission level:**
<OEM name, required level (1–5)>

### Phase 1 — Program Structure
- APQP team members and responsibilities: [names/roles]
- Program timeline: Design freeze [date] | FAI [date] | Production release [date]
- Known risks or constraints: [list]
- Control plan: [Y/N — if Y, confirm all characteristics are mapped]

### Phase 2 — Design and Process Validation
| Failure Mode | Severity | Current RPN | Mitigation | New RPN | Status |
|---|---|---|---|---|---|
| <mode> | <1–10> | <RPN> | <action> | <RPN> | <closed/open> |

| Critical Process Parameter | Process Capability Study Date | Cpk | Status |
|---|---|---|---|
| <parameter> | <date> | <Cpk value> | <meets 1.33 / below 1.33> |

### Phase 3 — PPAP Submission Readiness
| PPAP Component | Included | Complete | Notes |
|---|---|---|---|
| Dimensional layout (CAD/2D drawing) | Y/N | Y/N | <notes> |
| Material certifications | Y/N | Y/N | <notes> |
| Process capability studies | Y/N | Y/N | <notes> |
| Control plan | Y/N | Y/N | <notes> |
| FMEA summary | Y/N | Y/N | <notes> |
| First article inspection report | Y/N | Y/N | <notes> |
| Tooling documentation | Y/N | Y/N | <notes> |

Internal audit status: [completed / pending]

### Phase 4 — OEM Response
Submission date: <date>
OEM response: [pending / approved / conditional / rejected]
If conditional or rejected, required actions: <list>

### Phase 5 — Ongoing Control
Production ramp control plan: [in place / pending]
DHF/PHF baseline established: [Y/N]
First corrective actions (if any): <summary>

### Confidence
<high | medium | low> — <justification (e.g., "High: all Cpk studies met 1.33, FMEA mitigation complete, OEM approved." or "Low: capability study pending on tooling change, FMEA RPN for Mode X still > 100.")>
```
