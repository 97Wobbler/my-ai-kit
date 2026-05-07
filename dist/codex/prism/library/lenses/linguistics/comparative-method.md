---
name: comparative-method
display_name: Comparative Method
class: lens
underlying_class: native
domain: linguistics
source: Rasmus Rask (1818); systematized by Franz Bopp (1816) and August Schleicher; foundational to historical linguistics
best_for:
  - Reconstructing proto-language sound systems from attested descendant languages
  - Establishing genetic relationships between languages
  - Dating language divergence and identifying sound change patterns
one_liner: "Reconstruct proto-language phonology by tracing regular sound correspondences across related languages."
---

# Comparative Method

## Overview
The Comparative Method reconstructs the sound system of an ancestral language by identifying regular sound correspondences across its descendant languages. Rather than assuming a single ancestor and working backward (which risks circular reasoning), the method compares attested forms across multiple languages to extract the pattern of change that explains all variants simultaneously. Linguists reach for this when they need to establish whether languages share a common origin, determine the chronology of sound changes, or recover phonological features lost in modern speech but preserved in writing or cognate sets.

## Analytical Procedure

### Phase 1 — Assemble the Cognate Set

1. **Select a semantic domain.** Choose a concept (e.g., "water," "hand," "go") that is likely to be cognate across all candidate languages. Avoid borrowed terms, which obscure the ancestral sound pattern. Establish a list of ≥3 languages to compare.

2. **Collect the attested forms.** For each language, record the modern phonetic form and its orthographic representation side by side. Note the source (dictionary, corpus, native speaker elicitation). For each form, note:
   - Language and dialect
   - Phonetic transcription (IPA)
   - Morpheme boundaries (if multi-morphemic)
   - Meaning and semantic drift (if any)

3. **Verify cognacy by inspection.** Do the forms resemble each other? Are they unlikely to be borrowings from a shared source language (e.g., Latin in Romance languages)? Create a preliminary cognate set. Mark any forms you exclude and why.

### Phase 2 — Identify Sound Correspondences

4. **Align the cognate forms phoneme-by-phoneme.** Segment each form into its constituent sounds. Lay them out in a matrix so that corresponding positions align vertically:

   | Position | Language A | Language B | Language C |
   |---|---|---|---|
   | 1 (onset) | p | p | p |
   | 2 (nucleus) | a | a | a |
   | 3 (coda) | x | k | k |

5. **For each position, identify the correspondence pattern.** A correspondence is the set of sounds that appear in the same position across languages. For the coda above, the pattern is: x (in A) ~ k (in B) ~ k (in C).

6. **List all unique correspondences** extracted from the cognate set. Each correspondence is a ratio: Sound-in-A : Sound-in-B : Sound-in-C. Example: **p:p:p, a:a:a, x:k:k**.

7. **Check for consistency.** If the same correspondence ratio appears elsewhere in your data (e.g., x:k in another cognate set), mark it as a confirmed correspondence. If a sound pair appears in one position but not another, note the exception — it may signal a merger, split, or non-cognacy.

### Phase 3 — Apply Regularity Constraints

8. **Require that each correspondence be regular across all cognate sets.** A regular correspondence must hold the same in every cognate pair where those sounds appear in the same position. If x:k appears as a correspondence in position 3 of one cognate set, it must appear in position 3 of all cognate sets with x in Language A and k in Languages B or C at that position.

9. **Investigate irregularities.** If a cognate set breaks the correspondence pattern, decide:
   - **Non-cognacy.** The word in one language is borrowed or semantically drifted. Exclude it.
   - **Sound change exception.** The word underwent a secondary sound change not affecting others (e.g., assimilation before a certain sound). Document the environment.
   - **Merger or split.** One language underwent a phonological merger or split after the split from the ancestor. Note the merger/split event.

10. **Build a correspondence table.** Rows are "correspondences" (the ratios); columns are the language pairs being compared. Mark each correspondence as **regular** (appears consistently), **conditioned** (regular only in specific phonological environments), or **irregular** (appears in one or two cases without explanation).

    | Correspondence | A:B | A:C | B:C | Regularity |
    |---|---|---|---|---|
    | p:p | ✓ | ✓ | ✓ | Regular |
    | x:k | ✓ | ✓ | ✓ | Regular |
    | ŋ:n | ✓ | ✗ | ✗ | Conditioned (before velars in A) |

### Phase 4 — Reconstruct the Proto-Sound

