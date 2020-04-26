import socket


if __name__ == '__main__':
	
	HOST='localhost'
	port=12345
	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msg="hello"
	sock.sendto(msg.encode(), (HOST,port))
