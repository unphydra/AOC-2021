f = open("input.txt", "r")
input_data = f.read().split("\n")


def calculate_lines_overlaps(lines):
    coordinates = {}
    count = 0
    for line in lines:
        [first, second] = line.split(" -> ")
        [x1, y1] = map(lambda x: int(x), first.split(","))
        [x2, y2] = map(lambda x: int(x), second.split(","))
        # print(x1, y1, x2, y2, coordinates)
        if x1 == x2:
            # print("x equal")
            delta = 1 if y1 < y2 else -1
            # print("delta", delta)
            for i in range(y1, y2+delta, delta):
                key = '{},{}'.format(x1, i)
                # print("key to check", key)
                value = coordinates.get(key)
                if value == None:
                    # print("setting value of key:", key)
                    coordinates[key] = 1
                elif value == 1:
                    # print("in x", key)
                    count += 1
                    coordinates[key] += 1
        if y1 == y2:
            # print("y equal")
            delta = 1 if x1 < x2 else -1
            # print("delta", delta)
            for i in range(x1, x2+delta, delta):
                key = '{},{}'.format(i, y1)
                # print("key to check", key)
                value = coordinates.get(key)
                if value == None:
                    # print("setting value of key:", key)
                    coordinates[key] = 1
                elif value == 1:
                    # print("in y", key)
                    count += 1
                    coordinates[key] += 1
    return count


print(calculate_lines_overlaps(input_data))
