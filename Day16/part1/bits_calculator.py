
def translate_hex_to_bits(hex):
    mappings = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
                "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    result = ""
    for char in list(hex):
        result += mappings[char]
    return result


def splice(text, index):
    return text[:index], text[index:]


def calculate_version(bits):
    version, rest = splice(bits, 3)
    version = int(version, 2)
    id, rest = splice(rest, 3)
    length = 6
    if id == "100":
        while True:
            group, rest = splice(rest, 5)
            length += 5
            if not group.startswith("1"):
                if len(rest) < 5:
                    return version, length + len(rest)
                return version, length
    lengthId, rest = splice(rest, 1)
    if lengthId == "0":
        totalLength, rest = splice(rest, 15)
        totalLength = int(totalLength, 2)
        operatorBits, rest = splice(rest, totalLength)
        while True:
            subVersion, subLength = calculate_version(
                operatorBits)
            _, operatorBits = splice(operatorBits, subLength)
            version += subVersion
            if len(operatorBits) == 0:
                return version, totalLength + 22
    count, rest = splice(rest, 11)
    count = int(count, 2)
    length = 18
    for _ in range(count):
        subVersion, subLength = calculate_version(rest)
        _, rest = splice(rest, subLength)
        version += subVersion
        length += subLength
    return version, length


f = open("input.txt", "r")
print(calculate_version(translate_hex_to_bits(f.read())))
