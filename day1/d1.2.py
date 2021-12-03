import sys
from pathlib import Path


def list_of_sums(input):
    data = list(input.split())
    sums = []
    for idx, num in enumerate(data):
        if idx == len(data) - 2:
            break
        sum = int(num) + int(data[idx + 1]) + int(data[idx + 2])
        sums.append(sum)
    return sums


def count_increases(input):
    data = list_of_sums(input)
    print(data)
    count = 0
    for idx, num in enumerate(data):
        prev_num = data[idx - 1]
        print((idx, num))
        if idx == 0:
            continue
        if (num < prev_num) or (num == prev_num):
            continue
        count += 1
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        count_increases(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
