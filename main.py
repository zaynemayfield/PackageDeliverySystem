# Author: Zayne Mayfield
# Student ID: 000206367
import csv
from datetime import time
from truck import Truck
from packagehandler import PackageHandler


if __name__ == '__main__':

    ##################################################################################################################
    # INITIAL SETUP
    ##################################################################################################################

    # Loading in CSV and storing it in packages_csv
    with open("WGUPSPackageFile.csv") as packages_file:
        read_package = csv.reader(packages_file, delimiter=",", quotechar='"')
        packages_csv = [row for row in read_package]

    # create trucks
    truck_1 = Truck()
    truck_2 = Truck()
    truck_3 = Truck()

    # set departure time for trucks
    truck_1.set_departure_time(time(8))
    truck_2.set_departure_time(time(9, 5))
    truck_3.set_departure_time(time(10, 30))

    # throw all the packages to the package handler to send package info to package model and ge the object back and put
    # into the hash table
    all_packages = PackageHandler(packages_csv)

    # Divide packages
    truck_1_manual_loading = [13, 12, 14, 15, 16, 17, 19, 20, 21, 23, 29, 7, 34, 39, 40, 4]
    truck_2_manual_loading = [1, 3, 6, 18, 24, 25, 26, 30, 31, 32, 36, 37, 38]
    truck_3_manual_loading = [5, 9, 10, 11, 8, 2, 27, 28, 33, 35, 22]

    # Load into trucks
    for i in truck_1_manual_loading:
        truck_1.add_package(all_packages.look_up_hash_table_function(i))
    for i in truck_2_manual_loading:
        truck_2.add_package(all_packages.look_up_hash_table_function(i))
    for i in truck_3_manual_loading:
        truck_3.add_package(all_packages.look_up_hash_table_function(i))

    # function to reset the times to be able to run the reports again
    def reset_update_time():
        # reset trucks to 8 to refresh the report
        all_packages.reset_update_times(time(8))
        # reset all status for simulation to work correctly
        all_packages.reset_statuses()

    # Check user input and make changes according to the scenario
    def check_statuses(check_time):
        # Handle the wrong address package
        get_address_time = time(10, 30)
        wrong_address_package = all_packages.look_up_hash_table_function(9)
        if check_time >= get_address_time:
            wrong_address_package.set_address("410 S State St")
            wrong_address_package.set_zip("84111")
        else:
            wrong_address_package.set_address("300 State St")
            wrong_address_package.set_location_id(12)
            wrong_address_package.set_zip("84103")
            wrong_address_package.set_status("incorrect address")
            truck_3.sort_packages()

        # handle the delayed packages
        late_package_time = time(9, 5)
        if check_time < late_package_time:
            late_packages = [28, 6, 32, 25]
            for j in late_packages:
                all_packages.look_up_hash_table_function(j).set_status('delayed on flight')
        else:
            late_packages = [28, 6, 32, 25]
            for j in late_packages:
                all_packages.look_up_hash_table_function(j).set_status('at the hub')
        # If the check time is before 8:00 then set all update times to the user requested time.
        start_time = time(8)
        if check_time < start_time:
            all_packages.reset_update_times(check_time)

    # Sort the packages in the trucks using the Greedy algorithm
    truck_1.sort_packages()
    truck_2.sort_packages()
    truck_3.sort_packages()

    # Getet miles from each truck
    truck_1_total_miles = truck_1.get_total_miles()
    truck_2_total_miles = truck_2.get_total_miles()
    truck_3_total_miles = truck_3.get_total_miles()

    # calculate total miles and print out each truck miles and total miles
    total_truck_miles = truck_1_total_miles + truck_2_total_miles + truck_3_total_miles

    ##################################################################################################################
    # START OF GUI
    ##################################################################################################################
    # variable to keep the while loop or program running
    run_program = True
    # Main loop for the UI
    while run_program:
        # Will restart the update times to be able to run the simulation again with correct data
        reset_update_time()
        # Introduction and choices
        print('\n******* WGU Tracking System *******')
        print('Truck 1: ' + str(round(truck_1.get_total_miles(), 1)) + ' miles \t Truck 2: ' + str(
            truck_2.get_total_miles()) +
              ' miles \t Truck 3: ' + str(truck_3.get_total_miles()) + ' miles \t Total truck miles: '
              + str(total_truck_miles))
        decision = input("Choose an option:\n1: Track package by ID | 2: View all packages at specific time |"
                         " 3: Exit \nType in 1, 2 or 3: \n")
        # Handles tracking 1 package at a specific time
        if decision == '1':
            package_id = input(f'\nPlease enter package ID: ')
            get_time = input('Please enter a time in 24 hour format with only hour and minutes. Example: 13:24 \n')
            try:
                package_id = int(package_id)
                package = all_packages.look_up_hash_table_function(package_id)
                if package is not None:
                    print('\n Package ID seems to be invalid \n')
                (hour, minute) = get_time.split(':')
                new_hour = int(hour) % 23
                new_minute = int(minute) % 59
                check_statuses(time(new_hour, new_minute))
                truck_1.run_truck_until(time(new_hour, new_minute))
                truck_2.run_truck_until(time(new_hour, new_minute))
                truck_3.run_truck_until(time(new_hour, new_minute))
                print(f'\n\n{hour}:{minute} print out of package ID: {package_id}')
                package.print_out()
                print('\n')
            except:
                print('\nTime or package ID input is incorrect\n')

        # Handles tracking all packages at a specific time.
        elif decision == '2':
            get_time = input('Please enter a time in 24 hour format with only hour and minutes. Example: 13:24 \n')
            try:
                (hour, minute) = get_time.split(':')
                new_hour = int(hour) % 23
                new_minute = int(minute) % 59
                check_statuses(time(new_hour, new_minute))
                truck_1.run_truck_until(time(new_hour, new_minute))
                truck_2.run_truck_until(time(new_hour, new_minute))
                truck_3.run_truck_until(time(new_hour, new_minute))
                print(f'\n\n{hour}:{minute} print out of all packages')
                all_packages.print()
                print('\n\n')
            except:
                print('\nSomething went wrong!\n')

        # handles exiting the program
        elif decision == '3':
            run_program = False
        # handles incorrect input
        else:
            print("Input not understood, try again!")
