import socket
import sys
import threading

# Creating a socket object 'server'.
# 'AF_NET'-> Ipv4 addressing, 'SOCK_STREAM'-> for TCP protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Check for the proper arguments
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()


IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

#Binding the socket to the specified IP and port
server.bind((IP_address, Port))
server.listen(100)  #Accepts maximum of 100 clients

list_of_clients = [] #All the list of clients are stored here for futher use to broadcast

def clientthread(conn, addr): #Receives all the messages from a specific client and sends to all other clients
	# sends a message to the client whose user object is conn 
	conn.send("Welcome to this chatroom!".encode())
	while True:
			try:
				message = conn.recv(2048).decode()
				if message:
					print ("<" + addr[0] + "> " + message)
					# Calls broadcast function to send message to all 
					message_to_send = "<" + addr[0] + "> " + message 
					broadcast(message_to_send, conn)
				else: #This occurs when the client program or the socket stops working
					remove(conn)

			except: #Error Handler
				continue



def broadcast(message, connection):
	for clients in list_of_clients:
		if clients!=connection:
			try:
				clients.send(message.encode())
			except:
				clients.close()
				# if the link is broken, we remove the client 
				remove(clients)


def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

while True:

	conn, addr = server.accept()
	list_of_clients.append(conn) #Adds the client to list of all clients
	client_thread=threading.Thread(target = clientthread,args = (conn,addr,))
	client_thread.start() #Starts a new thread for every client
	print (str(addr[0]) + ":" + str(addr[1]) + " connected")

conn.close()
server.close()
