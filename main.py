import copy
import csv
import datetime
from datetime import time

import locations
from truck import Truck
from distance import Distance
from packagehandler import PackageHandler

if __name__ == '__main__':
    # Loading in CSV and storing it in packages_csv
    with open("WGUPSPackageFile.csv") as packages_file:
        read_package = csv.reader(packages_file, delimiter=",", quotechar='"')
        packages_csv = [row for row in read_package]

    # create truck 1
    truck_1 = Truck()
    # set departure time for truck 1
    truck_1.set_departure_time(time(8))
    # create truck 2
    truck_2 = Truck()
    # set departure time for truck 2
    truck_2.set_departure_time(time(9, 5))
    # create truck 3
    truck_3 = Truck()
    # set departure time for truck 3
    truck_3.set_departure_time(time(10, 30))
    # throwing all the packages to the package handler to send package info to package and ge the object back and put
    # into the hash table
    all_packages = PackageHandler(packages_csv)
        # array of package IDs that have to go in truck 1
    truck_1_manual_loading = [13, 12, 14, 15, 16, 17, 19, 20, 21, 23, 29, 7, 34, 39, 40, 4]
    # array of package IDs that have to go in truck 2
    truck_2_manual_loading = [1, 3, 6, 11, 22, 18, 24, 25, 26, 30, 31, 32, 36, 37, 38, 10]
    # array of package IDs that have to go in truck 3
    truck_3_manual_loading = [5, 9, 8, 2, 27, 28, 33, 35]
    # packages that are delayed by flight
    delayed_packages = [6, 28, 32, 25]
    # package with wrong address
    wrong_address_package = [9]
    # Load truck 1 with required packages
    for i in truck_1_manual_loading:
        truck_1.add_package(all_packages.get(i))
    # Load truck 2 with required packages
    for i in truck_2_manual_loading:
        truck_2.add_package(all_packages.get(i))
    # Load truck 3 with required packages
    for i in truck_3_manual_loading:
        truck_3.add_package(all_packages.get(i))

    for i in delayed_packages:
        package = all_packages.get(i)
        package.set_update_time(time(9, 5))

    for i in wrong_address_package:
        package = all_packages.get(i)
        package.set_update_time(time(10, 30))

    all_packages.print()
    print("Packages in Truck 1")
    truck_1.print_packages()
    print("Packages in Truck 2")
    truck_2.print_packages()
    print("Packages in Truck 3")
    truck_3.print_packages()

    truck_1.sort_packages()
    truck_2.sort_packages()
    truck_3.sort_packages()
    truck_1_total_miles = truck_1.get_total_miles()
    truck_2_total_miles = truck_2.get_total_miles()
    truck_3_total_miles = truck_3.get_total_miles()
    total_truck_miles =  truck_1_total_miles + truck_2_total_miles + truck_3_total_miles
    print('\n\n\n\nTruck 1: ' + str(truck_1.get_total_miles()) + ' miles \t Truck 2: ' + str(truck_2.get_total_miles()) +
          ' miles \t Truck 3: ' + str(truck_3.get_total_miles()) + ' miles')
    print('Total truck miles: ' + str(total_truck_miles))

    show_all_9 = time(9)
    show_all_10 = time(10)
    show_all_13 = time(13)
    truck_1.run_truck_until(show_all_9)
    all_packages.print()
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
