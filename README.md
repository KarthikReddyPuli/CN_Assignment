# CN_Assignment
Requires Python 3+

Place a test.pdf file in the directory
Create a directory named output

Start server by running
python server.py

Start client by running
python client.py

See the magic

SSL python files yet to be tested

Commands to generate SSL files

openssl req -new -x509 -days 365 -nodes -out client.pem -keyout client.key
openssl req -new -x509 -days 365 -nodes -out server.pem -keyout server.key