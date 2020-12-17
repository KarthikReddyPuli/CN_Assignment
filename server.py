# Import necessary modules/libraries  
import socket
import sys             
BUFFER_SIZE = 4096

# Create a socket object 'soc_obj'.
# NO params passed, to support both Ipv4 and Ipv6  
soc_obj = socket.socket()      
print ("Socket created successfully ") 
  
# Defining port and ip values  
# 'ip' intialized to an empty string, 
# so it is possible for different computers on the network to connect.
port, ip = 42420, ''             

#Now we bind to the port:
try:
    soc_obj.bind((ip, port))        
    print ("Socket binded to %s" %(port))  
except:
    print("Failed to bind socket. Error:" + str(sys.exc_info()))
    sys.exit()
  
# put the socket into listening mode.Allow to queue up a max of 7 requests.
soc_obj.listen(7)               
  
# infinite loop for processing requests; can be broken with keyboard interrupt.
while True:  
  
    # Establish connection with client.  
    client_socket, client_addr = soc_obj.accept()      
    print ('Established connection with:', client_addr)
    filename = client_socket.recv(BUFFER_SIZE).decode() 
    print(filename)
    # Writing the obtained data to file in 'output' folder.
    f = open('output/'+ filename,'wb')
    l = client_socket.recv(1024)
    while (l):
        f.write(l)
        l = client_socket.recv(1024)
    f.close()
    client_socket.close()
  
