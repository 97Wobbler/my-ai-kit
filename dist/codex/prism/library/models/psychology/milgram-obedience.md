---
name: milgram-obedience
display_name: Milgram Obedience
class: model
underlying_class: native
domain: psychology
source: Stanley Milgram, "Behavioral Study of Obedience," Journal of Abnormal and Social Psychology, 1963; extended in Obedience to Authority (1974)
best_for:
  - Explaining and predicting when individuals override personal moral judgment to comply with authority commands
  - Understanding conditions that amplify or attenuate obedience in hierarchical or institutional settings
one_liner: "Authority presence and legitimacy, psychological distance, graduated commitment, and diffusion of responsibility determine obedience to harmful directives."
---

# Milgram Obedience

## Overview

The Milgram Obedience model claims that ordinary individuals will inflict harm on an innocent person when directed to do so by an authority figure perceived as legitimate and responsible for the consequences. The model is **descriptive and predictive**: it explains *why* obedience occurs despite conflicting personal values, and predicts the conditions under which it will rise or fall. The central insight is that obedience is not primarily a personality trait or moral failure but a **structural outcome** driven by specific features of the authority relationship, social positioning, and task structure. Applying the model to a concrete scenario requires mapping the input's variables onto the model's drivers and reading off the predicted obedience probability.

## Core Variables and Relationships

1. **Perceived legitimacy and authority of the command source** — higher legitimacy → higher obedience.
   - Institutional affiliation (scientific, military, medical, corporate)
   - Credentials and expertise signaled by the authority
   - Formal role (experimenter, commander, manager vs. peer)
   - Appearance of competence and control
   - Pre-established social contract (e.g., "you agreed to participate in a study")

2. **Proximity and presence of the authority figure** — greater presence → higher obedience.
   - Physical proximity (in the same room vs. remote)
   - Visual contact (can the authority see you comply / disobey?)
   - Ability of the authority to monitor and reinforce compliance
   - Distance from the harm-doer to the victim (greater distance → higher obedience)

