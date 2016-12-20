import sys
from PyQt4 import QtGui

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from numpy import genfromtxt

import numpy as np


class Monitor(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        
        print('Loading data...')
        all_data = np.genfromtxt('../../CPP/cpp_SPHTutorial/csv_sph.out',delimiter=',')
        print('Organising data...')
        pID = all_data[:,0]
        self.allXY = all_data[:,1:3]
        self.nparticles = int(pID.max()) + 1
        self.position = 0
        self.x = self.allXY[self.position:self.position+self.nparticles,0]
        self.y = self.allXY[self.position:self.position+self.nparticles,1]
        self.position = self.position + self.nparticles + 1

        self.line = self.ax.scatter(self.x,self.y)
        
        # set figure limits
        axes = self.fig.gca()
        axes.set_xlim([-0.1, 1.1])
        axes.set_ylim([-0.1, 1.1])

        self.fig.canvas.draw()

        self.timer = self.startTimer(300)


    def timerEvent(self, evt):
        self.x = self.allXY[self.position:self.position+self.nparticles,0]
        self.y = self.allXY[self.position:self.position+self.nparticles,1]
        self.position = self.position + self.nparticles + 1
        # update the height of the bars, one liner is easier
        self.ax.cla()
        self.line = self.ax.scatter(self.x,self.y)
        
        # set figure limits
        axes = self.fig.gca()
        axes.set_xlim([-0.1, 1.1])
        axes.set_ylim([-0.1, 1.1])
        
        self.fig.canvas.draw()
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = Monitor()
    w.setWindowTitle("Particles")
    w.show()
    sys.exit(app.exec_())
    
