import itertools as it
import re
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.readlines()
    data = [l.strip() for l in data]
    return data

row = lambda z: int(z.imag)
col = lambda z: int(z.real)
    
def part1():
    data = load()

    X = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == 'X':
                X.append(c+(1j*r))
                
    R = len(data)
    C = len(data[0])
    dirs = [1, 1j, -1, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
    mas = "MAS"
    cnt = 0

    for x in X:
        for d in dirs:
            found = True
            cur = x
            for i in range(len(mas)):
                cur = cur + d
                if not (0 <= col(cur) < C and 0 <= row(cur) < R):
                    found = False
                    break
                if data[row(cur)][col(cur)] != mas[i]:
                    found = False
                    break
            cnt += found

    print(cnt)
    return


def part2():
    data = load()
    
    A = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == 'A':
                A.append(c+1j*r)
                
    R = len(data)
    C = len(data[0])
    dirs = [(1+1j, -1-1j), (-1+1j, 1-1j)]
    wrd = "MAS"
    cnt = 0
    for a in A:
        found = True
        ls = []
        for d in dirs:
            j = a + d[0]
            k = a + d[1]

            if not (0 <= j.real < C and 0 <= j.imag < R) or not (0 <= k.real < C and 0 <= k.imag < R):
                found = False
                break

            ls.append(sorted([data[int(j.imag)][int(j.real)], data[int(k.imag)][int(k.real)]]))
        found = ls == [["M", "S"], ["M", "S"]]
        cnt += found

        
    print(cnt)
    
    return

part1()
part2()