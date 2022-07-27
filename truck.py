from datetime import time
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

    def set_departure_time(self, time):
        self.departure_time = time
        print(self.departure_time)
        return

    def print_packages(self):
        for key in self.packages:
            self.packages[key].print_out()
