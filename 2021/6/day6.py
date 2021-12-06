from collections import Counter

with open('./day6.txt') as f:
    data = [int(x) for x in f.read().split(',')]

def part1():
    d = [*data]
    c = Counter(d)
    for i in range(80):
        new = 0
        for i,x in enumerate(d):
            if x == 0:
                d[i] = 6
                new += 1
            else:
                d[i] -= 1
        for _ in range(new):
            d.append(8)
    return len(d)

def part2(days=256):
    d = [*data]
    c = Counter(d)
    for day in range(days):
        turn = day%7
        if day > 7:
            c[turn] += c[day]
        c[day+9] = c[turn]
    return sum(c[i] for i in range(7)) + sum(c[i] for i in range(days, days+9))

# Roll forward each day directly rather than having a grouped section of the counter,
# and the rest of the counter representing new fish which haven't been moved to the 
# grouped section yet
def part2_alt(days=256):
    d = [*data]
    grouped = [data.count(i) for i in range(9)]
    for _ in range(days):
        cur = grouped.pop(0)
        grouped.append(cur)
        grouped[6] += cur
    return sum(grouped)

print(part1())
print(part2())
print(part2_alt())