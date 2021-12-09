import math

f = open("input.txt", "r")
input_data = list(map(lambda x: int(x), f.read().split(",")))


def count_new_fish(days, entry):
    if days < 0:
        return 0
    if days < 9:
        return 1
    prev = entry.get(days)
    if prev:
        return prev
    count = 1
    daysLeft = days-9
    while daysLeft >= 0:
        count += count_new_fish(daysLeft, entry)  # 0
        daysLeft -= 7
    entry[days] = count
    return count


def count_lanternfish(fishesLife, days):
    entry = {}
    entry2 = {}
    total = 0
    for fishLife in fishesLife:
        prev = entry.get(fishLife)
        if prev:
            total += prev
            continue
        count = 0
        daysLeft = days - fishLife - 1
        count += 1
        count += count_new_fish(daysLeft, entry2)
        while daysLeft >= 0:
            daysLeft -= 7
            # count += 1
            count += count_new_fish(daysLeft, entry2)
        total += count
        entry[fishLife] = count
    return total


print(count_lanternfish(input_data, 256))
