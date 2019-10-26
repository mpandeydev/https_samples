# API implemented by server, and called by client is specified below:




# Basic https server/client in Python
- https_server.py and https_client.py can be run in parallel, and client makes a request that server responds to.


# Parallel https server and clients
- Run parallel_https_server.py 

- Then run https_client1.py and https_client2.py

- The server responds to the two independent request streams in parallel.



# Creating SSL keys:


The passkey used for the checkedin keys is test123

openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365


Choose any passphrase, and for country/state/org/..., answer at least 3 questions. Otherwise cert.pem is empty.


create a directory called keys/ and save *.pem in there for the https_server.py code to work.
  
