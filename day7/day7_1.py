import sys
from pathlib import Path
from statistics import median
from math import floor


def find_fuel_costs(input):
    median_num = median(input)
    fuel_costs = [abs(median_num - num) for num in input]
    print(floor(sum(fuel_costs)))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).strip().split(",")
        input = [int(num) for num in input]
        find_fuel_costs(input)
    else:
        raise TypeError("This is not a file")
