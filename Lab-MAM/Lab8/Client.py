#!/usr/bin/env python3
# arp_client.py — simulator (run in Terminal B)

import socket, time

HOST, PORT = "127.0.0.1", 50000

def run_client():
    try:
        c = socket.create_connection((HOST, PORT), timeout=3)
    except Exception as e:
        print("[C] can't connect:", e)
        return

    seq = [
        "ARP:10.0.0.1:aa:aa:aa:01",
        "ARP:10.0.0.2:aa:aa:aa:02",
        "HELLO",
        "ARP:10.0.0.1:aa:aa:aa:01",
        "ARP:10.0.0.1:02:bb:cc:03",   # simulated conflict
        "quit"
    ]

    with c:
        for m in seq:
            print("[C] send:", m)
            c.sendall(m.encode())
            try:
                r = c.recv(1024).decode().strip()
                print("[C] reply:", r)
            except Exception:
                print("[C] no reply")
            time.sleep(0.6)

    print("[C] client done")

if __name__ == "__main__":
    run_client()