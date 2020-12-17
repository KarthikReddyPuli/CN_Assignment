# Import necessary modules 
import socket
import sys
import time

# Creating a socket object 'soc_obj'.
# 'AF_NET'-> Ipv4 addressing, 'SOCK_STREAM'-> for TCP protocol.
soc_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       

port, ip = 42420, '127.0.0.1'   # Defining port and ip details:          
filename = 'test.txt'           # test file to send to the server
# connect to the server on local computer  
try :
    soc_obj.connect((ip, port))
    print(f"Connected to {ip}:{port}.") 
except :
    print("Failed to establish connection")
    sys.exit() 

# sending the test file name,followed by test data
soc_obj.send(f"{filename}".encode("utf-8"))
time.sleep(0.5)      # waiting for a short while for server to recieve data
f = open (filename, "rb")
#Sending the data,1KB at a time.
l = f.read(1024)
while (l):
    soc_obj.send(l)
    l = f.read(1024)
# close the connection 
print(f"{filename} sent") 
soc_obj.close()  
