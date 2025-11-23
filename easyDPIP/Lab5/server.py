import socket, time

s = socket.socket()
s.bind(("127.0.0.1", 9001))
s.listen()
s.settimeout(1)

while True:
    try: 
        c, _ = s.accept()
        d = c.recv(4096).decode(errors='replace')

        print(f"[Server] received: {d}")
        print("[Server] sent ACK")

        c.sendall(b"ACK")
        c.close()

    except TimeoutError: pass