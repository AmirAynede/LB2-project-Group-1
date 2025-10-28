# 6.1 : Von Heijne Classifier Performance
## Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| **Data Organization** |
  |b| **Training:** <br> Building PSWM on Training data |
  |c| **Testing:** <br> Classification of Testing data|
  |d| **Performance Evaluation** |
  
### a. Data Organization
The whole dataset was organized into two tab separated files (.tsv) cointaining the necessary information for the final evaluation of the two classifiers. These files describe the [training](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/files/performance.tsv) and the [testing](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/files/benchmarking.tsv) data. Both can be found in the [06_performance/files](https://github.com/AmirAynede/LB2-project-Group-1/tree/main/06_performance/files) folder.
### b. Training
The Position Specific Weight Matrix (**PSWM**) was built on the whole positive training dataset, using 15 residue long Signal Peptide fragments which represent the most significant residues in the signal peptide. In particular, the 13 residues preceding the cleavage site and the 2 following the cleavage site.  
<br><br><br>
![PSWM](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/Von_Heijne/files/PSWM.png) 
<br><br><br>
### c. Testing
The optimal threshold was selected as the average of the values of the optimal thresholds found in the cross validation step, which description can be found in the dedicated folder: [04_vonHeijne](https://github.com/AmirAynede/LB2-project-Group-1/tree/main/04_vonHeijne). <br> <br>
The score computed utilizing the PSWM was obtained for each sequence in the testing dataset. Consequently, it was compared to the optimal threshold to infere the **presence** (*score > threshold*) or the **absence** (*score < threshold*) of the signal peptide. 
### d. Performance Evaluation
Finally, the prediction labels were compared to the true class labels to compute the following metrics: 
  | Metric | Value | 
  |:---:  | :---:  |
  |**Accuracy**| 0.9312 | 
  |**Precision**| 0.6614 | 
  |**Recall**| 0.7580 | 
  |**F1-score**| 0.7064 |
  |**MCC**| 0.6696| 
  | **Threshold** |   8.8089  |

 <br>
The results of this procedures were summarized in a confusion matrix:  <br><br><br>

![confusion matrix](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/Von_Heijne/files/CM.png)  <br><br><br>

