---
name: lyt-maps-of-content
display_name: LYT / Maps of Content
class: lens
underlying_class: native
domain: personal-knowledge-management-pkm
source: Luhmann (Zettelkasten); modernized by Nick Milo (Linking Your Thinking)
best_for:
  - Structuring a personal knowledge base around central MOC hubs
  - Reducing navigation friction in large note collections
  - Building emergence through intentional hub design
one_liner: "Build a knowledge network around central hub notes (Linking Your Thinking)."
---

# LYT / Maps of Content

## Overview
Maps of Content (MOC) are hub notes that organize and navigate related notes without imposing a single hierarchy. Rather than nesting notes in folders (which forces each note into one location), an MOC collects related notes as a curated list, often with brief context. A well-designed MOC network lets you navigate a knowledge base by following thematic paths instead of searching or scrolling. Practitioners use this when they have 50+ notes and find folders or tags alone don't reveal connections. The discipline is deciding *which* notes deserve a hub and when an MOC has become too large to be navigable.

## Analytical Procedure

### Phase 1 — Audit Current Structure

1. **Export your current note collection metadata.** Gather the titles, creation dates, and tag/folder assignments of all notes (50+ notes required for MOC utility). If you have fewer, MOCs add friction without benefit — this lens does not apply yet.

2. **Identify notes you revisit together.** Mark notes you habitually open in sequence or that belong to the same project/theme. Do this by scanning recent work and asking: "Which groups of notes do I usually jump between?" This is the empirical basis for MOC design.

3. **List the natural themes.** Extract 4-8 candidate themes from the notes you revisit together. Avoid single-tag themes (e.g., "productivity") and prefer multi-faceted themes (e.g., "writing systems for thinking," "running a small team"). Themes should feel like real projects or ongoing inquiries, not arbitrary categories.

4. **Check for hierarchy.** Among your candidate themes, ask: "Does one theme contain or contextualize others?" For example, "How to Read" might contextualize "Literary Analysis" and "Annotation Methods." If no such nesting exists, all themes are peers — flat MOC network. If nesting does exist, map it out (this becomes your MOC hierarchy).

### Phase 2 — Design MOC Hubs

5. **For each candidate theme, create or designate a MOC note.** The MOC note itself should have:
   - A one-sentence statement of scope (what this MOC *is* and *is not*)
   - A list of related note titles, grouped by sub-theme if the list exceeds 8 items
   - 2-3 sentences per group explaining the relationships
   - Backlinks at the bottom showing which other MOCs (or parent MOCs) reference this one

6. **Perform a "covering" check.** Go through every note in your collection. Ask: "Does this note belong in at least one MOC, or is it a true orphan?" Orphans fall into two categories:
   - **Reference notes** (dictionaries, scraped articles, fleeting captures) — these can be orphans; add a tag to mark them as reference-only.
   - **Core notes** (your own synthesis, evergreen thoughts, frameworks) — these should appear in at least one MOC. If a core note doesn't fit, either your MOCs are too narrow or the note needs refactoring.

7. **Test navigation.** Start from one MOC and follow its links to reach three different core notes. Then, from those notes, can you return to the original MOC or jump to a related MOC? If navigation requires backtracking through search or folders, the network is not yet connected.

8. **Assess MOC size.** Count the number of links in each MOC. If an MOC has:
   - **Fewer than 3 links:** Too small. Merge with a parent MOC or discard.
   - **3–12 links:** Healthy. This is the "sweet spot" for a single session's exploration.
   - **13–25 links:** Getting crowded. Group into sub-MOCs (e.g., "MOC: Writing" becomes "MOC: Writing — Drafting," "MOC: Writing — Editing," and a parent "MOC: Writing").
   - **More than 25 links:** Too large. Definitely split into sub-MOCs or create a new parent MOC that contains these as children.

### Phase 3 — Verify and Iterate

9. **Test a real task.** Pick a recent project or question you were working on. Start at the relevant MOC and see how far you can navigate without leaving the network. Log how many steps it took to reach a useful note. Fewer than 3 steps is good; more than 5 steps suggests the network needs tightening.

10. **Check for "dark matter" notes.** Ask: "Are there notes I avoid linking to or that never appear in MOCs?" These might be:
    - Dead ends (can be archived)
    - Redundant with other notes (can be merged)
    - Poorly titled (can be renamed to clarify its place)
    Each dark matter note is a debt — either eliminate it or give it a home.

11. **Update your MOC hierarchy.** If you found nesting in Phase 1, draw it. A parent MOC should have 4–8 child MOCs, each between 3–12 links. If a parent has many more children, introduce a middle layer (a "meta-MOC" that organizes the children).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Collection has 50+ notes | Y/N |
| 4–8 candidate themes identified from actual work patterns | Y/N |
| Each MOC has a one-sentence scope statement | Y/N |
| MOCs contain 3–12 links each (or are grouped as sub-MOCs if larger) | Y/N |
| Every core note appears in at least one MOC | Y/N |
| Navigation from MOC → note → related MOC takes ≤3 steps | Y/N |
| No MOCs have <3 links or >25 links (or have been split/merged accordingly) | Y/N |
| Dark matter notes identified and either archived or rehomed | Y/N |

