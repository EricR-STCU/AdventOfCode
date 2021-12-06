from collections import defaultdict

with open('./day5.txt') as f:
    data = [l.strip() for l in f.readlines()]

def line(s):
    a, _, b = s.split(' ')
    return ([int(p) for p in a.split(',')], [int(p) for p in b.split(',')])

def part1():
    d = [*data]
    
    field = defaultdict(int)
    lines = [line(l) for l in d]
    lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]
    

    for (a,b) in lines:
        if a[0] == b[0]:
            y = min(a[1], b[1])
            for i in range(abs(a[1]-b[1])+1):
                field[(a[0], y+i)] += 1
        if a[1] == b[1]:
            x = min(a[0], b[0])
            for i in range(abs(a[0]-b[0])+1):
                field[(x+i, a[1])] += 1

    return sum(v > 1 for v in field.values())


def part2():
    d = [*data]
    
    field = defaultdict(int)
    lines = [line(l) for l in d]

    for (a,b) in lines:
        if a[0] == b[0]:
            y = min(a[1], b[1])
            for i in range(abs(a[1]-b[1])+1):
                field[(a[0], y+i)] += 1
        elif a[1] == b[1]:
            x = min(a[0], b[0])
            for i in range(abs(a[0]-b[0])+1):
                field[(x+i, a[1])] += 1
        elif (a[0] < b[0] and a[1] < b[1]) or (b[0] < a[0] and b[1] < a[1]):
            x = min(a[0], b[0])
            y = min(a[1], b[1])
            for i in range(abs(b[0]-a[0])+1):
                field[(x+i, y+i)] += 1 
        else:
            x = min(a[0], b[0])
            y = max(a[1], b[1])
            for i in range(abs(a[0]-b[0])+1):
                field[(x+i, y-i)] += 1
    
    return sum(v > 1 for v in field.values())

print(part1())
print(part2())