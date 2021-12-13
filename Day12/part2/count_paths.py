from functools import reduce


def update_dict(paths, entry):
    dir = entry.split("-")
    cave_from, cave_to = dir
    if cave_from != 'end' and cave_to != 'start':
        connectedTo = paths.get(cave_from) or []
        connectedTo.append(cave_to)
        paths[cave_from] = connectedTo
    if cave_from != 'start' and cave_to != 'emd':
        connectedTo = paths.get(cave_to) or []
        connectedTo.append(cave_from)
        paths[cave_to] = connectedTo

    return paths


def get_parse_input():
    f = open("input.txt", "r")
    return reduce(update_dict, f.read().split("\n"), {})


def check_small_cave_twice(path):
    for p in path:
        if p.isupper() == False:
            if path.count(p) >= 2:
                return True
    return False


def calculate_paths(paths):
    count = 0
    currentPaths = [['start']]
    while(len(currentPaths) > 0):
        newPaths = []
        for path in currentPaths:
            last = path[-1]
            for next in paths[last]:
                if next == 'end':
                    count += 1
                    continue
                if next.isupper() == False and check_small_cave_twice(path):
                    try:
                        path.index(next)
                    except:
                        newPath = path.copy()
                        newPath.append(next)
                        newPaths.append(newPath)
                    continue
                newPath = path.copy()
                newPath.append(next)
                newPaths.append(newPath)
        currentPaths = newPaths
    return count


print(calculate_paths(get_parse_input()))
