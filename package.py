from datetime import time

import locations


class Package:
    def __init__(self, package_details):
        self.id = package_details[0]
        self.address = package_details[1]
        self.city = package_details[2]
        self.state = package_details[3]
        self.zip = package_details[4]
        self.delivery_deadline = package_details[5]
        self.weight = package_details[6]
        self.special_instructions = package_details[7]
        self.status = "at the hub"
        self.update_time = time(8)
        self.location_id = locations.addresses_csv[self.address]
        # self.print_out()
        # en route or delivered

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_delivery_deadline(self):
        return self.delivery_deadline

    def get_weight(self):
        return self.weight

    def get_special_instructions(self):
        return self.special_instructions

    def get_delivery_status(self):
        return self.status

    def get_location_id(self):
        return self.location_id

    def set_update_time(self, update_time):
        self.update_time = update_time

    def set_status(self, new_status):
        self.status = new_status
        print(str(self.id) + " " + str(self.status))

    def print_out(self):
        print("Package ID: " + self.id + "\t Address: " + self.location_id + " " + self.address + " " + self.city +
              ", " + self.state + " " + self.zip + "\t Delivery Deadline: " + self.delivery_deadline +
              "\t Weight: " + self.weight + "\t Status: " + self.status + " at " + str(self.update_time))
