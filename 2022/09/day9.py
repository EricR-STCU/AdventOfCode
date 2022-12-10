from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    data = [l.strip().split() for l in f]
    for d in data:
        d[1] = int(d[1])

dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1),
        'UR': (-1,1), 'UL': (-1, -1), 'DR': (1, 1), 'DL': (1, -1)}


def add(p1, p2): return (p1[0]+p2[0], p1[1]+p2[1])
def distance(p1, p2):
    if p1==p2: return 0
    elif abs(p1[0]-p2[0]) > 1 or abs(p1[1]-p2[1]) > 1: return 2
    return 1


def p1():
    vis = defaultdict(bool)
    vis[(0,0)] = True
    H = (0,0)
    T = (0,0)
    for d in data:
        dir = dirs[d[0]]
        for i in range(d[1]):
            H = add(H, dir)
            dxy = distance(H,T)
            if dxy==0 or dxy==1:
                continue
            match d[0]:
                case 'L':
                    if T[0] == H[0]:
                        T = add(T, dir)
                    elif T[0] == H[0] + 1:
                        T = add(add(T, dir), dirs['U'])
                    elif T[0] == H[0] - 1:
                        T = add(add(T, dir), dirs['D'])
                case 'R':
                    if T[0] == H[0]:
                        T = add(T, dir)
                    elif T[0] == H[0] + 1:
                        T = add(add(T, dir), dirs['U'])
                    elif T[0] == H[0] - 1:
                        T = add(add(T, dir), dirs['D'])
                case 'U':
                    if T[1] == H[1]:
                        T = add(T, dir)
                    elif T[1] == H[1] + 1:
                        T = add(add(T, dir), dirs['L'])
                    elif T[1] == H[1] - 1:
                        T = add(add(T, dir), dirs['R'])
                case 'D':
                    if T[1] == H[1]:
                        T = add(T, dir)
                    elif T[1] == H[1] + 1:
                        T = add(add(T, dir), dirs['L'])
                    elif T[1] == H[1] - 1:
                        T = add(add(T, dir), dirs['R'])
            vis[T] = True

    return sum(x for x in vis.values())


def diff(ph, pt):
   if ph[0] == pt[0]: return 'R' if ph[1] > pt[1] else 'L' 
   if ph[1] == pt[1]: return 'D' if ph[0] > pt[0] else 'U'
   match (ph[0]-pt[0], ph[1]-pt[1]):
        case (2, 1): return 'D'
        case (1, 2): return 'R'
        case (2, -1): return 'D'
        case (-1, 2): return 'R'
        case (-2, 1): return 'U'
        case (1, -2): return 'L'
        case (-2, -1): return 'U'
        case (-1, -2): return 'L'
        case (-2, -2): return 'UL'
        case (2, -2): return 'DL'
        case (-2, 2): return 'UR'
        case (2, 2): return 'DR'
        case _:
            print(ph, pt, "!"*20)


def p2():
    vis = defaultdict(bool)
    vis[(0,0)] = True
    H = 0
    knots = [(0,0)]*10
    for d in data:
        for _ in range(d[1]):
            dir = dirs[d[0]]
            knots[H] = add(knots[H], dir)
            for h in range(9):
                t = h+1
                dxy = distance(knots[h],knots[t])
                if dxy==0 or dxy==1:
                    continue
                dif = diff(knots[h], knots[t])
                dir = dirs[dif]
                match dif:
                    case 'L':
                        if knots[t][0] == knots[h][0]:
                            knots[t] = add(knots[t], dir)
                        elif knots[t][0] == knots[h][0] + 1:
                            knots[t] = add(add(knots[t], dir), dirs['U'])
                        elif knots[t][0] == knots[h][0] - 1:
                            knots[t] = add(add(knots[t], dir), dirs['D'])
                    case 'R':
                        if knots[t][0] == knots[h][0]:
                            knots[t] = add(knots[t], dir)
                        elif knots[t][0] == knots[h][0] + 1:
                            knots[t] = add(add(knots[t], dir), dirs['U'])
                        elif knots[t][0] == knots[h][0] - 1:
                            knots[t] = add(add(knots[t], dir), dirs['D'])
                    case 'U':
                        if knots[t][1] == knots[h][1]:
                            knots[t] = add(knots[t], dir)
                        elif knots[t][1] == knots[h][1] + 1:
                            knots[t] = add(add(knots[t], dir), dirs['L'])
                        elif knots[t][1] == knots[h][1] - 1:
                            knots[t] = add(add(knots[t], dir), dirs['R'])
                    case 'D':
                        if knots[t][1] == knots[h][1]:
                            knots[t] = add(knots[t], dir)
                        elif knots[t][1] == knots[h][1] + 1:
                            knots[t] = add(add(knots[t], dir), dirs['L'])
                        elif knots[t][1] == knots[h][1] - 1:
                            knots[t] = add(add(knots[t], dir), dirs['R'])
                    case x:
                        knots[t] = add(knots[t], dir)
            vis[knots[9]] = True

    return sum(x for x in vis.values())


def show(knots):
    xmin = min(k[0] for k in knots)
    xmax = max(k[0] for k in knots)
    ymin = min(k[1] for k in knots)
    ymax = max(k[1] for k in knots)
    lines = [['.' for _ in range(ymin, ymax+1)] for _ in range(xmin, xmax+1)]
    for k in knots:
        lines[k[0]-xmin][k[1]-ymin] = '#'
    for line in lines:
        print(''.join(line))


print(p1())
print(p2())