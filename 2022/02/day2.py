with open('./in.txt') as f:
    d = [l.strip().split(' ') for l in f.readlines()]


def p1():
    t = 0
    for x in d:
        match x:
            case ['A', 'X']:
                t += 4
            case ['A', 'Y']:
                t += 8
            case ['A', 'Z']:
                t += 3
            case ['B', 'X']:
                t += 1
            case ['B', 'Y']:
                t += 5
            case ['B', 'Z']:
                t += 9
            case ['C', 'X']:
                t += 7
            case ['C', 'Y']:
                t += 2
            case ['C', 'Z']:
                t += 6

    return t


def p2():
    t = 0
    for x in d:
        match x:
            case ['A', 'X']:
                t += 3
            case ['A', 'Y']:
                t += 4
            case ['A', 'Z']:
                t += 8
            case ['B', 'X']:
                t += 1
            case ['B', 'Y']:
                t += 5
            case ['B', 'Z']:
                t += 9
            case ['C', 'X']:
                t += 2
            case ['C', 'Y']:
                t += 6
            case ['C', 'Z']:
                t += 7

    return t


print(p1())
print(p2())