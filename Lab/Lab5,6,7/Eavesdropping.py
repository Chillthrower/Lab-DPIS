import socket

print("[Attacker] Listening...")

ls = socket.socket()
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind(("127.0.0.1", 9000))
ls.listen()

c, _ = ls.accept()
s = socket.socket()
s.connect(("127.0.0.1", 9001))
d = c.recv(4096).decode(errors='replace')
print(f"[Attacker] C->S: {d}")

s.sendall(d.encode())
r = s.recv(4096).decode(errors='replace')
c.sendall(r.encode())

print(f"[Attacker]S->C: {r}")
for x in (c, s, ls): x.close()
