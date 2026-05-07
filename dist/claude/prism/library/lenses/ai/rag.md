---
name: rag
display_name: Retrieval-Augmented Generation
class: lens
underlying_class: native
domain: ai
source: Lewis et al. (2020, Meta); operationalized in production LLM systems (OpenAI, Anthropic, 2023–2024)
best_for:
  - Auditing LLM outputs for factual grounding and source attribution
  - Diagnosing hallucination in knowledge-dependent tasks
  - Evaluating whether retrieval pipeline is actually informing generation
one_liner: "Retrieval-augmented generation — ground LLM answers in external documents for accuracy and traceability."
---

# Retrieval-Augmented Generation

## Overview
RAG systems supplement large language model generation with real-time document retrieval, intending to reduce hallucination and ground responses in external sources. This lens audits the pipeline to verify that retrieval is actually being used, that retrieved documents are relevant, and that the final output faithfully reflects what the sources say rather than drifting into invention. Practitioners use it when a RAG system produces confident-sounding but unsourced claims, when retrieval metrics look good but user-facing output feels unreliable, or when debugging why a retrieval-augmented model performs worse than the base model.

## Analytical Procedure

### Phase 1 — Instrumentation

1. **Capture the full pipeline state.** For a single user query:
   - Record the exact input prompt.
   - Log all documents retrieved (rank, score/relevance, full text).
   - Log the retriever's intermediate representations (e.g., embeddings, query reformulations).
   - Capture the LLM's input (the retrieval-augmented prompt shown to the model).
   - Capture the LLM's raw output (before any post-processing or filtering).
   - Capture any final output shown to the user.

2. **Identify the factual claims in the LLM output.** Read the response and extract every assertion about the world:
   - Bad extraction: "The system said something about climate."
   - Good extraction: "The response asserts that global temperature rose 1.1°C since 1850."
   Extract at least 3–5 claims, prioritizing ones that are specific, quantitative, or attributed to named entities or events.

3. **For each claim, determine its source.** Mark each claim as one of:
   - **In retrieved docs**: The claim appears verbatim or as a direct paraphrase in at least one document.
   - **Inferable from retrieved docs**: The claim requires synthesis across multiple retrieved documents but does not require external knowledge.
   - **Partially supported**: Only part of the claim is in the retrieved docs; the rest is inference or hallucination.
   - **Not in retrieved docs**: The claim does not appear in any retrieved document.
   - **Contradicted by retrieved docs**: The claim conflicts with what was retrieved.

### Phase 2 — Retrieval Quality Check

4. **Assess retrieval relevance.** For each of the top 5 retrieved documents, rate its relevance to the user query:
   - **Directly relevant**: Answers the query or provides information the query asks for.
   - **Tangentially relevant**: Related to the query topic but does not directly address the question.
   - **Irrelevant**: No clear connection to the query.

   Calculate the ratio of Directly Relevant documents in the top 5. A healthy RAG system should have ≥60% directly relevant documents in the top 5.

5. **Check for retrieval collapse.** Are all top 5 documents from the same source, time period, or author? If yes, the retriever may be over-clustering and missing diverse viewpoints. Note this.

6. **Verify that retrieval changed the output.** Re-run the same query against the base LLM (without retrieval) if possible. Compare:
   - Does the retrieved-augmented response cite or reference sources that the base model didn't mention?
   - Does the retrieved-augmented response include facts not present in the base model's output?
   - If both outputs are nearly identical, retrieval had no effect — flag this as a pipeline failure.

### Phase 3 — Faithfulness Analysis

7. **For each claim marked "In retrieved docs" or "Inferable," verify the inference path.** Trace how the LLM derived the claim from the documents:
   - Is the claim a verbatim excerpt? (High confidence in faithfulness.)
   - Is the claim a paraphrase that preserves meaning? (Medium confidence — check for semantic drift.)
   - Is the claim synthesized from multiple documents? (Medium-low confidence — check whether the synthesis is sound or whether the model invented a connection.)
   - Is the claim inferred using world knowledge (not in the docs)? (Low confidence — mark as hybrid.)

