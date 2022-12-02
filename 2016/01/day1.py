with open('./in.txt') as f:
    data = [l for l in f.readline().split(', ')]

def p1_():
    ds = [(1,0), (0,1), (-1,0), (0,-1)]
    d = 0
    x = (0,0)

    for i in data:
        match i[0]:
            case 'R':
                d = (d+1)%4
            case 'L':
                d = (d-1)%4
        x = add(x, ds[d], int(i[1:]))
    return x, sum(abs(i) for i in x)

def p2_():
    ds = [(1,0), (0,1), (-1,0), (0,-1)]
    d = 0
    x = (0,0)
    seen = set()
    seen.add(x)

    for i in data:
        match i[0]:
            case 'R':
                d = (d+1)%4
            case 'L':
                d = (d-1)%4
        x = add_seen(x, ds[d], int(i[1:]), seen)
        if x is None:
            return


def add(p1, p2, x=1):
    return (p1[0] + p2[0] * x, p1[1] + p2[1] * x)

def add_seen(p1, p2, x, seen):
    for i in range(x):
        p1 = add(p1, p2)
        if p1 in seen:
            print(p1, sum(abs(i) for i in p1))
            return
        seen.add(p1)
    return p1


print(p1_())
p2_()