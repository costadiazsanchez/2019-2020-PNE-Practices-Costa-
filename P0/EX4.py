from Seq0 import *

FOLDER = "../Session 4./"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for i in genes:
    seq = seq_read_fasta(FOLDER + i + ext)
    print ()
    print ("Gene: ", i)
    for e in bases:
        print(e, ":", seq_count_base(seq, e))