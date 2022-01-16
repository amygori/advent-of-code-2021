import sys
from pathlib import Path
from pprint import pprint as pp

DIGITS_BY_SEGMENTS = {
    7: 8,
    6: [0, 6, 9],
    5: [2, 3, 5],
    4: 4,
    3: 7,
    2: 1,
}

UNIQUE_LENGTHS = [2, 3, 4, 7]

def print_result(input):
    map_segments(input)


def map_segments(input):
    decoded_digits = []
    for line in input:
        data = line.partition("|")
        segments, _, output_value = data
        print("segments", segments)
        print("_", _)
        print("output_value", output_value)
        segment_map = {}

        for pattern in segments.split():
            if len(pattern) == 2:
                segment_map[1] = pattern
            elif len(pattern) == 3:
                segment_map[7] = pattern
            elif len(pattern) == 4:
                segment_map[4] = pattern
            elif len(pattern) == 7:
                segment_map[8] = pattern

        # map the unknown digits
        # map 6-digit patterns first so we can use them to deduce 5-digit patterns
        five_digits = [pattern for pattern in segments.split() if len(pattern) == 5]
        six_digits = [pattern for pattern in segments.split() if len(pattern) == 6]

        for pattern in six_digits:
            # if 7 is not a subset of this pattern it is a 6
            if not set(segment_map[7]).issubset(pattern):
                print(f"{pattern} has to be a 6")
                segment_map[6] = pattern
            # if 4 is a subset of pattern it is a 9
            elif set(segment_map[4]).issubset(pattern):
                print(f"{pattern} has to be a 9")
                segment_map[9] = pattern
            # anything else has to be 0
            else:
                print(f"{pattern} has to be a 0")
                segment_map[0] = pattern

        for pattern in five_digits:
            # if 7 is a subset of pattern it is a 3
            if set(segment_map[7]).issubset(pattern):
                print(f"{pattern} has to be a 3")
                segment_map[3] = pattern
            # if the pattern is a subset of 6 it is a 5
            elif set(pattern).issubset(segment_map[6]):
                print(f"{pattern} has to be a 5")
                segment_map[5] = pattern
            # anything else has to be 2
            else:
                print(f"{pattern} has to be a 2")
                segment_map[2] = pattern

        digit = decode_output_value(segment_map, output_value)
        print(digit)

def decode_output_value(segment_map, output):
    print(segment_map)
    output = output.strip().split()
    sorted_output_values = ["".join(sorted(value)) for value in output]
    sorted_values = ["".join(sorted(value)) for value in segment_map.values()]
    lookup_by_pattern = dict(zip(sorted_values, segment_map.keys()))
    digit = ''
    for num in [lookup_by_pattern[digit] for digit in sorted_output_values]:
        digit += str(num)
    return digit


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        map_segments(input)
    else:
        raise TypeError("This is not a file")
