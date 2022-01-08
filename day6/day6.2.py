import sys
from pathlib import Path

fish_states = {}


def simulate(fish_list, count=0):
    initial_states(fish_list)
    track_states()
    print(sum(fish_states.values()))


def track_states(count=0):
    if count == 256:
        return
    count += 1

    # add_new_fish
    number_of_new_fish = fish_states[0]

    # update fish states
    for state in fish_states.keys():
        if state < 8:
            fish_states[state] = fish_states[state + 1]
        else:
            fish_states[state] = number_of_new_fish

    fish_states[6] += number_of_new_fish

    track_states(count=count)


def initial_states(fish_list):
    for state in range(0, 9):
        fish_states[state] = 0
    for fish in fish_list:
        try:
            fish_states[fish] += 1
        except KeyError:
            fish_states[fish] = 1


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).strip().split(",")
        input = [int(num) for num in input]
        simulate(input)
    else:
        raise TypeError("This is not a file")
