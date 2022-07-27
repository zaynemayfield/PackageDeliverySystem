# class to handle sending package data to the package model, then putting package object into the hashtable
from package import Package


class PackageHandler:
    def __init__(self, packages):
        self.size = 10
        self.map = [None] * self.size
        self.load_package(packages)

    def get_hash(self, key):
        return int(key) % len(self.map)

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

    def get(self, package_key):
        hashed_key = self.get_hash(package_key)
        if self.map[hashed_key] is not None:
            for pack in self.map[hashed_key]:
                # hashed key in pack[0] is always an integer because it is the result of a math operation
                # package_key could be integer or string. Let's cast both to string to perform string comparison
                if str(pack[0]) == str(package_key):
                    return pack[1]
        return None

    def remove(self, package_key):
        hashed_key = self.get_hash(package_key)
        if self.map[hashed_key] is None:
            return False
        for i in range(0, len(self.map[hashed_key])):
            if self.map[hashed_key][i][0] == package_key:
                self.map[hashed_key].pop(i)
                return True

    def print(self):
        for slot in self.map:
            for pack in slot:
                if pack is not None:
                    pack[1].print_out

    def load_package(self, packages):
        for package in packages:
            new_package = Package(package)
            key = new_package.get_id()
            self.add(key, new_package)
