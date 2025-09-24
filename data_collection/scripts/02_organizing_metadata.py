import pandas as pd

neg_path = "~/project/data_collection/output/eukarya_SP_neg.tsv"
pos_path = "~/project/data_collection/output/eukarya_SP_pos.tsv"
unf_neg = pd.read_csv(neg_path, sep = "\t")
unf_pos = pd.read_csv(pos_path, sep = "\t")
