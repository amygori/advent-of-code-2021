import sys
from pathlib import Path


# track points that have already been counted
visited_points = []


def print_results(input):
    print("🥑 🍉 🥒 🍒 🥑 🍉 🥒 🍒 HERE WE GO 🥑 🍉 🥒 🍒 🥑 🍉 🥒 🍒")
    basins = []
    lowest_points_list = lowest_points(input)
    short_list = [(0, 1), (0, 9)]

    print(lowest_points_list)
    # [(0, 1), (0, 9), (2, 2), (4, 6)]
    for point in lowest_points(input):
        basin_size = check_points(point, input)
        print(f"🌳 YO we got a return value for point and it is {basin_size} 🌳")
        print(f"🎯 basin size for point {point} is {basin_size}")
        print(f"Visited points are {visited_points}")
        basins.append(basin_size)
    print(f"🌊 {basins}")


def num_at_point(point, input):
    line_index, num_index = point
    return int(input[line_index][num_index])


def check_points(point, input, count=0):
    # first time we check the low point, then we will need to check each of its neighbors.
    print("🦙 🦙 🦙 Count points! inputs are:")
    print(f"point: {point} | count: {count}")

    line_index, num_index = point
    line = input[line_index]
    if point in visited_points:
        return count

    # increment counter if not a 9 (we're still in the basin) and it's not already counted
    # if num_at_point(point, input) < 9 and point not in visited_points:
    visited_points.append(point)
    print(f"🦩 Added to Visited points: {visited_points}")

    count += 1

    # find its neightbors
    neighbors = get_neighbors(point, input)
    print(f"👽 Neighbors for {point} are {neighbors} 👽")

    for neighbor in neighbors:
        print("🍥 about to check neighbor ", neighbor)
        if num_at_point(neighbor, input) < 9 and neighbor not in visited_points:
            print(f"🧞‍♂️ Neighbor {neighbor} is about to be checked 🧞‍♂️")
            print(f"🫐 Count is currently {count} 🫐")
            count = check_points(neighbor, input, count)
        else:
            print(
                f"Neighbor {neighbor} did not pass test because it is {num_at_point(neighbor, input)} or in visited points: {visited_points}"
            )

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


def count_x(point, input):
    line_idx, num_idx = point
    line = input[line_idx]

    right = count_right(line, line_idx, num_idx)
    left = count_left(line, line_idx, num_idx)
    print(f"❌ In count_x, right count is {right}")
    print(f"🍋 and left count is {left}")

    return right + left


def count_y(point, input):
    line_idx, num_idx = point

    up = count_up(line_idx, num_idx, input)
    down = count_down(line_idx, num_idx, input)
    print(f"In count_y, up count is {up} and down count is {down}")
    return up + down


def count_right(line, line_idx, num_idx, count=0):
    print("🪴 count right starts here 🪐")
    # check to make sure that it's not at the right edge
    if num_idx < (len(line) - 1):
        print(f"The number we are considering is {line[num_idx]}")
        current_point = (line_idx, num_idx)
        if current_point not in visited_points and int(line[num_idx]) != 9:
            print(f"🧁 current point {current_point} not in visited points; counting 🍵")
            count = 1
            # visited_points.append(current_point)
            # count_right(line, line_idx, num_idx + 1, count)

    return count or 0


def count_left(line, line_idx, num_idx, count=0):
    # check to make sure it's not at the left edge
    print("🍋 🍃 Count Left is called 🍋 🍃")
    if num_idx > 0:
        print(f"The number we are considering is {line[num_idx]}")
        current_point = (line_idx, num_idx)
        if current_point not in visited_points and int(line[num_idx]) != 9:
            print(f"🧁 current point {current_point} not in visited points; counting 🍵")
            count = 1
            # visited_points.append(current_point)
        # count_left(line, line_idx, num_idx - 1, count)
    return count or 0


def count_down(line_idx, num_idx, input, count=0):
    # check to make sure it's not at the bottom edge
    if line_idx < (len(input) - 1):
        line = input[line_idx]
        current_point = (line_idx, num_idx)
        print("In count down, looking at ", input[line_idx][num_idx])
        if current_point not in visited_points and int(line[num_idx]) != 9:
            print("🐙 Hit a 9 in count down")
            count = 1
            # visited_points.append(current_point)

        # count_down(line_idx + 1, num_idx, input, count)
    return count or 0


def count_up(line_idx, num_idx, input, count=0):
    # check to make sure it's not at the top edge
    if line_idx > 0:
        line = input[line_idx]
        current_point = (line_idx, num_idx)
        print("In count up, looking at ", input[line_idx][num_idx])

        if current_point not in visited_points and int(line[num_idx]) != 9:
            count = 1
            # visited_points.append(current_point)
        # count_up(next_line, num_idx, input, count)
    return count or 0


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
