from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.253.130"
PORT = 8080

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
response = c.talk("Lo que quieras")
print(f"Response: {response}")
