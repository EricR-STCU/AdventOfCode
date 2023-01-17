from collections import defaultdict, Counter, deque
from string import ascii_lowercase
from heapq import *

with open('./in.txt') as f:
    data = [l.strip('\n') for l in f.readlines()]
    instructions = data.pop().strip()
    data.pop()
    ins = []
    num = []
    for i in range(len(instructions)):
        match instructions[i]:
            case 'L':
                ins.append((int(''.join(num)), -1))
                num = []
                continue
            case 'R':
                ins.append((int(''.join(num)), 1))
                num = []
                continue
            case c:
                num.append(c)
                continue
    ins.append((int(''.join(num)), 0))
    


def go(r, c, d, steps):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir = directions[d]
    for _ in range(steps):
        nextr = get_next_r(r, c, dir[0])
        nextc = get_next_c(r, c, dir[1])
        if data[nextr][nextc] == '#':
            break
        r, c = nextr, nextc
    return r, c

def get_next_r(r, c, dr):
    if dr == 0:
        return r
    elif r+dr < 0 or (dr == -1 and data[r+dr][c] == ' '):
        rr = len(data)-1
        while len(data[rr]) <= c:
            rr -= 1
        return rr
    elif len(data) <= r+dr or len(data[r+dr]) <= c or data[r+dr][c] == ' ':
        rr = 0
        while len(data[rr]) <= c or data[rr][c] == ' ':
            rr += 1
        return rr
    else:
        return r+dr


def get_next_c(r, c, dc):
    if dc == 0:
        return c
    elif c+dc < 0:
        return len(data[r])-1
    elif c+dc >= len(data[r]) and data[r][0] == ' ':
        return min(data[r].index('.'), (data[r]+'#').index('#'))
    elif c+dc >= len(data[r]) and data[r][0] != ' ':
        return 0
    elif data[r][c+dc] == ' ':
        return len(data[r])-1
    else:
        return c+dc


def go_sq(r, c, d, ins):
    print(ins)
    steps = ins[0]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(steps):
        dir = directions[d]
        nextr, rcc, rdd = get_next_r_sq(r, c, dir[0])
        crr, nextc, cdd = get_next_c_sq(r, c, dir[1])
        dd = 0
        if rdd != 0: dd = rdd
        if cdd != 0: dd = cdd
        if rcc != c:
            nextc = rcc
            print("cur ", r, c, "next ", nextr, nextc, "d ", d, dd)
        if crr != r:
            nextr = crr
            print("cur ", r, c, "next ", nextr, nextc, "d ", d, dd)
        if data[nextr][nextc] == '#':
            break
        r, c, d = nextr, nextc, (d+dd)%4
    return r, c, d
        

def get_next_r_sq(r, c, dr):
    if dr == 0:
        return r, c, 0
    elif r+dr < 0 or (dr == -1 and data[r+dr][c] == ' '):
        if 0<=c<50:
            return 50 + c, 50, 1
        elif 50<=c<100:
            return 150 + (c-50), 0, 1
        else:
            return len(data)-1, c - 100, 0
    elif len(data) <= r+dr or len(data[r+dr]) <= c or data[r+dr][c] == ' ':
        if 0<=c<50:
            return 0, c+100, 0
        elif 50<=c<100:
            return 150+c-50, 49, 1
        else:
            return 50 + c-100 , 99, 1
    else:
        return r+dr, c, 0


def get_next_c_sq(r, c, dc):
    if dc == 0:
        return r, c, 0
    elif c+dc < 0:
        if 0<=r<50:
            print(r, c, dc)
            assert False
        elif 50<=r<100:
            print(r, c, dc)
            assert False
        elif 100<=r<150:
            return 49 - (r-100), 50, 2
        else:
            return 0, r-150 +50, -1
    elif c+dc >= len(data[r]):
        if 0<=r<50:
            return 149-r, 99, 2
        elif 50<=r<100:
            return 49, 100+r-50, -1
        elif 100<=r<150:
            return 49-(r-100), 149, 2
        else:
            return 149, r-150+50, -1
    elif data[r][c+dc] == ' ':
        if 0<=r<50:
            return 149-r, 0, 2
        elif 50<=r<100:
            return 100, r-50, -1
        elif 100<=r<150:
            print(r, c, dc)
            assert False
        else:
            print(r, c, dc)
            assert False
    else:
        return r, c+dc, 0


def p1():
    r, c = 0, data[0].index('.')
    d = 0
    for i in ins:
        r, c = go(r, c, d, i[0])
        d = (d+i[1])%4
    return r+1, c+1, d, (r+1)*1000+(c+1)*4+d

def p2():
    r, c = 0, data[0].index('.')
    d = 0
    for i in ins:
        r, c, d = go_sq(r, c, d, i)
        d = (d+i[1])%4
    return r+1, c+1, d, (r+1)*1000+(c+1)*4+d


print(p1())
print(p2())