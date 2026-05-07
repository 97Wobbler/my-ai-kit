---
name: dread
display_name: DREAD Risk Rating
class: lens
underlying_class: native
domain: security
source: Microsoft Security Engineering Center, circa 2005
best_for:
  - Rating threats to software features during design and threat modeling
  - Comparing relative risk across multiple attack vectors
  - Structuring security discussions with technical and non-technical stakeholders
one_liner: "Score software threats across five elements — Damage, Reproducibility, Exploitability, Affected users, Discoverability."
---

# DREAD Risk Rating

## Overview
DREAD is a five-factor scoring method that converts qualitative threat descriptions into numerical risk ratings. It rates each identified threat across Damage, Reproducibility, Exploitability, Affected Users, and Discoverability — each on a scale of 1–10 — then averages them to produce a single comparable score. Practitioners use it during threat modeling to prioritize which threats deserve mitigation investment first and to make risk conversations explicit and reproducible rather than intuitive.

## Analytical Procedure

### Phase 1 — Identify the Threat

1. **State the threat in one sentence.** Describe what an attacker does and what they access or corrupt. Example: "An unauthenticated user sends a crafted XML payload to the API endpoint, bypassing input validation and reading arbitrary database records."

2. **Identify the attack surface.** Where does the threat originate — network, local, physical? How must an attacker position themselves?

3. **Confirm the threat is *possible*, not hypothetical.** Can you sketch a plausible exploit path with current technology? If it requires, say, quantum computing or a zero-day in the OS kernel, defer it to a lower-priority threat log.

### Phase 2 — Score the Five Factors

4. **Score Damage (1–10).** If the threat succeeds, how bad is the outcome?
   - 1–2: Logging information is disclosed.
   - 3–4: Application crash or single user data corrupted.
   - 5–6: Multiple users' data corrupted; application becomes unreliable.
   - 7–8: User authentication bypassed; sensitive data of many users exposed.
   - 9–10: Complete system compromise; attacker gains admin or can corrupt all data.

5. **Score Reproducibility (1–10).** How easy is it for an attacker to reliably trigger the threat?
   - 1–2: Exploit is unreliable; requires very specific conditions or luck.
   - 3–4: Exploit works most of the time but requires specific user action or network state.
   - 5–6: Exploit works consistently if the attacker knows the right inputs.
   - 7–8: Exploit works on most deployments; few configuration variations break it.
   - 9–10: Exploit works on all versions or deployments; no special conditions needed.

6. **Score Exploitability (1–10).** How much skill and effort does the exploit require?
   - 1–2: Requires strong cryptography knowledge, reverse engineering, and weeks of work.
   - 3–4: Requires programming knowledge and specialized tools; days to weeks of work.
   - 5–6: Requires basic programming and moderate effort; a few hours to days.
   - 7–8: Straightforward attack using common tools; an hour or two.
   - 9–10: Trivial; a script or web form submission.

7. **Score Affected Users (1–10).** What percentage of your user base can be harmed by this threat?
   - 1–2: <1% — a few privileged users or edge cases.
   - 3–4: 1–10% — a specific user role or demographic.
   - 5–6: 10–50% — a substantial portion of the user base.
   - 7–8: 50–90% — most users.
   - 9–10: 90–100% — every user or the system as a whole.

8. **Score Discoverability (1–10).** How easily can an attacker find this threat?
   - 1–2: Requires detailed system knowledge or security research; not public.
   - 3–4: Requires reverse engineering or source code access.
   - 5–6: Discoverable through testing or code review; documented in internal discussions.
   - 7–8: Obvious to anyone reading the code or testing the feature; warned about in forums or documentation.
   - 9–10: Public knowledge; published CVE, PoC available, documented in threat databases.

### Phase 3 — Calculate and Rank

9. **Compute the DREAD score:** Add the five factor scores and divide by 5. This yields a number from 1 to 10.

10. **Compare against your threat list.** If you have multiple threats, sort them by DREAD score (highest first). Threats scoring 7–10 are critical; 5–6 are moderate; below 5 are low priority.

11. **Document borderline disagreements.** If two reviewers score a factor differently by more than 2 points, note the delta and the reason. These often reveal unstated assumptions about your deployment environment.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Threat statement includes attacker action and target (not just "bad thing happens") | Y/N |
| All five factors are scored; no factor is left blank | Y/N |
| Each factor score is justified with a one-line note (e.g., "Damage: 8 — user credentials exposed") | Y/N |
| Scores are consistent with definitions (e.g., Exploitability of 2 truly does require cryptography expertise) | Y/N |
| If multiple reviewers scored, their disagreements (>2 point delta) are logged | Y/N |
| Final DREAD score is arithmetically correct | Y/N |

## Red Flags

- All five factor scores are identical or nearly identical. This suggests the reviewer scored the overall severity of the threat rather than each factor independently.
- Damage and Affected Users together account for most of the score, while Reproducibility and Exploitability are low. This often means the threat is scary-sounding but actually hard to execute; re-examine whether resources should be spent on it.
- Discoverability is 1–2 but Exploitability is 9–10. This is internally inconsistent — if the threat is trivial to exploit, attackers will find it. Recheck the scoring.
- DREAD score is used as a binary pass/fail gate ("Mitigate only if >7") rather than a ranking. The score is ordinal, not absolute; use it to prioritize work, not to declare threats acceptable or unacceptable.
- A threat is omitted because "everyone knows about it." Unknown threats often score highest. Discoverability being high does not exempt it from the list.

## Output Format

```
## DREAD Assessment

**Threat:**
<Statement: what the attacker does and what they access/corrupt.>

**Attack Surface:**
<Network / Local / Physical — and positioning required.>

### Factor Scores

| Factor | Score | Justification |
|---|---|---|
| Damage | _ / 10 | <one-line reason> |
| Reproducibility | _ / 10 | <one-line reason> |
| Exploitability | _ / 10 | <one-line reason> |
| Affected Users | _ / 10 | <one-line reason> |
| Discoverability | _ / 10 | <one-line reason> |

### DREAD Score
**(<damage> + <reproducibility> + <exploitability> + <affected users> + <discoverability>) / 5 = <score> / 10**

### Risk Tier
[ ] Critical (8–10)  |  [ ] Moderate (5–7)  |  [ ] Low (1–4)

### Mitigation Priority
<Explain why this threat ranks above or below other threats on your threat list.>

### Reviewer Notes
<If multiple reviewers: log any factor disagreements >2 points and the reason.>

### Confidence
<high | medium | low> — <justification based on consensus among reviewers and alignment of scores with definitions>
```
