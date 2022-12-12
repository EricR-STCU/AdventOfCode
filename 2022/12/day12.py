from collections import defaultdict, Counter, deque
from string import ascii_lowercase

with open('./in.txt') as f:
    data = [list(l.strip()) for l in f.readlines()]
    
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 'S':
                S = (x,y)
                data[y][x] = 'a'
            if data[y][x] == 'E':
                E = (x,y)
                data[y][x] = 'z'
    

def can_go(cur, target):
    return ascii_lowercase.index(target) <= ascii_lowercase.index(cur) + 1


def letter(p):
    return data[p[1]][p[0]]


def get_neighbors(p):
    r = []
    if 0 <= p[0] < len(data[0]) - 1: r.append((p[0] + 1, p[1]))
    if 0 < p[0] < len(data[0]): r.append((p[0] - 1, p[1]))
    if 0 <= p[1] < len(data) - 1: r.append((p[0], p[1]+1))
    if 0 < p[1] < len(data): r.append((p[0], p[1]-1))
    return [s for s in r if can_go(letter(p), letter(s))]


def p1(start=S):
    dx = defaultdict(lambda: 1e9)
    Q = deque([start])
    dx[start] = 0

    while Q:
        cur = Q.popleft()
        d = dx[cur]

        neighbors = [n for n in get_neighbors(cur) if dx[n] > d + 1]
        for n in neighbors:
            dx[n] = d + 1

        Q.extend(neighbors)

    return dx[E]


def p2():
    lowest = 1e9
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 'a':
                lowest = min(p1((x,y)), lowest)
    return lowest


print(p1())
print(p2())