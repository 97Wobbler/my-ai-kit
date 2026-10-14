# Folio shared contract (schema 1)

Folio is a skill-first reporting workflow. The agent owns interpretation and
original-source review; the Python tool owns deterministic references, CSV count
calculation, revision binding and output. A passing check is not semantic proof.

## Workspace bundle

Create `folio-report/bundle.json` (or another user-work directory) outside the
plugin. Preserve originals. The JSON contains readable Markdown report prose;
an optional `report.md` working copy is fine, but synchronize it explicitly into
`report` before checking or output. `bundle.json` is authoritative for a build.
No DB, task engine, server or obligatory dependency on other plugins.

```json
{
  "schema_version": 1,
  "title": "",
  "purpose": "Question and intended reader",
  "context": [{"text": "User-supplied background", "provenance": "user"}],
  "sources": [],
  "evidence": [],
  "claims": [],
  "report": "Free-form Markdown; citation syntax: [@E1]",
  "verification": null,
  "sharing": {"include_sources": []}
}
```

Source/evidence/claim IDs start with a letter and use letters, digits, `_`, `-`.
Display numbers are generated in report citation order; IDs remain stable on
reordering. IDs are bundle-local, not a global identity system.

## Sources and locators

`add-source` reads UTF-8 text/Markdown/canonical transcript or CSV with unique
headers. It does not transcribe audio. CSV `r2` means the first response (header
is row 1); fields and row identities are preserved, including missing-response
values. Text `l12` means physical line 12; heading and observed timestamp appear
in `locator`. Speakers are preserved as text and never inferred.

Each source has `id`, `title`, `origin` (portable original filename), `kind`,
`sha256` (original bytes), `snapshot_sha256`, optional private `local_path`,
optional `shared_url` (http/https), and `units` (`id`, `locator`, `text`, optional
CSV `fields`). HTML never exports `local_path`. Keep titles informative and
share-safe. Add `coverage` to describe excerpts/extraction limits; whole-input
registration uses all nonempty lines/CSV rows. Reader sees that these are
recorded snapshots, not unmodified embedded original binaries.

PDF or other format extraction may use available host tools. Preserve original
hash and true page/section location; set `kind: document`, record `coverage`,
and compute `snapshot_sha256` with `fingerprint(units)` from this script. This
does not claim a built-in PDF parser. Unsupported encoding/format is an input
issue, not a negative analytical finding.

Source refresh preserves IDs only when locators/content identity remain valid;
keep the prior bundle as history and re-extract affected evidence. The original
fingerprint detects local edits; snapshot fingerprint detects bundle mutation.
Unavailable originals are labelled, and review may explicitly use the recorded
snapshot with a stated coverage limit.

## Evidence and claims

Quote evidence:

```json
{"id":"E1","kind":"quote","source":"S1","unit":"l12",
 "quote":"Exact substring of that unit","context":"Why this passage matters"}
```

Keep surrounding units accessible, not just cherry-picked sentences. Locator
precision is mandatory; source-wide citations are insufficient for quotations.

CSV count aggregate:

```json
{"id":"E2","kind":"aggregate","source":"S2",
 "calculation":{"population":[{"column":"eligible","op":"eq","value":"yes"}],
                "match":[{"column":"preference","op":"eq","value":"chat"}]},
 "result":{"numerator":2,"denominator":3,"percent":66.6667,
           "population_units":["r2","r3","r4"],"matched_units":["r2","r3"]}}
```

Conditions are AND'd. Operators: `eq`, `ne`, `nonempty`. Population filters set
denominator/exclusions; match filters set numerator. Empty population has null
percent. `calculate` prints the authoritative result to copy into the evidence.
Do not automatically exclude unanswered cells unless that population rule is
justified. Count aggregate results include row membership, not just a percentage.

For non-count calculations use `kind: calculation`, `source`, `units` (exact
source unit IDs), `method` (reproducible formula/procedure), `result` (text or
number), and optional `context`. Skills independently recompute and document
those results; structural check only verifies traceability, not arithmetic.

Each material claim in the report is registered with `id`, `text` (exact prose
substring), `evidence` (IDs), `provenance` (`source`, `interpretation`,
`user_context`), and optional `limits`/`counterevidence`. `user_context` claims
need a `context` explanation and are not represented as respondent evidence.
Non-context claims without evidence fail. References alone do not prove support;
the verifier checks claim meaning against originals. Unregistered material claims
are a semantic coverage issue, not automatically detectable by a schema checker.

## Independent review

Run `check` to obtain current `revision`. Write review JSON:

```json
{"revision":"copy-current-revision",
 "checks":{"quotations":"Passages and adjacent context actually checked",
           "aggregates":"Population, missing answers and calculation checked",
           "claim_support":"Which claims were challenged and why supported",
           "counterevidence":"Contrary and conditional passages reviewed",
           "coverage":"Which original units were read; omissions/limits"},
 "findings":[{"target":"C1","status":"unresolved","reason":"Specific remaining ambiguity"}]}
```

Explain non-applicable checks. `record-review` binds the review to the current
revision and derives reviewed/unresolved status. Never generate these notes
without doing the described reading. Source/evidence/claim/context/prose edits
invalidate the revision. Layout, output format and inclusion changes do not
pretend to change semantic facts; each output is still rebuilt and checked.

## Sharing and rendering

`sharing.include_sources` selects source snapshots embedded in HTML. The report
and evidence descriptions are always included; nonembedded originals retain
their identity/location and availability trail. Inclusion is never permission
to disclose extra private material: inspect requested audience and anonymization
before selecting snapshots. Anonymize a separate derivative with traceable
mapping; do not falsify an exact quote silently.

HTML contains report/material tabs, citation previews, evidence detail, exact
unit navigation and return. It has no required fetch/CDN/font/server. Markdown
footnotes identify documents and positions, show support and optional shared
URLs; absence of an attached original is explicit. A shared URL is not a grant
of recipient access. Local-only paths cannot be the sole recipient source trail.

Formal shell mode has no analytical headings. Titles/headings/report prose are
user/analysis content, never baked into the viewer. Supported HTML prose is
headings, paragraphs, lists, tables, blockquotes, fenced/inline code, bold and
safe links. Raw HTML is displayed as text, not executed. Markdown prose is
preserved apart from citation replacement and removal of unusable local links.

## Commands

Resolve `<package>` from loaded skill; requires Python 3 standard library only.

```sh
python3 <package>/scripts/folio.py init <work>/bundle.json --title "Report title"
python3 <package>/scripts/folio.py add-source <work>/bundle.json input.csv --id S1
python3 <package>/scripts/folio.py check <work>/bundle.json --check-originals
python3 <package>/scripts/folio.py calculate <work>/bundle.json E2
python3 <package>/scripts/folio.py record-review <work>/bundle.json <work>/review.json
python3 <package>/scripts/folio.py render <work>/bundle.json report.html --format html
python3 <package>/scripts/folio.py render <work>/bundle.json report.md --format md
python3 <package>/scripts/folio.py shell empty.html --format html
python3 <package>/scripts/folio.py shell empty.md --format md
```

Outputs refuse overwrites by default. `render --force` is for explicitly
authorized replacement only. Source registration/review update only the designated
bundle; output bundle atomic writes prevent half-written JSON. Original files are
never modified by these commands. CLI exit 1 is failed check, 2 is invalid input
or runtime failure. Check warnings and review status remain distinct from errors.
