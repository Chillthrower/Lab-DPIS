#!/usr/bin/env python3
import socket, time

HOST, PORT = "127.0.0.1", 9001
BUFSIZE = 4096

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(1)
    s.settimeout(1.0)  # <-- timeout every 1 second
    print("[Server] listening on", (HOST, PORT))
    try:
        while True:
            try:
                conn, addr = s.accept()
            except socket.timeout:
                continue  # go back and check for Ctrl+C
            with conn:
                print("[Server] connection from", addr)
                data = conn.recv(BUFSIZE)
                if not data:
                    print("[Server] no data")
                else:
                    print("[Server] received:", data.decode(errors="replace"))
                    conn.sendall(b"Server->Client: ACK")
                    print("[Server] sent ACK")
    except KeyboardInterrupt:
        print("\n[Server] shutting down gracefully")
