from sys import argv

def clean_fasta(fasta, new):
    with open(fasta, "r") as reader:
        with open(new, "w") as writer:
            for line in reader: 
                if line.startswith(">"):
                    line = line.split("|")
                    writer.write("\n"+line[0][0]+line[1]+"\n")
                else:
                    writer.write(line.strip())
        
        

if __name__ == "__main__":
    fasta = argv[1]
    new = argv[2]
    clean_fasta(fasta, new)