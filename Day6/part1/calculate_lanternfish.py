import math

f = open("input.txt", "r")
input_data = list(map(lambda x: int(x), f.read().split(",")))


def count_new_fish(days):
    if days < 0:
        return 0
    if days < 9:
        return 1
    count = 1
    daysLeft = days-9
    while daysLeft >= 0:
        count += count_new_fish(daysLeft)  # 0
        daysLeft -= 7
    return count


def count_lanternfish(fishesLife, days):
    count = 0
    for fishLife in fishesLife:
        daysLeft = days - fishLife - 1
        count += 1
        count += count_new_fish(daysLeft)
        while daysLeft >= 0:
            daysLeft -= 7
            count += count_new_fish(daysLeft)
    return count


print(count_lanternfish(input_data, 80))
