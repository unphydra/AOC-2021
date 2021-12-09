from functools import reduce
from math import dist, floor

f = open("input.txt", "r")
input_data = f.read().split("\n\n")
numbers = input_data.pop(0).split(",")


def constructDict(context, currentValue, pos_x, pos_y):
    context.update({currentValue: {"marked": False, "x": pos_x, "y": pos_y}})
    return context


boards = list(map(lambda numberString: reduce(lambda context, nSet: constructDict(context,
                                                                                  nSet[1], nSet[0] % 5, floor(nSet[0]/5)), enumerate(numberString.split()), {}), input_data))


def populate(dict):
    dict["marked"] = True
    return dict


def checkForWinningBoard(board):
    row = {0: True, 1: True, 2: True, 3: True, 4: True}
    column = {0: True, 1: True, 2: True, 3: True, 4: True}
    for _, value in board.items():
        row[value["y"]] &= value["marked"]
        column[value["x"]] &= value["marked"]
    win = any(x == True for x in list(row.values())+list(column.values()))
    return win


def run_bingo(board, numbers):
    for number in numbers:
        for board in boards:
            dict = board.get(number)
            if dict:
                populate(dict)
            if checkForWinningBoard(board):
                return {"board": board, "number": number}


def calculate_score(boardDetails):
    total = 0
    for key, dict in boardDetails["board"].items():
        if dict["marked"] == False:
            total += int(key)
    return total * int(boardDetails["number"])


score = calculate_score(run_bingo(boards, numbers))
print(score)
