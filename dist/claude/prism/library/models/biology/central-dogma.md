---
name: central-dogma
display_name: Central Dogma (Crick)
class: model
underlying_class: native
domain: biology
source: Francis Crick, "On Protein Synthesis," Symposia of the Society for Experimental Biology, 1958; formalized in "Central Dogma of Molecular Biology," Nature, 1970
best_for:
  - Predicting the flow of genetic information through biological systems
  - Explaining how heritable mutations and environmental changes propagate to phenotype
  - Identifying where in the information pipeline a molecular defect will have phenotypic consequences
one_liner: "Genetic information flows unidirectionally DNA → RNA → protein with filtering and transformation at each step."
---

# Central Dogma (Crick)

## Overview

The Central Dogma claims that genetic information flows in a single direction: from DNA (genotype) through RNA (mRNA transcript) to protein (phenotype), and never reverse. The model is mechanistic and explanatory — it describes the molecular pathway by which a heritable instruction becomes a cellular function. The dogma does not predict *which* proteins are made in a given cell (that requires gene regulation), nor does it predict the full phenotypic consequence of a protein change (that requires system-level modeling). Rather, it specifies the one-way transfer channels through which information must pass, and therefore predicts where disruptions in that pipeline will or will not propagate downstream. The model is a useful filter for understanding causality: if you know where in the DNA → RNA → Protein pathway a mutation sits, you can predict whether it will affect the final protein and how.

## Core Variables and Relationships

The Central Dogma defines three sequential information transformations:

1. **DNA → RNA (Transcription)**
   - Input: double-stranded DNA sequence in a specific gene locus
   - Process: RNA polymerase reads one strand (template) and synthesizes complementary single-stranded mRNA
   - Output: mRNA sequence (transcript)
   - Drivers of information fidelity:
     - Accuracy of RNA polymerase (error rate ~10⁻⁴ to 10⁻⁵ per base)
     - Promoter recognition and transcription start site positioning
     - Splicing in eukaryotes (removal of introns, ligation of exons) — reduces information redundancy
     - 5' capping and 3' polyadenylation in eukaryotes (affect mRNA stability and translation initiation)
   - Information loss or alteration:
     - Introns are removed; only exons carry coding information to ribosomes
     - Regulatory sequences (enhancers, silencers) do not appear in the mRNA
     - Mutations in non-coding introns rarely propagate to protein unless they disrupt splice sites

2. **RNA → Protein (Translation)**
   - Input: mature mRNA (ribosome binding site + open reading frame + stop codon)
   - Process: ribosome reads mRNA codon-by-codon; tRNA molecules carry amino acids specified by the genetic code
   - Output: polypeptide chain (primary protein structure)
   - Drivers of information fidelity:
     - Genetic code (degeneracy: multiple codons → same amino acid)
     - Accuracy of tRNA aminoacylation (error rate ~10⁻⁴ per amino acid)
     - Start codon (AUG) recognition; stop codon (UAA, UAG, UGA) recognition
     - Ribosomal proofreading and tRNA discrimination
   - Information loss or alteration:
     - Synonymous mutations (silent mutations) do not change the amino acid sequence
     - Wobble base pairing at the third codon position masks some mutations
     - Mutations in the 5' UTR (untranslated region) do not change protein sequence but may affect translation rate
     - Frameshifts and nonsense mutations cause premature termination

3. **Protein → Phenotype (Protein Function)**
   - Input: primary amino acid sequence (folded protein with active sites)
   - Process: protein folds (driven by hydrophobic/hydrophilic interactions), post-translational modification, localization, assembly into complexes
   - Output: functional enzyme, receptor, structural protein, etc.
   - Drivers of phenotypic consequence:
     - Location of mutation in amino acid sequence (active site vs. surface vs. flexible loop)
     - Chemical properties of the substituted amino acid (charge, size, hydrophobicity)
     - Protein folding robustness (some positions tolerate substitution; others cause misfolding)
     - Gene dosage (how many copies of the gene; haploinsufficiency if only one functional copy remains)
   - Information loss or alteration:
     - Post-translational modifications (phosphorylation, ubiquitination, etc.) are not encoded in DNA — they depend on cellular context
     - Protein-protein interactions and regulatory signals are not predicted from sequence alone

The dogma's core claim is **linearity with one-way flow**: DNA → RNA → Protein is irreversible at the molecular level. Information cannot flow backward (e.g., protein sequence does not rewrite DNA).

## Key Predictions

- **Mutations in the coding sequence of a gene will produce a protein variant.** The severity of the phenotypic effect depends on where in the translation the mutation falls: a missense mutation in an active site will likely abolish function, while a synonymous mutation in a wobble position will have no effect.

- **A frameshift mutation (insertion or deletion not divisible by 3) will render all downstream codons unreadable**, producing a truncated or nonsensical protein; the phenotype will be loss-of-function regardless of the amino acid sequence downstream of the frameshift.

- **Mutations in promoter regions, introns, or the 3' UTR will have no direct effect on protein sequence**, but may alter when, where, or how much of the protein is made — affecting phenotype through regulation rather than protein structure.

- **A stop codon introduced mid-sequence (nonsense mutation) will cause translation termination**, producing a truncated protein lacking downstream domains; the phenotype is typically loss-of-function.

- **Silent / synonymous mutations (wobble-position changes that do not alter amino acid) will have no primary phenotypic effect** unless they affect codon usage bias, translation speed, or a cryptic regulatory element.

- **An amino acid substitution at a highly conserved residue is more likely to disrupt protein folding or function than a substitution at a variable position**, because conservation implies the position is under functional constraint.

## Application Procedure

Instantiate the model to predict how a molecular change (mutation, variant, or experimental perturbation) will propagate to phenotype.

