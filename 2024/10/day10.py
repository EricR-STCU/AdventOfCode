import itertools as it
import re
from collections import defaultdict, Counter, deque

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()

    data = [l.strip() for l in data]
    data = [[int(x) for x in l.strip()] for l in data]
    #data = [[int(x) for x in l.strip().split()] for l in data]

    return data
    
pos = lambda G, z: G[int(z.real)][int(z.imag)]
Z = lambda r, i: r +i*1j
is_in = lambda G, z: 0 <= int(z.real) < len(G) and 0 <= int(z.imag) < len(G[0])

def part1():
    G = load()
    R = len(G)
    C = len(G[0])
    dirs = [1, -1, 1j, -1j]

    ths = defaultdict(lambda: 0)

    for r in range(R):
        for c in range(C):
            p = Z(r, c)
            if pos(G, p) == 0:
                th = p
                Q = [p]
                seen = []
                while Q:
                    p = Q.pop()
                    cur = pos(G, p)
                    
                    if cur == 9:
                        if p not in seen:
                            ths[th] += 1
                            seen.append(p)

                    else:
                        for d in dirs:
                            if is_in(G, p+d) and (pos(G, p+d) == cur + 1):
                                Q.append(p+d)
    print(ths)
    print(sum(ths.values()))

    return


def part2():
    G = load()
    R = len(G)
    C = len(G[0])
    dirs = [1, -1, 1j, -1j]

    ths = defaultdict(lambda: 0)

    for r in range(R):
        for c in range(C):
            p = Z(r, c)
            if pos(G, p) == 0:
                th = p
                Q = [p]
                while Q:
                    p = Q.pop()
                    cur = pos(G, p)
                    
                    if cur == 9:
                        ths[th] += 1

                    else:
                        for d in dirs:
                            if is_in(G, p+d) and (pos(G, p+d) == cur + 1):
                                Q.append(p+d)
    print(ths)
    print(sum(ths.values()))

    return


part1()
part2()