import itertools as it
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()
    data = [l for l in data]
    return data
    
def part1():
    print("1")
    return


def part2():
    print("2")
    return

part1()
part2()