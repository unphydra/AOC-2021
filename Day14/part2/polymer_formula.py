from functools import reduce


def parse_rules(rules, ruleString):
    inst = ruleString.split(" -> ")
    rules.update({inst[0]: inst[1]})
    return rules


def check_and_update(pairs, pair, val):
    if pairs.get(pair) == None:
        pairs[pair] = 0
    pairs[pair] += val


def parse_input():
    f = open("input.txt", "r")
    formula, _, *rules = f.read().splitlines()
    rules = reduce(parse_rules, rules, {})
    pairs = {}
    for i in range(len(formula)-1):
        key = formula[i]+formula[i+1]
        check_and_update(pairs, key, 1)
    charCount = {}
    for c in formula:
        val = formula.count(c)
        charCount.update({c: val})
    return {"pairs": pairs, "rules": rules, "charCount": charCount}


def count_chars(info, step):
    pairs = info["pairs"].copy()
    for _ in range(step):
        for key, val in pairs.copy().items():
            middle = info["rules"][key]
            pairs[key] -= val
            firstPair = key[0] + middle
            check_and_update(pairs, firstPair, val)
            secondPair = middle + key[1]
            check_and_update(pairs, secondPair, val)
            check_and_update(info["charCount"], middle, val)
    return max(info["charCount"].values()) - min(info["charCount"].values())


print(count_chars(parse_input(), 40))
