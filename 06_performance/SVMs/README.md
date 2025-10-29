# 6.2 : SVM Classifier Performance
## Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| **Data Organization** |
  |b| **Feature Extraction** |
  |c| **Training:**|
  |c.1| Fitting model on training data features|
  |c.2| Feature Selection: <br> Random Forest|
  |c| **Testing:** <br> Classification of Testing data using final model|
  |d| **Performance Evaluation** |
  |e| **Visualization**|
### a. Data Organization
The whole dataset was organized into two tab separated files (.tsv) cointaining the necessary information for the final evaluation of the two classifiers. These files describe the [training](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/files/performance.tsv) and the [testing](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/files/benchmarking.tsv) data. Both can be found in the [06_performance/files](https://github.com/AmirAynede/LB2-project-Group-1/tree/main/06_performance/files) folder.
### b. Feature Extraction

### c. Training
#### c.1 Fitting model on training data features
#### c.2 Feature Selection: Random Forest
### d. Performance Evaluation
Finally, the prediction labels were compared to the true class labels to compute the following metrics: 
  | Metric | Value | 
  |:---:  | :---:  |
  |**Accuracy**|  | 
  |**Precision**|  | 
  |**Recall**|  | 
  |**F1-score**|  |
  |**MCC**| | 

 <br>
The results of this procedures were summarized in a confusion matrix:  <br><br><br>

### e. Visualization
#### Distribution of False Positives and False Negatives with respect to Kingdom and Species:
Using the [metadata](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/03_data_analysis/files/data.tsv) and the [results](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/results_SVM.tsv) of the SVM classification on the [testing](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/files/benchmarking.tsv) dataset, the Kingdom and Species distribution was plotted for both False Positives and False Negatives. 
<br><br>
[Kingdom Distribution: FP](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FP_kingdom.png): <br>
![Kingdom Distribution: FP](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FP_kingdom.png)
<br><br>
[Kingdom Distribution: FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FN_kingdom.png): <br>
![Kingdom Distribution: FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FN_kingdom.png)
<br><br>
[Species Distribution: FP](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FP_species.png): <br>
![Species Distribution: FP](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FP_species.png)
<br><br>
[Species Distribution: FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FN_species.png): <br>
![Species Distribution: FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/FN_species.png)
<br><br>
#### False Positive Rate: whole testing dataset vs TM-Helix carrying proteins
FPR is overall 0.02015.
Over false positives carrying a trans membrane domain in the first 90 residues the FPR is 0.07087
The FPR of sequences carryng a TM domain is 3.5178 times the FPR over all sequences.
#### Amino Acidic Composition comparison: True Positives vs False Negatives
[AA composition: TP vs FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/AA_Comp_TPvsFN.png)<br>
![AA composition: TP vs FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/AA_Comp_TPvsFN.png)
<br><br>
#### Features comparison: True Positives vs False Negatives
[Features: TP vs FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/Features_TPvsFN.png)<br>
![Features: TP vs FN](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/SVMs/files/Features_TPvsFN.png)
