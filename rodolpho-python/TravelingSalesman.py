import math
from random import random
import matplotlib.pyplot as plt

from City import City
from Tour import Tour
from TourManager import *


class TravelingSalesman:
    def __init__(self):
        for i in xrange(20):
            city = City()
            add_city(city)

        temp = 10000
        cooling_rate = 0.003

        current_solution = Tour()
        current_solution.generate_individual()

        print "Initial distance:", current_solution.get_distance()

        best = Tour(current_solution.get_tour())

        while temp > 1:
            new_solution = Tour(current_solution.get_tour())

            tour_pos1 = int(new_solution.tour_size() * random())
            tour_pos2 = int(new_solution.tour_size() * random())

            city_swap1 = new_solution.get_city(tour_pos1)
            city_swap2 = new_solution.get_city(tour_pos2)

            new_solution.set_city(tour_pos2, city_swap1)
            new_solution.set_city(tour_pos1, city_swap2)

            current_energy = current_solution.get_distance()
            neighbour_energy = new_solution.get_distance()

            if self.acceptance_probability(current_energy, neighbour_energy, temp) > random():
                current_solution = Tour(new_solution.get_tour())

            if current_solution.get_distance() < best.get_distance():
                best = Tour(current_solution.get_tour())

            temp *= 1 - cooling_rate

        print 'Final distance:', best.get_distance()
        print 'Tour:', best
        
        self.plot_graph(best)


    def acceptance_probability(self, energy, new_energy, temperature):
        if new_energy < energy:
            return 1.0
        return math.exp((energy - new_energy) / temperature)


    def plot_graph(self, cities):
        x_list = []
        y_list = []
        for city in cities.get_tour():
            x_list.append(city.x)
            y_list.append(city.y)

        plt.fill(x_list, y_list, edgecolor='b', fill=False)
        plt.plot(x_list, y_list, 'bo')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    TravelingSalesman()
