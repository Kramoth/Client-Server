import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',12345)
sock.bind(server_address)
sock.listen(1)
conn, addr =sock.accept()
data=conn.recv(1024)
print(data)
conn.send(b'receive')
sock.close()
