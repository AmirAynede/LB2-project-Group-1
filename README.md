# Prediction of Secretory Signal Peptide Presence in Eukaryotic Proteins
## Laboratory of Bioinformatics 2 2025/2026 -  Alma Mater Studiorum Università di Bologna

### Abstract
Signal peptides are short sequences at the N-terminus of proteins that direct them to the secretory pathway and are typically cleaved after translocation [(1)](https://www.sciencedirect.com/science/article/pii/S0171933518300189).  *In-silico* prediction of signal peptides is crucial for functional annotation and localization. 

## 1. Data Collection 
**Objective:** retrieve positive and negative datasets of eukaryotic proteins from UniProtKB.

The full description of the procedure can be found in the [README.md](01_data_collection/README.md) of the data_colection folder.

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
  | Output | [eukarya_SP_pos.tsv](01_data_collection/output/eukarya_SP_pos.tsv) <br> [pos.fasta](01_data_collection/output/pos.fasta) | [eukarya_SP_neg.tsv](01_data_collection/output/eukarya_SP_neg.tsv) <br> [neg.fasta](01_data_collection/output/neg.fasta) |

## 2. Data Preparation 
**Objective:** Reduce redundancy in the datasets, generate training and benchmarking sets, and create 5-fold cross-validation subsets for robust model evaluation

The full description of the procedure can be found in the [README.md](02_data_preparation/README.md) of the data_split folder.

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
| Positive  | 2,932          | 1,093            | [cluster-results-pos_rep_seq.fasta](02_data_preparation/files/cluster_output/cluster-results-pos_rep_seq.fasta) |
| Negative  | 20,615         | 8,934            | [cluster-results-neg_rep_seq.fasta](02_data_preparation/files/cluster_output/cluster-results-neg_rep_seq.fasta) |

**Extract Representative IDs and Metadata Collection**

The ID lists were randomized and split. The output files were used to filter the collective .tsv file. Two .tsv files were obtained to organize metadata related to positive and negative datasets.

| Section | Scripts | Files | 
|:---:|:---:|:---:|
| b  | [extract_rep_ids.py](data_split/scripts/01_extract_rep_ids.py)            | [neg_rep_id.txt](02_data_preparation/files/cluster_output/neg_rep_id.txt) <br> [pos_rep_id.txt](02_data_preparation/files/cluster_output/pos_rep_id.txt) |
| c  | 20,615         | [organizing_metadata.py](02_data_preparation/scripts/02_organizing_metadata.py)           | [[neg_dss.tsv](02_data_preparation/files/folded_datasets/neg_dss.tsv) and [pos_dss.tsv](02_data_preparation/files/folded_datasets/pos_dss.tsv) | 

**Output**
| Set / Fold | Negative sequences | Positive sequences | Total sequences |
|:---: |:---: |:---: |:---: |
| [Benchmarking](02_data_preparation/files/training_sets/bench_rand.txt)    | 1,787           | 219             | 2,006          |
| [Fold 1](02_data_preparation/files/training_sets/tr_set1_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 2](02_data_preparation/files/training_sets/tr_set2_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 3](02_data_preparation/files/training_sets/tr_set3_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 4](02_data_preparation/files/training_sets/tr_set4_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 5](02_data_preparation/files/training_sets/tr_set5_rand_id.txt)    | 1,429           | 174             | 1,603          |

## 3. Data Analysis and Visualization 
**Objective:** understand the structure and characteristics of the dataset.

The data visualization step provides insights into the characteristics of the positive and negative protein datasets used in this study. The plots were generated in Python using **matplotlib** and **seaborn**.

The full description of the procedure can be found in the [README.md](03_data_analysis/README.md) of the data_analysis folder.

### Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| Analyses |
  |b| Plot Summary | 
  |c| Results|
  
### Results
| Description and Plot Type | Dataset | Filename | 
|:-----------:|:--------:|:----------:|
| Kingdom distribution <br> (Pie & Bar) | All | [kingdom_dist.pdf](03_data_analysis/visualization/kingdom_dist.pdf) | 
| Species distribution <br> (Pie & Bar) | All | [species_dist.pdf](03_data_analysis/visualization/species_dist.pdf) | 
| Sequence length distribution <br> (KDE Plot, Boxplot, Histogram) | All | [seq_length.pdf](03_data_analysis/visualization/seq_length.pdf) | 
| Signal Peptide length distribution <br> ((KDE Plot, Boxplot, Histogram) | Positive | [SP_length.pdf](03_data_analysis/visualization/SP_length.pdf) | 
| Residue composition <br> (Bar Plot) | All compared to SwissProt | [residue_composition.pdf](03_data_analysis/visualization/residue_composition.pdf) | 
| Signal Peptide cleavage site logos <br> (Sequence Logo) | Positive | [logo.pdf](03_data_analysis/visualization/logo.pdf)| 

**Note:** All plots and analyses are reproducible using the uploaded [Data_Visualization.ipynb](03_data_analysis/scripts/04_Data_Analysis.ipynb) notebook. 

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
The best models were selected by a grid search over the hyperparameters utilizing MCC as performance metric. <br>
Overall, the models built utilizing all features performed best. <br>

#### Models trained over ALL FEATURES:

**Selected Hyperparameters and best validation MCC:** 

  | Round | Kernel | C | Gamma | MCC | 
  | :---:  | :---:  | :---:  | :---:  |:---:  |
  |**1**| 'rbf' | 1 | 0.01 | 0.823 |
  |**2**| 'rbf' | 10 | 'scale' | 0.877 |
  |**3**| 'rbf' | 10 | 0.01 | 0.822 |
  |**4**| 'rbf' | 10 | 0.01 | 0.844 | 
  |**5**| 'rbf' | 10 | 0.01 | 0.856 |

**Performance Evaluation Metrics over Testing data:**
| Metrics    | Value    |
| :--------- | :-------------- |
| **MCC**        | 0.826 ± 0.030   |
| **Precision**  | 0.851 ± 0.038   |
| **Recall**     | 0.841 ± 0.039   |
| **Accuracy**   | 0.967 ± 0.007   |
| **F1 score**   | 0.845 ± 0.026   |



  #### Models trained over SELECTED FEATURES:

**Selected Hyperparameters and best validation MCC:** 

  | Round | Kernel | C | Gamma | MCC | 
  | :---:  | :---:  | :---:  | :---:  |:---:  |
  |**1**| 'rbf' | 0.1 | 'scale' | 0.802 |
  |**2**| 'rbf' | 10 | 'scale' | 0.849 |
  |**3**| 'rbf' | 10 | 0.01 | 0.807 |
  |**4**| 'rbf' | 1 | 'scale' | 0.807 | 
  |**5**|'rbf' | 1 | 'scale' | 0.857 |

**Performance Evaluation Metrics over Testing data:**


| Metrics      | Value           |
| :----------- | :-------------- |
| **MCC**      | 0.801 ± 0.018   |
| **Precision**| 0.849 ± 0.034   |
| **Recall**   | 0.796 ± 0.041   |
| **Accuracy** | 0.962 ± 0.003   |
| **F1 score** | 0.821 ± 0.016   |



  
## References 
1. Owji, Hajar & Nezafat, Navid & Negahdaripour, Manica & HajiEbrahimi, Ali & Younes, Ghasemi. (2018). A Comprehensive Review of Signal Peptides: Structure, Roles, and Applications. European Journal of Cell Biology. 97. 10.1016/j.ejcb.2018.06.003.
