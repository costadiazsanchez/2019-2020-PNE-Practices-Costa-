import json
import http.client
import termcolor
from Seq1 import Seq

dict = {'SRCAP': 'ENSG00000080603', 'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379', 'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078', 'KDR':'ENSG00000128052', 'ANK2':'ENSG00000145362'}
bases = ['A', 'T', 'C', 'G']
input_name = input("Write the gene what you want to find data:")
server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
parameters = '?content-type=application/json'
url = server + endpoint + dict[input_name] + parameters

print("Server:", server)
print("URL: ", url)

# Connect with the server
conn = http.client.HTTPConnection(server)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", endpoint + dict[input_name] + parameters)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
console = json.loads(data1)
sequence = console['id']

termcolor.cprint('GENE:', 'green')
print(input_name)
termcolor.cprint("Description:", 'green')
print(console['desc'])
termcolor.cprint('Bases:', 'green')
print(console['seq'])

sequence = Seq(console['seq'])

termcolor.cprint('Total length:', 'green')
print(sequence.len())
termcolor.cprint ('A:', 'blue')
print(sequence.count_base('A'))
print('(', sequence.count_base('A')*100/sequence.len(), '%)')
termcolor.cprint ('C:', 'blue')
print(sequence.count_base('C'))
print('(', sequence.count_base('C')*100/sequence.len(), '%)')
termcolor.cprint ('G:', 'blue')
print(sequence.count_base('G'))
print('(', sequence.count_base('G')*100/sequence.len(), '%)')
termcolor.cprint ('T:', 'blue')
print(sequence.count_base('T'))
print('(', sequence.count_base('T')*100/sequence.len(), '%)')

total_bases = list(sequence.count().values())
maximum = max(total_bases)
termcolor.cprint("Most frequent base: ", 'green')
print(bases[total_bases.index(maximum)])
