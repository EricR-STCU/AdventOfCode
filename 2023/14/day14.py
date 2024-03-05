from collections import Counter


test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.readlines()
data = [list(d.strip()) for d in data]
    
def part1():
    G = {}
    for r in range(len(data)):
        for c in range(len(data[0])):
            cur = data[r][c]
            if cur == '#':
                G[c+r*1j] = cur
            elif cur == 'O':
                x = c + r*1j
                while True:
                    if x - 1j in G or x.imag == 0:
                        G[x] = cur
                        break
                    else:
                        x = x-1j
    total = 0
    for (k, v) in G.items():
        if v == 'O':
            total += len(data) - k.imag
    print(total)
    return


def part2():
    global data
    totals = []
    for i in range(4000):
        for r in range(len(data)):
            for c in range(len(data[0])):
                if data[r][c] == 'O':
                    R = r
                    data[r][c] = '.'
                    while True:
                        if R == 0 or data[R-1][c] in '#O':
                            data[R][c] = 'O'
                            break
                        R -= 1
        for c in range(len(data[0])):
            for r in range(len(data)):
                if data[r][c] == 'O':
                    C = c
                    data[r][c] = '.'
                    while True:
                        if C == 0 or data[r][C-1] in '#O':
                            data[r][C] = 'O'
                            break
                        C -= 1
        for r in range(len(data)-1, -1, -1):
            for c in range(len(data[0])):
                if data[r][c] == 'O':
                    R = r
                    data[r][c] = '.'
                    while True:
                        if R == len(data)-1 or data[R+1][c] in '#O':
                            data[R][c] = 'O'
                            break
                        R += 1
        for c in range(len(data[0])-1, -1, -1):
            for r in range(len(data)):
                if data[r][c] == 'O':
                    C = c
                    data[r][c] = '.'
                    while True:
                        if C == len(data[0])-1 or data[r][C+1] in '#O':
                            data[r][C] = 'O'
                            break
                        C += 1

        total = 0
        for r in range(len(data)):
            for c in range(len(data[0])):
                if data[r][c] == 'O':
                    total += len(data) - r
        totals.append(total)
    #cnt = Counter(totals)
    #cycle = [c for [c,i] in cnt.items() if i>10]
    #print(totals[-(len(cycle)*3):])
    x = 1_000_000_000 % 22
    print(totals[100*22+x-1])
    return

part1()
part2()