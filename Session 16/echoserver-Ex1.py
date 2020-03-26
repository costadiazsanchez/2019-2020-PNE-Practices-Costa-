import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080
sequence = ['AAAAAAAAAAAAAAAA', 'GGGGGGGGGGGGGGG','TTTTTTTTTTTTTTT', 'CCCCCCCCCCCCCCCCCCC', 'ACGTACGTACGTACGT']
FOLDER = "../Session 4/"
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
            first_w = 'form-1.html'
            output = Path('form-1.html').read_text()
            code = 200
        elif first_w == '/echo':
            #This is the content after interrogation mark.
            after_int = command2[1]
            #After interrogation mark there are two words, a name and a the value of the name, that are separated by an equal mark.
            w1, w2 = after_int.split ('=')
            output = Path("auxiliar.html").read_text()
            output = output +  f"<p>{w2}</p>"
            output = output + '<a href="/">Main page</a>'
            output = output + '</body>'
            output = output + '</html>'
            code = 200

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