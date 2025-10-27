def repr_list(fasta, text):
	with open(fasta, "r") as reader:
		with open(text, "w") as writer:
			for line in reader:
				if line.startswith(">"):
					writer.write(line[1:])
if __name__=="__main__":
	from sys import argv 
	fasta_neg = argv[1]	
	fasta_pos = argv[2]
	ids_neg = argv[3]
	ids_pos = argv[4]
	repr_list(fasta_neg, ids_neg)
	repr_list(fasta_pos, ids_pos)	
