from collections import defaultdict
from heapq import *

with open('./day15.txt') as f:
    data = f.readlines()
    data = [[int(c) for c in line.strip()] for line in data]


R = [1, 0, -1, 0]
C = [0, 1, 0, -1]
def neighbors(r,c,G):
    for dr, dc in zip(R,C):
        if 0 <= r+dr < len(G) and 0 <= c+dc < len(G[0]):
            yield (r+dr, c+dc)


def M(r,c,G):
    return len(G)-r + len(G[0])-c - 2


COST = defaultdict(lambda : 1e9)
def visit(G,r,c,x):
    COST[(r,c)] = x
    if r == len(G) - 1 and c == len(G[0]) - 1:
        return
    
    for rr, cc in neighbors(r,c,G):
        if x + G[rr][cc] < COST[(rr, cc)] and x + M(r,c,G) < COST[(len(G)-1, len(G[0])-1)]:
            visit(G,rr,cc,x+G[rr][cc])


'''BFS, bad'''
def part1():
    visit(data,0,0,0)
    return COST[(len(data)-1, len(data[0])-1)]

''' Roughly Dijkstra's?'''
def part2():
    pad_factor = 5
    G = [[0 for _ in range(len(data[0])*pad_factor)] for _ in range(len(data)*pad_factor)]
    for r in range(len(G)):
        for c in range(len(G)):
            G[r][c] = (data[r%len(data)][c%len(data[0])] + r//len(data) + c//len(data[0])) % 9
            if G[r][c] == 0:
                G[r][c] = 9
    
    COSTS = defaultdict(lambda : 1e9)
    Q = [(0,0,0)]
    heapify(Q)
    while Q:
        x,r,c = heappop(Q)
        if r == len(G) - 1 and c == len(G[0]) - 1:
            continue
        for rr, cc in neighbors(r,c,G):
            if x + G[rr][cc] < COSTS[(rr, cc)]:
                heappush(Q,(x + G[rr][cc], rr, cc))
                COSTS[(rr,cc)] = x + G[rr][cc]
 
    return COSTS[(len(G)-1, len(G[0])-1)]


print(part1())
print(part2())