import sys
from pathlib import Path
from operator import indexOf
from types import new_class


def simulate(fish_list, count=0):
    new_fish = 0
    if count == 0:
        print("Intial state: ", fish_list)
    if count == 80:
        print(len(fish_list))
        return
    count += 1
    new_fish_list = []
    for fish in fish_list:
        if int(fish) > 0:
            new_fish_list.append(int(fish) - 1)
        else:
            new_fish_list.append(6)
            new_fish += 1
    if new_fish:
        for i in range(new_fish):
            new_fish_list.append(8)

    simulate(new_fish_list, count=count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).strip().split(",")
        input = [int(num) for num in input]
        simulate(input)
    else:
        raise TypeError("This is not a file")
