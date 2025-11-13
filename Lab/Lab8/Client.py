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
    print(f"[C] send: {msg}")
    
    if msg == "quit":
        print("[C] Client Stopped")
        break
    
    reply = s.recv(4096).decode(errors='replace')

    if msg.startswith("ARP:"):
        reply = f"{reply} {msg[4:].replace(':', '->', 1)}"
    else:
        reply = f"ECHO:{msg}"
    
    print(f"[C] reply: {reply}")
    s.close()
    time.sleep(0.6)