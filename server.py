# first of all import the socket library  
import socket
import sys             

BUFFER_SIZE = 4096
# next create a socket object  
s = socket.socket()#supports both Ipv4 and Ipv6 with empty parameters       
print ("Socket successfully created") 
  
# reserve a port on your computer in our  
# case it is 12345 but it can be anything 
port = 12345                
ip = ''#accepts connections on all networks
resp_str = 'Thank you for connecting'
# Next bind to the port  
# we have not typed any ip in the ip field  
# instead we have inputted an empty string  
# this makes the server listen to requests  
# coming from other computers on the network  
s.bind((ip, port))        
print ("socket binded to %s" %(port))  
  
# put the socket into listening mode  
s.listen(5)   
print ("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs  
while True:  
  
    # Establish connection with client.  
    client_socket, client_addr = s.accept()      
    print ('Got connection from', client_addr )
    filename = client_socket.recv(BUFFER_SIZE)
    filename = filename.decode()
    f = open('output/'+ filename,'wb')
    l = client_socket.recv(1024)
    while (l):
        f.write(l)
        l = client_socket.recv(1024)
    f.close()
    client_socket.close()
  