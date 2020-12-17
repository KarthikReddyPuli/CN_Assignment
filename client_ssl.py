import socket
import ssl
import sys


#defining ip address and port values
ip_addr, port = '127.0.0.1', 42420

###---- Setting up the client socket ----##
# Creating a socket object, 'ssl_clientsoc'.
# 'AF_NET'-> Ipv4 addressing, 'SOCK_STREAM'-> for TCP protocol.
ssl_clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Blocking mode of transfer
ssl_clientsoc.setblocking(1)

# Connect to the server
try :
    ssl_clientsoc.connect((ip_addr, port))
    print(f"Connected to {ip_addr}:{port}.\n") 
except :
    print("Failed to establish connection")
    sys.exit() 

# Configuring the secure SSL connection:
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations('server.pem')
context.load_cert_chain(certfile="client.pem", keyfile="client.key")

if ssl.HAS_SNI:
    secure_sock = context.wrap_socket(ssl_clientsoc, server_side=False, server_hostname=ip_addr)
else:
    secure_sock = context.wrap_socket(ssl_clientsoc, server_side=False)

cert = secure_sock.getpeercert()
print("-----------------SERVER INFO-----------------")
print(cert)
print("-----------------END-----------------\n")

#ECHO client functionality:
print("Sending message....")
secure_sock.write('Test data!'.encode())
print(f"Response received -> {secure_sock.read(1024).decode()}")

secure_sock.close()
ssl_clientsoc.close()
