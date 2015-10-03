import math
from random import random


class City:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        if not x:
            self.x = random() * 200
        if not y:
            self.y = random() * 200


    def __str__(self):
        return '(%d, %d)' % (int(self.x), int(self.y))


    def distance_to(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        return math.sqrt((x_distance * x_distance) + (y_distance * y_distance))
