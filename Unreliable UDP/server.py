import sys
import random
import socket

HOSTNAME = socket.gethostname()
PORT = 65222

p,seed = float(sys.argv[1]), random.seed(sys.argv[2])

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('',PORT))

    print("bound")

    # STEP 3
    data,clientAddr = s.recvfrom(1024)

    data = data.decode()



    if not data:
        break

    if random.random() <= p:
        print(data, " -> dropped")

    printstatement = str(data)+" ->"
    
    # STEP 4 
    OC,e1,e2 = data.split(" ")
    
    # STEP 5
    if OC not in ["+","-","*","/"]:
        print(printstatement," 620 -1")
        s.sendto(bytes("620 -1",'utf-8'),clientAddr)
    
    elif (not e1.strip().replace('-',"").isnumeric()) or (not e2.strip().replace('-',"").isnumeric()):
        print(printstatement+" 630 -1")
        s.sendto(bytes("630 -1",'utf-8'),clientAddr)
    
    else:
        e1,e2 = int(e1), int(e2)

        if OC == "+":
            print(printstatement+" 200 "+ str(e1+e2))
            s.sendto(bytes("200 " + str(e1+e2),'utf-8'),clientAddr)
        elif OC == "-":
            print(printstatement+" 200 "+ str(e1-e2))
            s.sendto(bytes("200 " + str(e1-e2),'utf-8'),clientAddr)
        elif OC == "*":
            print(printstatement+" 200 "+ str(e1*e2))
            s.sendto(bytes("200 " + str(e1*e2),'utf-8'),clientAddr)
        elif OC == "/":
            if e2 == 0:
                print(printstatement+" 630 -1")
                s.sendto(bytes("630 -1",'utf-8'),clientAddr)
            else:
                print(printstatement+" 200 "+ str(e1/e2))
                s.sendto(bytes("200 " + str(e1/e2),'utf-8'),clientAddr)
        
