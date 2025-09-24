import pandas as pd
from sys import argv

'''
neg_path = "~/project/data_collection/output/eukarya_SP_neg.tsv"
pos_path = "~/project/data_collection/output/eukarya_SP_pos.tsv"
'''
neg_path = argv[1]
pos_path = argv[2]

unf_neg = pd.read_csv(neg_path, sep = "\t")
unf_pos = pd.read_csv(pos_path, sep = "\t")
