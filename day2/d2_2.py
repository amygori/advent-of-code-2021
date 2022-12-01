import sys
from pathlib import Path


class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0

    def down(self, increment):
        self.aim += increment

    def up(self, increment):
        self.aim -= increment

    def forward(self, increment):
        self.horizontal_position += increment
        self.depth += self.aim * increment


def pilot_the_sub(steps, submarine):
    for step in steps:
        direction, increment = step.split()
        go = getattr(submarine, direction)
        go(int(increment))

    print(submarine.depth * submarine.horizontal_position)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        with Path(file).open() as f:
            input = f.read().splitlines()
            submarine = Submarine()
            pilot_the_sub(input, submarine)
    else:
        raise TypeError("This is not a file")
