import socket
import sys
import threading

# Creating a socket object 'server'.
# 'AF_NET'-> Ipv4 addressing, 'SOCK_STREAM'-> for TCP protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Check for the proper arguments
if len(sys.argv) != 3:
	print ("Arguments format: <script>, <IP address>, <port number>")
	exit()


IP_addr = str(sys.argv[1])
port_num = int(sys.argv[2])

#Binding the socket to the specified IP and port
server.bind((IP_addr, port_num))
server.listen(50)  #Accepts maximum of 50 clients

#All the list of clients are stored in clients_list for futher use to broadcast
clients_list = [] 

def clientthread(con, address): #Receives all the messages from a specific client and sends to all other clients
	# message is sent to client. Client user object is con
	con.send("Successfully connected to chatroom".encode())
	while True:
			try:
				msg = con.recv(2048).decode()
				if msg:
					print ("<" + address[0] + "> " + msg)
					# message is sent to all using broadcast function 
					send_msg = "<" + address[0] + "> " + msg 
					broadcast(send_msg, con)
				else: #This occurs when the client program or the socket stops working
					remove(con)

			except: #Error Handler
				continue


# message is sent to all clients using broadcast function 
def broadcast(msg, con):
	for clients in clients_list:
		if clients!=con:
			try:
				clients.send(msg.encode())
			except:
				clients.close()
				# remove client if link is broken
				remove(clients)

#removes the object 
def remove(connection):
	if connection in clients_list:
		clients_list.remove(connection)

while True:

	con, address = server.accept()
	clients_list.append(con) #Adds the client to list of all clients
	client_thread=threading.Thread(target = clientthread,args = (con,address,))
	client_thread.start() #Starts a new thread for every client
	print (str(address[0]) + ":" + str(address[1]) + " connected")

con.close()
server.close()
