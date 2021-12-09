with open('./day9.txt') as f:
    data = [l.strip() for l in f.readlines()]
    data = [[int(x) for x in l] for l in data]


def find_basin(d, x_, y_):
    check = [(x_,y_)]
    basin = []
    while check:
        p = check.pop()
        x,y = p[0], p[1]
        if d[x][y] == 9 or d[x][y] == -1:
            continue
        if x!=0:
            check.append((x-1, y))
        if x!=len(d)-1:
            check.append((x+1, y))
        if y!=0:
            check.append((x, y-1))
        if y!=len(d[0])-1:
            check.append((x, y+1))
        d[x][y] = -1
        basin.append((x,y))
    return len(basin)


def part1():
    d = [*data]
    lows = 0
    for x, l in enumerate(d):
        for y, value in enumerate(l):
            if (x==0 or value < d[x-1][y]) and \
            (x==len(d)-1 or value < d[x+1][y]) and \
            (y==0 or value < d[x][y-1]) and \
            (y==len(l)-1 or value < d[x][y+1]):
                lows += value + 1
    return lows


def part2():
    d = [*data]
    sizes = []
    for x, l in enumerate(d):
        for y, value in enumerate(l):
            if (x==0 or value < d[x-1][y]) and \
            (x==len(d)-1 or value < d[x+1][y]) and \
            (y==0 or value < d[x][y-1]) and \
            (y==len(l)-1 or value < d[x][y+1]):
                sizes.append(find_basin(d, x, y))
    sizes.sort()
    return sizes[-1]*sizes[-2]*sizes[-3]


print(part1())
print(part2())