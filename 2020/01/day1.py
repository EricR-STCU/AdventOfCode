with open('./in.txt') as f:
    data = [int(l.strip()) for l in f.readlines()]

def p1():
    for i, x in enumerate(data):
        for y in data[i:]:
            if x+y == 2020:
                return x*y

def p2():
    for i, x in enumerate(data):
        for j, y in enumerate(data[i:]):
            for z in data[j:]:
                if x+y+z == 2020:
                    return x*y*z

print(p1())
print(p2())