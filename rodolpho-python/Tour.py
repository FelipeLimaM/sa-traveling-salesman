from random import shuffle

from TourManager import *

class Tour:
    _tour = []
    _distance = 0

    def __init__(self, tour=None):
        if tour:
            self._tour = tour
        else:
            for i in xrange(cities_number()):
                self._tour.append(None)


    def __str__(self):
        gene_string = ''
        for i in xrange(len(self._tour)):
            gene_string += str(self.get_city(i))
            if i < len(self._tour) - 1:
                gene_string += ' -> '
        return gene_string


    def get_tour(self):
        return self._tour


    def generate_individual(self):
        for i in xrange(cities_number()):
            self.set_city(i, get_city(i))
        shuffle(self._tour)


    def get_city(self, tourPosition):
        return self._tour[tourPosition]


    def set_city(self, tourPosition, city):
        self._tour[tourPosition] = city
        self._distance = 0


    def tour_size(self):
        return len(self._tour)


    def get_distance(self):
        if not self._distance:
            tour_distance = 0
            for i in xrange(len(self._tour)):
                from_city = self.get_city(i)
                destination_city = None
                if i + 1 < len(self._tour):
                    destination_city = self.get_city(i + 1)
                else:
                    destination_city = self.get_city(0)
                tour_distance += from_city.distance_to(destination_city)
            self._distance = tour_distance
        return self._distance
