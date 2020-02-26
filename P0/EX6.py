from Seq0 import *

FOLDER = "../Session 4./"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

gene = genes[0]
print ("Gene", gene, ":")
seq = seq_read_fasta(FOLDER+genes[0]+ ext)[:20]
reverse = seq_reverse(seq)
print ("Fragment:", seq)
print("Reverse:", reverse)