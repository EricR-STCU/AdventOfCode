from collections import defaultdict, Counter

with open('./day7.txt') as f:
    data = [int(x) for x in f.read().split(',')]

tri = lambda n: n * (n + 1) // 2

def part1():
    d = [*data]
    fuel = {}
    for i in range(min(d), max(d)+1):
        fuel[i] = sum(abs(x-i) for x in d)
    return min(fuel.values())

def part2():
    d = [*data]
    fuel = {}
    for i in range(min(d), max(d)+1):
        fuel[i] = sum(tri(abs(x-i)) for x in d)
    return min(fuel.values())

def one_liner():
    d = [*data]
    return min(sum(abs(x-i) for x in d) for i in range(min(d), max(d) + 1))

def analytic():
    d = [*data]
    d.sort()
    mean = sum(d) // len(d)
    median = d[len(d)//2]
    return (sum(abs(x-median) for x in d), sum(tri(abs(x-mean)) for x in d))

print(part1())
print(part2())
print(one_liner())
print(analytic())