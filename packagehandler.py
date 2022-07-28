# Class to handle sending package data to the package class, then putting information into the hashtable
from package import Package


class PackageHandler:
    # Constructor
    def __init__(self, packages):
        self.size = 10
        self.map = [None] * self.size
        for package in packages:
            new_package = Package(package)
            key = new_package.get_id()
            self.add(key, new_package)

    # Hashes the package ID by mod the length of the array
    def get_hash(self, key):
        return int(key) % len(self.map)

    # Adds a package to the hash table
    def add(self, key, package):
        hashed_key = self.get_hash(key)
        # I think labeled_package should use the package ID, not the hashed ID
        labeled_package = [key, package]
        if self.map[hashed_key] is None:
            self.map[hashed_key] = list([labeled_package])
            return True
        else:
            for pack in self.map[hashed_key]:
                if pack[0] == key:
                    pack[1] = package
                    return True
            self.map[hashed_key].append(labeled_package)
            return True

    # Gets a package from the hash table
    def get(self, package_key):
        hashed_key = self.get_hash(package_key)
        if self.map[hashed_key] is not None:
            for pack in self.map[hashed_key]:
                if str(pack[0]) == str(package_key):
                    return pack[1]
        return None

    # Goes through hash table and then prints out the information
    def print(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if j is not None:
                    self.map[i][j][1].print_out()

    # Goes through hash table and updates the status on each package
    def reset_statuses(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if j is not None:
                    self.map[i][j][1].set_status("at the hub")

    # Goes through hash table and updates the update time
    def reset_update_times(self, update_time):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if j is not None:
                    self.map[i][j][1].set_update_time(update_time)
