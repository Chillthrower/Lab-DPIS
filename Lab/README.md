pip install pycryptodome

Lab5,6,7: run server -> Eavesdropping or MITM -> client, Dictionary attack does not need client and server

Lab4:
    first run: openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
    
    then: Server -> Client