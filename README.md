# Prediction of Secretory Signal Peptide Presence in Eukaryotic Proteins
## Laboratory of Bioinformatics 2 2025/2026 -  Alma Mater Studiorum Università di Bologna

### Abstract
Signal peptides are typically short peptides located in the N-terminal of protein sequences that carry information for protein secretion and are cleaved upon localization. *In-silico* prediction of signal peptides is crucial for functional annotation and localization. 

## 1. Data Collection 📥
**Objective:** retrieve positive and negative datasets of eukaryotic proteins from UniProtKB.

### a. Selection criteria

**Positive dataset (secreted proteins with experimental SP evidence):**
  1. No fragments: Fragment: No (fragment:false)
  2. Select only eukaryotic proteins: Taxonomy [OC]: 2759 (taxonomy_id:2759)
  3. Filter-out sequences shorter than 40 residues: Sequence length: 40 to (length:[40 TO *])
  4. Filter-out unreviewed proteins: Reviewed: Yes (reviewed:true)
  5. Protein existence supported by experimental evidence: Protein Existance[PE]: Evidence at protein level (existence:1)
  6. Presence of experimentally validated signal peptide: Signal Peptide: * Evidence: Experimental (ft_signal_exp:*)
  7. Filter out proteins with SP shorter than 14 residues (custom filter, see below).

Final query: `(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) AND (ft_signal_exp:*)`

 > Number of results (22/09/2025): **2,949**

**Negative dataset (Non-secretory proteins, with defined subcellular localization):**
  1. No fragments: Fragment: No (fragment:false)
  2. Only reviewed proteins: Reviewed: Yes (reviewed:true)
  3. Select on protein with experimental SP evidence: Protein Existance[PE]: Evidence at protein level (existence:1)
  4. Only eukaryotic proteins: Taxonomy [OC]: 2759 (taxonomy_id:2759)
  5. Sequence length ≥ 40 residues: Sequence length: 40 to (length:[40 TO *])
  6. Exclude all proteins with any signal peptide: Signal Peptide: * Evidence: Any (NOT ft_signal_exp:*)
  7. Experimentally localized to cytosol, nucleus, mitochondrion, plastid, peroxisome, or cell membrane: Subcellular location term: SL-0173/SL-0191/SL-0173/SL-0204/SL-0209/SL-0039 Evidence: Experimental

Final query: `(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) NOT (ft_signal:*) AND ((cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0173) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0039))`

 > Number of results (22/09/2025): **20,615**

### b. Filtering of the Positive Dataset
UniProtKB does not directly allow filtering signal peptides by length.

A custom Python script was implemented to:
	•	Query UniProtKB via its REST API.
	•	Iterate through JSON results.
	•	Retain only proteins with signal peptides ≥ 14 residues.
	•	Export the final datasets in both .tsv and .fasta formats.
  
 > The final number of results in the positive dataset was: **2,932**

### c. Implementation Notes

About the implementation:
	•	API & Pagination: handled via the UniProtKB REST API (https://rest.uniprot.org/uniprotkb/). Pagination is implemented using the Link header.
	•	Batch retrieval: results are retrieved in batches of 500 entries.
	•	Retry mechanism: requests.Session() with retry strategy ensures robustness against temporary server unavailability.
	•	Output files: both .tsv (structured metadata) and .fasta (protein sequences) files are generated for downstream analysis.
	
### d. Output files
  The final amount of entries in the datasets can be found in the following table:
  
  | Dataset | No. entries | Output files |
  | ------------- | ------------- | ------------- |
  | Positive  | 20,615  | eukarya_SP_pos.tsv, pos.fasta |
  | Negative  | 2,932  | eukarya_SP_neg.tsv, neg.fasta |

### e. Reproducibility
The code for dataset generation is included in data_collection.py.

Execution:

`python data_collection.py --pos_out eukarya_SP_pos.tsv --neg_out eukarya_SP_neg.tsv --pos_fasta pos.fasta --neg_fasta neg.fasta`

Where:
	•	--pos_out and --neg_out: output TSV files.
	•	--pos_fasta and --neg_fasta: output FASTA files.
	•	The UniProt API queries are embedded in the script (pos_url, neg_url), but can be replaced with custom ones for reproducibility.
  
## 2. Data Preparation
**Objective:** preprocess datasets for cross-validation and benchmarking.

	The Positive and Negative datasets were clustered in order to avoid redundancy, which would have resulted in biases through the classification methods implementation. 

	
	After the clusterization was completed, the list of representative IDs was randomized (for both positive and negative datasets), to make sure the distrubution of the sequences would not bias the model. 
	Moreover, 80% of the data was used to create 5 training sets while the remaining 20% was labeled for benchmarking for both positive and negative datasets.
	Finally, each dataset was merged by its counterpart in a tailored `.tsv` file in which features, dataset label and fold label are reported. 

## 3. Data visualization
Using SEABORN and MATPLOTLIB, data were analysed to describe the feature distribution among the datasets.
Some informative plots and evaluations are available "[LINK TO THE DIRECTORY]"
## References 
