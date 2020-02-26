import socket

# SERVER IP, PORT
PORT = 8080
IP = "212.128.253.128"

while True:
  # -- Ask the user for the message
    user_message = input("Send me a message: ")

  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(str.encode(user_message))
  # -- Close the socket
    s.close()