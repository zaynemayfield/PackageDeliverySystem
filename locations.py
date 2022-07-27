import csv

with open("WGUPSAddressFile.csv") as addresses_file:
    read_address = csv.reader(addresses_file, delimiter=",", quotechar='"')
    addresses_csv = dict(read_address)