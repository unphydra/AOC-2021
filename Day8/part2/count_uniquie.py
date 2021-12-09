f = open("input.txt", "r")
input_data = f.read().split("\n")


def calculate_value(map, entry, digit):
    numberString = 0
    for c in digit:
        numberString += entry[c]
    return map[numberString]


def find_and_remove(list, length):
    picked = None
    for item in list:
        if len(item) == length:
            picked = item
            break
    list.remove(picked)
    return picked


def read_pattern(patterns):
    values = {}
    entry = [set(pattern) for pattern in patterns]

    one = find_and_remove(entry, 2)
    seven = find_and_remove(entry, 3)
    thirdPosSet = seven.difference(one)

    eight = find_and_remove(entry, 7)
    zero = find_and_remove(entry, 6)
    six = find_and_remove(entry, 6)
    nine = find_and_remove(entry, 6)

    corner = eight.intersection(zero).intersection(six).intersection(nine)
    secondPosSet = one.difference(corner.intersection(one))
    sevenPosSet = one.difference(secondPosSet)

    four = find_and_remove(entry, 4)
    fourOneDiff = four.difference(one)
    fourthPosSet = fourOneDiff.intersection(corner)
    firstPosSet = four.difference(one).difference(fourthPosSet)

    sixthPosSe = corner.difference(four).difference(thirdPosSet)
    fifthPosSet = eight.difference(four).difference(corner)

    values[firstPosSet.pop()] = 1
    values[secondPosSet.pop()] = 2
    values[thirdPosSet.pop()] = 3
    values[fourthPosSet.pop()] = 4
    values[fifthPosSet.pop()] = 5
    values[sixthPosSe.pop()] = 6
    values[sevenPosSet.pop()] = 7
    return values


valueNumberMap = {27: "0", 9: "1", 17: "2", 19: "3",
                  14: "4", 21: "5", 26: "6", 12: "7", 28: "8", 23: "9"}


def read_digits(pattarns, digits):
    pattarnData = read_pattern(pattarns)
    numberString = ""
    for digit in digits:
        numberString += calculate_value(valueNumberMap, pattarnData, digit)
    return numberString


def calculate_output(notes):
    total = 0
    for note in notes:
        total += int(read_digits(*list(map(lambda x: x.split(), note.split(" | ")))))
    return total


print(calculate_output(input_data))
