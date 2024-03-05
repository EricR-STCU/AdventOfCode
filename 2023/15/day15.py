from collections import defaultdict


test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.read().strip().split(',')
    
def part1():
    total = 0
    for d in data:
        val = 0
        for c in d:
            val += ord(c)
            val *= 17
            val = val%256
        total += val
    print(total)
    return


def part2():
    B = [[] for _ in range(256)]
    for d in data:
        val = 0
        if '=' in d:
            D = d[:d.index('=')]
        else:
            D = d[:d.index('-')]
        for c in D:
            val += ord(c)
            val *= 17
            val = val%256

        if '=' in d:
            [label, x] = d.split('=')
            x = int(x)
            if label in [x[0] for x in B[val]]:
                for i in range(len(B[val])):
                    if label == B[val][i][0]:
                        B[val][i] = (label, x)
                        break
            else:
                B[val].append((label, x))
        if '-' in d:
            label = d[:-1]
            for v in B:
                for i in range(len(v)):
                    if v[i][0] == label:
                        v.pop(i)
                        break

    total = 0
    for i, v in enumerate(B):
        for j, vv in enumerate(v):
            x = (i+1)*(j+1)*(vv[1])
            total += x
    print(total)
    return

part1()
part2()