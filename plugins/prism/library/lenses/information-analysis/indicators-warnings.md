---
name: indicators-warnings
display_name: Indicators & Warnings
class: lens
underlying_class: native
domain: information-analysis
source: Intelligence analysis tradecraft; formalized in warning systems (CIA, NGA); adapted from structured analytic techniques
best_for:
  - Detecting early signs of a developing situation before it becomes acute
  - Building a shared baseline for what to monitor and when to escalate
  - Reducing surprise and false alarms through systematic precursor definition
one_liner: "Pre-define leading signals of situational change and track them for early warning."
---

# Indicators & Warnings

## Overview

Instead of waiting for an event to occur and then reacting, define the observable precursors—the leading indicators—that predict it. Establish thresholds, feedback loops, and escalation triggers before they are needed. Practitioners use this lens to operationalize intuition ("we'll know it when we see it") into concrete signals that can be monitored, tested, and communicated to others. The discipline is specificity: vague warning signs ("mounting tension," "increased chatter") are useless until they become measurable.

## Analytical Procedure

### Phase 1 — Define the Target Event

1. **State the event you are trying to warn about.** Write it in one sentence. It should be concrete enough that you could determine after the fact whether it happened. "Market collapse" is too vague; "S&P 500 drops >20% in 30 days" is not.

2. **Establish the warning window.** How much advance notice do you need? Days? Weeks? Years? This determines which precursors are useful. A precursor that manifests 24 hours before the event is useless if you need 90-day warning.

3. **List the causal pathways.** What are the 3-5 ways this event could come about? Write each as a brief causal chain:
   - Pathway 1: A → B → C → Event
   - Pathway 2: X → Y → Event
   - etc.
   
   If you can only think of one pathway, the event may be unpredictable or you may be reasoning by analogy to past instances. Stress-test this.

### Phase 2 — Extract Candidate Indicators

4. **For each pathway, identify the observable nodes.** These are the points where the causal chain produces something measurable. Not every node is observable (internal political disagreement is hard to measure; public statements about it are easier).

5. **Generate candidate indicators at each node.** Ask: what would an external observer see, hear, or measure if this node is active?
   - If the pathway is "economic stress → social unrest → violence," candidate indicators include: unemployment rate, social media sentiment, permit denials for public gatherings, hospital admissions for injury, police deployments, etc.
   - List 2-4 candidates per node. Quantity helps later when some indicators go false.

6. **For each candidate indicator, specify:**
   - **Definition.** What exactly are you measuring? (Not "unemployment" but "unemployment rate > 8% for 3+ consecutive months")
   - **Source.** Where does the data come from? (Bureau of Labor Statistics, Glassdoor, company filings, news reports)
   - **Frequency.** How often is it updated? (Monthly, weekly, real-time)
   - **Historical baseline.** What is normal for this indicator? (Average, variance, seasonal pattern)

### Phase 3 — Set Thresholds and Escalation

7. **For each indicator, define a threshold that counts as a "warning."** Do not use the future event itself as the threshold. Use the precursor.
   - Bad: "We'll know it's coming when the stock price drops 20%." (This is the event, not a precursor.)
   - Good: "When unemployment rate exceeds 7% AND housing permits drop >15% month-on-month AND credit card delinquencies exceed 2.5%, activate yellow alert."

8. **Build in lag and confirmation.** A single indicator flipping is noise. Define:
   - **Confirmation rule.** How many of the candidate indicators must signal before you escalate?
   - **Duration rule.** How long must the signal persist? (E.g., threshold crossed for 2+ consecutive reporting periods, not just one spike)
   - **Escalation ladder.** Separate yellow (investigate further), orange (brief stakeholders), and red (activate contingency) based on evidence density.

9. **Document false positive baseline.** Run the indicators backward on historical data. If an indicator flips every month, it is noise, not warning. Record the false positive rate. Set thresholds so that a true positive is at least 5× more likely than a false positive, or acknowledge you will tolerate false alarms at a known rate.

### Phase 4 — Test and Iterate

10. **Backtest the warning system on 3-5 past instances of the event.** If the event has never happened, use near-misses or analogs from other domains. Did the indicators you defined actually precede the event in those cases? By how much?
    - If indicators appeared only 2 days before the event but your warning window was 30 days, the system fails.
    - If indicators appeared but were missed because they were scattered across too many data sources, redesign the confirmation rule.

11. **Document indicator failures.** For each past event, record which of your candidate indicators *failed to signal*. This failure list is as important as the success list; it guides you toward blind spots.

12. **Solicit challenge.** Present the indicator set to someone who disagrees with your event forecast. Ask: "What would need to happen for my warning system to be wrong?" Their answers are your stress tests.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Target event is concrete (not interpretive) and testable after the fact | Y/N |
| Warning window is stated and appropriate to the decision context | Y/N |
| At least 3 distinct causal pathways are identified | Y/N |
| Each candidate indicator has a definition (not just a name) | Y/N |
| Each indicator has a specified source, frequency, and baseline | Y/N |
| Thresholds are set on precursors, not on the event itself | Y/N |
| Confirmation rule (how many indicators + how long) is explicit | Y/N |
| Historical backtest on ≥3 past cases is documented | Y/N |
| False positive rate is estimated and acceptable | Y/N |
| At least one failure mode is identified and recorded | Y/N |

## Red Flags

- All indicators are lagging (they spike *after* the event or simultaneously). A true warning system needs leads, not coincidences.
- The threshold is set so permissively that the indicator flips constantly (false positive rate >30%). You have noise, not a warning.
- Thresholds were chosen by intuition ("it just feels right") rather than tested against historical data.
- The indicator set is very long (>15 indicators) with no confirmation rule. You are building a system that will alarm constantly and be ignored.
- No candidate indicators exist for one or more of the causal pathways. You have blind spots you haven't acknowledged.
- Backtest is skipped or retroactively invented. A warning system that is not tested on the past has not been tested.
- The target event is defined in terms of a predicted outcome ("the market will crash because earnings will fall") rather than the event itself ("market index falls >20% in 30 days"). This confuses prediction with warning.

## Output Format

```
## Indicators & Warnings System

**Target Event:**
<one sentence, testable>

**Warning Window:**
<time range required before event>

### Causal Pathways
1. <A → B → C → Event>
2. <X → Y → Event>
3. ...

### Candidate Indicators by Pathway

| Pathway | Node | Candidate Indicator | Definition | Source | Frequency | Baseline |
|---|---|---|---|---|---|---|
| 1 | A | <name> | <precise definition> | <source> | <frequency> | <baseline/variance> |

### Thresholds & Confirmation Rule
**Yellow Alert:** <indicator1 AND/OR indicator2 threshold> for <duration>
**Orange Alert:** <higher bar>
**Red Alert:** <highest bar>

### Backtest Results
| Past Event / Near-Miss | Date | Indicators That Signaled | Days Before Event | Indicators That Failed | Notes |
|---|---|---|---|---|---|
| <case> | <date> | <list> | <N days> | <list> | <...> |

### Historical False Positive Rate
<rate>% over <period>. Acceptable? Yes/No. Mitigation: <...>

### Identified Blind Spots
1. <failure mode>
2. <failure mode>

### Confidence
<high | medium | low> — <justification rooted in backtest quality, data availability, pathway completeness, and false positive rate>
```
```
