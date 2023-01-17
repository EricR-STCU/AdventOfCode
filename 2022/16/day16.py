from collections import defaultdict, Counter, deque
from string import ascii_lowercase

with open('./test.txt') as f:
    data = [l.strip() for l in f.readlines()]
    D = {}
    for line in data:
        valve = line.split(' ')[1]
        flow = int(line[line.index('=')+1:line.index(';')])
        # add a comma after lines that only lead to one valve
        ns = line[line.index(',')-2:].strip(',').split(', ')
        D[valve] = (valve, flow, ns)
    print(D)


def p1():
    t = 30
    G = {}
    cur = D['AA']
    for k, v in D:
        edges = {flow: v[1]}
        for n in v[2]:
            edges[n] = 1
        G[k] = edges
    while any(g['flow']==0 for g in G):
        for kcur, vcur in G.items():
            if vcur['flow'] == 0:
                for k, v in g.items():
                    G.pop(g)
    return


def p2():
    return


print(p1())
print(p2())