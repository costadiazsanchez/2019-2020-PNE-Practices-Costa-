import socket
import termcolor
from pathlib import Path

# -- Server network parameters
IP = "192.168.0.25"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    command = req_line.split(' ')
    command1 = command[0]
    command2 = command[1]
    response = ""

    if command1 == "GET":
        if command2 == '/info/A':
            response = Path("A.html").read_text()
        elif command2 == '/info/C':
            response = Path("C.html").read_text()
        elif command2 == '/info/T':
            response = Path("T.html").read_text()
        elif command2 == '/info/G':
            response = Path("G.html").read_text()

    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(response)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + response
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()