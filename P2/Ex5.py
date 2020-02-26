from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


folder = '../Session 4/'
gene = 'U5.txt'
location = (folder + gene)

PORT = 8081
IP = '192.168.0.13'

c = Client(IP, PORT)
print(c)

seq = Seq().read_fasta(location)
c.debug_talk("Gene", gene, "to the server")
c.debug_talk(str(seq))



