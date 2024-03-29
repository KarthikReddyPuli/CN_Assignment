# CN_Assignment
Requires Python 3+

Tested on Python 3.9.1

## File Transfer

Place a test.pdf file in the directory

Create a directory named output

Start server by running
```
python3 server.py
```

Start client by running
```
python3 client.py
```

See the magic

## SSL Echo program

Run the following commands to generate SSL certs
```
openssl req -new -x509 -days 365 -nodes -out client.pem -keyout client.key
```
```
openssl req -new -x509 -days 365 -nodes -out server.pem -keyout server.key
```

Command to start server
```
python3 server_ssl.py
```

Command to start client
```
python3 client_ssl.py
```

SSL python files yet to be tested

## Group Chat program

Run following command to start server
```
python3 server_chat.py ip port
```
ip = Server Bind IP

port = Server Bind port

Similarly run the following command to start client
```
python3 client_chat.py ip port
```
ip = Server IP

port = Server Port

## UDP Multicast
### Ipv4

Run the following command to start server
```
python3 server_multi.py
```
Similarly run the following command to start client
```
python3 client_multi.py
```

### Ipv6

Run the following command to start server
```
python3 server_multi.py -6
```
Similarly run the following command to start client
```
python3 client_multi.py -6
```