# CN_Assignment
Requires Python 3+

## File Transfer

Place a test.pdf file in the directory

Create a directory named output

Start server by running
```
python server.py
```

Start client by running
```
python client.py
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

SSL python files yet to be tested

## Group Chat program

Run following command to start server
```
python server_chat.py ip port
```
ip = Server Bind IP

port = Server Bind port

Similarly run the following command to start client
```
python client_chat.py ip port
```
ip = Server IP
port = Server Port