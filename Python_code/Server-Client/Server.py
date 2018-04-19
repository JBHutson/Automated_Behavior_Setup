import socket
import string

class myTCPServer(SocketServer.StreamRequestHandler):
	def handle (self):
		line = self.rfile.readline()
		print(line)

host = socket.gethostname()
port = 60221
server = SocketServer.TCPServer((host, port), myTCPServer)

server.serve_forever()