11. **For each correspondence, identify the most likely proto-sound.** Apply the following heuristics in order:
    - **Majority principle.** If a sound appears in 2+ descendant languages, it is a good candidate for the proto-form (sound change is often reductive).
    - **Phonological naturalness.** Prefer proto-sounds that undergo natural sound changes (e.g., p→f, t→s) rather than unnatural reversals.
    - **Typological plausibility.** Does the reconstructed phoneme fit the phonological inventory of the proto-language? (e.g., if all other obstruents are voiceless stops, a voiced fricative is less likely.)
    - **Distributional evidence.** If the proto-sound leaves traces in allomorphic variation or morphological rules, that supports the reconstruction.

12. **Write the proto-form phoneme-by-phoneme.** Denote reconstructed phonemes with an asterisk (e.g., *pat-wa "water"). Indicate confidence: *pat-wa (high), *pət-wa (medium, nucleus vowel uncertain), *pat-? (low, coda lost in all daughters).

### Phase 5 — Document Sound Changes

13. **For each daughter language, list the sound changes that separate it from the proto-language.** Order them chronologically if possible (using stratigraphy or other internal evidence). Example:
    - Proto-Indo-European *p → Grimm's Law: /f/ in Proto-Germanic
    - Proto-Germanic /f/ → /∅/ (word-finally) in Old English

14. **Verify that the reconstructed proto-forms, when the proposed sound changes are applied, yield the attested modern forms.** If they don't, revise either the reconstruction or the sound change hypothesis.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Cognate set contains ≥3 languages with plausible semantic matches | Y/N |
| No borrowings or obvious non-cognates remain in the set | Y/N |
| Sound correspondences are extracted and listed for every position | Y/N |
| Each correspondence is checked for regularity across all cognate pairs | Y/N |
| Irregularities are investigated and explained or excluded | Y/N |
| Proto-sound reconstruction applies majority principle and naturalness heuristics | Y/N |
| Proto-forms are marked with asterisks and confidence levels | Y/N |
| Sound changes from proto- to each daughter language are stated explicitly | Y/N |
| Proto-forms + proposed changes derive the attested forms | Y/N |

## Red Flags

- Cognate set is small (fewer than 3 languages) or contains near-homophones that may be borrowings. Small sets lack statistical power to distinguish regular correspondences from accidents.
- Correspondence rules are stated loosely ("usually p corresponds to p") rather than as formal ratios. This permits cherry-picking.
- Irregularities are dismissed without investigation. Every non-regular correspondence must be accounted for (non-cognacy, merger, conditioned change, or genuine exception).
- Proto-forms are reconstructed without justifying which heuristic broke a tie. If three languages have three different sounds, the reconstruction method must be transparent.
- The proposed sound changes are unnatural (e.g., /f/ → /p/, which violates markedness). Proto-forms should reconstruct via changes that are typologically attested.
- No attestation of intermediate stages. If sound changes are proposed (e.g., merger of /a/ and /ə/), there is no manuscript evidence or distributional trace showing the intermediate state.
- Proto-form derives attested forms only for some daughter languages but not others, and discrepancies are ignored.

## Output Format

```
## Comparative Reconstruction

**Semantic domain:** <concept>
**Languages compared:** <list>

### Cognate Set
| Language | Form | IPA | Notes |
|---|---|---|---|
| <lang> | <orth> | <IPA> | <morphology, semantic drift, source> |

### Sound Correspondences
| Correspondence | Position | Appearance count | Regularity |
|---|---|---|---|
| <ratio> | <slot (onset/nucleus/coda)> | <n cognates> | Regular / Conditioned / Irregular |

### Correspondence Table
| Proto position | Language A | Language B | Language C | Rule type |
|---|---|---|---|---|
| 1 (onset) | p | p | p | Regular |
| 2 (nucleus) | a | a | a | Regular |
| 3 (coda) | *? | k | k | Majority principle |

### Proto-reconstruction
| Cognate set | Proto-form | Confidence | Derivation |
|---|---|---|---|
| "water" | *pat-wa | High | All attested forms derive via regular changes |
| "hand" | *ken-d(?) | Medium | *d not directly attested; assumed from C-stem variants |

### Sound Changes
**Proto-Language A:**
- *p → p (no change)
- *a → a (no change)
- *-k → -x (post-vocalic velar fricativization)

**Proto-Language B:**
- *p → p (no change)
- *a → ə (vowel reduction in unstressed position)
- *-k → -k (no change)

### Verification
Proto-forms + proposed changes applied:
- *pat-wa + (A changes) → pat-xa ✓
- *pat-wa + (B changes) → pət-wa ✓

### Irregularities and Exclusions
- <form> excluded: borrowed from <source language>
- <correspondence>: conditioned by <phonological environment>

### Confidence
<high/medium/low> — <justification: e.g., "high — all correspondences are regular, proto-forms are phonologically natural, and sound changes are typologically attested across multiple cognate sets (n≥8)."; or "medium — small cognate set (n=3), one irregularity remains unexplained, proto-nucleus is uncertain.">
```
---
