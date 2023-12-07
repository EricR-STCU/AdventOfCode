with open("in.txt") as f:
    data = [d.strip() for d in f.readlines()]
    
def part1():
    total = 0
    for line in data:
        cur = idx(line)
        for game in games(line):
            rgb = truple(game)
            if not (rgb[0] <= 12 and rgb[1] <= 13 and rgb[2] <= 14):
                cur = 0
                break
        total += cur
    print(total)
    return


def part2():
    total = 0
    for line in data:
        gs = games(line)
        rgbs = [truple(g) for g in gs]
        total += max(rgb[0] for rgb in rgbs) * max(rgb[1] for rgb in rgbs) * max(rgb[2] for rgb in rgbs)
    print(total)
    return
    

def idx(line):
    return int(line[5:line.index(':')])


def games(line: str):
    g = line[line.index(':')+2:].strip()
    return g.split('; ')

def truple(game: str):
    colors = game.split(', ')
    r,g,b = 0,0,0
    for c in colors:
        g = int(c[:c.index('green')]) if 'green' in c else g
        r = int(c[:c.index('red')]) if 'red' in c else r
        b = int(c[:c.index('blue')]) if 'blue' in c else b
    return (r, g, b)
part1()
part2()