def calculate_power_consumption(numbers):
    numberLength = len(numbers[0])
    gama = 0
    epsilon = 0
    for i in range(numberLength):
        bits = list(map(lambda x: x[i], numbers))
        ones = len(list(filter(lambda x: x == "1", bits)))
        zeros = len(bits) - ones
        if ones > zeros:
            gama |= 1 << numberLength-i-1
            epsilon |= 0 << numberLength-i-1
        else:
            gama |= 0 << numberLength-i-1
            epsilon |= 1 << numberLength-i-1
    return gama*epsilon


f = open("binary_input.txt", "r")
numbers = f.read().split("\n")
print(calculate_power_consumption(numbers))
