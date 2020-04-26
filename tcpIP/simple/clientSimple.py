import socket


if __name__ == '__main__':
	
	HOST='localhost'
	port=12345
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, port))
	msg=raw_input("type a msg to send: \n")
	sock.send(msg.encode())
	data=sock.recv(1024)
	print(data)