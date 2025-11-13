import socket, ssl

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("cert.pem", "key.pem")
s = socket.socket()
s.bind(("127.0.0.1", 4443))
s.listen(1)
print("[+] Server listening on 127.0.0.1:4443 with TLS")

with ctx.wrap_socket(s, server_side=True) as ss:
    c, a = ss.accept()
    print("[+] Secure connection from: ", a)
    d = c.recv(1024).decode()
    print("[S] [Server] Received (after decryption): ", d)
    c.sendall(f"{d}".encode())
    c.close()