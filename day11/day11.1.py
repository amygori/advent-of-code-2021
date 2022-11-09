import sys
from pathlib import Path
from octopus import Octopus


octopuses = []


def count_flashes(input):
    assemble_octopus_grid(input)
    for i in range(1, 3):
        step(i)
        for row in octopuses:
            print([octopus.energy_level for octopus in row])


def assemble_octopus_grid(input):
    global octopuses
    for row_index, row in enumerate(input):
        grid_row = []
        for col_index, col in enumerate(row):
            octopus = Octopus(energy_level=int(col), x=int(col_index), y=int(row_index))
            grid_row.append(octopus)
        octopuses.append(grid_row)


def step(step):
    global octopuses
    for octopus_row in octopuses:
        for octopus in octopus_row:
            increase_energy_levels(octopus, step)
            check_for_flash_condition(step)
            reset_flashed_octopuses(step)
    print(f"🐬 finished step {step}")


def check_for_flash_condition(step):
    for octopus_row in octopuses:
        for octopus in octopus_row:
            if octopus.energy_level > 9 and not octopus.flashed_on_this_step(step):
                octopus.flash(step)
                for adjacent_octopus in octopus.adjacents:
                    increase_energy_levels(octopus, step)


def reset_flashed_octopuses(step):
    for octopus_row in octopuses:
        for octopus in octopus_row:
            if octopus.flashed_on_this_step(step):
                octopus.reset_energy_level()


def increase_energy_levels(octopus, step):
    if octopus.flashed_on_this_step(step):
        return
    octopus.increase_energy_level(step)

    # if octopus > 9 then it flashes
    # adjacent octopuses (horizontal, vertical, and diagonal) increase by 1
    # if octopus > 9 it flashes
    # continue as long as new octopuses are increased > 9
    # an octopus can only flash once per step
    # if octopus has flashed, it resets to 0


def should_flash(octopus):
    # if energy level > 9
    # if adjacent octopus has flashed
    # if it has not already flashed this step
    pass


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        count_flashes(input)
    else:
        raise TypeError("This is not a file")
