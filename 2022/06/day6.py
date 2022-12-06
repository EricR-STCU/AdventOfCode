from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    data = f.read().strip()


def p1():
    for i in range(len(data)):
        if len(set(data[i:i+4])) == 4:
            return i + 4


def p2():
    for i in range(len(data)):
        if len(set(data[i:i+14])) == 14:
            return i + 14


print(p1())
print(p2())