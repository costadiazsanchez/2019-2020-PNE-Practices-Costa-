import socket
import termcolor

PORT = 8085
IP = "212.128.253.130"
number_con = 0
list_of_clients = []

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("Server is configured!")

while number_con < 5:
    try:
        print("Waiting for Clients to connect")
        (cs, client_ip_port) = ls.accept()

        # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    else:
        print("A client has connected to the server!")
        list_of_clients.append(client_ip_port)

        msg_raw = cs.recv(2048)
        number_con += 1

        # Print the connection number
        print("CONNECTION {}. From the IP: {}".format(number_con, client_ip_port))

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Received Message: ")
        termcolor.cprint (f"{msg}", 'green')
        response = f"ECHO: {msg}\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the client socket
        cs.close()

print ("The following clients has connected to the server: ")
for element in range(len(list_of_clients)):
    print(f'Client {element}: {list_of_clients[element]}')

