import heapq


def parse_input():
    f = open("input.txt", "r")
    inputData = f.read().splitlines()
    entries = {}
    lastX = 0
    lastY = 0
    newEntries = {}
    for y in range(len(inputData)):
        if y > lastY:
            lastY = y
        line = list(inputData[y])
        for x in range(len(line)):
            if x > lastX:
                lastX = x
            elem = int(line[x])
            entries.update({(x, y): elem})
    newMaxX = 0
    newMaxY = 0
    for y in range(5):
        for x in range(5):
            for pos, val in entries.items():
                X, Y = pos
                newVal = val + x + y
                newX = X+((lastX+1)*x)
                newY = Y+((lastY+1)*y)
                if newX > newMaxX:
                    newMaxX = newX
                if newY > newMaxY:
                    newMaxY = newY
                newEntries.update(
                    {(newX, newY): newVal if newVal < 10 else newVal % 9})
    return {"entries": newEntries, "last": (newMaxX, newMaxY)}
    # return {"entries": entries, "last": (lastX, lastY)}


def get_low_risk_path(info):
    queue = [(0, (0, 0))]
    minRisk = {(0, 0): 0}
    visited = {(0, 0)}

    while queue:
        risk, (x, y) = heapq.heappop(queue)
        if (x, y) == info["last"]:
            return risk

        for adjacent in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
            if adjacent not in info["entries"] or adjacent in visited:
                continue
            visited.add(adjacent)
            newRisk = risk + info["entries"][adjacent]
            if newRisk < minRisk.get(adjacent, 999999):
                minRisk[adjacent] = newRisk
                heapq.heappush(queue, (newRisk, adjacent))


print(get_low_risk_path(parse_input()))
