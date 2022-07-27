from datetime import time
from math import ceil

import numpy

from distance import Distance
from package import Package


class Truck:
    def __init__(self):
        self.package_limit = 16
        self.package_count = 0
        self.speed = 18
        self.packages = {}
        self.starting_location = 0
        self.location_id = 0
        self.departure_time = time()
        self.route = {}
        self.load_data()

    def add_package(self, package: Package):
        if self.package_limit > self.package_count:
            self.packages[package.get_id()] = package
            self.package_count += 1

    def remove_package(self, package):
        del self.packages[package.get_id()]
        self.package_count -= 1

    def get_packages(self):
        return self.packages

    def get_package_count(self):
        return self.package_count

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
        return

    def print_packages(self):
        print("Departure time: " + str(self.departure_time))
        for key in self.packages:
            self.packages[key].print_out()

    def sort_packages(self):
        from_location = self.starting_location
        temp_packages = []
        for key in self.packages:
            temp_packages.append(self.packages[key])
        i = self.package_count
        while i > 0:
            route = self.min_distance_from(from_location, temp_packages)
            self.route[route[0].get_id()] = route
            from_location = route[0].get_location_id()
            del temp_packages[route[3]]
            i -= 1
            if i == 0:
                distance_back_home = self.distance_between(from_location, 0)
                last_route = [None, distance_back_home, self.get_time_amount(distance_back_home), None]
                self.route[99] = last_route
        print(self.route)

    def load_data(self):
        distances_file = open("WGUPSDistanceTable.csv")
        self.distances2d = numpy.genfromtxt(distances_file, delimiter=",")

    def distance_between(self, add1, add2):
        if int(add2) > int(add1):
            distance = self.distances2d[int(add2)][int(add1)]
            return distance
        elif int(add1) > int(add2):
            distance = self.distances2d[int(add1)][int(add2)]
            return distance
        else:
            return 0

    def get_time_amount(self, distance):
        return time(0, ceil((distance / 18) * 60))

    def min_distance_from(self, from_id, packages):
        next_route = []
        next_package = None
        min_distance = 1e7
        min_distance_index = 0
        array_index_counter = 0
        for package in packages:
            to_id = package.get_location_id()
            distance = self.distance_between(from_id, to_id)
            if distance < min_distance:
                min_distance = distance
                next_package = package
                min_distance_index = array_index_counter
            array_index_counter += 1
        next_route.append(next_package)
        next_route.append(min_distance)
        next_route.append(self.get_time_amount(min_distance))
        next_route.append(min_distance_index)
        return next_route

    def get_total_miles(self):
        total_miles = 0
        for key in self.route:
            total_miles += int(self.route[key][1])
        return total_miles

    def run_truck_until(self, time_until):
        print(time_until)
        print(self.departure_time)
        if time_until > self.departure_time:
            print("it's greater")
            for key in self.packages:
                self.packages[key].set_status("en route")



