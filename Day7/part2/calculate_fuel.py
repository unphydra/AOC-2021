import math
f = open("input.txt", "r")
input_data = list(map(lambda x: int(x), f.read().split(",")))


def calculate_fuel(positions):
    entry = {}
    lowest = math.inf
    largest = sorted(positions)[-1]
    for i in range(largest+1):
        prev = entry.get(i)
        if prev:
            if prev < lowest:
                lowest = prev
            continue
        total = 0
        for pos in positions:
            n = abs(pos - i)
            n2 = (n*(n+1))/2
            total += n2
        if total < lowest:
            lowest = total
        entry[i] = total
    return lowest


print(calculate_fuel(input_data))