1. **Define the locus and the molecular change precisely.**
   - Is it a DNA mutation (point mutation, insertion, deletion)?
   - If DNA: in what region (promoter, exon, intron, UTR)?
   - If exon: which codon(s) and what is the change (synonymous, missense, frameshift, nonsense)?
   - Write the DNA position, reference allele, and alternate allele.

2. **Trace the change through the pipeline.**
   - Will it affect transcription? (Check: is it in a promoter or splice site? Does it create a new stop codon in RNA?)
   - Will the resulting mRNA be translated? (Check: does the mutation disrupt the ribosome binding site, start codon, or create a premature stop?)
   - Will the protein be produced? (Check: is the protein truncated, misfolded, or present at normal levels?)

3. **Identify the level of information filtering.**
   - **DNA level** (transcriptional): mutation affects whether or how much mRNA is made.
   - **RNA level** (splicing, stability): mutation affects which exons are included or mRNA decay rate.
   - **Translation level** (coding sequence, codon usage): mutation affects amino acid sequence or translation efficiency.
   - **Post-translation level** (folding, modification, localization): mutation affects protein function after synthesis.

4. **Predict the protein consequence.**
   - Using the genetic code and codon degeneracy, determine what amino acid change (if any) results.
   - If missense: assess whether the substitution is conservative (similar chemical properties) or radical.
   - If frameshift, nonsense, or splice-disrupting: predict truncation or loss of expression.

5. **Map to phenotype.**
   - Is the affected protein essential (loss causes obvious phenotype) or redundant (loss is cryptic)?
   - Is the affected domain catalytic, structural, or regulatory? (Catalytic defects typically cause loss of function; regulatory defects may cause ectopic expression.)
   - Does the gene have multiple isoforms or paralogs that might compensate?

6. **Check boundary conditions** (see below). If the mutation affects non-coding regulatory elements, post-translational modification, or protein-complex assembly, note that the basic Central Dogma pathway does not fully explain phenotype and additional analysis is needed.

## Boundary Conditions

The Central Dogma is a one-way molecular pipeline and is incomplete or misleading under the following conditions:

- **Gene regulation and non-coding variants.** The dogma says nothing about *when* or *where* a gene is expressed, only that the information flows DNA → RNA → Protein. A mutation in a distant enhancer or in the chromatin structure can abolish expression without touching the coding sequence. Supplement with a gene-regulation model (cis-regulatory elements, transcription factors, chromatin state).

- **Post-translational modification.** The dogma predicts the amino acid sequence, not the final protein form. Phosphorylation, ubiquitination, cleavage, disulfide bonding, and glycosylation are not encoded in DNA and cannot be predicted from sequence alone. These modifications can be necessary for function (e.g., protease cleavage of pro-proteins). Use proteomic or structural models in parallel.

- **Protein-protein interactions and cellular context.** A protein may have the correct sequence but misfold, aggregate, or fail to localize in a given cell type or condition. The Central Dogma does not account for chaperones, crowding, or compartmentalization.

- **RNA-level regulation (miRNA, small RNAs, nonsense-mediated decay).** Some mutations create or destroy miRNA binding sites or trigger nonsense-mediated decay, causing loss of mRNA without a coding-sequence defect. These are "RNA secondary effects" not fully captured by the basic dogma.

- **Reverse transcription and retroviral integration.** The dogma states information does not flow from RNA back to DNA; however, reverse transcriptase (in retroviruses and some transposons) violates this. If the locus is a retroviral insertion or a transposable element, information can be recopied into DNA.

- **Epigenetic inheritance.** DNA methylation, histone modifications, and chromatin state can be heritable across cell divisions without changing the DNA sequence. These represent information flow not captured by the sequence-centric dogma.

- **Phenotypic buffering and genetic background.** A severe coding mutation may have no obvious phenotype if the cell or organism can compensate (redundancy, feedback, developmental buffering). The Central Dogma predicts the protein-level consequence, not the organism-level resilience.

## Output Format

```
## Central Dogma Analysis: <gene / mutation>

**Locus:** <chromosome:position, reference allele, alternate allele>
**Mutation type:** <point, frameshift, indel, etc.>
**Location in gene:** <promoter, exon, intron, UTR, splice site>

### Information flow trace
| Stage | Input | Mutation effect | Output | Propagates downstream? |
|---|---|---|---|---|
| Transcription | DNA sequence | <does it affect promoter, splice site, or stability?> | mRNA made or not | Yes / No / Altered |
| Translation | mRNA codon | <synonymous / missense / nonsense / frameshift> | Protein sequence | Yes / No / Truncated |
| Function | Amino acid sequence | <conservative / radical / deletion> | Active / Inactive / Misfolded | Yes / No / Unknown |

### Predicted protein consequence
- Amino acid change (if any): <reference → alternate, e.g., "Leu123Arg">
- Molecular class: <synonymous / missense conservative / missense radical / frameshift / nonsense / splice-disrupting / non-coding>
- Protein-level outcome: <normal sequence and level / truncated / absent / misloc alized / unstable>

### Phenotypic prediction
- Expected consequence: <loss of function / gain of function / no effect / context-dependent>
- Confidence in prediction: <high / medium / low>
- Rationale: <which stage of the pipeline is disrupted, and is downstream compensation likely?>

### Boundary-condition check
<which boundary conditions apply? (regulatory, post-translational, epigenetic, genetic background, etc.) Does the Central Dogma fully explain the predicted phenotype, or is complementary analysis needed?>

### Confidence: high | medium | low
<reasoning: clarity of the molecular defect + position in the pipeline + whether the protein is essential + whether boundary conditions cloud the prediction>
```
