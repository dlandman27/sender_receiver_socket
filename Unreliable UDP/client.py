import socket

HOSTNAME = socket.gethostname()
PORT = 65222
FILENAME = "operations.txt"
SERVERNAME = socket.gethostname()
PORT = 65222

with open(FILENAME, 'r') as f:
    operations = f.readlines()
    for operation in operations:

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Handles Timer Function
            d = 0.1

            while True:

                s.sendto(bytes(operation,"utf-8"), (SERVERNAME,PORT))
                s.settimeout(d)

                try:
                    data,_ = s.recvfrom(1024)
                    data = data.decode()
                    print(data)
                    break
                except:
                    d = d * 2
                    if d > 2:
                        print("Error 300 Server is Dead!!")
                        serverDead = True
                        raise Exception("Request timed out: the server is dead")

                    print("Request timed out: resending")

