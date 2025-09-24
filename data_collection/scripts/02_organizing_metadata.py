import pandas as pd
from sys import argv
import time as t

neg_file = argv[1]
pos_file = argv[2]
neg_id = argv[3]
pos_id = argv[4]

THE_tsv = argv[5]

def filter_tsv(filename, id_list, newfile):
    with open(id_list, "r") as ids:
        with open(filename, "r") as data:
            with open(newfile, "a") as DAfile: 
                for line in ids:
                    print(line)
                    t.sleep(5)
                    for l in data:
                        print(l)
                        t.sleep(5)
                        if l.startswith(line.rstrip()):
                            DAfile.write(l)
                            break

filter_tsv(pos_file,pos_id,THE_tsv)
filter_tsv(neg_file,neg_id,THE_tsv)

'''
col_labels = ["UniProt ID", "Species", "Kingdom", "Seq Length", "Cleavage Site", "TransM Helix 90", "T/B", "T_id"]
unf_neg = pd.read_csv(neg_path, sep = "\t", names = col_labels)
unf_pos = pd.read_csv(pos_path, sep = "\t",  names = col_labels)

#def filter_df(dataframe, id_file):

print(unf_neg.head(5))
print("")
print(unf_pos.head(5))

"""


unf(r) and fil (w):
for line in unf:
    if line.startswith(line id):
        filter.writeline
'''