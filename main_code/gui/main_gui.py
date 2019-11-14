""" main window for the GUI """

import random
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Lick-o-Meter'
        self.width = 1200
        self.height = 900
        self.mainWidget = QWidget(self)
        self.cageOne = PlotCanvas(self.mainWidget)
        self.cageTwo = PlotCanvas(self.mainWidget)
        self.cageThree = PlotCanvas(self.mainWidget)
        self.cageFour = PlotCanvas(self.mainWidget)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.center()

        windowLayout = QGridLayout(self.mainWidget)

        windowLayout.addWidget(self.cageOne,0,0)
        windowLayout.addWidget(self.cageTwo,0,1)
        windowLayout.addWidget(self.cageThree,1,0)
        windowLayout.addWidget(self.cageFour,1,1)

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
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.fig.subplots_adjust(bottom=0.30)
        self.xs = []
        self.ys = []
        self.i = 1

    def animate(self, i):
        self.xs.append(self.i)
        self.i = self.i + 1
        self.ys.append(random.randint(1, 21))

        self.xs = self.xs[-10:]
        self.ys = self.ys[-10:]

        self.ax.clear()
        self.ax.plot(self.xs, self.ys)

        self.ax.set_xlabel('Minute of Experiment')
        self.ax.set_ylabel('Licks')

    def setName(self, plotName):
        self.axes.set_title(plotName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ani = animation.FuncAnimation(ex.cageOne.fig, ex.cageOne.animate, interval=1000)
    ani = animation.FuncAnimation(ex.cageTwo.fig, ex.cageTwo.animate, interval=1000)
    ani = animation.FuncAnimation(ex.cageThree.fig, ex.cageThree.animate, interval=1000)
    ani = animation.FuncAnimation(ex.cageFour.fig, ex.cageFour.animate, interval=1000)
    sys.exit(app.exec())
