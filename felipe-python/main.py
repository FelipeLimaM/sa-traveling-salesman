# import numpy as np
import matplotlib.pyplot as plt
from TS import *

class Gui:
    fig = ''
    ax = ''
    X = []
    Y = []


    def on_press(self,event):

        if event.button == 1:
            self.X.append(event.xdata)
            self.Y.append(event.ydata)
            self.set_figure('')


    def set_figure(self,string):
        plt.cla()
        self.reload()
        self.ax.set_title(string)
        plt.plot(self.X,self.Y, 'bo')
        plt.draw()


    def on_key(self,event):
        if event.key == "enter":
            self.ax.set_title('Aguarde')
            plt.draw()
            coords = list(plt.gca().get_lines()[0].get_xydata())
            points = []
            for coord in coords:
                points.append(City(coord[0],coord[1]))

            #magic
            magic = SimulatedAnnealing(points)
            points, string = magic.run()

            self.X = []
            self.Y = []
            for p in points:
                self.X.append(p.getX())
                self.Y.append(p.getY())

            self.set_figure(string)
            plt.fill(self.X, self.Y, edgecolor='r', fill=False) 
            
            plt.draw()

        if event.key == 'r':
            self.X = []
            self.Y = []
            plt.cla()
            self.reload()
            plt.draw()


    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)


    def reload(self):
        self.ax.set_title('')
        plt.grid(True)
        plt.ylim(0, 10.0)
        plt.xlim(0, 10.0)


    def build(self):
        self.reload()
        plt.show()



teste = Gui()
teste.build()