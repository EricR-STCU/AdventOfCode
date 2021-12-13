from collections import defaultdict

with open('./day12.txt') as f:
    data = [line.strip().split('-') for line in f.readlines()]

PATHS = set()
PATHS2 = set()
END = 'end'
START = 'start'
CAVES = defaultdict(set)
for a, b in data:
    CAVES[a].add(b)
    CAVES[b].add(a)


def is_big(cave):
    return cave == cave.upper()


def process(cur, seen, path):
    if cur == END:
        PATHS.add(path+END)
        return
    if not is_big(cur):
        seen.add(cur)
    for cave in CAVES[cur]:
        if cave not in seen:
            process(cave, seen.copy(), path+cur+',')
        
            
def process2(cur, seen, path, two):
    if cur == END:
        PATHS2.add(path+END)
        return
    if not is_big(cur):
        seen.add(cur)
    for cave in CAVES[cur]:
        if cave != START and not (two and cave in seen):
            process2(cave, seen.copy(), path+cur+',', two or cave in seen)


def part1():
    process(START, set(), '')
    return len(PATHS)


def part2():
    process2(START, set(), '', False)
    return len(PATHS2)

print(part1())
print(part2())