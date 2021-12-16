import math


def translate_hex_to_bits(hex):
    mappings = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
                "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    result = ""
    for char in list(hex):
        result += mappings[char]
    return result


def splice(text, index):
    return text[:index], text[index:]


subTypeMapping = {
    "000": sum,
    "001": math.prod,
    "010": min,
    "011": max,
    "101": lambda x: 1 if x[0] > x[1] else 0,
    "110": lambda x: 1 if x[0] < x[1] else 0,
    "111": lambda x: 1 if x[0] == x[1] else 0
}


def calculate_version(bits):
    _, rest = splice(bits, 3)
    id, rest = splice(rest, 3)
    length = 6
    if id == "100":
        val = ""
        while True:
            group, rest = splice(rest, 5)
            length += 5
            val += group[1:]
            if not group.startswith("1"):
                if len(rest) < 5:
                    return int(val, 2), length + len(rest)
                return int(val, 2), length
    lengthId, rest = splice(rest, 1)
    if lengthId == "0":
        totalLength, rest = splice(rest, 15)
        totalLength = int(totalLength, 2)
        operatorBits, rest = splice(rest, totalLength)
        values = []
        while True:
            val, subLength = calculate_version(
                operatorBits)
            _, operatorBits = splice(operatorBits, subLength)
            values.append(val)
            if len(operatorBits) == 0:
                return subTypeMapping[id](values), totalLength + 22
    count, rest = splice(rest, 11)
    count = int(count, 2)
    length = 18
    values = []
    for _ in range(count):
        val, subLength = calculate_version(rest)
        _, rest = splice(rest, subLength)
        length += subLength
        values.append(val)
    return subTypeMapping[id](values), length


f = open("input.txt", "r")
print(calculate_version(translate_hex_to_bits(f.read())))
