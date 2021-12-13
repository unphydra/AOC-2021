def parse_input():
    f = open("input.txt", "r")
    inputData = f.read().split("\n\n")
    cords = set(inputData[0].split("\n"))
    folds = inputData[1].split("\n")
    return {"cords": cords, "folds": folds}


def fold_and_count(cords, line, pos):
    newCords = set()
    for cordString in cords:
        cord = cordString.split(',')
        x = int(cord[0])
        y = int(cord[1])
        if line == 'x':
            if x > pos:
                newX = pos + pos - x
                newCords.add('{},{}'.format(newX, y))
                continue
        if line == 'y':
            if y > pos:
                newY = pos + pos - y
                newCords.add('{},{}'.format(x, newY))
                continue
        newCords.add(cordString)
    return len(newCords)


def get_first_fold(folds):
    foldData = folds[0].split("=")
    num = int(foldData[1])
    line = foldData[0].split(" ")[-1]
    return [line, num]


input = parse_input()
print(fold_and_count(input["cords"], *get_first_fold(input["folds"])))
