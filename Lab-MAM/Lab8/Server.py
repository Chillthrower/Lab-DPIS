#!/usr/bin/env python3
# arp_server.py — detector (run in Terminal A)

import socket
from collections import defaultdict

HOST, PORT = "127.0.0.1", 50000
ip_to_macs = defaultdict(set)

def run_server():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[S] listening on {HOST}:{PORT} — waiting for client...")
    try:
        conn, addr = s.accept()
        print("[S] client connected:", addr)
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                msg = data.decode().strip()
                print("[S] recv:", msg)
                if msg.startswith("ARP:"):
                    _, ip, mac = (msg.split(":", 2) + ["", ""])[:3]
                    mac = mac.lower()
                    prev = set(ip_to_macs[ip])
                    ip_to_macs[ip].add(mac)
                    conn.sendall(f"ACK {ip}->{mac}".encode())
                    if len(ip_to_macs[ip]) > 1 and mac not in prev:
                        print("!!! ALERT: IP", ip, "seen with MACs", ", ".join(sorted(ip_to_macs[ip])))
                elif msg.lower() in ("quit", "exit"):
                    conn.sendall(b"bye")
                    break
                else:
                    conn.sendall(f"ECHO:{msg}".encode())
    except KeyboardInterrupt:
        print("\n[S] interrupted")
    finally:
        s.close()
        print("[S] server stopped")

if __name__ == "__main__":
    run_server()