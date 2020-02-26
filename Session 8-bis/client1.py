import socket

IP = '212.128.253.128'
PORT = 8080

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode(""))

msg = s.recv(2000)
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))


# Closing the socket
s.close()