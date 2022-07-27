# Code understanding and structure from Joe James 1/22/2016 https://www.youtube.com/watch?v=9HFbhPscPU0
import numpy as numpy


class Distance:
    def __init__(self):
        distances_file = open("WGUPSDistanceTable.csv")
        self.distances2d = numpy.genfromtxt(distances_file, delimiter=",")

    def distance_between(self, add1, add2):
        return self.distances2d[add1][add2]

    def min_distance_from(self, from_id, truck_packages):
        next_package = None
        min_distance = 1e7
        for package in truck_packages:
            to_id = package.get_location_id()
            distance = self.distance_between(from_id, to_id)
            if distance < min_distance:
                min_distance = distance
                next_package = package
        return min_distance
