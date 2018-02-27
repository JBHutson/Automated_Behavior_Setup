import serial
import numpy
import matplotlib.pyplot as plt

# arrays for number of licks
cage1Licks = []
cage2Licks = []
cage3Licks = []

# arrays for Time

cage1Times = []
cage2Times = []
cage3Times = []

def parseLicksAndTimes(cage, cageLicks, cageTimes):
    singleLicksAndTime = cage.split(",")
    licks = singleLicksAndTime[0]
    time = singleLicksAndTime[1]
    cageLicks.append(licks)
    cageTimes.append(time)

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

    parseLicksAndTimes(cage1, cage1Licks, cage1Times)
    parseLicksAndTimes(cage2, cage2Licks, cage2Times)
    parseLicksAndTimes(cage3, cage3Licks, cage3Times)







