# SVM-Based Protein Classification

This repository contains the code and results for training and evaluating Support Vector Machine (SVM) classifiers to distinguish protein classes using a set of physicochemical and sequence-derived features. 
The pipeline implements robust feature extraction, model selection and systematic evaluation using cross-validation. The main goal of this repository is to classify protein sequences and understand which features most contribute to prediction accuracy. 
The analysis compares SVM models trained on all features against those trained on a subset selected via feature importance strategies.



### a. Data Preparation & Feature Extraction

a1. Protein sequence data is parsed and transformed into fixed length vectors using custom feature extraction functions.

a2. Extracted features encode amino acid composition, hydrophobicity, secondary structure propensity (alpha-helix, beta-sheet), charge and transmembrane helix propensity.

### b. Feature Scaling

All features are standardized using StandardScaler for optimal model convergence and fair weighting.

### c. SVM Model Training & Cross-validation
   
c1. Stratified cross-validation (5 folds) is used to split the data for robust assessment.

c2. Hyperparameters (C, gamma, and kernel) are optimized for each fold using grid search, maximizing the Matthews Correlation Coefficient (MCC) on the validation set.

### d. Feature Selection (For Selected Features Model)
   
d1. Random Forest feature importances and MCC curves are used to identify the most informative features for SVM classification.

d2. The optimal subset is chosen and a secondary SVM is retrained and evaluated.

### e. Evaluation & Metrics
   
e1. Test performance is aggregated over all folds.

e2. Metrics reported: MCC, Precision, Recall, Accuracy, and F1 score.


## Results

### Models trained over ALL FEATURES

Performance Evaluation Metrics over Testing data:

| Round      | MCC           | Precision      | Recall        | Accuracy      | F1 score      |
| :--------: | :-----------: | :------------: | :-----------: | :-----------: | :-----------: |
| **1**      | 0.853         | 0.923          | 0.817         | 0.976         | 0.867         |
| **2**      | 0.781         | 0.821          | 0.789         | 0.958         | 0.805         |
| **3**      | 0.839         | 0.841          | 0.874         | 0.968         | 0.857         |
| **4**      | 0.856         | 0.852          | 0.897         | 0.972         | 0.874         |
| **5**      | 0.802         | 0.819          | 0.826         | 0.961         | 0.824         |
| **Mean ± Std** | 0.826 ± 0.030 | 0.851 ± 0.038  | 0.841 ± 0.039 | 0.967 ± 0.007 | 0.845 ± 0.026 |


### Models trained over SELECTED FEATURES

Performance Evaluation Metrics over Testing data:

| Round         | MCC        | Precision   | Recall     | Accuracy   | F1 score   |
| :---:         | :---:      | :---:       | :---:      | :---:      | :---:      |
| **1**         | 0.799      | 0.914       | 0.731      | 0.963      | 0.813      |
| **2**         | 0.774      | 0.819       | 0.777      | 0.957      | 0.798      |
| **3**         | 0.822      | 0.849       | 0.834      | 0.967      | 0.841      |
| **4**         | 0.818      | 0.830       | 0.845      | 0.964      | 0.838      |
| **5**         | 0.791      | 0.832       | 0.794      | 0.960      | 0.813      |
| **Mean ± Std**| 0.801 ± 0.018 | 0.849 ± 0.034 | 0.796 ± 0.041 | 0.962 ± 0.003 | 0.821 ± 0.016 |


The full pipeline ensures that model selection is unbiased and performance is measured on unseen data. 
Random Forest feature importance is used as a guide but feature subset size is selected using validation performance curves. 
The included metrics provide a comprehensive view of model performance, especially for imbalanced datasets such as proteins.
