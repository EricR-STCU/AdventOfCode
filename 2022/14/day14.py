from collections import defaultdict, Counter, deque
from string import ascii_lowercase

with open('./in.txt') as f:
    data = [l.strip() for l in f.readlines()]
    G = defaultdict(lambda: '.')
    G[(0, 500)] = "+"
    P = []
    for line in data:
        pairs = line.split(' -> ')
        p = []
        for pair in pairs:
            a, b = pair.split(',')
            p.append((int(a), int(b)))
        P.append(p)
    for line in P:
        for i in range(len(line)-1):
            start = min(line[i][1], line[i+1][1])
            end = max(line[i][1], line[i+1][1]) + 1
            for r in range(start, end):
                start = min(line[i][0], line[i+1][0])
                end = max(line[i][0], line[i+1][0]) + 1
                for c in range(start, end):
                    G[(r, c)] = '#'
                    

# works for the test case
def show():
    for r in range(15):
        line = []
        for c in range(480, 525):
            line.append(G[(r, c)])
        print(''.join(line))

            

def down(p): return (p[0]+1, p[1])
def left(p): return (p[0]+1, p[1]-1)
def right(p): return (p[0]+1, p[1]+1)
    

def p1():
    lower_bound = max(g[0] for g in G.keys())
    cur = (0, 500)
    while cur[0] < lower_bound:
        if G[down(cur)] == '.':
            cur = down(cur)
            continue
        elif G[left(cur)] == '.':
            cur = left(cur)
            continue
        elif G[right(cur)] == '.':
            cur = right(cur)
            continue
        else:
            G[cur] = 'o'
            cur = (0, 500)
            continue
    return sum(g == 'o' for g in G.values())


def p2():
    lower_bound = max(g[0] for g in G.keys())
    cur = (0, 500)
    for i in range(500 - lower_bound*2, 500 + lower_bound*2):
        G[(lower_bound + 2, i)] = '#'
    while True:
        if G[(0, 500)] == 'o':
            break
        if G[down(cur)] == '.':
            cur = down(cur)
            continue
        elif G[left(cur)] == '.':
            cur = left(cur)
            continue
        elif G[right(cur)] == '.':
            cur = right(cur)
            continue
        else:
            G[cur] = 'o'
            cur = (0, 500)
            continue
    return sum(g == 'o' for g in G.values())


print(p1())
print(p2())