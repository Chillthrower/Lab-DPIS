#!/usr/bin/env python3
# client.py - minimal client that connects to proxy (attacker) at :9000
import socket

PROXY_HOST, PROXY_PORT = "127.0.0.1", 9000
MSG = "Client->Server: exam answer: 42"

with socket.socket() as s:
    s.connect((PROXY_HOST, PROXY_PORT))
    print("[Client] sending:", MSG)
    s.sendall(MSG.encode())
    reply = s.recv(4096)
    if reply:
        print("[Client] got reply:", reply.decode(errors="replace"))
    else:
        print("[Client] no reply")

