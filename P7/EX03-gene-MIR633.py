import json
import http.client
import termcolor

dict = {'MIR633': 'ENSG00000207552'}

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
parameters = '?content-type=application/json'
url = server + endpoint + dict['MIR633'] + parameters

print("Server:", server)
print("URL: ", url)

# Connect with the server
conn = http.client.HTTPConnection(server)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", endpoint + dict['MIR633'] + parameters)
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
print('MIR633')
termcolor.cprint("Description:", 'green')
print(console['desc'])
termcolor.cprint('Bases:', 'green')
print(console['seq'])
