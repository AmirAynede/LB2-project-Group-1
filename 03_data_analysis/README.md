## Data Analysis and Visualization 
**Objective:** understand the structure and characteristics of the dataset.

The data visualization step provides insights into the characteristics of the positive and negative protein datasets used in this study. The plots were generated in Python using **matplotlib** and **seaborn**.

### a. Analyses

- **Taxonomic Distribution:** Kingdom and species distributions for both training and benchmarking datasets were analyzed to ensure representative sampling across major eukaryotic groups.  
- **Sequence Length:** Distribution of sequence lengths was compared between positive and negative datasets, as well as between training and benchmarking subsets.  
- **Signal Peptide (SP) Length:** Length distributions of SPs in the positive dataset were analyzed for both training and benchmarking sequences.  
- **Amino Acid Composition:** Residue composition of SPs was compared against the SwissProt background distribution.  
- **Sequence Logos:** Cleavage site motifs of SPs were visualized using [WebLogo](https://weblogo.berkeley.edu/logo.cgi), highlighting conserved positions.

### b. Plot Summary

| Plot Type | Dataset | Filename | Description |
|:-----------:|:--------:|:----------:|:-------------:|
| Pie & Bar | Training | [t_kingdom.pdf](data_analysis/visualization/t_kingdom.pdf) | Kingdom distribution of training sequences |
| Pie & Bar | Positive Training | [pos_t_kingdom.pdf](data_analysis/visualization/pos_t_kingdom.pdf) | Kingdom distribution of positive training sequences |
| Pie & Bar | Negative Training | [neg_t_kingdom.pdf](data_analysis/visualization/neg_t_kingdom.pdf) | Kingdom distribution of negative training sequences |
| Pie & Bar | Benchmarking | [b_kingdom.pdf](data_analysis/visualization/b_kingdom.pdf) | Kingdom distribution of benchmarking sequences |
| Pie & Bar | Positive Benchmarking | [pos_b_kingdom.pdf](data_analysis/visualization/pos_b_kingdom.pdf)  | Kingdom distribution of positive benchmarking sequences |
| Pie & Bar | Negative Benchmarking | [neg_b_kingdom.pdf](data_analysis/visualization/neg_b_kingdom.pdf) | Kingdom distribution of negative benchmarking sequences |
| Pie & Bar | Training | [t_species.pdf](data_analysis/visualization/t_species.pdf) <br> [t_species_bar.pdf](data_analysis/visualization/t_species_bar.pdf)| Species distribution of training sequences |
| Pie & Bar | Positive Training | [pos_t_species.pdf](data_analysis/visualization/pos_t_species.pdf) <br> [pos_t_species_bar.pdf](data_analysis/visualization/pos_t_species_bar.pdf)| Species distribution of positive training sequences |
| Pie & Bar | Negative Training | [neg_t_species.pdf](data_analysis/visualization/neg_t_species.pdf) <br> [neg_t_species_bar.pdf](data_analysis/visualization/neg_t_species_bar.pdf)| Species distribution of negative training sequences |
| Pie & Bar | Benchmarking | [b_species.pdf](data_analysis/visualization/b_species.pdf) <br> [b_species_bar.pdf](data_analysis/visualization/b_species_bar.pdf) | Species distribution of benchmarking sequences |
| Pie & Bar | Positive Benchmarking | [pos_b_species.pdf](data_analysis/visualization/pos_b_species.pdf) <br> [pos_b_species_bar.pdf](data_analysis/visualization/pos_b_species_bar.pdf)| Species distribution of positive benchmarking sequences |
| Pie & Bar | Negative Benchmarking | [neg_b_species.pdf](data_analysis/visualization/neg_b_species.pdf) <br> [neg_b_species_bar.pdf](data_analysis/visualization/neg_b_species_bar.pdf)| Species distribution of negative benchmarking sequences |
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
| KDE | Positive | [SP_length_dist.pdf](data_analysis/visualization/SP_length_dist.pdf) | Signal peptide length distribution |
| Boxplot | Positive | [SP_length_box.pdf](data_analysis/visualization/SP_length_box.pdf) | Signal peptide length distribution |
| Histogram | Positive | [SP_length_hist.pdf](data_analysis/visualization/SP_length_hist.pdf) | SP length probability distribution |
| Bar Plot | All | [residue_composition.pdf](data_analysis/visualization/residue_composition.pdf) | Amino acid composition: Training, Benchmarking, SwissProt |
| Sequence Logo | Positive | [t_logo.png](data_analysis/visualization/t_logo.png) | SP cleavage site logos Training (via WebLogo) |
| Sequence Logo | Positive | [b_logo.png](data_analysis/visualization/b_logo.png) | SP cleavage site logos Benchmarking (via WebLogo) |

**Note:** All plots and analyses are reproducible using the uploaded [Data_Visualization.ipynb](data_analysis/scripts/04_Data_Analysis.ipynb) notebook. 

## Major conclusions of data analysis
**Taxonomic distribution:**
- Kingdom distribution: most proteins belong to Metazoa, followed by Fungi and Viridiplantae. Training and benchmarking sets share a similar taxonomic composition.
- Species distribution: most proteins belong to Homo sapiens. Training and benchmarking sets share a similar taxonomic composition.
  
**Protein sequence length:**
- Protein length: No significant difference between training (T) and benchmarking (B) sets. So no bias was introduced by data splitting.
- Positive dataset proteins tend to be shorter.
- Negative dataset proteins behave more “normally.”
- Protein length cannot be used to separate datasets.

**Signal peptide length:**
- Median length ≈ 20–25 residues, consistent with biological expectations.
- SPs shorter than 14 residues were filtered out.

**Residue composition:**
- Apolar residues (especially Leucine, Alanine and Valine) are highly enriched; L occurs about twice as frequently compared to SwissProt.
- Hydrophobic residues dominate, as expected for SPs.
- Charged residues are underrepresented compared to SwissProt.
- Overrepresentation of hydrophobic/apolar residues and underrepresentation of charged residues can be exploited as SP features.

**Sequence logo:**
- Clear hydrophobic core observed in the peptide before the cleavage site.
- Conserved cleavage site motif: X-Ala-X.
- Training vs. benchmarking: No major compositional differences detected, whcich translates to good dataset splitting.
