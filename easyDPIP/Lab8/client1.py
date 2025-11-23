import socket, time

MESSAGE = [
    "ARP:10.0.0.1:aa:aa:aa:01",
    "ARP:10.0.0.2:aa:aa:aa:02",
    "HELLO",
    "ARP:10.0.0.1:aa:aa:aa:01",
    "ARP:10.0.0.1:02:bb:cc:03",
    "quit"
]

for msg in MESSAGE:
    s = socket.socket()
    s.connect(("127.0.0.1", 9001))
    s.sendall(msg.encode())
    reply = s.recv(4096).decode(errors='replace')
    reply = f"{reply} {msg}"
    print(f"[C] send: {msg}")
    print(f"[C] reply: {reply}")
    s.close()
    time.sleep(0.6)