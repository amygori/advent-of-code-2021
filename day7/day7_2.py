import sys
from pathlib import Path
from statistics import mean
from math import ceil, floor


def find_fuel_costs(input):
    mean_num = floor(mean(input))
    steps = [abs(num - mean_num) for num in input]
    fuel_costs = [sum(range(num + 1)) for num in steps]
    print(ceil(sum(fuel_costs)))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).strip().split(",")
        input = [int(num) for num in input]
        find_fuel_costs(input)
    else:
        raise TypeError("This is not a file")
