import itertools as it
from collections import defaultdict, Counter
import re

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.read()
    return data

# matches things that look like "mul(123,456)"
mul_expression = r"mul\((\d+),(\d+)\)"
    
def part1():
    data = load()

    # This doesn't return list(Match), it returns list(tuple)
    # where the tuple contains all the groups
    matches = re.findall(mul_expression, data)

    cnt = sum(int(m[0])*int(m[1]) for m in matches)

    print(cnt)
    return


def part2():
    data = load()
    
    good = True
    cnt = 0
    for i in range(len(data)):
        if data[i:].startswith("don't()"):
            good = False
        if data[i:].startswith("do()"):
            good = True
        if good and re.match(mul_expression, data[i:]):
            m = re.match(mul_expression, data[i:])
            cnt += int(m[1]) * int(m[2])

    print(cnt)
    return

part1()
part2()