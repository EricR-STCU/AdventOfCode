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
    
    cnt = 0
    for row in data:
        inc_or_dec = row == sorted(row) or row == sorted(row)[::-1]
        diff_size = True
        for i in range(len(row)-1):
            diff_size &= 0 < abs(row[i] - row[i+1]) <= 3

        cnt += inc_or_dec and diff_size
    
    print(cnt)
    return


def part2():
    data = load()
    
    cnt = 0
    for row in data:
        has_good_config = False
        for j in range(len(row)):
            row_test = row.copy()
            row_test.pop(j)

            inc_or_dec = row_test == sorted(row_test) or row_test == sorted(row_test)[::-1]
            diff_size = True

            for i in range(len(row_test)-1):
                diff_size &= 0 < abs(row_test[i] - row_test[i+1]) <= 3

            has_good_config = inc_or_dec and diff_size
            if has_good_config:
                cnt += 1
                break

    
    print(cnt)
    return

part1()
part2()
