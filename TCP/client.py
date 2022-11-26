import socket

HOSTNAME = socket.gethostname()
PORT = 65222
f = open("operations.txt","r")
operations = f.readlines()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOSTNAME, PORT))
    for operation in operations:
        s.sendall(bytes(operation,"utf-8"))
        data = s.recv(1024).decode()
        STATUS,VAL = data.split(" ")
        STATUS = int(STATUS)

        if STATUS == 200:
            print("Result is "+ VAL)
        elif STATUS == 620:
            print("ERROR 620 Invalid Operator")
        elif STATUS == 630:
            print("ERROR 630 Invalid Operands")

    s.close()