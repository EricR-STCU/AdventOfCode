from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    data = [l.strip() for l in f]
    
vis = defaultdict(bool)
Y = len(data[0])
X = len(data)


def is_vis(x, y):
    val = data[x][y]
    l = all(data[x][i] < val for i in range(0, y))
    r = all(data[x][i] < val for i in range(Y-1, y, -1))
    u = all(data[i][y] < val for i in range(0, x))
    d = all(data[i][y] < val for i in range(X-1, x, -1))
    return l or r or u or d


def sees(x,y):
    if y == 0 or x == 0 or x == X - 1 or y == Y - 1:
        return 0

    val = data[x][y]
    total = 1

    # left
    cur = y - 1
    while cur > 0 and not data[x][cur] >= val:
        cur -= 1
    total *= y-cur

    # right
    cur = y + 1
    while cur < Y - 1 and not data[x][cur] >= val:
        cur += 1
    total *= cur-y

    # up
    cur = x - 1
    while cur > 0 and not data[cur][y] >= val:
        cur -= 1
    total *= x-cur

    # down
    cur = x + 1
    while cur < X - 1 and not data[cur][y] >= val:
        cur += 1
    total *= cur-x

    return total


def p1():
    for x, line in enumerate(data):
        for y, val in enumerate(line):
            vis[(x,y)] = is_vis(x,y)
    return sum(i for i in vis.values())


def p2():
    for x, line in enumerate(data):
        for y, val in enumerate(line):
            vis[(x,y)] = sees(x,y)
    return max(i for i in vis.values())


print(p1())
print(p2())