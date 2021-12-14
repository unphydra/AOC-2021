def parse_rules(ruleString):
    inst = ruleString.split(" -> ")
    pair: list = list(inst[0])
    elem = inst[1].lower()
    pair.insert(1, elem)
    inst[1] = "".join(pair)
    return inst


def parser_input():
    f = open("input.txt", "r")
    inputData = f.read().split("\n\n")
    rules = list(map(parse_rules,  inputData[1].split("\n")))
    return {"formula": inputData[0], "rules": rules}


def replace(formula, pair, elem):
    newFormula = formula.replace(pair, elem)
    if newFormula == formula:
        return newFormula
    return replace(newFormula, pair, elem)


def apply_rules(info):
    formula = info["formula"]
    for _ in range(10):
        newFormula = formula
        for pair, elem in info["rules"]:
            newFormula = replace(newFormula, pair, elem)
        formula = newFormula.upper()
    return formula


def calculate_most_sub_least(formula):
    counts = {}
    results = []
    formulas = list(formula)
    for char in formulas:
        if counts.get(char) == None:
            count = formulas.count(char)
            counts.update({char: count})
            results.append({"char": char, "count": count})
    sortedFormulas = sorted(results, key=lambda x: x["count"])
    lowest = sortedFormulas[0]
    highest = sortedFormulas[-1]
    return highest["count"] - lowest["count"]


print(calculate_most_sub_least(apply_rules(parser_input())))
