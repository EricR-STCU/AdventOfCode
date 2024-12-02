import itertools as it
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()
    data = [[int(x) for x in l.split()] for l in data]
    return data
    
def part1():
    data = load()
    
    c = 0
    for l in data:
        r = sorted(l)
        s = l == r or l == r[::-1]
        diff = True
        for i in range(len(l)-1):
            d = abs(l[i] - l[i+1])
            if d == 0 or d > 3:
                diff = False
                break
        c += (1 if s and diff else 0)

    
    print(c)
    return


def part2():
    data = load()
    
    c = 0
    for ll in data:
        isgood = False
        for j in range(len(ll)):
            l = ll.copy()
            l.pop(j)
            r = sorted(l)
            s = l == r or l == r[::-1]
            diff = True
            for i in range(len(l)-1):
                d = abs(l[i] - l[i+1])
                if d == 0 or d > 3:
                    diff = False
                    break
            isgood = s and diff
            if isgood:
                c += 1
                break

    
    print(c)
    return

part1()
part2()