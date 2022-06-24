from enum import auto
import sys
from pathlib import Path

CLOSE_BRACKET_PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
OPENING_BRACKETS = CLOSE_BRACKET_PAIRS.values()
CLOSING_BRACKETS = CLOSE_BRACKET_PAIRS.keys()
OPEN_BRACKET_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}

POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def complete_lines(input):
    lines = get_incomplete_lines(input)

    unclosed_brackets = get_unclosed_brackets(lines)
    scores = []
    for brackets in unclosed_brackets:
        closing_brackets = []
        for bracket in brackets:
            closing_brackets.append(OPEN_BRACKET_PAIRS[bracket])
        closing_brackets.reverse()
        scores.append(score_line(closing_brackets))

    find_middle_score(scores)


def find_middle_score(scores):
    sorted_scores = sorted(scores)

    middle = sorted_scores[len(sorted_scores) // 2]
    print(f"🦆 Middle score: {middle}")


def score_line(autocomplete, total=0):
    for char in autocomplete:
        total *= 5
        total += POINTS[char]
    return total


def get_unclosed_brackets(input):
    list_of_unclosed_brackets = []
    for line in input:
        stack = []
        for bracket in line:
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)

            else:
                # bracket in CLOSING_BRACKETS
                if (
                    stack[-1] == CLOSE_BRACKET_PAIRS[bracket]
                ):  # if the brackets match we can remove them
                    stack.pop()
        list_of_unclosed_brackets.append(stack)
    return list_of_unclosed_brackets


def get_incomplete_lines(lines):
    incomplete_lines = lines[:]
    stack = []
    for line in lines:
        for bracket in line:
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            else:
                if (
                    stack[-1] == CLOSE_BRACKET_PAIRS[bracket]
                ):  # if the brackets match we can remove them
                    stack.pop()
                else:
                    incomplete_lines.remove(line)

                    break
    return incomplete_lines


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        complete_lines(input)
    else:
        raise TypeError("This is not a file")
