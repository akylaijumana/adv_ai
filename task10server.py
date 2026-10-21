import socket

s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen()
print("waiting...")
conn, addr = s.accept()
print(conn.recv(1024).decode())
conn.send(b"hi from server")
conn.close()
s.close()