# CN_Assignment
Requires Python 3+


For File Transfer


Place a test.pdf file in the directory

Create a directory named output


Start server by running

python server.py


Start client by running

python client.py


See the magic


For SSL create the SSL files with the following commands and run the server_ssl and client_ssl


openssl req -new -x509 -days 365 -nodes -out client.pem -keyout client.key

openssl req -new -x509 -days 365 -nodes -out server.pem -keyout server.key


SSL python files yet to be tested