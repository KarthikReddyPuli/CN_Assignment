# Import socket module  
import socket
import sys
import os

# Create a socket object  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
  
# Define the port on which you want to connect  
port = 12345                
ip = '127.0.0.1'
filename = 'test.pdf'
filesize = os.path.getsize(filename)
# connect to the server on local computer  
s.connect((ip, port))
print(f"Connected to {ip}:{port}")  
s.send(f"{filename}".encode("utf-8"))
f = open (filename, "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
# close the connection 
print(f"{filename} sent") 
s.close()  