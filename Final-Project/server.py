import http.server
import socketserver
from pathlib import Path
import termcolor
import json
from Seq1 import Seq

# Define the Server's port
PORT = 8080
parameters = '?content-type=application/json'
server = 'rest.ensembl.org'
conn = http.client.HTTPConnection(server)
BASES = ['A', 'C', 'G', 'T']

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

        # Command 2 is used to delete the interrogation mark.
        command2 = command[1].split('?')

        # This is the content before interrogation mark.
        first_w = command2[0]
        code = 404

        try:
            if first_w == "/":
                output = Path('indexf.html').read_text()
                code = 200

            else:
                try:
                    if first_w in '/listSpecies':  # /info/species?content-type=application/json
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
                            if len(lim_species) >= int(w2):
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
                            else:
                                output = Path('errorf.html').read_text()

                        output += '''<a href="/">Main page</a>
                                      </body>
                                      </html>'''

                    elif first_w in "/chromosomeLength":  # /info/assembly/homo_sapiens?content-type=application/json
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

                        if x2 == '':
                            output = Path('errorf.html').read_text()
                        elif w2 == '':
                            output = Path('errorf.html').read_text()
                        else:
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

                    elif first_w in '/karyotype':  # /info/assembly/homo_sapiens?content-type=application/json
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

                    try:

                        if first_w in '/geneSeq':  # /sequence/id/ENSG00000157764?content-type=text/plain
                            auxiliar_endpoint = 'xrefs/symbol/homo_sapiens/'
                            after_int = command2[1]
                            w1, w2 = after_int.split('=')
                            conn.request("GET", auxiliar_endpoint + w2 + parameters)
                            r1 = conn.getresponse()
                            data1 = r1.read().decode("utf-8")
                            auxiliar_console = json.loads(data1)
                            identificator = auxiliar_console[0]
                            id_gene = identificator['id']

                            endpoint = 'sequence/id/'
                            conn.request("GET", endpoint + id_gene + parameters)
                            r2 = conn.getresponse()
                            data2 = r2.read().decode("utf-8")
                            console = json.loads(data2)


                            output = f'''<!DOCTYPE html>
                                   <html lang = "en">            
                                   <head>  
                                   <meta charset = "utf-8"
                                     <title> SEQUENCE GENE </title>
                                     </head>
                                     <body style="background-color: lightblue;">       
                                  '''
                            sequence = f'{console["seq"]}'
                            output += f'<p> The sequence of gene {w2} is:  </p>'
                            output += f'<textarea rows = "100" "cols = 100"> {sequence} </textarea>'
                            output += '''<a href="/">Main page</a>
                                          </body>
                                          </html>'''

                        elif first_w in '/geneInfo':  # /lookup/id/ENSG00000157764?content-type=text/plain
                            auxiliar_endpoint = 'xrefs/symbol/homo_sapiens/'
                            after_int = command2[1]
                            w1, w2 = after_int.split('=')
                            conn.request("GET", auxiliar_endpoint + w2 + parameters)
                            r1 = conn.getresponse()
                            data1 = r1.read().decode("utf-8")
                            auxiliar_console = json.loads(data1)
                            identificator = auxiliar_console[0]
                            id_gene = identificator['id']

                            endpoint = 'lookup/id/'
                            conn.request("GET", endpoint + id_gene + parameters)
                            r2 = conn.getresponse()
                            data2 = r2.read().decode("utf-8")
                            console = json.loads(data2)

                            output = f'''<!DOCTYPE html>
                                  <html lang = "en">            
                                  <head>  
                                  <meta charset = "utf-8"
                                    <title> INFO ABOUT GENE {w2} </title>
                                    </head>
                                    <body style="background-color: lightblue;"> '''
                            output += f'<p> The gene is on chromosome {console["seq_region_name"]}</p>'
                            output += f'<p> The identificator is {id_gene}</p>'
                            output += f'<p> The gene start on position {console["start"]}</p>'
                            output += f'<p> The gene ends on position {console["end"]}</p>'
                            output += f'<p> The length of the gene is {console["end"] - console["start"]} </p>'
                            output += '''<a href="/">Main page</a>
                                         </body>
                                         </html>'''

                        elif first_w in '/geneCalc':  # /sequence/id/ENSG00000157764?content-type=text/plain
                            auxiliar_endpoint = 'xrefs/symbol/homo_sapiens/'
                            after_int = command2[1]
                            w1, w2 = after_int.split('=')
                            conn.request("GET", auxiliar_endpoint + w2 + parameters)
                            r1 = conn.getresponse()
                            data1 = r1.read().decode("utf-8")
                            auxiliar_console = json.loads(data1)
                            identificator = auxiliar_console[0]
                            id_gene = identificator['id']

                            endpoint = 'sequence/id/'
                            conn.request("GET", endpoint + id_gene + parameters)
                            r2 = conn.getresponse()
                            data2 = r2.read().decode("utf-8")
                            console = json.loads(data2)
                            sequence = Seq(console["seq"])

                            output = f'''<!DOCTYPE html>
                                      <html lang = "en">            
                                      <head>  
                                      <meta charset = "utf-8"
                                        <title> CALCULATIONS ABOUT GENE {w2} </title>
                                        </head>
                                        <body style="background-color: lightblue;"> '''
                            output += f'<p> The length of the gene is {sequence.len()}</p>'
                            for element in BASES:
                                output += f'\n{element}: {sequence.count_base(element)} ({sequence.count_base(element) * 100 / sequence.len()}%)'
                            output += '''\n<a href="/">Main page</a>
                                         </body>
                                         </html>'''

                        elif first_w in '/geneList':
                            endpoint = 'overlap/region/human/'
                            after_int = command2[1]
                            v1, v2, v3 = after_int.split('&')
                            w1, w2 = v1.split('=')  # w1 = chromo and w2 = value(chromo)
                            t1, t2 = v2.split("=")  # t1 = start and t2 = value (start)
                            z1, z2 = v3.split("=")  # z1 = ends and z2 = value (ends)
                            conn.request("GET",
                                         endpoint + w2 + ':' + t2 + '-' + z2 + '?feature=gene;content-type=application/json')
                            r1 = conn.getresponse()
                            data1 = r1.read().decode("utf-8")
                            console = json.loads(data1)
                            output = f'''<!DOCTYPE html>
                                      <html lang = "en">            
                                      <head>  
                                      <meta charset = "utf-8"
                                        <title> GENE LIST OF THE CHROMOSOME {w2} that starts at {t2} and ends at {z2} </title>
                                        </head>
                                        <body style="background-color: lightblue;"> '''
                            for element in console:
                                output += f'<p> - {element["external_name"]}</p>'

                            output += '''<a href="/">Main page</a>
                                         </body>
                                         </html>'''
                    except IndexError:
                        output = Path('errorf.html').read_text()

                except ValueError:
                    output = Path('errorf.html').read_text()

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