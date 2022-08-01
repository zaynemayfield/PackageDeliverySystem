# Class to handle sending package data to the package class, then putting information into the hash table
from package import Package

# This class handles the Hash table!
class PackageHandler:
    # Constructor
    def __init__(self, packages):
        self.size = 10
        self.hash_table = [None] * self.size
        for package in packages:
            new_package = Package(package)
            key = new_package.get_id()
            self.insert(key, new_package)

    # Hashes the package ID by mod the length of the array
    def get_hash(self, key):
        return int(key) % len(self.hash_table)

    # Adds a package to the hash table
    def insert(self, key, package):
        # Hashes the key
        hashed_key = self.get_hash(key)
        # Gets key and package together
        labeled_package = [key, package]
        # If that part of the hash table array is empty
        if self.hash_table[hashed_key] is None:
            # Place the key and the packed at that spot in the hash table array
            self.hash_table[hashed_key] = list([labeled_package])
            return True
        else:
            # If the index for that spot in the array is not None Then check if that key is already there then update
            # the package
            for pack in self.hash_table[hashed_key]:
                if pack[0] == key:
                    pack[1] = package
                    return True
            # if the package key was not found in that spot in the hash table then append it.
            self.hash_table[hashed_key].append(labeled_package)
            return True

    # Gets a package from the hash table
    def look_up_hash_table_function(self, package_key):
        # get the hashed key
        hashed_key = self.get_hash(package_key)
        # check if that spot in the hash table array or index is not None
        if self.hash_table[hashed_key] is not None:
            # loop through the lists and find where key == key
            for pack in self.hash_table[hashed_key]:
                if str(pack[0]) == str(package_key):
                    # return the package
                    return pack[1]
        return None

    # Goes through hash table and then prints out the information
    def print(self):
        for i in range(0, len(self.hash_table)):
            for j in range(0, len(self.hash_table[i])):
                if j is not None:
                    self.hash_table[i][j][1].print_out()

    # Goes through hash table and updates the status on each package
    def reset_statuses(self):
        # go thorugh whole hash table
        for i in range(0, len(self.hash_table)):
            # Go through each element in that index of the hash table
            for j in range(0, len(self.hash_table[i])):
                # If it is not None then update the status
                if j is not None:
                    self.hash_table[i][j][1].set_status("at the hub")

    # Goes through hash table and updates the update time
    def reset_update_times(self, update_time):
        for i in range(0, len(self.hash_table)):
            for j in range(0, len(self.hash_table[i])):
                if j is not None:
                    self.hash_table[i][j][1].set_update_time(update_time)
