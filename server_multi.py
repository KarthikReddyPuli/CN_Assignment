import struct
import socket
import sys

## Defining required values
port = 42420
multicast_group4, multicast_group6 = '224.3.1.1', 'ff08:6069:6069:6069:6069:6069:6069:6069'

# Check if the right command line argument is given
if len(sys.argv) == 1:
    print("Please give the  \'-4\' or \'-6\' argument ")
    sys.exit()
if sys.argv[1] == "-6":
    group = multicast_group6
elif sys.argv[1] == "-4":
    group = multicast_group4
else:
    print("Enter valid argument (either \'-4\' or \'-6\')")
    sys.exit()

# Look up multicast group address using 'getaddrinfo' and find out IP version
addrinfo = socket.getaddrinfo(group, None)[0]

# Create a socket object
soc_obj = socket.socket(addrinfo[0], socket.SOCK_DGRAM)


soc_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind it to the port
try:
    soc_obj.bind(('', port))       
    print ("Socket binded to %s" %(port))  
except:
    print("Failed to bind socket. Error:" + str(sys.exc_info()))
    sys.exit()

## Joining info of multicast group is being configured:
group_bin = socket.inet_pton(addrinfo[0], addrinfo[4][0])
# Join group
if addrinfo[0] == socket.AF_INET: # 'AF_NET' flag corresponding to Ipv4
    mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
    soc_obj.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
else:                            # Ipv6
    mreq = group_bin + struct.pack('@I', 0)
    soc_obj.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

# Infinite loop to keep printing any data we receive.
# Can be terminated with a keyboard interrupt
while True:
    data, sender = soc_obj.recvfrom(1500)
    while data[-1:] == '\0': data = data[:-1] # Strip trailing \0's
    print (str(sender) + '  ' + repr(data.decode()))


