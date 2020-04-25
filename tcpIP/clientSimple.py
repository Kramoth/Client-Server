import socket

HOST='localhost'
port=12345
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, port))
sock.send(b"hi")
data=sock.recv(1024)
print(data)