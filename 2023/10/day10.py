test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.readlines()

G = [list(l.strip()) for l in data]

def add(p, d):
    return (p[0]+d[0], p[1]+d[1])


def part1():
    start = (0,0)
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] == 'S':
                start = (r,c)
    cur = start
    dd = {'n': (-1, 0), 'e': (0,1), 's': (1,0), 'w': (0, -1)}
    d = dd['s']
    cnt = 1
    cur = add(cur, d)
    while True:
        p = G[cur[0]][cur[1]]
        if p == 'S':
            break
        if p == 'J':
            d = dd['w'] if d == dd['s'] else dd['n']
        if p == 'L':
            d = dd['e'] if d == dd['s'] else dd['n']
        if p == '7':
            d = dd['w'] if d == dd['n'] else dd['s']
        if p == 'F':
            d = dd['e'] if d == dd['n'] else dd['s']
        cur = add(cur, d)
        cnt += 1
    print(cnt//2)
    return


def part2():
    dd = {'n': (-1, 0), 'e': (0,1), 's': (1,0), 'w': (0, -1)}
    start = (0,0)
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] == 'S':
                start = (r,c)
    GG = []
    for r in G:
        GG.append(r.copy())

    cur = start
    d = dd['s']
    cur = add(cur, d)
    while True:
        p = G[cur[0]][cur[1]]
        GG[cur[0]][cur[1]] = 'X'
        if p == 'S':
            break
        if p == 'J':
            d = dd['w'] if d == dd['s'] else dd['n']
        if p == 'L':
            d = dd['e'] if d == dd['s'] else dd['n']
        if p == '7':
            d = dd['w'] if d == dd['n'] else dd['s']
        if p == 'F':
            d = dd['e'] if d == dd['n'] else dd['s']
        cur = add(cur, d)
    for r in range(len(GG)):
        for c in range(len(GG[0])):
            if GG[r][c] != 'X':
                GG[r][c] = ' '

    cur = start
    d = dd['s']
    cur = add(cur, d)
    while True:
        p = G[cur[0]][cur[1]]
        GG[cur[0]][cur[1]] = 'X'
        if p == 'S':
            break
        if p == '|':
            if GG[cur[0]][cur[1]-1] == ' ':
                GG[cur[0]][cur[1]-1] = 'r' if d == dd['s'] else 'l'
            if GG[cur[0]][cur[1]+1] == ' ':
                GG[cur[0]][cur[1]+1] = 'l' if d == dd['s'] else 'r'
        if p == '-':
            if GG[cur[0]-1][cur[1]] == ' ':
                GG[cur[0]-1][cur[1]] = 'l' if d == dd['e'] else 'r'
            if GG[cur[0]+1][cur[1]] == ' ':
                GG[cur[0]+1][cur[1]] = 'r' if d == dd['e'] else 'l'
        if p == 'J':
            if GG[cur[0]][cur[1]+1] == ' ':
                GG[cur[0]][cur[1]+1] = 'l' if d == dd['s'] else 'r'
            if GG[cur[0]+1][cur[1]] == ' ':
                GG[cur[0]+1][cur[1]] = 'l' if d == dd['s'] else 'r'
            d = dd['w'] if d == dd['s'] else dd['n']
        if p == 'L':
            if GG[cur[0]][cur[1]-1] == ' ':
                GG[cur[0]][cur[1]-1] = 'r' if d == dd['s'] else 'l'
            if GG[cur[0]+1][cur[1]] == ' ':
                GG[cur[0]+1][cur[1]] = 'r' if d == dd['s'] else 'l'
            d = dd['e'] if d == dd['s'] else dd['n']
        if p == '7':
            if GG[cur[0]][cur[1]+1] == ' ':
                GG[cur[0]][cur[1]+1] = 'r' if d == dd['n'] else 'l'
            if GG[cur[0]-1][cur[1]] == ' ':
                GG[cur[0]-1][cur[1]] = 'r' if d == dd['n'] else 'l'
            d = dd['w'] if d == dd['n'] else dd['s']
        if p == 'F':
            if GG[cur[0]][cur[1]-1] == ' ':
                GG[cur[0]][cur[1]-1] = 'l' if d == dd['n'] else 'r'
            if GG[cur[0]-1][cur[1]] == ' ':
                GG[cur[0]-1][cur[1]] = 'l' if d == dd['n'] else 'r'
            d = dd['e'] if d == dd['n'] else dd['s']
        cur = add(cur, d)
    for r in GG:
        print(''.join(r))
    cnt = 0
    for r in GG:
        for c in r:
            if c == 'r':
                cnt += 1
    print(cnt, cnt+53)
    return

#part1()
part2()