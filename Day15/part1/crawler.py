import math


def get_pos(x, y):
    return '{},{}'.format(x, y)


def get_cord(pos):
    return list(map(lambda x: int(x), pos.split(',')))


def parse_input():
    f = open("input.txt", "r")
    inputData = f.read().splitlines()
    entries = {}
    lastX = 0
    lastY = 0
    for y in range(len(inputData)):
        if y > lastY:
            lastY = y
        line = list(inputData[y])
        for x in range(len(line)):
            if x > lastX:
                lastX = x
            elem = int(line[x])
            entries.update({get_pos(x, y): elem})
    return {"entries": entries, "last": get_pos(lastX, lastY)}


def get_adjacent(entries, pos):
    cord = get_cord(pos)
    x = cord[0]
    y = cord[1]
    result = []
    for ad in [get_pos(x, y-1), get_pos(x, y+1), get_pos(x-1, y), get_pos(x+1, y)]:
        val = entries.get(ad)
        if val != None:
            result.append([val, ad])
    return sorted(result)


def get_low_risk_path(info):
    points = [['0,0', 0]]
    lowestRisk = math.inf
    keyRisk = {}
    while(len(points) != 0):
        newPoints = []
        for key, totalRisk in points:
            prevRisk = keyRisk.get(key)
            if prevRisk != None and prevRisk <= totalRisk:
                continue
            else:
                keyRisk[key] = totalRisk
            if totalRisk >= lowestRisk:
                continue
            if key == info["last"]:
                if lowestRisk > totalRisk:
                    lowestRisk = totalRisk
                continue
            # print(key, totalRisk)
            for val, adjacent in get_adjacent(info["entries"], key):
                newPoints.append([adjacent, totalRisk+val])
        points = newPoints
    # print(keyRisk)
    return lowestRisk


print(get_low_risk_path(parse_input()))
