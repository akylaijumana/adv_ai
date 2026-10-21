import os, socket

os.system("ping 8.8.8.8")

s = socket.socket()
s.settimeout(2)
result = s.connect_ex(("8.8.8.8", 53))
print("port 53 open:", result == 0)
s.close()