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
    # print("num1 ", num1, " num2 ", num2)
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
    # print(num, x, y, x0, x2, y0, y2)
    partialFn = partial(check_if_num_lowest, num)
    return partialFn(get_value(lists, x, y0)) and partialFn(get_value(lists, x, y2)) and partialFn(get_value(lists, x0, y)) and partialFn(get_value(lists, x2, y))


def get_risk_levels(lists):
    entries = []
    for y in range(len(lists)):
        list = lists[y]
        for x in range(len(list)):
            num = int(list[x])
            if check_if_num_lowest_in_adjacent(lists, num, int(x), int(y)):
                # print(foo)
                # if foo:
                entries.append(num)
    return entries


def calculate_total(list):
    total = 0
    for e in list:
        total += e + 1
    return total


# print(input_data[0])
print(calculate_total(get_risk_levels(input_data)))
