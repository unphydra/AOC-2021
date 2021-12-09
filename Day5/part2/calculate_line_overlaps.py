f = open("input.txt", "r")
input_data = f.read().split("\n")


def calculate_lines_overlaps(lines):
    coordinates = {}
    count = 0
    for line in lines:
        [first, second] = line.split(" -> ")
        [x1, y1] = map(lambda x: int(x), first.split(","))
        [x2, y2] = map(lambda x: int(x), second.split(","))
        if x1 == x2:
            delta = 1 if y1 < y2 else -1
            for i in range(y1, y2+delta, delta):
                key = '{},{}'.format(x1, i)
                value = coordinates.get(key)
                if value == None:
                    coordinates[key] = 1
                elif value == 1:
                    count += 1
                    coordinates[key] += 1
        if y1 == y2:
            delta = 1 if x1 < x2 else -1
            for i in range(x1, x2+delta, delta):
                key = '{},{}'.format(i, y1)
                value = coordinates.get(key)
                if value == None:
                    coordinates[key] = 1
                elif value == 1:
                    count += 1
                    coordinates[key] += 1
        try:
            slope = (y2-y1)/(x2-x1)
            if slope == 1.0 or slope == -1.0:
                deltaX = 1 if x1 < x2 else -1
                deltaY = 1 if y1 < y2 else -1
                y = y1 - deltaY
                for i in range(x1, x2+deltaX, deltaX):
                    y += deltaY
                    key = '{},{}'.format(i, y)
                    value = coordinates.get(key)
                    if value == None:
                        coordinates[key] = 1
                    elif value == 1:
                        count += 1
                        coordinates[key] += 1
        except:
            continue
    return count


print(calculate_lines_overlaps(input_data))
