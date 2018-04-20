import serial
import time
# import numpy
# import matplotlib.pyplot as plt

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
    licks = int(singleLicksAndTime[0])
    time = singleLicksAndTime[1]
    cageLicks.append(licks)
    cageTimes.append(time)
    print licks

def manipulation(dataLine):
    licksAndTimes = dataLine.split(';')

f = open('random.txt', 'r')

while 1:
    where = f.tell()
    line = f.readline()
    if not line:
        time.sleep(1)
        f.seek(where)
    else:
        manipulation(line)

    # first parse
    # cage1 = licksAndTimes[0]
    # cage2 = licksAndTimes[1]
    # cage3 = licksAndTimes[2]
    

    #parseLicksAndTimes(cage1, cage1Licks, cage1Times)
   # parseLicksAndTimes(cage2, cage2Licks, cage2Times)
   # parseLicksAndTimes(cage3, cage3Licks, cage3Times)







