from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    data = [l.strip() for l in f]
    

def p1():
    X = 1
    cycle = 1
    strengths = {}
    for l in data:
        if l == "noop":
            strengths[cycle] = cycle*X
            cycle += 1
            continue
        _, arg = l.split(' ')
        arg = int(arg)
        strengths[cycle] = cycle*X
        strengths[cycle+1] = (cycle+1)*X
        cycle += 2
        X += arg
    return sum(strengths[c] for c in range(20, 240+1, 40))


def crt(crt):
    return '\n'.join(''.join(row) for row in crt)


def p2():
    X = 1
    cycle = 1
    CRT = [[' ']*40 for _ in range(6)]
    xs = {}
    for l in data:
        if l == "noop":
            xs[cycle] = X
            cycle += 1
            continue
        _, arg = l.split(' ')
        arg = int(arg)
        xs[cycle] = X
        xs[cycle+1] = X
        cycle += 2
        X += arg
    for i in range(0, 240):
        x, y = i // 40, i % 40
        if y-1 <= xs[i+1] <= y+1:
            CRT[x][y] = '\u2588'
    return crt(CRT)


print(p1())
print(p2())