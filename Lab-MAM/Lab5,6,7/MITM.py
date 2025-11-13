#!/usr/bin/env python3
# attacker_mitm.py - MITM proxy that tampers client->server ("42" -> random two-digit)
import socket, random

LISTEN, SERVER = ("127.0.0.1", 9000), ("127.0.0.1", 9001)
BUFSIZE = 4096

with socket.socket() as listen_sock:
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind(LISTEN)
    listen_sock.listen(1)
    print("[Attacker-MITM] listening on", LISTEN, "forward to", SERVER)
    client_sock, addr = listen_sock.accept()
    with client_sock:
        print("[Attacker] client connected", addr)
        with socket.socket() as serv:
            serv.connect(SERVER)
            data = client_sock.recv(BUFSIZE)
            if data:
                text = data.decode(errors="replace")
                print("[Attacker] captured (C->S):", text)
                # tamper: replace "42" with random two-digit
                newval = str(random.randint(10,99))
                tampered = text.replace("42", newval)
                print("[Attacker] tampered ->", tampered)
                serv.sendall(tampered.encode())
                resp = serv.recv(BUFSIZE)
                print("[Attacker] captured (S->C):", resp.decode(errors="replace"))
                client_sock.sendall(resp)
            else:
                print("[Attacker] no data from client")
    print("[Attacker] done")

