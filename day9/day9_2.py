import sys
from pathlib import Path


visited_points = []


def print_results(input):
    basins = []

    for point in lowest_points(input):
        basin_size = check_points(point, input)
        basins.append(basin_size)
    b1, b2, b3 = sorted(basins)[-3:]
    print(f"Multiplying the size of the three largest basins: {b1 * b2 * b3}")


def num_at_point(point, input):
    line_index, num_index = point
    return int(input[line_index][num_index])


def check_points(point, input, count=0):
    line_index, num_index = point
    line = input[line_index]

    # mark that we've checked this point
    visited_points.append(point)

    # increment the counter
    count += 1

    # find its neightbors
    neighbors = get_neighbors(point, input)

    # recursively call this function for each neighboring point that should be checked
    for neighbor in neighbors:
        if num_at_point(neighbor, input) < 9 and neighbor not in visited_points:
            count = check_points(neighbor, input, count)

    return count


def get_neighbors(point, input):
    line_index, num_index = point
    line = input[line_index]

    neighbors = []
    if num_index < (len(line) - 1):
        right = (line_index, num_index + 1)
        neighbors.append(right)
    if line_index < (len(input) - 1):
        down = (line_index + 1, num_index)
        neighbors.append(down)
    if num_index > 0:
        left = (line_index, num_index - 1)
        neighbors.append(left)
    if line_index > 0:
        up = (line_index - 1, num_index)
        neighbors.append(up)

    return neighbors


def lowest_points(input):
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
                # store lowest points as a tuple of line_index, num_index
                lowest_points.append((line_index, num_index))
    return lowest_points


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print_results(input)
    else:
        raise TypeError("This is not a file")
