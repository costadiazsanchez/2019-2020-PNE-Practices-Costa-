from Seq0 import *

FOLDER = "../Session 4./"
EXT = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN"]

for i in genes:
    seq = seq_read_fasta(FOLDER + i + EXT)
    print ("Gene", i," -----> Length:", seq_len(seq))