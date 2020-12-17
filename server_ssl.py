import socket
import ssl
import sys
import pprint

#defining ip address and port values
ip_addr, port = '127.0.0.1', 42420

###---- Setting up the server socket ----##
# Creating a socket object, 'ssl_serversoc'.
# 'AF_NET'-> Ipv4 addressing, 'SOCK_STREAM'-> for TCP protocol.
ssl_serversoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_serversoc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Binding the socket:
try:
    ssl_serversoc.bind((ip_addr, port))       
    print ("Socket binded to %s" %(port))  
except:
    print("Failed to bind socket. Error:" + str(sys.exc_info()))
    sys.exit()

# Setting max queue size of requests
ssl_serversoc.listen(7)

client, fromaddr = ssl_serversoc.accept()
# Configuring secure SSL connection
secure_sock = ssl.wrap_socket(client, server_side=True, ca_certs = "client.pem", certfile="server.pem", keyfile="server.key", cert_reqs=ssl.CERT_REQUIRED,
                        ssl_version=ssl.PROTOCOL_TLSv1_2)

print("-----------------CLIENT INFO-----------------")

print(repr(secure_sock.getpeername()))
#print(secure_sock.cipher())
print(pprint.pformat(secure_sock.getpeercert()))
cert = secure_sock.getpeercert()
print(cert)
print("-----------------END-----------------")

#ECHO Server implementation

print("\nReceiving data....")
try:
    data = secure_sock.read(1024)
    print(f"Data recieved -> {data.decode()}")
    secure_sock.write(data)
finally:
    secure_sock.close()
    ssl_serversoc.close()
