import itertools as it
import re
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.read().strip()
    nums = []
    for c in data:
        nums.append(int(c))



    return nums
    

def part1():
    data = load()

    disk = []
    file = True
    id = 0
    for d in data:
        for i in range(d):
            disk.append(id if file else ".")

        id += 1 if file else 0
        file = not file
        
    i = 0
    while "." in disk:
        cur = disk.pop()
        while True:
            if disk[i] == ".":
                disk[i] = cur
                break
            i += 1

    check = sum(i*x for i, x in enumerate(disk))

    #print(''.join(str(x) for x in disk))
    print(check)
    return


def part2():
    data = load()

    disk = []
    file = True
    id = 0
    for d in data:
        for i in range(d):
            disk.append(id if file else ".")

        id += 1 if file else 0
        file = not file
        
    cur = len(disk)-1
    while cur and any(x == "." for x in disk[:cur]):
        id = disk[cur]
        #print(''.join(str(x) for x in disk))
        print(cur, id)
        block_len = sum(1 for x in disk if id == x)
        check_str = ''.join((str(x%10) if x != "." else ".") for x in disk[:cur])
        insert = check_str.find("."*block_len)
        if insert > 0:
            for i in range(block_len):
                disk[insert+i] = id
                disk[cur-i] = "."
        while True:
            cur -= 1
            if disk[cur] != "." and disk[cur] != id and disk[cur] < id:
                break

    print(''.join((str(x%10) if x != "." else ".") for x in disk[:100]))
        
    check = sum(i*x for i, x in enumerate(disk) if x != ".")

    print(check)
    return


#part1()
part2()