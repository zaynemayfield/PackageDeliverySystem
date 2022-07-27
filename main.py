import csv
import datetime

import locations
from truck import Truck
from distance import Distance
from packagehandler import PackageHandler

if __name__ == '__main__':
    # Loading in CSV and storing it in packages_csv
    with open("WGUPSPackageFile.csv") as packages_file:
        read_package = csv.reader(packages_file, delimiter=",", quotechar='"')
        packages_csv = [row for row in read_package]

    # throwing all the packages to the package handler to send package info to package and ge the object back and put
    # into the hash table
    all_packages = PackageHandler(packages_csv)
    # create truck 1
    truck_1 = Truck()
    # set departure time for truck 1
    truck_1.set_departure_time(datetime.time(8))
    # create truck 2
    truck_2 = Truck()
    # set departure time for truck 2
    truck_2.set_departure_time(datetime.time(9, 5))
    # create truck 3
    truck_3 = Truck()
    # set departure time for truck 3
    truck_3.set_departure_time(datetime.time(10, 30))
    # array of package IDs that have to go in truck 1
    truck_1_manual = [13, 14, 15, 16, 19, 20, 34, 39]
    # array of package IDs that have to go in truck 2
    truck_2_manual = [3, 6, 18, 25, 26, 36, 38]
    # array of package IDs that have to go in truck 3
    truck_3_manual = [9, 8]
    # packages that need to be delivered before 10:30
    load_next_time_sensitive = [1, 29, 30, 31, 37, 40]
    # the rest of the packages that can be delivered whenever
    load_last = [2, 4, 5, 7, 10, 11, 12, 17, 21, 22, 23, 24, 27, 28, 32, 33, 35]

    print(all_packages.get(13))
    # Load truck 1 with required packages
    for i in truck_1_manual:
        truck_1.add_package(all_packages.get(i))
    # Load truck 2 with required packages
    for i in truck_2_manual:
        truck_2.add_package(all_packages.get(i))
    # Load truck 3 with required packages
    for i in truck_3_manual:
        truck_3.add_package(all_packages.get(i))


    # package9 = packages.get(9)
    # package9.print_out()

# The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
# WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the
# correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.

#
# Leave at 9:05 Must be on Truck two 3, 18, 36, 38, 6, 25, 26
# Leave at 8:00 Must be on Truck One 15, 14, 19, 13, 20, 16, 39, 34
# Must be on truck three 9, 8
# Delayed by flight: 6, 28, 32, 25
# by 10:30 - - 29, 1, 30, 31, 40, 37
# can go later: 27,35,7,29
# Need to go together (27,35), (29,7), (2,33), (31,32), (4,40), (5,37)
# need to update package 9 to this correct address: 410 S State St., Salt Lake City, UT 84111
