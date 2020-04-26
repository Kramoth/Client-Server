import socket
import sys


if __name__ == '__main__':
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ('localhost',12345)
	sock.bind(server_address)
	bytesAddressPair = sock.recvfrom(1024)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	print("from %s: %s"%(address,message))
	sock.close()
