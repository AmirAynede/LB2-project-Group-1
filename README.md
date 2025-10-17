# Prediction of Secretory Signal Peptide Presence in Eukaryotic Proteins
## Laboratory of Bioinformatics 2 2025/2026 -  Alma Mater Studiorum Università di Bologna

### Abstract
Signal peptides are short sequences at the N-terminus of proteins that direct them to the secretory pathway and are typically cleaved after translocation [(1)](https://www.sciencedirect.com/science/article/pii/S0171933518300189).  *In-silico* prediction of signal peptides is crucial for functional annotation and localization. 

## 1. Data Collection 
**Objective:** retrieve positive and negative datasets of eukaryotic proteins from UniProtKB.

The full description of the procedure can be found in the [README.md](data_collection/README.md) of the data_colection folder.

### Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| Selection criteria |
  |b| Filtering the Positive Dataset | 
  |c| Implementation notes|
  |d| Output files | 
  |e| Reproducibility |

### Results
  | Datasets | Positive | Negative |
  | :---:  | :---: | :---:  |
  | Query | `(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) AND (ft_signal_exp:*)`| `(existence:1) AND (length:[40 TO *]) AND (reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) NOT (ft_signal:*) AND ((cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0173) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0039))` |
  | No. entries | Before filtering: 2,949 <br> After filtering: 2,932| 20,615 |
  | Output | [eukarya_SP_pos.tsv](data_collection/output/eukarya_SP_pos.tsv) <br> [pos.fasta](data_collection/output/pos.fasta) | [eukarya_SP_neg.tsv](data_collection/output/eukarya_SP_neg.tsv) <br> [neg.fasta](data_collection/output/neg.fasta) |

## 2. Data Preparation 
**Objective:** Reduce redundancy in the datasets, generate training and benchmarking sets, and create 5-fold cross-validation subsets for robust model evaluation

The full description of the procedure can be found in the [README.md](data_split/README.md) of the data_split folder.

### Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| Clustering |
  |b| Extract Representative IDs | 
  |c| Metadata Collection |
  |d| Data Splitting and Cross-Validation | 
  |e| Output |
  
### Results

**Clustering**
| Dataset   | Input sequences | No. of clusters | File | 
|:---:|:---:|:---:|:---:|
| Positive  | 2,932          | 1,093            | [cluster-results-pos_rep_seq.fasta](data_split/files/cluster_output/cluster-results-pos_rep_seq.fasta) |
| Negative  | 20,615         | 8,934            | [cluster-results-neg_rep_seq.fasta](data_split/files/cluster_output/cluster-results-neg_rep_seq.fasta) |

**Extract Representative IDs and Metadata Collection**

The ID lists were randomized and split. The output files were used to filter the collective .tsv file. Two .tsv files were obtained to organize metadata related to positive and negative datasets.

| Section | Scripts | Files | 
|:---:|:---:|:---:|
| b  | [extract_rep_ids.py](data_split/scripts/01_extract_rep_ids.py)            | [neg_rep_id.txt](data_split/files/cluster_output/neg_rep_id.txt) <br> [pos_rep_id.txt](data_split/files/cluster_output/pos_rep_id.txt) |
| c  | 20,615         | [organizing_metadata.py](data_split/scripts/02_organizing_metadata.py)           | [[neg_dss.tsv](data_split/files/folded_datasets/neg_dss.tsv) and [pos_dss.tsv](data_spit/files/folded_datasets/pos_dss.tsv) | 

**Output**
| Set / Fold | Negative sequences | Positive sequences | Total sequences |
|:---: |:---: |:---: |:---: |
| [Benchmarking](files/training_sets/bench_rand.txt)    | 1,787           | 219             | 2,006          |
| [Fold 1](files/training_sets/tr_set1_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 2](files/training_sets/tr_set2_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 3](files/training_sets/tr_set3_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 4](files/training_sets/tr_set4_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 5](files/training_sets/tr_set5_rand_id.txt)    | 1,429           | 174             | 1,603          |

## 3. Data Analysis and Visualization 
**Objective:** understand the structure and characteristics of the dataset.

The data visualization step provides insights into the characteristics of the positive and negative protein datasets used in this study. The plots were generated in Python using **matplotlib** and **seaborn**.

The full description of the procedure can be found in the [README.md](data_analysis/README.md) of the data_analysis folder.

### Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| Analyses |
  |b| Plot Summary | 
  |c| Results|
  
### Results
| Description and Plot Type | Dataset | Filename | 
|:-----------:|:--------:|:----------:|
| Kingdom distribution <br> (Pie & Bar) | All | [t_kingdom.pdf](data_analysis/visualization/t_kingdom.pdf) <br>[pos_t_kingdom.pdf](data_analysis/visualization/pos_t_kingdom.pdf) <br> [neg_t_kingdom.pdf](data_analysis/visualization/neg_t_kingdom.pdf) <br> [b_kingdom.pdf](data_analysis/visualization/b_kingdom.pdf) <br> [pos_b_kingdom.pdf](data_analysis/visualization/pos_b_kingdom.pdf) <br> [neg_b_kingdom.pdf](data_analysis/visualization/neg_b_kingdom.pdf) | 
| Species distribution <br> (Pie & Bar) | All | [t_species.pdf](data_analysis/visualization/t_species.pdf) <br> [t_species_bar.pdf](data_analysis/visualization/t_species_bar.pdf) <br> [pos_t_species.pdf](data_analysis/visualization/pos_t_species.pdf) <br> [pos_t_species_bar.pdf](data_analysis/visualization/pos_t_species_bar.pdf) <br>  [neg_t_species.pdf](data_analysis/visualization/neg_t_species.pdf) <br> [neg_t_species_bar.pdf](data_analysis/visualization/neg_t_species_bar.pdf) <br>  [b_species.pdf](data_analysis/visualization/b_species.pdf) <br> [b_species_bar.pdf](data_analysis/visualization/b_species_bar.pdf) <br> [pos_b_species.pdf](data_analysis/visualization/pos_b_species.pdf) <br> [pos_b_species_bar.pdf](data_analysis/visualization/pos_b_species_bar.pdf) <br>  [neg_b_species.pdf](data_analysis/visualization/neg_b_species.pdf) <br> [neg_b_species_bar.pdf](data_analysis/visualization/neg_b_species_bar.pdf)| 
| Sequence length distribution <br> (KDE Plot) | All | [Seq_length_posneg.pdf](data_analysis/visualization/Seq_length_posneg.pdf) <br> [Seq_length_TB.pdf](data_analysis/visualization/Seq_length_TB.pdf) <br> [Seq_length_pos.pdf](data_analysis/visualization/Seq_length_pos.pdf)  <br> [Seq_length_neg.pdf](data_analysis/visualization/Seq_length_neg.pdf) | 
| Sequence length distribution <br> (Boxplot) | All | [Seq_length_posneg_box.pdf](data_analysis/visualization/Seq_length_posneg_box.pdf)  <br> [Seq_length_TB_box.pdf](data_analysis/visualization/Seq_length_TB_box.pdf)  <br> [Seq_length_pos_box.pdf](data_analysis/visualization/Seq_length_pos_box.pdf) <br> [Seq_length_neg_box.pdf](data_analysis/visualization/Seq_length_neg_box.pdf) | 
| Sequence length distribution <br> (Histogram) | All | [Seq_length_posneg_hist.pdf](data_analysis/visualization/Seq_length_posneg_hist.pdf) <br> [Seq_length_TB_hist.pdf](data_analysis/visualization/Seq_length_TB_hist.pdf) <br> [Seq_length_pos_hist.pdf](data_analysis/visualization/Seq_length_pos_hist.pdf) <br> [Seq_length_neg_hist.pdf](data_analysis/visualization/Seq_length_neg_hist.pdf)  | 
| Signal Peptide length distribution <br> (KDE plot) | Positive | [SP_length_dist.pdf](data_analysis/visualization/SP_length_dist.pdf) |
| Signal Peptide length distribution <br> (Boxplot)  | Positive | [SP_length_box.pdf](data_analysis/visualization/SP_length_box.pdf) | Signal peptide length distribution |
| Signal Peptide length distribution <br> (Histogram) | Positive | [SP_length_hist.pdf](data_analysis/visualization/SP_length_hist.pdf) | SP length probability distribution |
| Residue composition <br> (Bar Plot) | All compared to SwissProt | [residue_composition.pdf](data_analysis/visualization/residue_composition.pdf) | 
| Signal Peptide cleavage site logos <br> (Sequence Logo) | Positive | [t_logo.png](data_analysis/visualization/t_logo.png) <br> [b_logo.png](data_analysis/visualization/b_logo.png) | 

**Note:** All plots and analyses are reproducible using the uploaded [Data_Visualization.ipynb](data_analysis/scripts/04_Data_Analysis.ipynb) notebook. 

## 4. The vonHeijne method for SP detection 
**Objective:** Classify eukaryotic protein sequences with respect to the presence or absence of a signal peptide (SP) using a position-specific weight matrix (PSWM)-based approach inspired by the *von Heijne* method.

### Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| **Data Organization** |
  |b| **Training** |
  |b.1| Position-Specific Weight Matrix Computation | 
  |c| **Validation**|
  |c.1| Sequence Scoring |
  |c.2| Optimal Threshold Selection|
  |d| **Testing**|
  |d.1| Sequences Classification| 
  |e| **Performance Evaluation**| 
  
The detailed workflow and implementation can be found in the [vonHeijne/](vonHeijne/) directory.

### Results
  | Metric | Value |
  | :---:  | :---:  |
  |**Accuracy**| 0.9320 ± 0.0085| 
  |**Precision**| 0.6830 ± 0.0646| 
  |**Recall**| 0.7300 ± 0.0560| 
  |**F1 Score**| 0.7012 ± 0.0226| 
  |**MCC**| 0.6664 ± 0.0258|
  |**Threshold**| 8.8089 ± 0.5967| 

  ## 5. SVM classifier for SP detection
**Objective:** Classify eukaryotic protein sequences with respect to the presence or absence of a signal peptide (SP) building a Support Vector Machine (SVM) based on features extracted from the training dataset sequences.

### Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| **Data Organization** |
  |b| **Features Definition** |
  |c| **Training and Validation** |
  |c.1| Feature Extraction and Scaling |
  |c.2| Grid Search Over Hyperparameters | 
  |c.3| Features Selection (Random Forest) | 
  |d| **Model Testing**|
  |d.1| Over Selected Features| 
  |d.2| Over All Features|

### Results
The best models were selected by a grid search over the hyperparameters utilizing F1 score and MCC as performance metrics.

| Round | 1 | 2 | 3 | 4 | 5 |
  | :---:  | :---:  | :---:  | :---:  | :---:  | :---:  |
  |**Selected Features** <br> (Over the Best 29 Features)| MCC: 25 <br> F1: 25 | MCC: 25 <br> F1: 25 | MCC: 29 <br> F1: 29 | MCC: 24 <br> F1: 24 | MCC: 28 <br> F1: 28 | 



  | Round | Kernel (Selected) | Kernel (All) | C (Selected) |C (All) | Gamma (Selected) | Gamma (All)| 
  | :---:  | :---:  | :---:  | :---:  | :---:  | :---:  | :---:  | 
  |**1**| MCC: "rbf" <br> F1: "rbf" | MCC: "rbf" <br> F1: "rbf" | MCC: 0.1 <br> F1: 1 | MCC: 1 <br> F1: 1 | MCC: "scale" <br> F1: 0.01 | MCC: 0.01 <br> F1: 0.01 |
  |**2**| MCC: "rbf" <br> F1: "rbf" | MCC: "rbf" <br> F1: "rbf" | MCC: 10 <br> F1: 10 | MCC: 10 <br> F1: 10 | MCC: "scale" <br> F1: "scale" | MCC: "scale" <br> F1: "scale" |
  |**3**| MCC: "rbf" <br> F1: "rbf" | MCC: "rbf" <br> F1: "rbf" | MCC: 10 <br> F1: 10 | MCC: 10 <br> F1: 10 | MCC: 0.01 <br> F1: 0.01 | MCC: 0.01 <br> F1: 0.01 |
  |**4**| MCC: "rbf" <br> F1: "rbf" | MCC: "rbf" <br> F1: "rbf" | MCC: 1 <br> F1: 1 | MCC: 10 <br> F1: 10 | MCC: "scale" <br> F1: "scale" | MCC: 0.01 <br> F1: 0.01 | 
  |**5**| MCC: "rbf" <br> F1: "rbf" | MCC: "rbf" <br> F1: "rbf" | MCC: 1 <br> F1: 1 | MCC: 10 <br> F1: 10 | MCC: "scale" <br> F1: "scale" | MCC: 0.01 <br> F1: 0.01 |


  | Round | MCC (Selected) | MCC (All) | F1 (Selected) | F1 (All)| 
  | :---:  | :---:  | :---:  | :---:  | :---:  | 
  |**1**| 0.799| 0.853 | 0.840 | 0.867 |
  |**2**| 0.774 | 0.781 | 0.798 | 0.805 |
  |**3**| 0.822 | 0.839 | 0.841 | 0.857 |
  |**4**| 0.818 | 0.859 | 0.838 | 0.874 | 
  |**5**| 0.791 | 0.802 | 0.813 | 0.824 |
  |**Average**| 0.801 | 0.823 | 0.826 | 0.845 |


  
## References 
1. Owji, Hajar & Nezafat, Navid & Negahdaripour, Manica & HajiEbrahimi, Ali & Younes, Ghasemi. (2018). A Comprehensive Review of Signal Peptides: Structure, Roles, and Applications. European Journal of Cell Biology. 97. 10.1016/j.ejcb.2018.06.003.
