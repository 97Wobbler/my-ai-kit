---
name: customer-journey-map
display_name: Customer Journey Map
class: lens
underlying_class: native
domain: marketing
source: origin uncertain; popularized in service design (Shostack, 1982) and experience design practice
best_for:
  - Identifying gaps and friction points across the customer lifecycle
  - Aligning teams around shared understanding of customer experience
  - Prioritizing touchpoint improvements by impact and effort
one_liner: "Map every touchpoint from awareness to advocacy and track emotion and behavior along the way."
---

# Customer Journey Map

## Overview
A Customer Journey Map visualizes the sequence of interactions a customer has with a brand or product across time, stages, and channels. The map plots touchpoints (direct interactions), moments of truth (high-impact decisions), emotional peaks and valleys, and behind-the-scenes systems enabling each interaction. Practitioners use this to surface invisible friction, uncover moments where competitors are winning, and align cross-functional teams on where investment matters most.

## Analytical Procedure

### Phase 1 — Define Scope and Persona

1. **Select a specific customer segment and journey stage.** Do not map "all customers" — map a discrete slice: "SMB buyer, awareness to purchase" or "power user, onboarding to month 3." Write one sentence describing who this segment is and what goal they are pursuing in this journey.

2. **Identify the time horizon.** When does the journey start (e.g., first awareness) and end (e.g., advocacy, churn)? Mark the stage boundaries explicitly on your map.

3. **List all known channels and touchpoints.** Brainstorm every possible interaction: website, email, sales call, product UI, support chat, community, reviews, word-of-mouth, ads. Organize by channel (digital, human, physical). Include passive touchpoints (they see an ad but don't click) and active ones (they fill a form).

### Phase 2 — Map the Timeline

4. **Arrange touchpoints chronologically.** Plot them on a horizontal axis representing the journey's time span. Spacing reflects actual time between interactions (days, weeks). Do not assume uniform spacing.

5. **For each touchpoint, document:**
   - **What happens:** the concrete action or moment (e.g., "customer reads product review on G2").
   - **Who triggers it:** the customer, the company, a third party, or mutual.
   - **Channel:** web, email, app, phone, in-person, etc.
   - **Intent:** what the customer wants to accomplish here.
   - **What the customer learns:** what information or impression they take away.

6. **Mark critical moments of truth.** These are touchpoints where a single negative experience can end the journey (e.g., slow checkout, delayed support response). Flag them visually.

### Phase 3 — Layer Emotional and Behavioral Data

7. **Score emotional state at each touchpoint.** Use a scale of −2 (very frustrated), −1 (discouraged), 0 (neutral), +1 (satisfied), +2 (delighted). Base this on user research, interviews, or behavioral proxies (e.g., bounce rate, support ticket escalation). If you lack data, mark it as "unknown" and flag it for research.

8. **Identify painpoints and opportunities.** A painpoint is a place where the emotional score is negative or where the customer abandons the journey. An opportunity is a moment where a small improvement would shift emotion sharply positive (e.g., adding a progress indicator to a form, reducing checkout to one click).

9. **Plot the "customer effort" curve.** For each touchpoint, estimate the friction: is this task easy, medium, or hard for the customer? Common friction: unclear next steps, repeated data entry, waiting, decision paralysis, distrust.

### Phase 4 — Capture Behind-the-Scenes Systems

10. **Map company touchpoints and processes.** For each customer touchpoint, document what's happening inside the organization: sales workflow, backend data flow, support escalation path, marketing automation, fulfillment process. Often misalignment here causes customer friction.

11. **Note handoffs and bottlenecks.** Where does the journey cross department boundaries (marketing → sales, sales → onboarding, product → support)? Gaps and delays often happen here.

12. **Document assumptions and data gaps.** Where does your map rely on guessing? Where do you lack user research, telemetry, or behavioral data? List explicitly.

### Phase 5 — Synthesis and Prioritization

13. **Identify patterns.** Are there phases where friction clusters (e.g., all during onboarding)? Are there moments where company capability doesn't match customer expectations (e.g., customer expects instant support; company offers 24-hour SLA)?

14. **Quantify impact and effort.** For each painpoint or opportunity, estimate:
   - **Impact:** What percentage of customers drop out here? How much does fixing this improve retention, conversion, or satisfaction?
   - **Effort:** How difficult is the fix? (engineering hours, cost, organizational alignment needed)
   Score each as high/medium/low.

15. **Prioritize interventions.** Focus on high-impact, low-effort fixes first. Avoid low-impact changes, even if they seem easy.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Specific customer segment and stage defined in one sentence | Y/N |
| Time horizon has explicit start and end | Y/N |
| Touchpoints are chronologically ordered and spaced by actual time | Y/N |
| Each touchpoint includes: what happens, who triggers it, channel, intent, what customer learns | Y/N |
| Critical moments of truth are identified and marked | Y/N |
| Emotional score is assigned to every touchpoint (or marked unknown + flagged) | Y/N |
| At least 3 painpoints and 3 opportunities are explicitly named | Y/N |
| Customer effort is estimated at each touchpoint | Y/N |
| Company-side processes are mapped for at least 5 customer touchpoints | Y/N |
| Assumptions and data gaps are documented | Y/N |
| Interventions are scored impact × effort and prioritized | Y/N |

## Red Flags

- The journey describes "all customers" or multiple stages spliced together. Scope creep kills actionability.
- Emotional scores are all neutral or all positive. Either the research was superficial or motivated reasoning kicked in.
- No critical moments of truth are marked. Most journeys have 2–4. Missing them suggests the map is generic, not specific to this segment.
- Company-side processes are absent. This is often where the real opportunity lies, but it requires cross-functional input.
- Painpoints are listed but not tied to drop-off rates or churn data. Anecdotes and assumptions don't prioritize.
- All interventions are marked "high impact, low effort." This is rarely true. Honest maps have trade-offs.
- No data gaps are documented. Every journey map relies on some guessing. Naming it shows rigor.

## Output Format

```
## Customer Journey Map

**Segment:** <customer type and goal>
**Journey stage:** <start → end>
**Time horizon:** <duration>

### Timeline & Touchpoints

| Stage | Touchpoint | Channel | Who triggers | Customer intent | What learned | Emotion | Effort | Critical? |
|---|---|---|---|---|---|---|---|---|
| <stage name> | <action> | <web/email/phone/...> | <customer/company/3rd party> | <...> | <...> | [−2 to +2] | [H/M/L] | Y/N |

### Painpoints (≥3)
1. <Touchpoint>: <Description of friction> — Impact: H/M/L | Effort to fix: H/M/L
2. ...

### Opportunities (≥3)
1. <Touchpoint>: <Small change that would improve emotion/effort> — Impact: H/M/L | Effort: H/M/L
2. ...

### Behind-the-Scenes: Company Processes
<For 3–5 critical touchpoints, describe the internal workflow/system that enables it. Note handoffs and bottlenecks.>

### Assumptions & Data Gaps
- <Area where you guessed or lack data>
- <Area where research is needed>

### Prioritized Interventions
1. <High-impact, low-effort fix>
2. <Medium-impact, low-effort fix>
3. <High-impact, medium-effort fix>

### Confidence
<high/medium/low> — <high if based on user research and telemetry; medium if research is partial; low if mostly assumptions or single interviews>
```
