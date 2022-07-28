from datetime import time
import csv


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
        self.location_id = self.get_location_ids_from_csv()

    def get_location_ids_from_csv(self):
        with open("WGUPSAddressFile.csv") as addresses_file:
            read_address = csv.reader(addresses_file, delimiter=",", quotechar='"')
            addresses_csvfile = dict(read_address)
            return addresses_csvfile[self.address]

    def get_id(self):
        return self.id

    def get_location_id(self):
        return self.location_id

    def set_update_time(self, update_time):
        self.update_time = update_time

    def set_status(self, new_status):
        self.status = new_status

    def set_address(self, address):
        self.address = address

    def set_zip(self, zipcode):
        self.zip = zipcode

    def print_out(self):
        # print(f"ID: {self.id:<2}\t{self.address:<38}  {self.city:<16} {self.zip}\t Deadline: "
        #      f"{self.delivery_deadline:<8}\t {self.status:<17} \tWeight: {self.weight}")
        print(f"ID: {self.id:<2}\t{self.address:<38}  {self.city:<16} {self.zip}\t Deadline: "
              f"{self.delivery_deadline:<8}\t {self.status:<17} at {str(self.update_time)}\tWeight: {self.weight}kg")
