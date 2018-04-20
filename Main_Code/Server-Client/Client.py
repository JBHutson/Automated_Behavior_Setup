import sys
import socket
import serial

# set host port ip-address and port
serverHost = ''
serverPort = 60221

# create socket object
sock = socket(AF_INET, SOCK_STREAM)

# connect socket object ot server
sock.connect((serverHost, serverPort))

# open serial communication between arduino and the client
arduinoData = serial.Serial('com4', 9600)

# recieve data from the arduino and push it to the server
while True:
	while(arduinoData.inWaiting()==0):
                pass
        arduinoString = arduinoData.readline()
        arduinoString = arduinoString.decode().strip('\r\n')
        sock.send(arduinoString+'\n')
	
sock.shutdown(0)
sock.close()

