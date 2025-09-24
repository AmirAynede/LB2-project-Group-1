# Prediction of the secretory signal peptide
## Laboratory of Bioinformatics 2 2025/2026 -  Alma Mater Studiorum Università di Bologna

### Abstract
> Signal peptides are typically short peptides located in the N-terminal of proteins. They carry information for protein secretion and are cleaved upon localization.
> *In-silico* prediction of signal peptides is crucial for functional annotation and localization.

## 1. Data Collection
**Objective:** retrieve relevant datasets from UniProtKB.

### a. Selection criteria

**For the positive dataset:**
  1. No fragments: Fragment: No (fragment:false)
  2. Select only eukaryotic proteins: Taxonomy [OC]: 2759 (taxonomy_id:2759)
  3. Filter-out sequences shorter than 40 residues: Sequence length: 40 to (length:[40 TO *])
  4. Filter-out unreviewed proteins: Reviewed: Yes (reviewed:true)
  5. Select on protein with experimental SP evidence: Protein Existance[PE]: Evidence at protein level (existence:1)
  6. Filter out proteins with SP shorter than 14 residues: Signal Peptide: * Evidence: Experimental (ft_signal_exp:*)

  Final query: `(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) AND (ft_signal_exp:*)`

  Number of results (22/09/2025): **2,949**

**For the negative dataset:**
  1. No fragments: Fragment: No (fragment:false)
  2. Filter-out unreviewed proteins: Reviewed: Yes (reviewed:true)
  3. Select on protein with experimental SP evidence: Protein Existance[PE]: Evidence at protein level (existence:1)
  4. Select only eukaryotic proteins: Taxonomy [OC]: 2759 (taxonomy_id:2759)
  5. Filter-out sequences shorter than 40 residues: Sequence length: 40 to (length:[40 TO *])
  6. Filter-out sequences having SP (any evidence): Signal Peptide: * Evidence: Any (ft_signal_exp:*)
  7. Select only proteins experimentally verified to be localized into cytosol, nucleus, mitochondrion, plastid, peroxisome or cell membrane: Subcellular location term: SL-0173/SL-0191/SL-0173/SL-0204/SL-0209/SL-0039 Evidence: Experimental

  Final query: `(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) NOT (ft_signal:*) AND ((cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0173) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0039))`

  Number of results (22/09/2025): **20,615**

### b. Filter of the positive dataset
  In order to filter out the sequences with SP shorter than 14 residues, a python script was implemented.
  The final number of results in the positive dataset was: **2,932**
  
### c. Summary
  The final amount of entries in the datasets can be found in the following table:
  
  | Dataset | No. entries |
  | ------------- | ------------- |
  | Positive  | 20,615  |
  | Negative  | 2,932  |
  
## 2. Data Preparation
**Objective:** preprocess datasets for cross-validation and benchmarking.
