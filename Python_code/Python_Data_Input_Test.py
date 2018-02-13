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
    # first parse
    licksAndTimes = arduinoString.split(";")
    cage1 = licksAndTimes[0]
    cage2 = licksAndTimes[1]
    cage3 = licksAndTimes[2]


def parseLicksAndTimes(cage):
    singleLicksAndTime = cage.split(",")
    return singleLicksAndTime





