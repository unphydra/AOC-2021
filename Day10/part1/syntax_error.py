f = open("input.txt", "r")
input_data = f.read().split("\n")


chuckSyntaxMap = {"(": ")", "{": "}", "[": "]", "<": ">"}
openings = {"(", "{", "[", "<"}


def get_last(list):
    try:
        return list[-1]
    except:
        return None


def check_for_closing(list):
    listToCheck = []
    for item in list:
        itemInSet = item in openings
        if itemInSet:
            closing = chuckSyntaxMap[item]
            listToCheck.append(closing)
            continue
        lastClosing = get_last(listToCheck)
        if item == lastClosing:
            listToCheck.pop()
            continue
        return item
    return None


valueMap = {")": 3, "]": 57, "}": 1197, ">": 25137}


def run_suntax_check(lists):
    wrongSyntax = []
    total = 0
    for list in lists:
        result = check_for_closing(list)
        if result != None:
            wrongSyntax.append(result)
    for syntax in wrongSyntax:
        total += valueMap[syntax]
    return total


print(run_suntax_check(input_data))
