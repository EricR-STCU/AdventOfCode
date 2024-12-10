import itertools as it
import re
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()

    data = [l.strip() for l in data]
    #data = [[int(x) for x in l.strip().split()] for l in data]

    return data
    

r = lambda z: int(z.real)
c = lambda z: int(z.imag)


def part1():
    G = load()
    R = len(G)
    C = len(G[0])
    p = 0+0j
    d = 0j
    for row in range(len(G)):
        if "^" in G[row]:
            p = row + 1j*G[row].find("^")
            d = -1+0j
            break
        if "v" in G[row]:
            p = row + 1j*G[row].find("v")
            d = 1+0j
            break
        if ">" in G[row]:
            p = row + 1j*G[row].find(">")
            d = 0+1j
            break
        if "<" in G[row]:
            p = row + 1j*G[row].find("<")
            d = 0-1j
            break
        
    G = [list(l.strip()) for l in G]
    visited = set()
    next = p+d
    while True:
        visited.add(p)
        next = p + d
        if not (0 <= r(next) < R and 0 <= c(next) < C):
            break
        G[r(p)][c(p)] = "X"
        if G[r(next)][c(next)] == "#":
            d = d*-1j
            next = p + d
        p = next
    
        #print(p, d)
        #for l in G:
            #print(l)
    print(len(visited))

    return


def part2():
    G = load()
    R = len(G)
    C = len(G[0])
    p = 0+0j
    d = 0j
    for row in range(len(G)):
        if "^" in G[row]:
            p = row + 1j*G[row].find("^")
            d = -1+0j
            break
        if "v" in G[row]:
            p = row + 1j*G[row].find("v")
            d = 1+0j
            break
        if ">" in G[row]:
            p = row + 1j*G[row].find(">")
            d = 0+1j
            break
        if "<" in G[row]:
            p = row + 1j*G[row].find("<")
            d = 0-1j
            break
        
    spots = []
    for rr in range(R):
        print(rr, R)
        for cc in range(C):
            if G[rr][cc] != ".":
                continue

            pp = p
            dd = d
            GG = load()
            GG = [list(l.strip()) for l in GG]
            GG[rr][cc] = "#"


            visited = set()
            next = pp+dd
            while True:
                if (pp,dd) in visited:
                    spots.append(rr + cc*1j)
                    break
                visited.add((pp,dd))

                next = pp + dd

                if not (0 <= r(next) < R and 0 <= c(next) < C):
                    break
                GG[r(pp)][c(pp)] = "X"
                if GG[r(next)][c(next)] == "#":
                    dd = dd*-1j
                    next = pp + dd
                if GG[r(next)][c(next)] == "#":
                    print("double")
                    dd = dd*-1j
                    next = pp + dd
                pp = next
    print()
    print(max(z.real for z in spots))
    print(max(z.imag for z in spots))
    print(min(z.real for z in spots))
    print(min(z.imag for z in spots))
    print(len(spots))

    return


part1()
part2()