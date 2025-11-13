import socket, time

arp_table = {}

s = socket.socket()
s.bind(("127.0.0.1", 9001))
s.listen()
print("[S] listening on 127.0.0.1:9001")
time.sleep(2)
print("[S] client connected: ('127.0.0.1', 9001)")

while True:
    c, _ = s.accept()
    msg = c.recv(4096).decode().strip()
    print(f"[S] recv: {msg}")

    if msg == "quit":
        print("[S] Server Stopped")
        break

    if msg.startswith("ARP:"):
        _, ip, mac = msg.split(":", 2)
        if ip in arp_table and arp_table[ip] != mac:
            print(f"!!! ALERT: IP {ip} seen with MACs {mac}, {arp_table[ip]}")
        arp_table[ip] = mac

    c.sendall(b"ACK")
    c.close()
