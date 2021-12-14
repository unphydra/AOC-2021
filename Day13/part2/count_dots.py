def parse_input():
    f = open("input.txt", "r")
    inputData = f.read().split("\n\n")
    cords = set(inputData[0].split("\n"))
    folds = inputData[1].split("\n")
    return {"cords": cords, "folds": folds}


def folded_cords(cords, line, pos):
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
    return newCords


def get_fold_data(fold):
    foldData = fold.split("=")
    num = int(foldData[1])
    line = foldData[0].split(" ")[-1]
    return [line, num]


def get_highest(cords, pos):
    highest = 0
    for cordString in cords:
        cord = cordString.split(',')
        if int(cord[pos]) > highest:
            highest = int(cord[pos])
    return highest


def show_paper(cords: set):
    print(cords)
    X = get_highest(cords, 0)
    Y = get_highest(cords, 1)
    print(X, Y)
    for y in range(Y+1):
        line = ""
        for x in range(X+1):
            try:
                cords.index('{},{}'.format(x, y))
                line += '#'
            except:
                line += "."
        print(line)


def fold_paper_and_show():
    input = parse_input()
    newCords = input["cords"]
    for fold in input["folds"]:
        newCords = folded_cords(newCords, *get_fold_data(fold))
    show_paper(list(newCords))


fold_paper_and_show()
