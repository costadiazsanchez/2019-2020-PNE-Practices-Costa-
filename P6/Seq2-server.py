import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080
sequence = ['AAAAAAAAAAAAAAAA', 'GGGGGGGGGGGGGGG','TTTTTTTTTTTTTTT', 'CCCCCCCCCCCCCCCCCCC', 'ACGTACGTACGTACGT']
FOLDER = "../P6/"
EXT = ".txt"

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        command = self.requestline.split(' ')
        #Command 2 is used to delete the interrogation mark.
        command2 = command[1].split('?')
        #This is the content before interrogation mark.
        first_w = command2[0]
        output = Path('error.html').read_text()
        code = 404

        if first_w == "/":
            output = Path('ex4.html').read_text()
            code = 200

        elif first_w == '/ping':
            output = Path('ping.html').read_text()
            code = 200

        elif first_w == '/get':
            # This is the content after interrogation mark.
            after_int = command2[1]
            # After interrogation mark there are two words, a name and a the value of the name, that are separated by an equal mark.
            w1, w2 = after_int.split('=')
            x = int(w2)
            sequence_n = sequence[x]

            output = f'''<!DOCTYPE html>
            <html lang = "en">
            <head>
            <meta charset = "utf-8">
            <title> RESULT </title>
            </head> 
            <body>
            <h2> Sequence number: {x} </h2>
            <p> {sequence_n} </p>
            <a href="/">Main page</a>
            </body>
            </html>'''
            code = 200

        elif first_w == '/gene':
            # This is the content after interrogation mark.
            after_int = command2[1]
            # After interrogation mark there are two words, a name and a the value of the name, that are separated by an equal mark.
            w1, w2 = after_int.split('=')
            seq = Seq()
            sequence_g = str(seq.read_fasta(FOLDER + w2 + EXT))

            output = f'''<!DOCTYPE html>
                       <html lang = "en">
                       <head>
                       <meta charset = "utf-8">
                       <title> RESULT </title>
                       </head> 
                       <body>
                       <h2> Gene: {w2} </h2>
                       <p> {sequence_g} </p>
                       <a href="/">Main page</a>
                       </body>
                       </html>'''
            code = 200

        elif first_w == '/operation':
            final = ''
            # This is the content after interrogation mark.
            after_int = command2[1]
            check = after_int.split('&')
            # After interrogation mark there are two words, a name and a the value of the name, that are separated by an equal mark.
            w1, w2 = check[0].split('=')
            x1, x2 = check[1].split('=') #x2 es la opción elegida.
            seq = Seq(w2)
            if x2 == 'Comp':
                final = seq.complement()
            elif x2 == 'Rev':
                final = seq.reverse()
            elif x2 == 'Info':
                length = seq.len()
                count_A = seq.count_base('A')
                count_C = seq.count_base('C')
                count_G = seq.count_base('G')
                count_T = seq.count_base('T')
                perc_A = round(((count_A*100)/length), 3)
                perc_C = round(((count_C * 100)/length), 3)
                perc_G = round(((count_G * 100) / length), 3)
                perc_T = round(((count_T * 100) / length), 3)

                final = f'Total length: {length}\n A: {count_A} ({perc_A}%)\n C: {count_C} ({perc_C}%)\n G: {count_G} ({perc_G}%)\n T: {count_T} ({perc_T}%)'
                code = 200

            output = f'''<!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8"
                        <title> RESULT </title>
                        </head> 
                        <body>
                        <h2> Sequence:</h2>
                        <p> {w2} </p>
                        <h2> Operation:</h2>
                        <p> {x2} </p>
                        <h2> Result: </h2>
                        <p> {final} </p>
                        <a href="/">Main page</a>
                        </body>
                        </html>'''

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