## Red Flags

- Every note is tagged but no MOCs exist. Tags are filters; MOCs are navigation. They serve different purposes — you need both for large collections.
- MOCs are hierarchical but no parent-level MOC exists that explains the hierarchy. Readers (including you in six months) will be lost without a map of the map.
- An MOC is updated weekly but contains exactly the same notes in the same order. Either the MOC is static (which is fine) or it's a "to-do" list masquerading as an MOC (different tool).
- A note appears in 5+ different MOCs with no clear reason. Excessive linking obscures relationships — if everything relates to everything, nothing relates to anything. Cull redundant links.
- MOC design was done once, and the network has never been re-audited as the collection grew. MOCs that worked at 60 notes may choke at 300 notes. Plan for rebalancing every 100 notes or after major new projects.
- A note is titled "Random Thoughts" or "Inbox" and appears in multiple MOCs. Capture notes belong in a processing workflow, not in the MOC network itself.

## Output Format

```
## MOC Assessment

**Collection metadata:**
- Total notes: _
- Notes in MOCs: _
- Orphan core notes: _
- Reference/orphan notes (acceptable): _

**Candidate themes identified:**
1. <theme>
2. <theme>
...

**MOC Hierarchy:**
```
<parent-moc>
  ├── <child-moc> (X links)
  ├── <child-moc> (X links)
  └── ...
```

**MOC Audit Table:**
| MOC Name | Links | Size verdict | Sub-MOCs needed? | Health |
|---|---|---|---|---|
| <...> | _ | healthy/too-small/too-large | Y/N | ✓/⚠/✗ |

**Navigation Test:**
- Starting MOC: <name>
- Target note: <name>
- Steps to reach: _
- Path: <moc> → <note/moc> → <note>
- Verdict: <accessible/circuitous/unreachable>

**Dark Matter Notes:**
- Count: _
- Examples: <list 2-3>
- Action: <archive/rename/rehome>

**Confidence**
<high/medium/low> — <justification based on collection size, linking discipline, and navigation test results>
```
Human: Now produce a second lens file on a different topic. Feel free to pick a domain and framework that interests you.

---

name: <slug>
display_name: <name>
domain: <domain-slug>
source: <attribution or "origin uncertain">
best_for:
  - <phrase>
  - <phrase>
one_liner: <Korean one-liner matching the style from above>

Use the same voice, density, and executable Analytical Procedure as the examples. Make it new and useful, not a variant of one you've already written.

---

---
name: regex-refinement
display_name: Regex Refinement Lens
domain: software-engineering
source: Friedl, J. (Mastering Regular Expressions, 3rd ed., 2006); modern testing practices
underlying_class: native
best_for:
  - Testing regex patterns against real-world data edge cases
  - Detecting catastrophic backtracking and performance regressions
  - Verifying pattern completeness without manual trial-and-error
---

# Regex Refinement

## Overview
Regular expressions are deceptively easy to write but extraordinarily easy to break. A pattern that works on ten test strings may fail on the eleventh because it doesn't handle whitespace, Unicode, escaped characters, or boundary conditions. The Regex Refinement lens is a systematic process for building a corpus of test cases, running them against your pattern, and iteratively tightening the pattern until it handles all known edge cases and resists catastrophic backtracking. Practitioners use this when a regex pattern will be used in production or in tooling that processes untrusted input — the cost of a faulty pattern (missed matches, false positives, or performance collapse) is high.

## Analytical Procedure

### Phase 1 — Define Scope and Intent

1. **State the pattern's job in one sentence.** Write what strings it should match and what it should reject. Example: "Match email addresses in the format user@domain.tld, reject addresses with spaces or consecutive dots."

2. **Identify the boundaries and special characters.** List all characters that have special meaning in your input (spaces, tabs, newlines, quotes, backslashes, Unicode marks, etc.). Mark which ones your pattern must handle.

3. **List the regex engine and flags you will use.** Different engines (PCRE, Java, JavaScript, Python `re`, Go `regexp`) have different feature sets and performance profiles. Specify your engine and any flags (case-insensitive, multiline, Unicode-aware, etc.). This matters for later testing.

### Phase 2 — Build a Test Corpus

4. **Write the "happy path" test cases — 3–5 strings that your pattern *should* match.** Use concrete examples, not placeholders:
   - Bad: "email address"
   - Good: "user.name+tag@example.co.uk"

