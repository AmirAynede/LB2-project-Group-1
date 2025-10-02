# Prediction of Secretory Signal Peptide Presence in Eukaryotic Proteins
## Laboratory of Bioinformatics 2 2025/2026 -  Alma Mater Studiorum Università di Bologna

### Abstract
Signal peptides are short sequences at the N-terminus of proteins that direct them to the secretory pathway and are typically cleaved after translocation [(1)](https://www.sciencedirect.com/science/article/pii/S0171933518300189).  *In-silico* prediction of signal peptides is crucial for functional annotation and localization. 

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

Final query: 
```bash
(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) AND (ft_signal_exp:*)
```

 > Number of results (22/09/2025): **2,949**

**Negative dataset (Non-secretory proteins, with defined subcellular localization):**
  1. No fragments: Fragment: No (fragment:false)
  2. Only reviewed proteins: Reviewed: Yes (reviewed:true)
  3. Select on protein with experimental SP evidence: Protein Existance[PE]: Evidence at protein level (existence:1)
  4. Only eukaryotic proteins: Taxonomy [OC]: 2759 (taxonomy_id:2759)
  5. Sequence length ≥ 40 residues: Sequence length: 40 to (length:[40 TO *])
  6. Exclude all proteins with any signal peptide: Signal Peptide: * Evidence: Any (NOT ft_signal_exp:*)
  7. Experimentally localized to cytosol, nucleus, mitochondrion, plastid, peroxisome, or cell membrane: Subcellular location term: SL-0173/SL-0191/SL-0173/SL-0204/SL-0209/SL-0039 Evidence: Experimental

Final query: 
```bash
(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) NOT (ft_signal:*) AND ((cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0173) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0039))
```

 > Number of results (22/09/2025): **20,615**

### b. Filtering of the Positive Dataset
UniProtKB does not directly allow filtering signal peptides by length.

A custom Python script was implemented to:  
- Query UniProtKB via its REST API  
- Iterate through JSON results  
- Retain only proteins with signal peptides ≥ 14 residues  
- Export the final datasets in both `.tsv` and `.fasta` formats  
  
 > The final number of results in the positive dataset was: **2,932**

### c. Implementation Notes

- API & Pagination: handled via the UniProtKB REST API (https://rest.uniprot.org/uniprotkb/). Pagination is implemented using the Link header.
- Batch retrieval: results are retrieved in batches of 500 entries.
- Retry mechanism: requests.Session() with retry strategy ensures robustness against temporary server unavailability.
- Output files: both .tsv (structured metadata) and .fasta (protein sequences) files are generated for downstream analysis.
	
### d. Output files
  The final amount of entries in the datasets can be found in the following table:
  
  | Dataset | No. entries | Output files |
  | ------------- | ------------- | ------------- |
  | Positive  | 20,615  | [eukarya_SP_pos.tsv](data_collection/output/eukarya_SP_pos.tsv), [pos.fasta](data_collection/output/pos.fasta) |
  | Negative  | 2,932  | [eukarya_SP_neg.tsv](data_collection/output/eukarya_SP_neg.tsv), [neg.fasta](data_collection/output/neg.fasta) |

### e. Reproducibility
The code for dataset generation is included in [data_collection.py](data_collection/scripts/00_data_collect.py).

Execution:

```bash 
python data_collection.py --pos_out eukarya_SP_pos.tsv --neg_out eukarya_SP_neg.tsv --pos_fasta pos.fasta --neg_fasta neg.fasta
```

Where:
- --pos_out and --neg_out: output TSV files.
- --pos_fasta and --neg_fasta: output FASTA files.
- The UniProt API queries are embedded in the script (pos_url, neg_url), but can be replaced with custom ones for reproducibility.
  
## 2. Data Preparation 🗂️
**Objective:** Reduce redundancy in the datasets, generate training and benchmarking sets, and create 5-fold cross-validation subsets for robust model evaluation

### a. Sequence Clustering
Positive and negative sequences were clustered separately to avoid redundancy, which could bias the classification methods, with MMseqs2.

Parameters:
- Minimum sequence identity: 30% (--min-seq-id 0.3)
- Coverage: 40% (-c 0.4)
- Coverage mode: 0 (--cov-mode 0)
- Cluster mode: 1 (--cluster-mode 1)

Example command for positive sequences:
```bash
mmseqs easy-cluster ../output/pos.fasta cluster-results-pos tmp --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1
 ```
Example command for negative sequences:
```bash
mmseqs easy-cluster ../output/neg.fasta cluster-results-neg tmp --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1
 ```
Outcome: Representative sequences were selected from each cluster.
| Dataset   | Input sequences | No. of clusters | File | 
|-----------|----------------|----------------|----------------|
| Positive  | 2,932          | 1,093            | [cluster-results-pos_all_seqs.fasta](data_split/files/cluster_output/cluster-results-pos_all_seqs.fasta)
| Negative  | 20,615         | 8,934            | [cluster-results-neg_all_seqs.fasta](data_split/files/cluster_output/cluster-results-neg_all_seqs.fasta)

### b. Extract Representative IDs
A custom Python script was used to extract the IDs of representative sequences from the clustered FASTA files and can be found in [extract_rep_ids.py](data_split/scripts/01_extract_rep_ids.py).

Execution:
```bash
python extract_representative_ids.py neg.fasta pos.fasta neg_ids.txt pos_ids.txt
 ```
### c. Filter Original TSVs
The original TSV files were filtered to retain only the representative sequences with the script [organizing_metadata.py](data_split/scripts/02_organizing_metadata.py).
The filtered TSVs contain:
- UniProt ID
- Species
- Kingdom
- Sequence length
- Cleavage site / Transmembrane helix (as relevant)
- Training/Benchmark label 
- Fold assignment 

The final files are: [neg_dss.tsv](data_split/files/folded_datasets/neg_dss.tsv) and [pos_dss.tsv](data_split/files/folded_datasets/pos_dss.tsv)

### d. Training and Benchmarking Split

**Randomization:** Representative sequences were randomized to avoid biases.

**Split of positive and negative datasets:** 
- 80%: training sets
- 20%: benchmarking set

### e. 5-Fold Cross-Validation
- The training set was split into 5 folds while preserving the positive/negative ratio.
- Each protein’s fold assignment was recorded in the .tsv file for reproducibility (the label 0 means benchmarking set).
- This ensures that models can be trained and validated without data leakage.

### f. Output
| Set / Fold | Negative sequences | Positive sequences | Total sequences |
|------|-----------------|-----------------|----------------|
| [Benchmarking](data_split/files/training_sets/bench_rand.txt)    | 1,787           | 219             | 2,006          |
| [Fold 1](data_split/files/training_sets/tr_set1_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 2](data_split/files/training_sets/tr_set2_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 3](data_split/files/training_sets/tr_set3_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 4](data_split/files/training_sets/tr_set4_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 5](data_split/files/training_sets/tr_set5_rand_id.txt)    | 1,429           | 174             | 1,603          |

## 3. Data Analysis and Visualization 📊

The data visualization step provides insights into the characteristics of the positive and negative protein datasets used in this study. The plots were generated in Python using **matplotlib** and **seaborn**.

### a. Analyses

- **Taxonomic Distribution:** Kingdom and species distributions for both training and benchmarking datasets were analyzed to ensure representative sampling across major eukaryotic groups.  
- **Sequence Length:** Distribution of sequence lengths was compared between positive and negative datasets, as well as between training and benchmarking subsets.  
- **Signal Peptide (SP) Length:** Length distributions of SPs in the positive dataset were analyzed for both training and benchmarking sequences.  
- **Amino Acid Composition:** Residue composition of SPs was compared against the SwissProt background distribution.  
- **Sequence Logos:** Cleavage site motifs of SPs were visualized using [WebLogo](https://weblogo.berkeley.edu/logo.cgi), highlighting conserved positions.

### b. Plot Summary

| Plot Type | Dataset | Filename | Description |
|-----------|--------|----------|-------------|
| Pie & Bar | Training | [t_kingdom.pdf](data_analysis/visualization/t_kingdom.pdf) | Kingdom distribution of training sequences |
| Pie & Bar | Positive Training | [pos_t_kingdom.pdf](data_analysis/visualization/pos_t_kingdom.pdf) | Kingdom distribution of positive training sequences |
| Pie & Bar | Negative Training | [neg_t_kingdom.pdf](data_analysis/visualization/neg_t_kingdom.pdf) | Kingdom distribution of negative training sequences |
| Pie & Bar | Benchmarking | [b_kingdom.pdf](data_analysis/visualization/b_kingdom.pdf) | Kingdom distribution of benchmarking sequences |
| Pie & Bar | Positive Benchmarking | [pos_b_kingdom.pdf](data_analysis/visualization/pos_b_kingdom.pdf)  | Kingdom distribution of positive benchmarking sequences |
| Pie & Bar | Negative Benchmarking | [neg_b_kingdom.pdf](data_analysis/visualization/neg_b_kingdom.pdf) | Kingdom distribution of negative benchmarking sequences |
| Pie & Bar | Training | [t_species.pdf](data_analysis/visualization/t_species.pdf) / [t_species_bar.pdf](data_analysis/visualization/t_species_bar.pdf)| Species distribution of training sequences |
| Pie & Bar | Positive Training | [pos_t_species.pdf](data_analysis/visualization/pos_t_species.pdf) / [pos_t_species_bar.pdf](data_analysis/visualization/pos_t_species_bar.pdf)| Species distribution of positive training sequences |
| Pie & Bar | Negative Training | [neg_t_species.pdf](data_analysis/visualization/neg_t_species.pdf) / [neg_t_species_bar.pdf](data_analysis/visualization/neg_t_species_bar.pdf)| Species distribution of negative training sequences |
| Pie & Bar | Benchmarking | [b_species.pdf](data_analysis/visualization/b_species.pdf) / [b_species_bar.pdf](data_analysis/visualization/b_species_bar.pdf) | Species distribution of benchmarking sequences |
| Pie & Bar | Positive Benchmarking | [pos_b_species.pdf](data_analysis/visualization/pos_b_species.pdf) / [pos_b_species_bar.pdf](data_analysis/visualization/pos_b_species_bar.pdf)| Species distribution of positive benchmarking sequences |
| Pie & Bar | Negative Benchmarking | [neg_b_species.pdf](data_analysis/visualization/neg_b_species.pdf) / [neg_b_species_bar.pdf](data_analysis/visualization/neg_b_species_bar.pdf)| Species distribution of negative benchmarking sequences |
| KDE Plot | All | [Seq_length_posneg.pdf](data_analysis/visualization/Seq_length_posneg.pdf) | Sequence length distribution: positives vs negatives |
| KDE Plot | All | [Seq_length_TB.pdf](data_analysis/visualization/Seq_length_TB.pdf) | Sequence length distribution: training vs benchmarking |
| KDE Plot | Positive | [Seq_length_pos.pdf](data_analysis/visualization/Seq_length_pos.pdf)  | Sequence length of positives: training vs benchmarking |
| KDE Plot | Negative | [Seq_length_neg.pdf](data_analysis/visualization/Seq_length_neg.pdf)  | Sequence length of negatives: training vs benchmarking |
| Boxplot | All | [Seq_length_posneg_box.pdf](data_analysis/visualization/Seq_length_posneg_box.pdf)  | Sequence length comparison |
| Boxplot | All | [Seq_length_TB_box.pdf](data_analysis/visualization/Seq_length_TB_box.pdf)  | Sequence length comparison |
| Boxplot | Positive | [Seq_length_pos_box.pdf](data_analysis/visualization/Seq_length_pos_box.pdf) | Training vs benchmarking |
| Boxplot | Negative | [Seq_length_neg_box.pdf](data_analysis/visualization/Seq_length_neg_box.pdf) | Training vs benchmarking |
| Histogram | All | [Seq_length_posneg_hist.pdf](data_analysis/visualization/Seq_length_posneg_hist.pdf) | Sequence length probability distributions |
| Histogram | All | [Seq_length_TB_hist.pdf](data_analysis/visualization/Seq_length_TB_hist.pdf) | Sequence length probability distributions |
| Histogram | Positive | [Seq_length_pos_hist.pdf](data_analysis/visualization/Seq_length_pos_hist.pdf)  | Training vs benchmarking |
| Histogram | Negative | [Seq_length_neg_hist.pdf](data_analysis/visualization/Seq_length_neg_hist.pdf)  | Training vs benchmarking |
| KDE | Positive | [SP_length_dist.pdf](data_analysis/visualization/SP_length__dist.pdf) | Signal peptide length distribution |
| Boxplot | Positive | [SP_length_box.pdf](data_analysis/visualization/SP_length_box.pdf) | Signal peptide length distribution |
| Histogram | Positive | [SP_length_hist.pdf](data_analysis/visualization/SP_length_hist.pdf) | SP length probability distribution |
| Bar Plot | All | [residue_composition.pdf](data_analysis/visualization/residue_composition.pdf) | Amino acid composition: Training, Benchmarking, SwissProt |
| Sequence Logo | Positive | [t_logo.png](data_analysis/visualization/t_logo.png) | SP cleavage site logos Training (via WebLogo) |
| Sequence Logo | Positive | [b_logo.png](data_analysis/visualization/b_logo.png) | SP cleavage site logos Benchmarking (via WebLogo) |

**Note:** All plots and analyses are reproducible using the uploaded [Data_Visualization.ipynb](data_analysis/scripts/04_Data_Analysis.ipynb) notebook. 

## Major conclusions of data analysis



## References 
1. Owji, Hajar & Nezafat, Navid & Negahdaripour, Manica & HajiEbrahimi, Ali & Younes, Ghasemi. (2018). A Comprehensive Review of Signal Peptides: Structure, Roles, and Applications. European Journal of Cell Biology. 97. 10.1016/j.ejcb.2018.06.003.
