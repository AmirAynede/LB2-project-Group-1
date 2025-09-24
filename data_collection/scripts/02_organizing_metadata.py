import pandas as pd
from sys import argv
import time as t

neg_path = argv[1]
pos_path = argv[2]
neg_id_path = argv[3]
pos_id_path = argv[4]

col_labels = ["UniProt ID", "Species", "Kingdom", "Seq Length", "Cleavage Site", "TransM Helix 90", "T/B", "T_id"]
unf_neg = pd.read_csv(neg_path, sep = "\t", names = col_labels)
unf_pos = pd.read_csv(pos_path, sep = "\t",  names = col_labels)
neg_id_df = pd.read_csv(neg_id_path,sep = "\n", names = ["UniProt ID"])
pos_id_df = pd.read_csv(pos_id_path,sep = "\n", names = ["UniProt ID"])


#def filter_df(dataframe, id_file):

print(unf_neg.head(5))
print("")
print(unf_pos.head(5))
print("")
print(unf_neg[unf_neg["UniProt ID"].str.upper().str.strip().isin(
neg_id_df["UniProt ID"].str.upper().str.strip())])
print("")
print(unf_pos[unf_pos["UniProt ID"].str.upper().str.strip().isin(
pos_id_df["UniProt ID"].str.upper().str.strip())])
