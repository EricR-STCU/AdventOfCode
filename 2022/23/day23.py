from collections import defaultdict, Counter, deque
from string import ascii_lowercase
from heapq import *

with open('./in.txt') as f:
    data = [l.strip('\n') for l in f.readlines()]
    _Elfs = set()
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '#':
                _Elfs.add((r, c))
    
def copy(G):
    new = []
    for g in G:
        new.append(g)
    return new
    

def add(p1, p2): return (p1[0]+p2[0], p1[1]+p2[1])


def elfs(E):
    for r in range(min(r for r, _ in E), max(r for r, _ in E)+1):
        s = ''
        for c in range(min(c for _, c in E), max(c for _, c in E)+1):
            s = s+('#' if (r, c) in E else '.')
        print(s)



def get_proposed(Elfs):
    next = {}
    for elf in Elfs:
        is_alone = True
        candidate = None
        for i in range(4):
            sees_any = False
            for dd in dx[(i+I)%4]:
                if add(elf, dd) in Elfs:
                    is_alone = False
                    sees_any = True
                    break
            if not sees_any and candidate is None:
                candidate = add(elf, cd[(i+I)%4])
        if candidate and not is_alone:
            if candidate not in next.values():
                next[elf] = candidate
            else:
                next[elf] = elf
                match = None
                for k, v in next.items():
                    if v == candidate:
                        match = k
                        break
                next[match] = match
        else:
            next[elf] = elf
    return next


I = 0
cd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dx = [
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
    [(-1, -1), (1, -1), (0, -1)],
    [(-1, 1), (1, 1), (0, 1)]
]
def p1():
    global _Elfs
    global I
    I = 0
    Elfs = _Elfs.copy()
    for _ in range(10):
        proposed = get_proposed(Elfs)
        Elfs = set(proposed.values())
        I = (I+1)%4
    total = 0
    for r in range(min(r for r, c in Elfs), max(r for r, c in Elfs)+1):
        for c in range(min(c for r, c in Elfs), max(c for r, c in Elfs)+1):
            if (r, c) not in Elfs:
                total += 1
    return total

def p2():
    global _Elfs
    global I
    I = 0
    Elfs = _Elfs.copy()
    i = 0
    while True:
        i+=1
        print(i)

        proposed = get_proposed(Elfs)
        Elfs = set(proposed.values())
        if all(k==v for k, v in proposed.items()):
            break
        I = (I+1)%4
    return i

print(p1())
print(p2())