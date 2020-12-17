import socket  
import sys 
import threading

BUFFER_SIZE = 2048

def recv_and_print(server): #This functions runs in different thread which receives messages from server and prints it
    while True:
        try:
            data = server.recv(BUFFER_SIZE).decode()
            if data:
                print(data)
            else: #This occures when the server link is broken
                print("Connection closed by server")
        except: #Error Handler
            continue
    

# Creating a socket object 'server'.
# 'AF_NET'-> Ipv4 addressing, 'SOCK_STREAM'-> for TCP protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Check for the proper arguments 
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number") 
	exit() 

IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))

recv_thread=threading.Thread(target = recv_and_print,args = (server,))
recv_thread.start() #Starts the message receiving thread
while True: 
    input_msg = input("")
    server.send(input_msg.encode()) #Waits for input and sends it


server.close()