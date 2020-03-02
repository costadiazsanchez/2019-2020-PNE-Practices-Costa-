from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


folder = '../Session 4/'
gene = 'FRAT1.txt'
location = (folder + gene)
length = 10

PORT = 8081
IP = '192.168.0.13'

c = Client(IP, PORT)
print(c)

seq = Seq().read_fasta(location)
b_string = str(seq)
print(f"Gene {gene}: {b_string}")
c.talk(f"Gene {gene} win fragment of {length} elements: ")
for element in range(5):
    fragment = b_string[element*length:(element+1)*length]
    print (f"Fragment{element+1}: {fragment}")
    c.talk(f"Fragment{element+1}: {fragment}")

