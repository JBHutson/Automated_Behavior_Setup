import serial
# import numpy
# import matplotlib.pyplot as plt
# from drawnow import *

arduinoData = serial.Serial('com4', 9600)

while True:
    while(arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    arduinoString = arduinoString.decode().strip('\r\n')
    print(arduinoString)





