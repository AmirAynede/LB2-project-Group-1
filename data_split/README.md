## Data Preparation 🗂️
**Objective:** Reduce redundancy in the datasets, generate training and benchmarking sets, and create 5-fold cross-validation subsets for robust model evaluation

### a. Clustering
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
|:---:|:---:|:---:|:---:|
| Positive  | 2,932          | 1,093            | [cluster-results-pos_rep_seq.fasta](files/cluster_output/cluster-results-pos_rep_seq.fasta)
| Negative  | 20,615         | 8,934            | [cluster-results-neg_rep_seq.fasta](files/cluster_output/cluster-results-neg_rep_seq.fasta)

### b. Extract Representative IDs
A custom Python script was used to extract the IDs of representative sequences from the clustered FASTA files and can be found in [extract_rep_ids.py](scripts/01_extract_rep_ids.py).

Execution:
```bash
python extract_representative_ids.py neg.fasta pos.fasta neg_rep_id.txt pos_rep_id.txt
 ```
The final files are: [neg_rep_id.txt](files/cluster_output/neg_rep_id.txt) and [pos_rep_id.txt](files/cluster_output/pos_rep_id.txt).

### c. Metadata Collection
**Randomization:** Representative sequences were randomized to avoid biases. The final files are: [neg_rand_id.txt](files/cluster_output/neg_rand_id.txt) and [pos_rand_id.txt](files/cluster_output/pos_rand_id.txt).

The original TSV files were filtered to retain only the representative sequences with the script [organizing_metadata.py](scripts/02_organizing_metadata.py).
The filtered TSVs contain:
- UniProt ID
- Species
- Kingdom
- Sequence length
- Cleavage site / Transmembrane helix (as relevant)
- Training/Benchmark label 
- Fold assignment 

The final files are: [neg_dss.tsv](files/folded_datasets/neg_dss.tsv) and [pos_dss.tsv](files/folded_datasets/pos_dss.tsv).

### d. Data Splitting and Cross-Validation
**Split of positive and negative datasets:** 
- 80%: training sets
- 20%: benchmarking set

**5-Fold Cross-Validation:**
- The training set was split into 5 folds while preserving the positive/negative ratio.
- Each protein’s fold assignment was recorded in the .tsv file for reproducibility (the label 0 means benchmarking set).
- This ensures that models can be trained and validated without data leakage.

| Set / Fold | Negative sequences ID file | Positive sequences ID file | 
|:---:|:---:|:---:|
| Benchmarking    | [neg_bench_id.txt](files/cluster_output/neg_bench_id.txt)           | [pos_bench.txt](files/cluster_output/pos_bench.txt)               | 
| Fold 1    | [neg_tr1_id.txt](files/cluster_output/neg_tr1_id.txt)               | [pos_tr1_id.txt](files/cluster_output/pos_tr1_id.txt)            | 
| Fold 2    | [neg_tr2_id.txt](files/cluster_output/neg_tr2_id.txt)            | [pos_tr2_id.txt](files/cluster_output/pos_tr2_id.txt)             | 
| Fold 3    | [neg_tr3_id.txt](files/cluster_output/neg_tr3_id.txt)            | [pos_tr3_id.txt](files/cluster_output/pos_tr3_id.txt)            | 
| Fold 4    | [neg_tr4_id.txt](files/cluster_output/neg_tr4_id.txt)            | [pos_tr4_id.txt](files/cluster_output/pos_tr4_id.txt)            | 
| Fold 5    | [neg_tr5_id.txt](files/cluster_output/neg_tr5_id.txt)            | [pos_tr5_id.txt](files/cluster_output/pos_tr5_id.txt)            | 


### e. Output
| Set / Fold | Negative sequences | Positive sequences | Total sequences |
|:---: |:---: |:---: |:---: |
| [Benchmarking](files/training_sets/bench_rand.txt)    | 1,787           | 219             | 2,006          |
| [Fold 1](files/training_sets/tr_set1_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 2](files/training_sets/tr_set2_rand_id.txt)    | 1,430           | 175             | 1,605          |
| [Fold 3](files/training_sets/tr_set3_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 4](files/training_sets/tr_set4_rand_id.txt)    | 1,429           | 175             | 1,604          |
| [Fold 5](files/training_sets/tr_set5_rand_id.txt)    | 1,429           | 174             | 1,603          |
