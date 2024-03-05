from collections import deque


test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.readlines()

G = [list(d.strip()) for d in data]
R = len(G)
C = len(G[0])
def L(i):
    if 0<=i.real<C and 0<=i.imag<R:
        return G[int(i.imag)][int(i.real)]
    return None
backslash = {1:1j, -1:-1j, -1j:-1, 1j:1}
slash = {1:-1j, -1:1j, -1j:1, 1j:-1}
    
def part1():
    cur = 0+0j
    dir = 1
    stack = deque()
    stack.append((cur, dir))
    S = set()
    while len(stack)>0:
        [cur, dir] = stack.pop()
        x = L(cur)
        if x is None:
            continue
        if (cur, dir) in S:
            continue
        else:
            S.add((cur, dir))
        if x == '\\':
            dir = backslash[dir]
            stack.append((cur+dir, dir))
        if x == '/':
            dir = slash[dir]
            stack.append((cur+dir, dir))
        if x == '-' and dir in [1, -1]:
            stack.append((cur+dir, dir))
        if x == '-' and dir in [1j, -1j]:
            stack.append((cur+1, 1))
            stack.append((cur-1, -1))
        if x == '|' and dir in [1, -1]:
            stack.append((cur+1j, 1j))
            stack.append((cur-1j, -1j))
        if x == '|' and dir in [1j, -1j]:
            stack.append((cur+dir, dir))
        if x == '.':
            stack.append((cur+dir, dir))
    pts = len(set([x for (x, _) in list(S)]))
    print(pts)
    return


def part2():
    E = []
    to_try = [(i, 1j) for i in range(C)]
    to_try += [(i+(R-1)*1j, -1j) for i in range(C)]
    to_try += [(i*1j, 1) for i in range(R)]
    to_try += [((C-1)+i*1j, -1) for i in range(R)]
    for (start, startdir) in to_try:
        stack = deque()
        stack.append((start, startdir))
        S = set()
        while len(stack)>0:
            [cur, dir] = stack.pop()
            x = L(cur)
            if x is None:
                continue
            if (cur, dir) in S:
                continue
            else:
                S.add((cur, dir))
            if x == '\\':
                dir = backslash[dir]
                stack.append((cur+dir, dir))
            if x == '/':
                dir = slash[dir]
                stack.append((cur+dir, dir))
            if x == '-' and dir in [1, -1]:
                stack.append((cur+dir, dir))
            if x == '-' and dir in [1j, -1j]:
                stack.append((cur+1, 1))
                stack.append((cur-1, -1))
            if x == '|' and dir in [1, -1]:
                stack.append((cur+1j, 1j))
                stack.append((cur-1j, -1j))
            if x == '|' and dir in [1j, -1j]:
                stack.append((cur+dir, dir))
            if x == '.':
                stack.append((cur+dir, dir))
        pts = len(set([x for (x, _) in list(S)]))
        E.append(pts)
    print(max(E))
    return

part1()
part2()