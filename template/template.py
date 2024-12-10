import itertools as it
import re
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()

    #data = [l.strip() for l in data]
    #data = [[int(x) for x in l.strip().split()] for l in data]

    return data
    

def part1():
    data = load()


    print(data)
    return


def part2():
    data = load()


    print("2")
    return


part1()
part2()