#openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"

import socket, ssl

MESSAGE = "Hello Secure World!"

ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile="cert.pem")

with socket.create_connection(("127.0.0.1", 4443)) as s, ctx.wrap_socket(s, server_hostname="localhost") as c:

    c.sendall(MESSAGE.encode())

    print("[+] TLS connected")
    print("[C] Sending:", MESSAGE)
    print("[C] Received from server: Secure reply:", c.recv(1024).decode())