from collections import defaultdict, Counter, deque
from string import ascii_lowercase

with open('./in.txt') as f:
    data = f.read()
    packets = []
    for pair in data.split('\n\n'):
        a, b = pair.split('\n')
        exec(f'packets.append(({a}, {b}))')
    

def compare(a, b):
    if type(a) is int and type(b) is int:
        if a < b: return True
        if a > b: return False
        return None

    if type(a) is list and type(b) is list:
        c = None
        for (aa, bb) in zip(a, b):
            c = compare(aa, bb)
            if c is not None: return c
        if len(a) < len(b): return True
        if len(a) > len(b): return False
        return None

    if type(a) is int and type(b) is list:
        a = [a]
        return compare(a, b)
    if type(a) is list and type(b) is int:
        b = [b]
        return compare(a, b)
    return None
    

def p1():
    total = 0
    for i, (a, b) in enumerate(packets):
        if compare(a, b): total += i + 1
    return total

def p2():
    l = [[[2]], [[6]]]
    for (a, b) in packets:
        l.append(a)
        l.append(b)

    for i in range(len(l)):
        for j in range(i, len(l)):
            if not compare(l[i], l[j]):
                l[i], l[j] = l[j], l[i]

    return (l.index([[2]]) + 1) * (l.index([[6]]) + 1)


print(p1())
print(p2())