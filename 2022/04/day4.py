from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    d = [l.strip().replace(',' , '-').split('-') for l in f.readlines()]
    d = [[int(n)  for n in line] for line in d]

def p1():
    return sum(
        (s1<=s2 and e1>=e2) or (s2<=s1 and e2>=e1)
        for s1, e1, s2, e2 in d
    )


def p2():
    return sum(
        (s1 <= s2 <= e1) or (s2 <= s1 <= e2)
        for s1, e1, s2, e2 in d
    )


print(p1())
print(p2())