import itertools as it
import re
from collections import defaultdict, Counter
from math import gcd

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()

    data = [l.strip() for l in data]

    return data
    
pos = lambda G, z: G[int(z.real)][int(z.imag)]
Z = lambda r, i: r +i*1j

def part1():
    G = load()
    nodes = set()
    antennas = defaultdict(lambda: [])
    R = len(G)
    C = len(G[0])

    for r in range(R):
        for c in range(C):
            if pos(G, Z(r, c)) != ".":
                antennas[G[r][c]].append(Z(r, c))

    for locations in antennas.values():
        
        for a, b in it.combinations(locations, 2):
            diff = a-b
            first = b-diff
            second = a+diff

            if 0 <= first.real < R and 0 <= first.imag < C:
                nodes.add(first)
            if 0 <= second.real < R and 0 <= second.imag < C:
                nodes.add(second)
        
    print(len(nodes))
    return


def part2():
    G = load()
    R = len(G)
    C = len(G[0])

    nodes = set()
    antennas = defaultdict(lambda: [])

    for r in range(R):
        for c in range(C):
            z = Z(r, c)
            if pos(G, z) != ".":
                antennas[pos(G, z)].append(z)

    for antenna in antennas.values():
        
        for a, b in it.combinations(antenna, 2):
            diff = a-b
            diff = diff / gcd(int(diff.real), int(diff.imag))

            cur = a

            while 0 <= cur.real < R and 0 <= cur.imag < C:
                nodes.add(cur)
                cur += diff
            
            diff *= -1
            cur = a + diff

            while 0 <= cur.real < R and 0 <= cur.imag < C:
                nodes.add(cur)
                cur += diff
        
    # visualize grid
    #for r in range(R):
        #for c in range(C):
            #z = Z(r, c)
            #if z in nodes:
                #print("#", end="")
            #else:
                #print(".", end="")
        #print()

    print(len(nodes))
    return


part1()
part2()