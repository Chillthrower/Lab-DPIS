import socket

MESSAGE = "Client->Server: exam answer: 42"
s = socket.socket()
s.connect(("127.0.0.1", 9000))
s.sendall(MESSAGE.encode()); 
reply = s.recv(4096).decode(errors='replace')
print(f"[Client] sending: {MESSAGE}")
print(f"[Client] got reply: Server->Client: {reply}")
s.close()