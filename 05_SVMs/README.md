# SVM-Based Protein Classification

**Objective:** training and evaluating Support Vector Machine (SVM) classifiers to distinguish protein classes using a set of physicochemical and sequence-derived features. 


### a. Data Preparation & Feature Extraction

Protein sequence data was parsed and transformed into fixed length vectors using custom feature extraction functions.

Extracted features encode:
- Amino acid composition
- Hydrophobicity
- Secondary structure propensity (alpha-helix, beta-sheet)
- Charge
- Transmembrane helix propensity

All the scales were retrieved from [ProtScale](https://web.expasy.org/protscale/).

For this task, the Jupyter notebook [08_SVM_main.ipynb](./scripts/08_SVM_main.ipynb) was used.

### b. Feature Scaling

All features are standardized using StandardScaler for optimal model convergence and fair weighting.

### c. SVM Model Training & Cross-validation
   
Stratified cross-validation (5 folds) is used to split the data for robust assessment.

Hyperparameters (C, gamma, and kernel) are optimized for each fold using grid search, maximizing the Matthews Correlation Coefficient (MCC) on the validation set.

### d. Feature Selection (For Selected Features Model)
   
Random Forest feature importances and MCC curves are used to identify the most informative features for SVM classification.

The optimal subset is chosen and a secondary SVM is retrained and evaluated.

The top features contributing to SVM model performance, as identified by Random Forest Gini importance in round 1, are visualized below:

![Top Features (Round 1)](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/05_SVMs/files/Top_Features_round1.jpg?raw=true)

This bar plot ranks the twenty most important features contributing to the SVM model, as determined by Random Forest Gini importance in round 1.

### e. Performance Evaluation
   
Test performance is aggregated over all folds.

Metrics reported: MCC, Precision, Recall, Accuracy, and F1 score.

#### Models trained over ALL FEATURES

Performance Evaluation Metrics over Testing data:

| Round      | MCC           | Precision      | Recall        | Accuracy      | F1 score      |
| :--------: | :-----------: | :------------: | :-----------: | :-----------: | :-----------: |
| **1**      | 0.853         | 0.923          | 0.817         | 0.976         | 0.867         |
| **2**      | 0.781         | 0.821          | 0.789         | 0.958         | 0.805         |
| **3**      | 0.839         | 0.841          | 0.874         | 0.968         | 0.857         |
| **4**      | 0.856         | 0.852          | 0.897         | 0.972         | 0.874         |
| **5**      | 0.802         | 0.819          | 0.826         | 0.961         | 0.824         |
| **Mean ± Std** | 0.826 ± 0.030 | 0.851 ± 0.038  | 0.841 ± 0.039 | 0.967 ± 0.007 | 0.845 ± 0.026 |

#### Models trained over SELECTED FEATURES

Performance Evaluation Metrics over Testing data:

| Round         | MCC        | Precision   | Recall     | Accuracy   | F1 score   |
| :---:         | :---:      | :---:       | :---:      | :---:      | :---:      |
| **1**         | 0.799      | 0.914       | 0.731      | 0.963      | 0.813      |
| **2**         | 0.774      | 0.819       | 0.777      | 0.957      | 0.798      |
| **3**         | 0.822      | 0.849       | 0.834      | 0.967      | 0.841      |
| **4**         | 0.818      | 0.830       | 0.845      | 0.964      | 0.838      |
| **5**         | 0.791      | 0.832       | 0.794      | 0.960      | 0.813      |
| **Mean ± Std**| 0.801 ± 0.018 | 0.849 ± 0.034 | 0.796 ± 0.041 | 0.962 ± 0.003 | 0.821 ± 0.016 |

The effect of including more top features on model performance is visualized below. This plot was used to select the optimal number of features for the SVM:

![MCC vs Validation Size (Round 1)](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/05_SVMs/files/MCC_vs_Val_round1.jpg?raw=true)

This curve illustrates how the SVM’s validation MCC changes as more top-ranked features are included, informing optimal feature subset selection.


To summarize prediction results, the combined confusion matrix across all test sets is shown. It reports the aggregate true/false positive and negative counts, highlighting robust model performance:

![Combined Confusion Matrix (5 Rounds)](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/05_SVMs/files/CM_all_combined.jpg?raw=true)

This matrix summarizes the overall prediction results, showing true positives, true negatives, false positives, and false negatives for the test sets across all cross-validation rounds.


The full pipeline ensures that model selection is unbiased and performance is measured on unseen data. 
Random Forest feature importance is used as a guide but feature subset size is selected using validation performance curves. 
The included metrics provide a comprehensive view of model performance, especially for imbalanced datasets such as proteins.
