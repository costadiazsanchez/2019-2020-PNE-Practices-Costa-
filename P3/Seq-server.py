import socket
import termcolor
from Seq1 import Seq

IP = '127.0.0.1'
PORT = 8080

genes = ['AAAA', 'ACAC', 'GTGT', 'ACGT', 'GTAA']
bases = ['A', 'C', 'G', 'T']
folder = '../Session 4/'
gene = '.txt'
output = ''

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("Server is configured!")

while True:
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

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        if len(msg) >= 2:
            x1, x2 = msg.split("")
        else:
            x1 = msg
        

        if x1 == 'PING':
            termcolor.cprint("PING command!", 'yellow')
            print("OK!")
            output += "OK!\n"

        elif x1 == 'GET':
            for element in range(len(genes)):
                if element == int(x2):
                    termcolor.cprint('GET!', 'yellow')
                    output += genes[element]
                    print (genes[element])

        elif x1 == 'INFO':
            sequence = Seq(x2)
            termcolor.cprint('INFO!', 'yellow')
            print('Sequence: ', x2)
            print("Total length: ", sequence.len())
            output += f'Sequence: {x2}\n'
            output += f'Total length: {sequence.len()}\n'
            for element in bases:
                print (f'{element}: {sequence.count_base(element)} ({sequence.count_base(element)*100/sequence.len()}%)')
                output += f'{element}: {sequence.count_base(element)} ({sequence.count_base(element)*100/sequence.len()}%)\n'

        elif x1 == 'COMP':
            sequence = Seq(x2)
            termcolor.cprint('COMP!', 'yellow')
            print (sequence.complement())
            output += sequence.complement()

        elif x1 == 'REV':
            sequence = Seq(x2)
            termcolor.cprint('REV!', 'yellow')
            print(sequence.reverse())
            output += sequence.reverse()

        elif x1 == 'GENE':
            seq = Seq()
            sequence_g = str(seq.read_fasta(folder + x2 + gene))
            termcolor.cprint('GENE!', 'yellow')
            print(sequence_g)
            output += f'{sequence_g}'


        # -- The message has to be encoded into bytes
        cs.send(output.encode())

        # -- Close the client socket
        cs.close()
