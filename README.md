Creating SSL keys:

openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365


Choose any passphrase, and for country/state/org/..., answer at least 3 questions. Otherwise cert.pem is empty.


create a directory called keys/ and save *.pem in there for the https_server.py code to work.
  
