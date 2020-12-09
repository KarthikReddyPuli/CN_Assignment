# first of all import the socket library  
import socket
import sys             

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
# next create a socket object  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
print ("Socket successfully created") 
  
# reserve a port on your computer in our  
# case it is 12345 but it can be anything 
i = 0 
port = 12345                
ip = ''
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
    c, addr = s.accept()      
    print ('Got connection from', addr )
    filename = c.recv(BUFFER_SIZE).decode()
    f = open('output/'+ filename,'wb')
    l = c.recv(1024)
    while (l):
        f.write(l)
        l = c.recv(1024)
    f.close()
    c.close()
    i = i+1
  