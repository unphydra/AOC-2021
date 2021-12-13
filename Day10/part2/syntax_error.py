f = open("input.txt", "r")
input_data = f.read().split("\n")


chuckSyntaxMap = {"(": ")", "{": "}", "[": "]", "<": ">"}
openings = {"(", "{", "[", "<"}


def get_last(list):
    try:
        return list[-1]
    except:
        return None


valueMap = {")": 1, "]": 2, "}": 3, ">": 4}


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
        return None
    listToCheck.reverse()
    total = 0
    for i in listToCheck:
        total *= 5
        total += valueMap[i]
    return total


def run_suntax_check(lists):
    wrongSyntax = []
    for list in lists:
        result = check_for_closing(list)
        if result != None:
            wrongSyntax.append(result)
    return sorted(wrongSyntax)[int(len(wrongSyntax)/2)]


print(run_suntax_check(input_data))
