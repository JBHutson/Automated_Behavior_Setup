import sys
import socket

serverHost = ''
serverPort = 60221

sock = socket(AF_INET, SOCK_STREAM)

sock.connect((serverHost, serverPort))

while line != 'close':
	line = 
	sock.send(line+'\n')
	
sock.shutdown(0)
sock.close()

