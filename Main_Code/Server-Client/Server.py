import socket
import string

# open the txt file that will hold the data
f = open('random.txt', 'w')

# override the defualt server handler
class myTCPServer(SocketServer.StreamRequestHandler):
	def handle (self):
		line = self.rfile.readline()
		f.write(str(line)+'\n')

# get the hostname and port number for the computer running the server
host = socket.gethostname()
port = 60221

# create the server
server = SocketServer.TCPServer((host, port), myTCPServer)

# run the server
server.serve_forever()
