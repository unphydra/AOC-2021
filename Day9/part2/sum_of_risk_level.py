f = open("input.txt", "r")
input_data = list(map(lambda x: list(x), f.read().split("\n")))


def get_value(list, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return int(list[y][x])
    except:
        return None


def check_if_num_lowest(num1, num2):
    if num2 == None:
        return True
    return num1 < num2


def partial(fn, arg):
    return lambda x: fn(arg, x)


def check_if_num_lowest_in_adjacent(lists, num, x, y):
    x0 = x-1
    x2 = x+1
    y0 = y-1
    y2 = y+1
    partialFn = partial(check_if_num_lowest, num)
    return partialFn(get_value(lists, x, y0)) and partialFn(get_value(lists, x, y2)) and partialFn(get_value(lists, x0, y)) and partialFn(get_value(lists, x2, y))


def get_risk_levels(lists):
    entries = {}
    for y in range(len(lists)):
        list = lists[y]
        for x in range(len(list)):
            num = int(list[x])
            if check_if_num_lowest_in_adjacent(lists, num, int(x), int(y)):
                key = get_point(x, y)
                entries[key] = key
    return entries


def get_coordinate(point):
    return list(map(lambda x: int(x), point.split(',')))


def get_point(x, y):
    return '{},{}'.format(x, y)


def get_adjacent(cord):
    x, y = cord
    return [
        [x, y+1],
        [x, y-1],
        [x-1, y],
        [x+1, y]
    ]


def crawl_and_count(lists, entries, startingPoint):
    points = startingPoint.copy()
    count = 0
    visited = {}
    while len(points) > 0:
        newPoints = []
        for point in points:
            if(visited.get(point) != None):
                continue
            if(entries.get(point) != None):
                return None
            entries[point] = point
            visited[point] = point
            count += 1
            cord = get_coordinate(point)
            adjacent = get_adjacent(cord)
            for x, y in adjacent:
                value = get_value(lists, x, y)
                if value != None and value != 9:
                    newPoints.append(get_point(x, y))
        points = newPoints
    return count


def calculate_basin(lowPoints, lists):
    entries = {}
    counts = []
    for point in lowPoints.keys():
        count = crawl_and_count(lists, entries, [point])
        counts.append(count)
    return counts


def multiple_three_largest_basin(list):
    l = sorted(list, reverse=True)
    return l[0]*l[1]*l[2]


lowPoints = get_risk_levels(input_data)
print(lowPoints)
print(multiple_three_largest_basin(calculate_basin(lowPoints, input_data)))
