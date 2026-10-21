import socket

c = socket.socket()
c.connect(("127.0.0.1", 5000))
c.send(b"hi from client")
print(c.recv(1024).decode())
c.close()