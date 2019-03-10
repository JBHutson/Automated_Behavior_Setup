# This code runs on the computer, parses and manipulates data 

import serial
import time
import numpy as np
import matplotlib.pyplot as plt

class dataModel:

    def __init__(self):
        self.cage1Licks = []
        self.cage2Licks = []
        self.cage3Licks = []
        self.cage4Licks = []
        self.cage1Times = []
        self.cage2Times = []
        self.cage3Times = []
        self.cage4Times = []

    def parseLicksAndTimes(self, cage, cageLicks, cageTimes):
        singleLicksAndTime = cage.split(",")
        licks = int(singleLicksAndTime[0])
        time = singleLicksAndTime[1]
        cageLicks.append(licks)
        cageTimes.append(time)


