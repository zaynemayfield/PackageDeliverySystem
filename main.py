# Author: Zayne Mayfield
# Student ID: 000206367


import csv
from datetime import time

import main
from truck import Truck
from packagehandler import PackageHandler


def restart_program():
    return


if __name__ == '__main__':

    ##################################################################################################################
    # Initial Setup
    ##################################################################################################################

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
    # throw all the packages to the package handler to send package info to package model and ge the object back and put
    # into the hash table
    all_packages = PackageHandler(packages_csv)
    # array of package IDs that have to go in truck 1
    truck_1_manual_loading = [13, 12, 14, 15, 16, 17, 19, 20, 21, 23, 29, 7, 34, 39, 40, 4]
    # array of package IDs that have to go in truck 2
    truck_2_manual_loading = [1, 3, 6, 18, 24, 25, 26, 30, 31, 32, 36, 37, 38]
    # array of package IDs that have to go in truck 3
    truck_3_manual_loading = [5, 9, 10, 11, 8, 2, 27, 28, 33, 35, 22]
    # packages that are delayed by flight
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
    # Update incorrect address
    all_packages.get(9).set_address("410 S State St")
    all_packages.get(9).set_city("Salt Lake City")
    all_packages.get(9).set_state("UT")
    all_packages.get(9).set_zip("84111")

    def reset_update_time():
        all_new_packages = all_packages
        # update truck 1 to 8am, truck 2 to 9:05am and truck 3 to 10:30 as that is their departure times
        for j in truck_1_manual_loading:
            package1 = all_new_packages.get(j)
            package1.set_update_time(time(8))

        for j in truck_2_manual_loading:
            package1 = all_new_packages.get(j)
            package1.set_update_time(time(9, 5))

        for j in truck_3_manual_loading:
            package1 = all_new_packages.get(j)
            package1.set_update_time(time(10, 30))
    reset_update_time()
    # Sort the packages in the trucks using the Greedy algorithm
    truck_1.sort_packages()
    truck_2.sort_packages()
    truck_3.sort_packages()
    # get miles from each truck
    truck_1_total_miles = truck_1.get_total_miles()
    truck_2_total_miles = truck_2.get_total_miles()
    truck_3_total_miles = truck_3.get_total_miles()
    # calculate total miles and print out each truck miles and total miles
    total_truck_miles = truck_1_total_miles + truck_2_total_miles + truck_3_total_miles
    ##################################################################################################################
    # Initial Setup
    ##################################################################################################################
    run_program = True

    while run_program:
        reset_update_time()
        print('\n******* WGU Tracking System *******')
        print('Truck 1: ' + str(truck_1.get_total_miles()) + ' miles \t Truck 2: ' + str(
            truck_2.get_total_miles()) +
              ' miles \t Truck 3: ' + str(truck_3.get_total_miles()) + ' miles \t Total truck miles: '
              + str(total_truck_miles))
        decision = input("Choose an option: \t 1: Track package by ID \t 2: View all packages at specific time \t"
                         "3: Exit \nType in either 1, 2 or 3: \n")
        if decision == '1':
            package_id = input(f'\nPlease enter package ID: ')
            get_time = input('Please enter a time in 24 hour format with only hour and minutes. Example: 13:24 \n')
            try:
                package_id = int(package_id)
                package = all_packages.get(package_id)
                if package is not None:
                    print('\n Package ID seems to be invalid \n')
                (hour, minute) = get_time.split(':')
                new_hour = int(hour) % 23
                new_minute = int(minute) % 59
                truck_1.run_truck_until(time(new_hour, new_minute))
                truck_2.run_truck_until(time(new_hour, new_minute))
                truck_3.run_truck_until(time(new_hour, new_minute))
                print(f'\n\n{hour}:{minute} print out of package ID: {package_id}')
                package.print_out()
                print('\n')
            except:
                print('\nTime or package ID input is incorrect\n')

        elif decision == '2':
            get_time = input('Please enter a time in 24 hour format with only hour and minutes. Example: 13:24 \n')
            try:
                (hour, minute) = get_time.split(':')
                new_hour = int(hour) % 23
                new_minute = int(minute) % 59
                truck_1.run_truck_until(time(new_hour, new_minute))
                truck_2.run_truck_until(time(new_hour, new_minute))
                truck_3.run_truck_until(time(new_hour, new_minute))
                print(f'\n\n{hour}:{minute} print out of all packages')
                all_packages.print()
                print('\n\n')
            except:
                print('\nSomething went wrong!\n')
        elif decision == 3:
            run_program = False
        else:
            print("Input not understood, try again!")
