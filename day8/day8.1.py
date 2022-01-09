import sys
from pathlib import Path

DIGITS_BY_SEGMENTS = {
    7: 8,
    6: [0, 6, 9],
    5: [2, 3, 5],
    4: 4,
    3: 7,
    2: 1,
}

UNIQUE_VALUES = [2, 3, 4, 7]


def decode_segments(input):
    count = 0
    for line in input:
        data = line.partition("|")
        patterns, _, output_value = data
        for seq in output_value.split():
            if len(seq) in UNIQUE_VALUES:
                count += 1
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        decode_segments(input)
    else:
        raise TypeError("This is not a file")
