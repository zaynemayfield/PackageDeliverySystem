# Code understanding and structure from Joe James 1/22/2016 https://www.youtube.com/watch?v=9HFbhPscPU0
from datetime import time
from math import ceil

import numpy as numpy


class Distance:
    def __init__(self):
        distances_file = open("WGUPSDistanceTable.csv")
        self.distances2d = numpy.genfromtxt(distances_file, delimiter=",")

    def distance_between(self, add1, add2):
        return self.distances2d[add1][add2]

    def get_time_amount(self, distance):
        return time(0, ceil((distance/18)*60))

    def min_distance_from(self, from_id, packages):
        next_route = None
        next_package = None
        min_distance = 1e7
        for package in packages:
            to_id = package.get_location_id()
            distance = self.distance_between(from_id, to_id)
            if distance < min_distance:
                min_distance = distance
                next_package = package
        next_route.append(next_package)
        next_route.append(min_distance)
        next_route.append(self.get_time_amount(min_distance))
        return next_route
