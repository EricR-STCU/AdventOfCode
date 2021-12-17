with open('./day17.txt') as f:
    data = f.read().strip()
data = data.split(': ')[1]
xs, ys = data.split(', ')
xs = [int(x) for x in xs[2:].split('..')]
ys = [int(y) for y in ys[2:].split('..')]
tx = list(range(min(xs), max(xs) + 1))
ty = list(range(min(ys), max(ys) + 1))


def step(vx, vy, x, y):
    x += vx
    y += vy
    if vx != 0:
        vx = vx - 1 if vx > 0 else vx + 1
    return vx, vy - 1, x, y


def min_vx():
    n = 0
    while n*(n+1) // 2 < min(tx):
        n += 1
    return n


def part1():
    max_height = 0
    for ivx in range(min_vx(), max(tx)):
        for ivy in range(abs(min(ty))):
            cur_max = 0
            x,y = 0, 0
            vx, vy = ivx, ivy
            while 0 <= x < max(tx) and y > min(ty):
                vx, vy, x, y = step(vx, vy, x, y)
                if y > cur_max:
                    cur_max = y
                if x in tx and y in ty and cur_max > max_height:
                    max_height = cur_max
    return max_height

    
def part2():
    aims = []
    for ivx in range(min_vx(), max(tx) + 1):
        for ivy in range(min(ty), abs(min(ty))):
            x,y = 0, 0
            vx, vy = ivx, ivy
            while 0 <= x < max(tx) and y > min(ty):
                vx, vy, x, y = step(vx, vy, x, y)
                if x in tx and y in ty:
                    aims.append((ivx, ivy))
                    break
    return len(aims)


print(part1())
print(part2())