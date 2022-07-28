import csv
from datetime import date, datetime, time, timedelta
from math import ceil
from package import Package

# Handles everything with the trucks


class Truck:
    # Constructor
    def __init__(self):
        self.package_limit = 16
        self.package_count = 0
        self.speed = 18
        self.packages = {}
        self.starting_location = 0
        self.location_id = 0
        self.departure_time = time()
        self.route = {}
        self.master_distance = 0.0
        self.master_time = self.departure_time
        self.distances2d = self.load_distance()

    # Load distances
    def load_distance(self):
        with open("WGUPSDistanceTable.csv") as packages_file:
            read_package = csv.reader(packages_file, delimiter=",", quotechar='"')
            return [row for row in read_package]
            print(packages_csv)

    # Adds package
    def add_package(self, package: Package):
        if self.package_limit > self.package_count:
            self.packages[package.get_id()] = package
            self.package_count += 1

    # Sets the time of departure for the truck and also sets the master time used for tracking route
    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
        self.master_time = departure_time
        return

    # Sorts all the packages on the truck using the greedy algorithm
    def sort_packages(self):
        # Sets initial location to the hub 0
        from_location = self.starting_location
        # Create temp package holder to delete the package to run the algorithm
        temp_packages = []
        # Loads the temp package holder from the main packages
        for key in self.packages:
            temp_packages.append(self.packages[key])
        # Sets i to the number of packages on the truck
        i = self.package_count
        # Main loop to create the route for the truck
        while i > 0:
            # Pass from location and all the packages to the greedy algorithm
            route = self.min_distance_from(from_location, temp_packages)
            # Add the closest package to the route
            self.route[route[0].get_id()] = route
            # Set the next from location to this location
            from_location = route[0].get_location_id()
            # Delete the package from temp_packages so it cannot be compared in the algorithm again
            del temp_packages[route[3]]
            i -= 1
            # if this is the last time then need to calculate back to the Hub
            if i == 0:
                distance_back_home = self.distance_between(from_location, 0)
                last_route = [None, distance_back_home, self.get_time_amount(distance_back_home), None]
                self.route[99] = last_route

    # Calculates the distance between and returns the distance - have to check with input is larger
    def distance_between(self, add1, add2):
        if int(add2) > int(add1):
            distance = self.distances2d[int(add2)][int(add1)]
            return float(distance)
        elif int(add1) > int(add2):
            distance = self.distances2d[int(add1)][int(add2)]
            return float(distance)
        else:
            return 0

    # Calculates the time it takes to travel a distance with 18 MPH
    def get_time_amount(self, distance):
        return ceil((distance / 18) * 60)

    # This run the greedy algorithm checking which of the packages is closet
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

    # Adds all the distances up from the route
    def get_total_miles(self):
        total_miles = 0
        for key in self.route:
            total_miles += self.route[key][1]
        return total_miles

    # increments the current time with the minutes to add
    def add_minutes_to_time(self, timeval, minutes_to_add):
        dt = datetime.combine(date.today(), timeval) + timedelta(minutes=minutes_to_add)
        return dt.time()

    # this runs the simulation using the route data and checking for when the time is greater than or equal to user
    # input time
    def run_truck_until(self, time_until):
        if time_until >= self.departure_time:
            for key in self.packages:
                self.packages[key].set_status("en route")
        self.master_time = self.departure_time
        for key in self.route:
            self.master_time = self.add_minutes_to_time(self.master_time, self.route[key][2])
            if self.master_time <= time_until:
                self.master_distance += self.route[key][1]
                if self.route[key][0] is not None:
                    self.route[key][0].set_status("delivered")
                    self.route[key][0].set_update_time(self.master_time)
            else:
                return




