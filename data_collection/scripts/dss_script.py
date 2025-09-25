import pandas as pd
from sys import argv

'''import time as t

id_file = argv[1]
tsv_file = argv[2]
tsv_filtered = argv[3]

def filter_tsv(id_list, filename, newfile):
    with open(id_list, "r") as ids:
        with open(newfile, "a") as DAfile: 
            for line in ids:
                #line = line.upper().rstrip()
                with open(filename, "r") as data:
                    for l in data:
                        #linee = l.upper().rstrip()
                        if l.startswith(line.rstrip()):
                            DAfile.write(l.rstrip() + "\t0\n")

filter_tsv(id_file, tsv_file, tsv_filtered)

'''
neg = argv[1]
pos = argv[2]
neg_labels = ["UniProt_ID", "Species", "Kingdom", "Seq_Length", "TransM_Helix_90"]
pos_labels = ["UniProt_ID", "Species", "Kingdom", "Seq_Length", "Cleavage"]
unf_neg = pd.read_csv(neg, sep = "\t", names = neg_labels)
unf_pos = pd.read_csv(pos, sep = "\t",  names = pos_labels)

#def filter_df(dataframe, id_file):

print(unf_neg.head(5))
print("")
print(unf_pos.head(5))

