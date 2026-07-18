import csv
import sys


def decision(row):
    if row["maintenance_window"].lower() != "yes":
        return "block"
    if int(row["active_alarms"]) > 0:
        return "block"
    if int(row["healthy_neighbors"]) < 2:
        return "block"
    return "allow"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['site']} {decision(row)}")


if __name__ == "__main__":
    main(sys.argv[1])
