import pandas as pd
from sys import argv

neg_path = argv[1]
#pos_path = argv[2]

col_labels = ["UniProt ID", "Species", "Kingdom", "Seq Length", "Cleavage Site", "TransM Helix 90", "T/B", "T_id"]
unf_neg = pd.read_csv(neg_path, sep = "\t", names = col_labels)
#unf_pos = pd.read_csv(pos_path, sep = "\t")

#def filter_df(dataframe, id_file):

print(unf_neg.head(5))

