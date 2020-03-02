from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


folder = '../Session 4/'
gene = 'FRAT1.txt'
location = (folder + gene)
length = 10

PORT1 = 8080
PORT2 = 8081
IP = '192.168.0.13'

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print(c1)
print(c2)

seq = Seq().read_fasta(location)
b_string = str(seq)
print(f"Gene {gene}: {b_string}")
c1.talk(f"Gene {gene} win fragment of {length} elements: ")
c2.talk(f"Gene {gene} win fragment of {length} elements: ")
for element in range(10):
    fragment = b_string[element*length:(element+1)*length]
    print (f"Fragment {element+1}: {fragment}")
    if element % 2:
        c2.talk(f"Fragment {element+1}: {fragment}")
    else:
        c1.talk(f"Fragment {element+1}: {fragment}")

