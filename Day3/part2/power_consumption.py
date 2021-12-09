def calculate_gasses_rating(numbers, fn):
    numberLength = len(numbers[0])
    newNumbers = numbers

    for i in range(numberLength):
        bits = list(map(lambda x: x[i], newNumbers))
        ones = len(list(filter(lambda x: x == "1", bits)))
        zeros = len(bits) - ones
        newNumbers = list(
            filter(lambda num: fn(num, ones, zeros, i), newNumbers))
        if len(newNumbers) == 1:
            break
    return int(newNumbers[0], 2)


def check_oxygen(numbers, ones, zeros, i):
    if ones >= zeros:
        return numbers[i] == "1"
    return numbers[i] == "0"


def check_co2(numbers, ones, zeros, i):
    if ones >= zeros:
        return numbers[i] == "0"
    return numbers[i] == "1"


f = open("binary_input.txt", "r")
numbers = f.read().split("\n")

co2 = calculate_gasses_rating(numbers, check_co2)
oxy = calculate_gasses_rating(numbers, check_oxygen)
print(co2*oxy)
