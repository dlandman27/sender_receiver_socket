import socket

HOSTNAME = socket.gethostname()
PORT = 65222

# STEP 1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOSTNAME,PORT))
    s.listen()
    # accept connections from outside
    (clientsocket, address) = s.accept()

    with clientsocket:
        # Prints confirmation of connection
        print(f"Connected by {address}")

        # STEP 2
        while True:
            # STEP 3
            data = clientsocket.recv(1024).decode()

            if not data:
                break

            printstatement = data+" ->"
            
            # STEP 4 
            OC,e1,e2 = data.split(" ")
            
            # STEP 5
            if OC not in ["+","-","*","/"]:
                print(printstatement," 620 -1")
                clientsocket.send(bytes("620 -1",'utf-8'))
            
            elif (not e1.strip().replace('-',"").isnumeric()) or (not e2.strip().replace('-',"").isnumeric()):
                print(printstatement+" 630 -1")
                clientsocket.send(bytes("630 -1",'utf-8'))
            
            else: # STEP 5/6/7    
                e1,e2 = int(e1), int(e2)

                if OC == "+":
                    print(printstatement+" 200 "+ str(e1+e2))
                    clientsocket.send(bytes("200 " + str(e1+e2),'utf-8'))
                elif OC == "-":
                    print(printstatement+" 200 "+ str(e1-e2))
                    clientsocket.send(bytes("200 " + str(e1-e2),'utf-8'))
                elif OC == "*":
                    print(printstatement+" 200 "+ str(e1*e2))
                    clientsocket.send(bytes("200 " + str(e1*e2),'utf-8'))
                elif OC == "/":
                    if e2 == 0:
                        print(printstatement+" 630 -1")
                        clientsocket.send(bytes("630 -1",'utf-8'))
                    else:
                        print(printstatement+" 200 "+ str(e1/e2))
                        clientsocket.send(bytes("200 " + str(e1/e2),'utf-8'))
        
