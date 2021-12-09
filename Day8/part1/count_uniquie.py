f = open("input.txt", "r")
input_data = list(map(lambda x:   x.split(
    "|")[1].strip().split(" "), f.read().split("\n")))


def count_unique(lists):
    count = 0
    for list in lists:
        for x in list:
            length = len(x)
            if length == 2 or length == 4 or length == 3 or length == 7:
                count += 1
    return count


print(count_unique(input_data))
