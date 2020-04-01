import json
import http.client
import termcolor

server = 'rest.ensembl.org'
endpoint = '/info/ping'
parameters = '?content-type=application/json'
url = server + endpoint + parameters

print("Server:", server)
print("URL: ", url)

# Connect with the server
conn = http.client.HTTPConnection(server)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", endpoint + parameters)
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
ping = console['ping']

if ping == 1:
    termcolor.cprint("The database is running! PING is OK", 'green')
else:
    termcolor.cprint("Database is not running well!", 'red')