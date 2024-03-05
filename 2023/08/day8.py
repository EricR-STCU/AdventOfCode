from itertools import cycle


with open("in.txt") as f:
    data = f.readlines()
    
def part1():
    x = [T(d) for d in data[2:]]
    dirs = data[0].strip()
    cur = 'AAA'
    map = {}
    for y in x:
        map[y.name] = y
    cnt = 0

    for d in cycle(dirs):
        cnt += 1
        if d == 'R':
            cur = map[cur].right
        if d == 'L':
            cur = map[cur].left
        if cur == 'ZZZ':
            break
    print(cnt)
    return


def part2():
    x = [T(d) for d in data[2:]]
    dirs = data[0].strip()
    nodes = [y.name for y in x if y.name.endswith('A')]
    map = {}
    for y in x:
        map[y.name] = y
    cnt = 0

    for d in cycle(dirs):
        if cnt%100_000==0:
            print(cnt)
        cnt += 1
        new_nodes = []
        for n in nodes:
            if d == 'R':
                new_nodes.append(map[n].right)
            if d == 'L':
                new_nodes.append(map[n].left)
        nodes = new_nodes
        if all(n.endswith('Z') for n in nodes):
            break
    print(cnt)
    return

def p3():
    x = [T(d) for d in data[2:]]
    dirs = data[0].strip()
    nodes = [y.name for y in x if y.name.endswith('A')]
    map = {}
    for y in x:
        map[y.name] = y
    cnt = 0
    ss = []

    print(nodes)
    for d in cycle(dirs):
        cnt += 1
        new_nodes = []
        for n in nodes:
            if d == 'R':
                x = map[n].right
            if d == 'L':
                x = map[n].left
            if x.endswith('Z'):
                ss.append(cnt)
            else:
                new_nodes.append(x)
        nodes = new_nodes
        
        if len(nodes) == 0:
            break
    print(ss)
    return

class T():
    def __init__(self, l: str):
        self.name = l[:3]
        l = l[6:].strip()
        l = l.replace('(', '').replace(')', '')
        self.right = l.split(', ')[1]
        self.left = l.split(', ')[0]

     
p3()