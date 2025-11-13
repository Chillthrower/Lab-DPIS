import socket, ssl

HOST, PORT = "127.0.0.1", 4443

# Create SSL context for the client
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile="cert.pem")

# Connect and wrap socket
with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname="localhost") as ssock:
        print("[+] TLS connection established")

        msg = "Hello Secure World!"
        print("[Client] Sending:", msg)
        ssock.sendall(msg.encode())

        reply = ssock.recv(1024).decode()
        print("[Client] Received from server:", reply)
