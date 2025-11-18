# 6: Performance Evaluation of Classifiers (Von Heijne, SVM)
## Workflow
  | Section | Title |
  | :---:  | :---:  |
  |a| **Data Organization** |
  |b| **Performance Evaluation of Von Heijne Method** |
  |c| **Performance Evaluation of SVM Method** |
  |d| **Analysis of Results** |
  
### a. Data Organization
The whole dataset was organized into two tab separated files (.tsv) cointaining the necessary information for the final evaluation of the two classifiers. These files describe the [training](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/files/performance.tsv) and the [testing](https://github.com/AmirAynede/LB2-project-Group-1/blob/main/06_performance/files/benchmarking.tsv) data. <br>
For each sequence, the files report: <br>
  
  | UniProt ID | Class |Fold Label |	Sequence| SP| Prediction |	Cleavage Site |Sequence Length |	TM Helix |
  | :---:  | :---:  |:---:  | :---:  |:---:  |:---:  | :---:  |:---:  | :---:  |
  | P47710 |	1| 	0| 	MRLLILTCL...KMESSISSS|	LLILTCLVAVALARP|	0	|15.0|	185|	False|
  | ... |	1| 	0| 	...|	...|	0	|...|	...|	False|
  | ... |	1| 	0| 	...|	...|	0	|...|	...|	False|
  | ... |	1| 	0| 	...|	...|	0	|...|	...|	False|
  | ... |	1| 	0| 	...|	...|	0	|...|	...|	False|
  | Q96GZ6 |	0	|0	|MDGTETRQR...WAGMLLDYF	|NIL	|0	|0.0|	507|	True |	0| 	0| 
  | ... |	0| 	0| 	...|	...|	0	|...|	...|	False|
  | ... |	0| 	0| 	...|	...|	0	|...|	...|	True|
  | ... |	0| 	0| 	...|	...|	0	|...|	...|	False|
  | ... |	0| 	0| 	...|	...|	0	|...|	...|	False|


<br>
Where:

* UniProt ID: all protein IDs.
* Class: Label addressing class of the protein.
  - **1** for positive class proteins, the ones having the signal peptide.
  - **2** for negative class proteins not having the signal peptide.  
* Fold Label: addressing for the fold to which the protein is assigned:
  - 0 = Testing data
  - 1 = 1st fold of training data
  - 2 = 2nd fold of training data
  - 3 = 3rd fold of training data
  - 4 = 4th fold of training data
  - 5 = 5th fold of training data 
* Sequence: first 90 residues of the sequence are reported.
* SP: relevant signal peptide residues for positive sequences, 'NIL' for negatives. 
* Prediction: initially set to 0, updated after each procedure is performed.
* Cleavage Site: reports the cleavage position for positive sequences, 0 for negatives.
* Sequence Length: reports the sequence lenght.
* TM Helix: reports 'True' for negative sequences having a Trans-Membrane domain in the first 90 residues, 'False' otherwise. 

<br>Both can be found in the [06_performance/files](https://github.com/AmirAynede/LB2-project-Group-1/tree/main/06_performance/files) folder.

### d. Analysis of Results:
#### d.1 Von Heijne
#### d.2 SVM
Details can be found in the [README](https://github.com/AmirAynede/LB2-project-Group-1/tree/main/06_performance/SVMs) of the [SVMs](https://github.com/AmirAynede/LB2-project-Group-1/tree/main/06_performance/SVMs) performance evaluation folder.





