from Seq0 import *

FILENAME = "U5.txt"
FOLDER = "../Session 4./"
FILE = FOLDER + FILENAME

seq = seq_read_fasta(FILE)
print ("DNA file: ", FILENAME)
print ("The first 20 bases are: ", seq[:20])