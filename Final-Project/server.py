import http.server
import socketserver
from pathlib import Path
import termcolor
import json

# Define the Server's port
PORT = 8080
parameters = '?content-type=application/json'
server = 'rest.ensembl.org'
conn = http.client.HTTPConnection(server)

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        count = 0

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        command = self.requestline.split(' ')

        #Command 2 is used to delete the interrogation mark.
        command2 = command[1].split('?')

        #This is the content before interrogation mark.
        first_w = command2[0]
        code = 404

        try:
            if first_w == "/":
                output = Path('indexf.html').read_text()
                code = 200

            else:
                if first_w in '/listSpecies':
                    endpoint = 'info/species'
                    # The content after the interrogation mark.
                    after_int = command2[1]
                    w1, w2 = after_int.split('=')
                    conn.request("GET", endpoint + parameters)
                    r1 = conn.getresponse()
                    data1 = r1.read().decode("utf-8")
                    console = json.loads(data1)
                    lim_species = console['species']

                    if w2 == '':
                        output = f'''<!DOCTYPE html>
                               <html lang = "en">            
                               <head>  
                               <meta charset = "utf-8">
                                 <title> LIST OF SPECIES </title>
                                 </head>
                                 <body style="background-color: lightblue;">       
                                <p>The total number of species is {len(lim_species)}</p>
                                '''
                        for element in lim_species:
                            output += f'''<p> - {element["display_name"]}</p>'''
                            code = 200

                    else:
                        output = f'''<!DOCTYPE html>
                                   <html lang = "en">            
                                   <head>  
                                   <meta charset = "utf-8">
                                     <title> LIST OF SPECIES </title>
                                     </head>
                                     <body style="background-color: lightblue;">       
                                     <p>The total number of species is {len(lim_species)}</p>
                                     <p>The limit of species is {w2}.</p>
                                    <p>The name of the species are: </p>
                                   '''
                        for element in lim_species:
                            if count < int(w2):
                                output += f'<p> - {element["display_name"]}</p>'
                                count = count + 1
                                code = 200

                    output += '''<a href="/">Main page</a>
                                  </body>
                                  </html>'''

                elif first_w in "/chromosomeLength":
                    endpoint = 'info/assembly/'
                    after_int = command2[1]
                    v1, v2 = after_int.split('&')
                    w1, w2 = v1.split('=')
                    x1, x2 = v2.split('=')

                    conn.request("GET", endpoint + w2 + parameters)
                    r1 = conn.getresponse()
                    data1 = r1.read().decode("utf-8")
                    console = json.loads(data1)
                    chromo_data = console['top_level_region']
                    output = ''
                    for element in chromo_data:
                        if element['name'] == x2:
                            output += f'''<!DOCTYPE html>
                            <html lang = "en">            
                            <head> 
                            <meta charset = "utf-8">
                            <title> 3) </title>
                            </head>
                            <body style="background-color: lightblue;"> 
                            <p>The length of the chromosome is: {element['length']} </p>
                            <a href="/">Main page</a>
                            </body></html>'''
                    code = 200

                elif first_w in '/karyotype':
                    endpoint = 'info/assembly/'
                    after_int = command2[1]
                    w1, w2 = after_int.split('=')
                    conn.request("GET", endpoint + w2 + parameters)
                    r1 = conn.getresponse()
                    data1 = r1.read().decode("utf-8")
                    console = json.loads(data1)
                    karyo_data = console['karyotype']
                    output = f'''<!DOCTYPE html>
                           <html lang = "en">            
                           <head>  
                           <meta charset = "utf-8"
                             <title> THE NAME OF THE CHROMOSOMES ARE: </title>
                             </head>
                             <body style="background-color: lightblue;">       
                          '''

                    for element in karyo_data:
                        output += f'<p> - {element} </p>'

                    output += '''<a href="/">Main page</a>
                                  </body>
                                  </html>'''
                    code = 200

        except KeyError:
            output = Path('errorf.html').read_text()




        self.send_response(code)

            # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(output)))

            # The header is finished
        self.end_headers()

            # Send the response message
        self.wfile.write(str.encode(output))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()