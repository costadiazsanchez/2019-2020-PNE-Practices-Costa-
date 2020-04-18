from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

print ('*Testing PING...')
print (c.talk('OK!'))

print('*Testing GET...')
for element in range(5):
    print (f'GET {element}: {c.talk(element)}')

print('*Testing INFO...')
print (c.talk('GET ACGTACGT'))

print('*Testing COMP...')
print (c.talk('COMP ACGTCAGT'))

print('*Testing REV...')
print(c.talk('REV ACGTCGTA'))

print ('*Testing GENE...')
for element in ['U5', 'ADA', 'FRAT1', 'RNU6_269P', 'FXN']:
    print(c.talk(element))