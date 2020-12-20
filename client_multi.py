import time
import struct
import socket
import sys

## Defining required values
port = 42420
multicast_group4, multicast_group6 = '224.3.1.1', 'ff08:6069:6069:6069:6069:6069:6069:6069'
# ttl set to '1' to restrict connection to local network.
# Can be increased to reach other networks
ttl = 1 

if len(sys.argv) == 0:
    print("Please give the  \'-4\' or \'-6\' argument ")
    sys.exit()
if sys.argv[1] == "-6":
    group = multicast_group6
elif sys.argv[1] == "-4":
    group = multicast_group4
else:
    print("Enter valid argument (either \'-4\' or \'-6\')")
    sys.exit()


#storing address info of the group
addrinfo = socket.getaddrinfo(group, None)[0]

soc_obj = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

# Configuring group info
ttl_bin = struct.pack('@i', ttl)
if addrinfo[0] == socket.AF_INET: # IPv4
    soc_obj.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl_bin)
else:
    soc_obj.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl_bin)

print("Sending data to server!")
while True:
    data = "Test msg!"
    soc_obj.sendto((data).encode(), (addrinfo[4][0], port))
    time.sleep(1)
