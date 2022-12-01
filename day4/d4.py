import sys
from pathlib import Path
from itertools import chain, filterfalse
from operator import indexOf
from pprint import pprint as pp
from pdb import set_trace as bp

win = False
score = 0
boards = []
winning_boards = []


def flatten(list_of_lists):
    """Flatten one level of nesting"""
    return chain.from_iterable(list_of_lists)


def play(input):
    numbers, *board_data = input
    numbers = numbers.split(",")
    make_boards(board_data)
    print("boards: 🍌")
    print(boards)
    for count, number in enumerate(numbers):
        mark_boards(number)
    winning_board_idx, winning_num = winning_boards[-1]
    calc_score(boards[int(winning_board_idx)], winning_num)


def make_boards(board_data):
    """
    Take the board data and compose into 5x5 arrays
    """
    # [[''], ['22 13 17 11  0'], [' 8  2 23  4 24'], ['21  9 14 16  7'], [' 6 10  3 18  5'], [' 1 12 20 15 19'], [''], [' 3 15  0  2 22'], [' 9 18 13 17  5'], ['19  8  7 25 23'], ['20 11 10 24  4'], ['14 21 16 12  6'], [''], ['14 21 17 24  4'], ['10 16 15  9 19'], ['18  8 23 26 20'], ['22 11 13  6  5'], [' 2  0 12  3  7']]
    data = [item.split() for item in board_data]
    for count, row_set in enumerate(data):
        if not row_set:
            # Start new board
            boards.append([])
            continue
        try:
            boards[len(boards) - 1].append([num for num in row_set])
        except IndexError as err:
            print(err)


def mark_boards(bingo_num):
    for idx, board in enumerate(boards):
        if indexOf(boards, board) in dict(winning_boards):
            # If this board has already won, don't continue marking it
            continue
        for index, row in enumerate(board):
            for i, each_num in enumerate(row):
                if each_num == bingo_num:
                    row[i] = "X"
            check_for_bingo(board, bingo_num)


def check_for_bingo(board, bingo_num):
    """Check for five marked numbers in a row horizontally or vertically"""
    check_row(board, bingo_num)
    check_column(board, bingo_num)


def check_row(board, bingo_num):
    for row in board:
        if all(item in ["X"] for item in row):
            claim_bingo(board, bingo_num)
            break


def check_column(board, bingo_num):
    for col in range(5):
        column = []
        for row in board:
            column.append(row[col])
        if all(item in ["X"] for item in column):
            claim_bingo(board, bingo_num)
            break


def calc_score(board, winning_num):
    board_nums = list(filterfalse(lambda n: n == "X", flatten(board)))
    score = int(winning_num) * sum([int(num) for num in board_nums])
    print(score)


def claim_bingo(board, bingo_num):
    if indexOf(boards, board) not in dict(winning_boards):
        # Track boards that have won and the number they won with
        winning_boards.append((indexOf(boards, board), bingo_num))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        play(input)
    else:
        raise TypeError("This is not a file")

