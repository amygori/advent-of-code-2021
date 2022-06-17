import sys
from pathlib import Path


def print_risk_levels(input):
    lowest_points = []
    for line_index, item in enumerate(input):
        for num_index, num in enumerate(item):
            num = int(num)
            # check above and below
            adjacent_nums = []
            # if not first line check same position in line above
            if line_index > 0:
                num_above = input[line_index - 1][num_index]
                adjacent_nums.append(int(num_above))
            # if not last line check same position below
            if line_index < (len(input) - 1):
                num_below = input[line_index + 1][num_index]
                adjacent_nums.append(int(num_below))
            # if not first num in line check num before
            if num_index > 0:
                num_to_the_left = item[num_index - 1]
                adjacent_nums.append(int(num_to_the_left))
            # if not last num in line check num after
            if num_index < (len(item) - 1):
                num_to_the_right = item[num_index + 1]
                adjacent_nums.append(int(num_to_the_right))
            # if this is the lowest of all the adjacent nums, it must be a lowest point
            if num < min(adjacent_nums):
                lowest_points.append(int(num))
    print(sum(lowest_points) + len(lowest_points))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print_risk_levels(input)
    else:
        raise TypeError("This is not a file")
