#!/usr/bin/env python3
# attacker_eavesdrop.py - simple proxy that logs (no tamper)
import socket

LISTEN, SERVER = ("127.0.0.1", 9000), ("127.0.0.1", 9001)
BUFSIZE = 4096

with socket.socket() as listen_sock:
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind(LISTEN)
    listen_sock.listen(1)
    print("[Attacker-EAVESDROP] listening on", LISTEN, "forward to", SERVER)
    client_sock, addr = listen_sock.accept()
    with client_sock:
        print("[Attacker] client connected", addr)
        with socket.socket() as serv:
            serv.connect(SERVER)
            data = client_sock.recv(BUFSIZE)
            if data:
                text = data.decode(errors="replace")
                print("[Attacker] captured (C->S):", text)   # eavesdropper sees plaintext
                serv.sendall(data)                           # forward unchanged
                resp = serv.recv(BUFSIZE)
                print("[Attacker] captured (S->C):", resp.decode(errors="replace"))
                client_sock.sendall(resp)
            else:
                print("[Attacker] no data from client")
    print("[Attacker] done")

