from Client0 import Client

PORT = 8085
IP = "192.168.0.25"

for element in range(5):
    c = Client(IP, PORT)
    c.debug_talk(f"Message {element}")
