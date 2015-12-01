# import numpy as np
import matplotlib.pyplot as plt
from TS import *

class Gui:
    fig = ''
    ax = ''
    current = ''
    X = []
    Y = []


    def on_press(self,event):

        if event.button == 1:
            self.X.append(event.xdata)
            self.Y.append(event.ydata)
            self.set_figure('')


    def set_figure(self,string):
        self.ax.cla()
        self.reload()
        self.ax.set_title(string)
        self.ax.plot(self.X,self.Y, 'bo')
        plt.draw()


    def on_key(self,event):
        if event.key == "enter":
            self.ax.set_title('Aguarde')
            plt.draw()
            points = []
            for e in xrange(len(self.X)):
                points.append(City(self.X[e],self.Y[e]))

            #magic
            magic = SimulatedAnnealing(points,self.current)
            points, string = magic.run()

            self.X = []
            self.Y = []
            for p in points:
                self.X.append(p.getX())
                self.Y.append(p.getY())

            self.set_figure(string)
            self.ax.fill(self.X, self.Y, edgecolor='r', fill=False) 
            
            plt.draw()

        if event.key == 'r':
            self.X = []
            self.Y = []
            plt.cla()
            self.reload()
            plt.draw()


    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(211)
        self.current = self.fig.add_subplot(212)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)



    def reload(self):
        self.ax.set_title('')
        self.ax.grid(True)
        self.ax.set_ylim(0, 10.0)
        self.ax.set_xlim(0, 10.0)


    def build(self):
        self.reload()
        plt.show()



teste = Gui()
teste.build()