import sys
from pathlib import Path

BRACKET_PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
OPENING_BRACKETS = BRACKET_PAIRS.values()
CLOSING_BRACKETS = BRACKET_PAIRS.keys()


POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def check_balanced_brackets(input):
    stack = []
    illegal_chars = []
    for line in input:
        for bracket in line:
            print(bracket)
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            else:
                # bracket in CLOSING_BRACKETS
                if (
                    stack[-1] == BRACKET_PAIRS[bracket]
                ):  # if the brackets match we can remove them
                    stack.pop()
                else:
                    print("corrupt 😈")
                    prev_bracket = stack[-1]
                    illegal_chars.append(bracket)
                    break
    print(illegal_chars)
    get_syntax_error_score(illegal_chars)


def get_syntax_error_score(errors):
    print("score:")
    print(sum([POINTS[err] for err in errors]))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        check_balanced_brackets(input)
    else:
        raise TypeError("This is not a file")
