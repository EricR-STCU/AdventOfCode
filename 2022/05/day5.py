from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    data = [l.strip('\n')for l in f.readlines()]


def parse_stacks(raw):
    stacks = [[] for _ in range(9)]
    for line in raw:
        for i, x in enumerate(line[1::4]):
            if x != ' ':
                stacks[i].insert(0,x)
    return stacks


def p1():
    stacks = parse_stacks(data[:8])
    directions = data[10:]
    for dx in directions:
        dx = [int(n) for n in dx.split(' ')[1::2]]
        for _ in range(dx[0]):
            stacks[dx[2]-1].append(stacks[dx[1]-1].pop())
    return ''.join([s.pop() for s in stacks])


def p2():
    stacks = parse_stacks(data[:8])
    directions = data[10:]
    for dx in directions:
        dx = [int(n) for n in dx.split(' ')[1::2]]
        temp = []
        for _ in range(dx[0]):
            temp.insert(0, stacks[dx[1]-1].pop())
        stacks[dx[2]-1] += temp
    return ''.join([s.pop() for s in stacks])


print(p1())
print(p2())