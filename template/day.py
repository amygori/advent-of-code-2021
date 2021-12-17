import sys
from pathlib import Path


def do_the_thing(input):
    print(input)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        do_the_thing(input)
    else:
        raise TypeError("This is not a file")
