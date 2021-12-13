with open('./day13.txt') as f:
    data = f.read()

X = 0
Y = 1
DOT = '@'
NOT_DOT = ' '
coords, folds = data.split('\n\n')
coords = [[int(i.split(',')[X]), int(i.split(',')[Y])] for i in coords.split('\n')]
folds = [f.split(' ')[-1] for f in folds.split('\n')]
folds = [f.split('=')[0] for f in folds]
G = [[NOT_DOT 
    for x in range(max(i[X] for i in coords)+1)] 
    for y in range(max(i[Y] for i in coords)+1)]
for P in coords:
    G[P[Y]][P[X]] = DOT


def p(grid):
    for row in grid:
        print(''.join(row))
    print()
    return


def fold_y(grid):
    up = grid[:len(grid)//2]
    down = grid[len(grid)//2:]
    for y, row in enumerate(down):
        for x, val in enumerate(row):
            if val == DOT:
                up[len(up)-y][x] = DOT
    return up


def fold_x(grid):
    left = [row[:len(grid[0])//2] for row in grid]
    right = [row[len(grid[0])//2:] for row in grid]
    for y, row in enumerate(right):
        for x, val in enumerate(row):
            if val == DOT:
                left[y][len(left[0])-x] = DOT
    return left


def part1():
    grid = [row.copy() for row in G]

    grid = fold_y(grid) if folds[0] == 'y' else fold_x(grid)
    return sum(sum(val == DOT for val in row) for row in grid)

def part2():
    grid = [row.copy() for row in G]

    for fold in folds:
        grid = fold_y(grid) if fold == 'y' else fold_x(grid)

    return '\n'.join([''.join(row) for row in grid])

print(part1())
print(part2())