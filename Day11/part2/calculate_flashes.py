from functools import reduce
import ast

f = open("input.txt", "r")
input_data = f.read().split("\n")


def get_value(list, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return int(list[y][x])
    except:
        return None


def update_value(lists, x, y, value):
    lists[y][x] = value
    return int(value)


def adjacent(lists, x, y):
    x0 = x-1
    x2 = x+1
    y0 = y-1
    y2 = y+1
    adjacent_num = []
    for i in [[x, y0], [x, y2], [x0, y], [x2, y], [x0, y0], [x2, y0], [x0, y2], [x2, y2]]:
        value = get_value(lists, i[0], i[1])
        if value != None:
            adjacent_num.append(i)
    return adjacent_num


def reset(lists, flashes):
    for i in list(flashes):
        pos = ast.literal_eval(i)
        update_value(lists, pos[0], pos[1], 0)


def check_reset_count(lists):
    count = 0
    for y in range(len(lists)):
        nums = lists[y]
        for x in range(len(nums)):
            num = int(nums[x])
            if num > 9:
                count += 1
                update_value(lists, x, y, 0)
    return count


def update_adjacent(lists, x, y):
    value = update_value(lists, x, y, int(get_value(lists, x, y))+1)
    if value == 10:
        for i in adjacent(lists, x, y):
            update_adjacent(lists, i[0], i[1])


def calculate_flashes(input_data):
    lists = list(map(lambda x: list(x), input_data))
    totalLen = reduce(lambda x, y: x+len(y), lists, 0)
    count = 0
    step = 1
    while(True):
        for y in range(len(lists)):
            nums = lists[y]
            for x in range(len(nums)):
                update_adjacent(lists, x, y)
        count = check_reset_count(lists)
        if count == totalLen:
            return step
        step += 1


print(calculate_flashes(input_data))
