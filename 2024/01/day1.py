import itertools as it
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()
    l = [int(l.split()[0]) for l in data]
    r = [int(l.split()[1]) for l in data]
    return (l, r)
    
def part1():
    l, r = load()
    l.sort()
    r.sort()
    
    print(sum(abs(a-b) for a, b in zip(l, r)))


def part2():
    l, r = load()
    counter = Counter(r)

    print(sum(x * counter[x] for x in l))

part1()
part2()