from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Lick-o-Meter'
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.center()
        
        self.mainWidget = QWidget(self)

        windowLayout = QHBoxLayout(self.mainWidget)

        cageOne = PlotCanvas(self.mainWidget)
        cageOne.setName('Cage 1')
        cageTwo = PlotCanvas(self.mainWidget)
        cageTwo.setName('Cage 2')
        cageThree = PlotCanvas(self.mainWidget)
        cageThree.setName('Cage 3')
        cageFour = PlotCanvas(self.mainWidget)
        cageFour.setName('Cage 4')

        windowLayout.addWidget(cageOne)
        windowLayout.addWidget(cageTwo)
        windowLayout.addWidget(cageThree)
        windowLayout.addWidget(cageFour)

        self.mainWidget.setFocus()
        self.setCentralWidget(self.mainWidget)

        self.show()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        self.axes.plot(data, 'r-')
        self.draw()

    def setName(self, plotName):
        self.axes.set_title(plotName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
