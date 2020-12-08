# Import socket module  
import socket
import sys             
  
# Create a socket object  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
  
# Define the port on which you want to connect  
port = 12345                
ip = '127.0.0.1'
pdf_name = 'test.pdf'
# connect to the server on local computer
addrInfo = socket.getaddrinfo(ip,port)
print(addrInfo)  
s.connect((ip, port))  
  
f = open (pdf_name, "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
# close the connection  
s.close()  