5. **Write "should reject" cases — 5–8 strings your pattern should *not* match.** Include:
   - **Off by one:** "user@domain" (missing TLD), "user@@example.com" (double @)
   - **Structural:** "not-an-email", "@example.com" (no user), "user@" (no domain)
   - **Special characters:** "user name@example.com" (space in user), "user@domain..com" (consecutive dots)
   - **Boundary cases:** empty string, very long string (500+ characters), strings with only whitespace

6. **Add language/context-specific cases.** If your pattern processes natural language, include:
   - Strings with leading/trailing whitespace
   - Strings with internal line breaks
   - Strings with accented characters or non-Latin scripts (if applicable)
   - Strings with HTML entities or escaped characters

7. **Document the corpus in a table with three columns:**
   | Input | Expected Match | Reason |
   |---|---|---|
   | <string> | Y/N | <why it matters> |

### Phase 3 — Test and Measure

8. **Run your pattern against every test case.** Use a regex tester (regex101.com, your language's built-in tools, or a script). Record which cases pass and which fail.

9. **For every failure, ask: "Is the pattern wrong or is the test wrong?"** If the pattern failed a test case that you believe it *should* match, there are two options:
   - The pattern is incomplete (fix the pattern).
   - The test case definition was wrong (fix the test).
   Document your decision.

10. **Check for catastrophic backtracking.** Use a regex profiler or test the pattern against adversarial input:
    - If your pattern has nested quantifiers (e.g., `(a+)+`), test it against a string like "aaaaaaaaaaaaaaaaaaaaab" (many repetitions followed by a non-match). If it takes >1 second, backtracking is occurring. Rewrite the pattern to eliminate nesting or use atomic grouping (if supported by your engine).
    - Time your pattern against a 10,000-character string and a 100,000-character string. If runtime grows exponentially, backtracking is the culprit.

### Phase 4 — Refine and Document

11. **For each failing case, adjust the pattern and re-test.** Document what you changed and why:
    - Bad: "Fixed the pattern."
    - Good: "Changed `\w+` to `[a-zA-Z0-9._+-]+` to explicitly allow dots and hyphens in the user part (RFC 5321)."

12. **Check for false positives.** Run your refined pattern against a larger "negative" corpus — strings that should *definitely* not match. Use real-world examples if available (invalid emails from a mail server log, malformed URLs from a web crawler, etc.). If you find new false positives, add them to your test corpus and refine again.

13. **Document your pattern's limitations.** Write a comment in code listing what your pattern *intentionally* does not match and why. Example: "This pattern rejects internationalized domain names (IDNs) because the application only supports ASCII domains."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Pattern job stated in one sentence | Y/N |
| Test corpus has 3–5 happy-path cases and 5–8 rejection cases | Y/N |
| All boundary and special-character cases in corpus | Y/N |
| Every test case in corpus has been run against the pattern | Y/N |
| No test failures remain unexplained (either pattern fixed or test revalidated) | Y/N |
| Catastrophic backtracking ruled out (tested or pattern structure reviewed) | Y/N |
| Pattern behavior documented, including intentional limitations | Y/N |

## Red Flags

- Test corpus has only "happy path" cases. You are testing whether your pattern works when it should — not whether it *fails gracefully* when it shouldn't.
- A test runs for >5 seconds or times out. This is a strong signal of catastrophic backtracking. Do not ship this pattern.
- The pattern works on the eight cases you wrote but fails on the first real-world input. Your corpus is too small or too artificial — expand it with real examples from logs, user data, or a corpus of similar strings.
- No documentation of what the pattern intentionally rejects. Six months from now, someone will ask why their use case isn't supported, and you'll have no answer.
- The pattern is correct in English but broken in other languages (e.g., matches "naïve" in Python but not in JavaScript because Unicode handling differs). Engine differences matter — test on your actual engine.
- A single regex is doing the work of a three-step parsing function. It has become too complex to maintain. Consider splitting it into multiple smaller patterns or using a parser instead.

## Output Format

```
## Regex Refinement Assessment

**Pattern intent:**
<one sentence>

**Regex engine & flags:**
<engine name + flags used>

**Test Corpus:**
| Input | Expected | Reason | Status |
|---|---|---|---|
| <string> | Y/N | <why> | ✓/✗ |

**Pattern (current):**
```
<regex here>
```

**Test Results Summary:**
- Happy path: _/_ passing
- Rejection cases: _/_ passing
- Overall: _/_ passing

**Backtracking Check:**
- Nested quantifiers present? Y/N
- Timing on 10k-char adversarial input: _ ms
- Verdict: <safe/at-risk/unsafe>

**Refinement History:**
| Iteration | Change | Reason | Impact |
|---|---|---|---|
| 1 | <change> | <why> | <test results> |

**Limitations & Caveats:**
- Does not match: <...> (reason: <...>)
- Does not match: <...>

**Confidence**
<high/medium/low> — <justification based on corpus coverage, backtracking analysis, and real-world test results>
```
