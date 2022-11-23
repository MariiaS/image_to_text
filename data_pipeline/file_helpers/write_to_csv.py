import csv


def write_to_file(path_to_file, row):
    with open(path_to_file, "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
