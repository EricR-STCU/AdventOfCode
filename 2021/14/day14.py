from collections import defaultdict, Counter, deque

with open('./day14.txt') as f:
    data = f.read()

X, pairs = data.split('\n\n')
pairs = pairs.strip().split('\n')
P = defaultdict(str)
P = {p.split(' -> ')[0]: p.split(' -> ')[1] for p in pairs}


def part1():
    global X
    for _ in range(10):
        Y = ''
        for i in range(len(X)):
            Y += X[i]
            if X[i:i+2] in P:
                Y += P[X[i:i+2]]
        X = Y
    c = Counter(X)
    cc = c.most_common()
    return max(c.values()) - min(c.values())

memo = defaultdict(Counter)
DEPTH = 40
def R(x, c, i):
    if i == DEPTH:
        return c
    if (x, i) in memo:
        return memo[(x,i)]
    if x in P and i < DEPTH:
        c[P[x]] += 1
        c += R(x[0]+P[x], Counter(), i + 1)
        c += R(P[x]+x[1], Counter(), i + 1)
        memo[(x,i)] = c.copy()
        return c

def part2():
    C = Counter(X)
    for i in range(len(X)-1):
        C += R(X[i:i+2], Counter(), 0)
    return max(C.values()) - min(C.values())

print(part1())
print(part2())