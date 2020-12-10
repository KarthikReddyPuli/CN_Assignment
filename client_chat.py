# Python program to implement client side of chat room. 
import socket  
import sys 
import threading

BUFFER_SIZE = 2048

def recv_and_print(server):
    while True:
        try:
            data = server.recv(BUFFER_SIZE).decode()
            if data:
                print(data)
            else:
                print("Connection closed by server")
        except:
            continue
    


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number") 
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))

x=threading.Thread(target = recv_and_print,args = (server,))
x.start()
while True: 
    input_msg = input("")
    server.send(input_msg.encode())


server.close()