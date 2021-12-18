import math


def check(vx, vy, data):
    minX, maxX, minY, maxY = data
    x = 0
    y = 0
    while True:
        x = x + vx
        y = y + vy
        vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else 0
        vy = vy - 1
        if minX <= x and x <= maxX and minY <= y and y <= maxY:
            return True
        elif maxX < x or y < minY:
            return False


def countDistinctVelocities(data):
    minX, maxX, minY, _ = data
    count = 0
    for vx in range(math.ceil(math.sqrt(minX)), maxX+1):
        for vy in range(minY, minY * -1+1):
            if check(vx, vy, data):
                count += 1
    return count


# target area: x=20..30, y=-10..-5
example = (20, 30, -10, -5)
# target area: x=156..202, y=-110..-69
problem = (156, 202, -110, -69)

print(countDistinctVelocities(problem))