8. **For claims marked "Not in retrieved docs" or "Contradicted," investigate the origin.**
   - Is this a fact the base model would know (within its training data cutoff)?
   - Is this a hallucination specific to the retrieval-augmented setup (e.g., the model falsely cited a document)?
   - Is this a pre-training artifact (the model defaulted to its learned patterns when retrieval failed)?

### Phase 4 — Attribution and Usability

9. **Check explicit source attribution.** Does the LLM output:
   - Cite document titles, URLs, or author names?
   - Provide quotations with page numbers or section references?
   - Use citation syntax (e.g., "[1]", "[source]") that a user can verify?
   - If not, mark as "No attribution." If yes, verify that citations are accurate — the cited source must actually contain the claim.

10. **Assess end-user verifiability.** Can a user click through or look up the source to verify the claim?
    - Easy: Citations include URL and are clickable.
    - Medium: Citations are present but require manual lookup.
    - Hard: Claims are supported but not cited; user would need to re-run retrieval to verify.
    - Impossible: Claims are not grounded in provided sources.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All pipeline states (query, retrieval, prompt, output) are logged | Y/N |
| At least 3 distinct factual claims extracted from the output | Y/N |
| Each claim is tagged: In docs / Inferable / Partial / Not in docs / Contradicted | Y/N |
| Top-5 retrieval relevance is calculated (≥60% directly relevant) | Y/N |
| Retrieval collapse check performed (diversity of sources assessed) | Y/N |
| Retrieved-augmented output is compared to base model output | Y/N |
| Each non-doc claim is investigated for origin (training artifact vs. hallucination) | Y/N |
| Attribution check completed (citations present and verifiable) | Y/N |

## Red Flags

- All claims are marked "In retrieved docs" and every top-5 document is rated "Directly relevant." This suggests either cherry-picked examples or an overly lenient evaluation. Re-run on a harder query or a failure case.
- Claims marked "Inferable from docs" but the inference path is opaque — the model connected dots in a way that is not reconstructible from the source material.
- Retrieval and base model outputs are identical. The retrieval pipeline is not affecting generation; investigate whether the retriever is working or whether the prompt is ignoring the documents.
- High citation density but citations are generic ("According to the documents...") and do not point to specific sources.
- Contradicted claims: The output states X, but the retrieved document clearly states not-X. This is a hard failure of the pipeline.
- No diversity in retrieved sources (all from one domain, author, or time period). The retriever is not exploring the full knowledge base.

## Output Format

```
## RAG Audit Report

**Query:**
> <user input>

**Retrieval Summary:**
- Documents retrieved: <count>
- Top-5 directly relevant: <N/5>
- Retrieval collapse: Yes / No
- [If yes, note the clustering pattern]

**Factual Claims Analysis:**
| Claim | Source Status | Citation Present | Verifiable |
|---|---|---|---|
| <claim 1> | In docs / Inferable / Partial / Not in docs / Contradicted | Y/N | Y/N |
| <claim 2> | <...> | <...> | <...> |
| <claim 3> | <...> | <...> | <...> |

**Faithfulness Assessment:**
- Claims in docs: <N> (high confidence)
- Claims inferable: <N> (medium confidence; synthesis path: <brief description>)
- Claims not in docs: <N> (origin: training artifact / hallucination / hybrid)
- Claims contradicted: <N> (FAILURE)

**Attribution Quality:**
- Explicit citations: Yes / No
- Citation format: <verbatim/URL/metadata/other>
- User verifiability: Easy / Medium / Hard / Impossible

**Comparison to Base Model:**
- Retrieved-augmented output differs from base model: Yes / No
- Key differences: <list or "none">

**Pipeline Status:**
- Retrieval is active and informing generation: Yes / No
- Retrieved documents are relevant: Yes / Partial / No
- Output faithfully reflects sources: Yes / Partial / No

**Confidence:**
<high | medium | low> — <justification. E.g., "high: all claims grounded, citations verifiable, retrieval diversity confirmed"; "low: output contradicts retrieval, unclear inference paths, no citations">
```
