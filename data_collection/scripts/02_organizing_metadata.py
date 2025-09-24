import pandas as pd
from sys import argv

neg_path = argv[1]
#pos_path = argv[2]

unf_neg = pd.read_csv(neg_path, sep = "\t")
#unf_pos = pd.read_csv(pos_path, sep = "\t")

#def filter_df(dataframe, id_file):

print(unf_neg.head(5))

