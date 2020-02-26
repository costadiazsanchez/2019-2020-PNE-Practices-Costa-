from Seq0 import *

FOLDER = "../Session 4./"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for i in genes:
    seq = seq_read_fasta(FOLDER+i+ext)
    dict = seq_count(seq)
    best = ''
    maximum = 0
    for x, val in dict.items():
        while val > maximum:
            maximum = val
            best = x
    print("Gene", i, ': Most frequent base:', best)