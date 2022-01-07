from collections import Counter
from pathlib import Path
import sys

graph = {}


def read_coordinates(input):
    coordinates = [item.split(" -> ") for item in input]
    plot_coordinates(coordinates)


def plot_coordinates(coordinates):
    for item in coordinates:
        segment_start = item[0].split(",")
        segment_end = item[1].split(",")
        x1 = int(segment_start[0])
        y1 = int(segment_start[1])
        x2 = int(segment_end[0])
        y2 = int(segment_end[1])
        if x1 == x2:
            start, end = sorted([y1, y2])
            for y in range(start, end + 1):
                if (x1, y) not in graph:
                    graph[(x1, y)] = 1
                else:
                    graph[(x1, y)] += 1
        if y1 == y2:
            start, end = sorted([x1, x2])
            for x in range(start, end + 1):
                if (x, y1) not in graph:
                    graph[(x, y1)] = 1
                else:
                    graph[(x, y1)] += 1
    print_report()


def print_report():
    count = Counter(graph.values())
    # count only values larger than 1
    print(count.total() - count[1])


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        read_coordinates(input)
    else:
        raise TypeError("This is not a file")
