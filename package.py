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

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip(self, zipcode):
        self.zip = zipcode

    def print_out(self):
        print(f"ID: {self.id:<2}\t{self.address:<38}  {self.city:<16} {self.zip}\t"
              f"Deadline: {self.delivery_deadline:<8}\t{self.status} at {str(self.update_time)}\tWeight: {self.weight}")
