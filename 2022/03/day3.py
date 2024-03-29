from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    d = [l.strip() for l in f.readlines()]


def one_liner(): #I'm sorry lol
    return sum(ord((set(r[:len(r)//2])&set(r[len(r)//2:])).pop()) - (96 if (set(r[:len(r)//2])&set(r[len(r)//2:])).pop().islower() else 64 - 26) for r in d)


def score(c):
    return ord(c) - (96 if c.islower() else 64 - 26)


def p1():
    common = []
    for r in d:
        a = set(r[:len(r)//2])
        b = set(r[len(r)//2:])
        common.append((a&b).pop())

    return sum(score(c) for c in common)


def p2():
    common = []
    for A, B, C in zip(d[::3], d[1::3], d[2::3]):
        a = set(A)
        b = set(B)
        c = set(C)
        common.append((a&b&c).pop())
    
    return sum(score(c) for c in common)


print(p1())
print(one_liner())
print(p2())