3. **Graduated commitment and task structure** — incremental steps → higher obedience.
   - Initial requests are small and seemingly harmless
   - Escalation is gradual (15V → 30V → 450V in Milgram's paradigm)
   - Each step is framed as a necessary part of the procedure, not optional
   - Psychological momentum — sunk cost of prior compliance
   - Framing of the task as scientific, necessary, or for a greater good

4. **Diffusion of responsibility** — unclear accountability → higher obedience.
   - Authority figure claims responsibility ("I take full responsibility")
   - Harm is mediated (not direct; through a machine, proxy, or impersonal process)
   - Decision appears shared or delegated ("the experiment requires this")
   - Role clarity obscures personal agency ("you are following protocol")

5. **Nature and salience of the harm** — abstract or invisible harm → higher obedience.
   - Auditory vs. visual feedback from the victim (screams are harder to ignore than silence)
   - Physical proximity to the victim (touching vs. distant)
   - Explicit clarity of harm (clear injury vs. ambiguous effects)
   - Victim's status or perceived legitimacy (are they a deserving subject?)

6. **Presence and voice of the victim** — victim objection → lower obedience.
   - Victim can be heard or seen protesting
   - Victim can demand to be released
   - Victim's expressions of pain or refusal are salient and direct

The composite obedience probability rises as: (legitimacy + authority presence + graduated commitment + diffusion of responsibility) and falls as (harm salience + victim proximity + victim objections). When the authority is clearly legitimate and present, the task is framed as necessary and graduated, and harm is mediated and distant, obedience rates are typically 65%+ even to clearly dangerous commands. When any of these factors is removed or reversed — especially when the victim is proximate and vocal — obedience drops sharply (to <10% in extreme reversals).

## Key Predictions

- **Baseline obedience is high (65%+) when the authority is institutional, proximate, and the task is framed as graduated and necessary.** Most subjects will administer maximum shock to an innocent person under these conditions, despite verbal distress. Personality traits, gender, and self-reported moral convictions are weak predictors.

- **Obedience drops dramatically (to <10%) when the victim is physically proximate, audibly protesting, and explicitly demanding to be released.** Hearing the victim's voice becomes a competing authority that overwhelms the experimental authority.

- **Graduated commitment is load-bearing.** If the first request is to administer 450V directly with no graduated steps, obedience collapses. Small initial commitments create psychological momentum and obscure the eventual magnitude of harm.

- **Authority presence matters more than authority legitimacy.** A telephone command from the same experimenter drops obedience significantly (to ~20%), even though the authority's legitimacy is identical. Physical presence is the dominant driver.

- **Diffusion of responsibility through mediating the harm (using a machine, proxy, or delegation) increases obedience substantially.** Subjects will obey more readily when they deliver shock via a button or lever than when required to inflict direct physical contact.

- **When two authorities conflict (the experimenter says "continue" and the victim says "stop"), obedience shifts to the victim.** The authority relationship is unstable when competing voices are present; proximity and salience determine which is heeded.

## Application Procedure

Instantiate the model against a concrete hierarchical scenario where an individual is pressured to act against their stated values or conscience.

1. **Define the scenario and participants precisely.** Who is the authority? Who is the subordinate (the potential harm-doer)? Who is the victim? What is the directive? What is the harm or moral cost of compliance?

2. **Assess the legitimacy and institutional framing of the authority.**
   - Is the authority embedded in a recognized institution (military, corporation, medical, research)?
   - Do they have visible credentials, titles, or role authority?
   - Is there a pre-established social contract or agreement to follow instructions?
   - Score: High / Medium / Low legitimacy.

3. **Assess the proximity and presence of the authority.**
   - Is the authority physically present or remote (phone, email, written order)?
   - Can the authority monitor compliance directly?
   - Can the authority reinforce or sanction non-compliance?
   - Score: High / Medium / Low presence.

4. **Assess the task structure and commitment gradient.**
   - Are requests graduated (small → large) or immediate and stark?
   - Is the harm framed as necessary, temporary, or part of a larger procedure?
   - Has the subordinate already complied with smaller or morally neutral requests?
   - Is there a sunk-cost dynamic (prior steps that make reversal costly)?
   - Score: High / Medium / Low graduated commitment.

5. **Assess responsibility diffusion.**
   - Does the authority claim explicit responsibility ("I take full responsibility")?
   - Is the harm mediated (machine, proxy, bureaucratic process) or direct?
   - Is the subordinate's role framed as mechanical or procedural rather than volitional?
   - Score: High / Medium / Low diffusion.

6. **Assess the salience and proximity of the harm.**
   - Is the victim visible, audible, or abstract?
   - Is the subordinate in physical contact with the victim or separated?
   - Is the harm's reality and severity salient and unmistakable, or plausible but unverified?
   - Score: High / Medium / Low harm salience.

7. **Assess victim objections and voice.**
   - Can the victim protest, demand release, or withdraw consent?
   - Are victim objections heard and salient, or absent / suppressed?
   - Can the victim's voice compete with the authority's voice?
   - Score: Strong / Weak / Absent victim voice.

8. **Composite obedience prediction.** Map the six variables onto the composite formula (qualitatively):
   - Obedience likelihood = f(legitimacy, authority presence, graduated commitment, responsibility diffusion) − harm salience − victim voice.
   - Estimate as High / Medium / Low obedience probability.

9. **Check boundary conditions** (below). Flag any that apply.

## Boundary Conditions

The Milgram model was developed in a specific historical, cultural, and institutional context (1960s American research laboratory) and breaks down or becomes partial under several conditions:

- **High moral salience and pre-commitment.** Milgram's subjects were surprised by the escalation of harm; they had not explicitly pre-committed to obeying an order to inflict maximum pain. In contexts where the harm is **known and salient from the start**, and the subordinate has made a public moral stand against it, obedience drops sharply regardless of authority pressure. The model assumes the subject is somewhat deceived or has not explicitly confronted the moral choice.

- **Peer or group dissent.** Milgram's design isolated the subordinate; a single confederate who refused to obey dropped the obedience rate from ~65% to ~10%. In real hierarchies with visible peer resistance, conformity to the authority is undermined. The model applies to isolated individuals; group dynamics require separate analysis.

- **Cultural and institutional context variation.** Obedience rates vary substantially across cultures and time periods (Kilham & Mann's 1974 Australian replication showed lower obedience; later replications in some contexts show lower rates). The model is most predictive in individualistic Western institutional contexts with clear status hierarchies. In cultures with different concepts of authority, obligation, or moral individualism, the weights may shift.

- **Personal relationship or accountability to the victim.** Milgram's victim was a stranger; the subordinate bore no prior relationship and no fear of reciprocal harm. When the subordinate has personal stakes (relationship, reputation, future interaction) with the victim, or when they believe the victim can later retaliate or judge them, obedience is further reduced. The model treats the victim as abstract; real relationships complicate it.

- **Explicit legal or professional codes.** In contexts where the subordinate has been trained in a professional code (medical ethics, military law, law enforcement standards) that explicitly forbids harm or mandates disobedience to unlawful orders, the authority's legitimacy is undermined. The model assumes the subordinate has no competing authority or formal obligation; trained professionals with explicit codes are more resistant.

- **Self-awareness of the Milgram finding itself.** Subjects tested after widespread knowledge of Milgram's results show lower obedience, suggesting the model's predictions erode with public awareness. This is a meta-boundary: the model predicts behavior under a condition of naïveté; once the naïveté is public, the condition dissolves.

## Output Format

```
## Milgram Obedience Analysis: <scenario name>

**Scenario:** <authority, subordinate, victim, directive, moral cost — one sentence>

### Variable assessment

| Variable | Level | Evidence |
|---|---|---|
| Authority legitimacy | H/M/L | <institutional affiliation, credentials, pre-established contract> |
| Authority presence | H/M/L | <physical proximity, monitoring capacity> |
| Graduated commitment | H/M/L | <step size, framing, sunk cost, psychological momentum> |
| Responsibility diffusion | H/M/L | <authority's claim to responsibility, harm mediation, role framing> |
| Harm salience | H/M/L | <victim visibility, contact, clarity of harm> |
| Victim voice | Strong/Weak/Absent | <can victim protest, demand release, override authority> |

### Composite prediction
- **Obedience probability:** High / Medium / Low
- **Load-bearing variables:** <which 1–2 variables are driving the prediction>
- **Fragility:** <which single variable, if shifted, would most change the prediction>

### Scenario variations
<if relevant, note how obedience would change if one variable were altered — e.g., "If the victim were proximate and audible, obedience would drop to Low">

### Boundary-condition check
<which boundary conditions apply and whether the prediction is still robust>

### Confidence: high | medium | low
<reasoning: clarity of variable values + fit to boundary conditions + whether the scenario matches Milgram's context (isolated subject, surprised by escalation, no pre-commitment)>
```
