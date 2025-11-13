import socket, ssl

HOST, PORT = "127.0.0.1", 4443

# Create SSL context for the server
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# Create a normal TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind((HOST, PORT))
sock.listen(5)
print(f"[+] Server listening on {HOST}:{PORT} with TLS")

# Accept and wrap connection
with context.wrap_socket(sock, server_side=True) as ssock:
    conn, addr = ssock.accept()
    print("[+] Secure connection from:", addr)

    # Receive and decode client message
    data = conn.recv(1024).decode()
    print("[Server] Received (after decryption):", data)

    # Send reply
    reply = "Secure reply: " + data
    conn.sendall(reply.encode())
    conn.close()
