## von Heijne Method for Signal Peptide Detection
**Objective:** To classify protein sequences as *secretory (SP+)* or *non-secretory (SP–)* by modeling the conserved amino acid composition and positional patterns typical of signal peptides.

### a. Data Organization
The dataset was derived from the **training set** used in the main pipeline, containing 15-residue fragments around SP cleavage sites for positive sequences and equivalent regions for negatives.  
A 5-fold cross-validation scheme was applied.

### b. Training
#### b.1 Position-Specific Weight Matrix (PSWM) Computation
A PSWM was computed from the 15-residue fragments of positive sequences.  
Each position in the fragment is scored according to the log-ratio between observed amino acid frequencies and background frequencies from the SwissProt database.

**Formula:**

$$
\text{PSWM}_{i,j} = \log_2 \left( \frac{f_{i,j} + 1}{p_i} \right)
$$

where:  
- $f_{i,j}$ = frequency of amino acid $i$ at position $j$ in the training fragments  
- $p_i$ = background frequency of amino acid $i$ in SwissProt

**Visualization:** PSWM heatmaps were generated to visualize the positional amino acid preferences. Annotated log2 enrichment scores highlighted over- and under-represented residues, confirming hydrophobic enrichment and the canonical **A–X–A motif**.

### c. Validation
#### c.1 Sequence Scoring
Each 90-residue sequence fragment is scanned using a sliding 15-residue window.  
The **maximum PSWM score** across the window is retained as the sequence score.

#### c.2 Optimal Threshold Selection
Precision–Recall curves were computed using validation data.  
The **F1-maximizing threshold** was selected for each round.

**Visualization:** Precision–Recall curves were used to show model performance per fold and combined across folds. Optimal thresholds were highlighted to indicate the best trade-off between precision and recall.

### d. Testing
#### d.1 Sequences Classification
Sequences from the test fold were scored using the trained PSWM and classified according to the optimal threshold from the corresponding validation fold.
**Visualization:** Confusion matrices were used to display true positives, true negatives, false positives, and false negatives. Colored cells enhanced visual distinction between correct and incorrect predictions.

### e. Performance Evaluation
Performance metrics were computed for each cross-validation round and averaged:

| Metric | Mean ± SD |
|:--|:--:|
| **Accuracy** | 0.9320 ± 0.0085 |
| **Precision** | 0.6830 ± 0.0646 |
| **Recall** | 0.7300 ± 0.0560 |
| **F1 Score** | 0.7012 ± 0.0226 |
| **MCC** | 0.6664 ± 0.0258 |
| **Optimal Threshold** | 8.8089 ± 0.5967 |

## Interpretation of Results
- The *von Heijne* method reliably classifies signal peptides.  
- **MCC** is the most informative metric, reflecting consistent performance under class imbalance.  
- **Accuracy** is inflated due to the skewed dataset and should not be used alone.  
- **PSWM heatmaps** reveal biologically meaningful patterns:  
  - Enrichment of **hydrophobic residues** (Leucine, Alanine).  
  - Depletion of **charged residues**.  
  - Confirmation of the canonical **A–X–A motif** at cleavage sites.  
- **Precision–Recall (PR) curves** are preferred over ROC curves for evaluation under imbalance.  
- The **average PR curve across folds** shows stable and robust classifier behavior.

## Output Files

| Description| Dataset | Filename |
|:-------------------------:|:-------:|:--------:|
| Position-Specific Weight Matrix (PSWM) per fold <br> (Heatmap) | Training fold | [PSWM_round1.pdf](./visualization/PSWM_round1.pdf) <br> [PSWM_round2.pdf](./visualization/PSWM_round2.pdf) <br> [PSWM_round3.pdf](./visualization/PSWM_round3.pdf) <br> [PSWM_round4.pdf](./visualization/PSWM_round4.pdf) <br> [PSWM_round5.pdf](./visualization/PSWM_round5.pdf) |
| Combined PSWM across all folds <br> (Heatmap) | All folds | [PSWMs_all_rounds.pdf](./visualization/PSWMs_all_rounds.pdf) |
| Precision–Recall Curve per fold | Validation fold | [PRC_round1.pdf](./visualization/PRC_round1.pdf) <br> [PRC_round2.pdf](./visualization/PRC_round2.pdf) <br> [PRC_round3.pdf](./visualization/PRC_round3.pdf) <br> [PRC_round4.pdf](./visualization/PRC_round4.pdf) <br> [PRC_round5.pdf](./visualization/PRC_round5.pdf) |
| Combined Precision–Recall Curve across folds | All folds | [PRC_all_rounds.pdf](./visualization/PRC_all_rounds.pdf) |
| Confusion Matrix per fold <br> (TP, TN, FP, FN) | Testing fold | [CM_round1.pdf](./visualization/CM_round1.pdf) <br> [CM_round2.pdf](./vonHeijne/CM_round2.pdf) <br> [CM_round3.pdf](./visualization/CM_round3.pdf) <br> [CM_round4.pdf](./visualization/CM_round4.pdf) <br> [CM_round5.pdf](./visualization/CM_round5.pdf) |
| Combined Confusion Matrix across folds | All folds | [CM_all_rounds.pdf](./visualization/CM_all_rounds.pdf) |

---

## Implementation Notes

The full implementation is provided in the Jupyter notebook [06_vonHeijne.ipynb](./scripts/06_vonHeijne.ipynb), developed using:
- **Python 3.10+**
- **NumPy**, **Pandas**
- **Matplotlib**, **Seaborn**
- **scikit-learn** (for metrics and precision–recall analysis)
