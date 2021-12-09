import math
f = open("input.txt", "r")
input_data = list(map(lambda x: int(x), f.read().split(",")))


def calculate_fuel(positions):
    entry = {}
    lowest = math.inf
    for i in positions:
        prev = entry.get(i)
        if prev:
            if prev < lowest:
                lowest = prev
            continue
        total = 0
        for pos in positions:
            total += abs(pos - i)
        if total < lowest:
            lowest = total
        entry[i] = total
    return lowest


print(calculate_fuel(input_data))
