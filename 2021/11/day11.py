with open('./day11.txt') as f:
    data = [l.strip() for l in f.readlines()]
    data = [[int(x) for x in l] for l in data]


rr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
cc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
def flash(r,c,grid):
    for r_, c_ in zip(rr, cc):
        if 0 <= r+r_ < len(grid) and 0 <= c+c_ < len(grid[r]):
            grid[r+r_][c+c_] += 1
    grid[r][c] = -1e9
    return


def all_flashed(grid):
    for row in grid:
        for x in row:
            if x > 0:
                return False
    return True


def reset_grid(grid):
    for row in grid:
        for c, x in enumerate(row):
            if row[c] < 0:
                row[c] = 0
    return


def increment_grid(grid):
    for row in grid:
        for c, x in enumerate(row):
            row[c] += 1
    return


def step(grid, step2=False):
    increment_grid(grid)
    
    flashes = 0
    continue_searching = True
    while continue_searching:
        continue_searching = False
        for r, line in enumerate(grid):
            for c, x in enumerate(line):
                if x > 9:
                    continue_searching = True
                    flashes += 1
                    flash(r,c,grid)
    reset_grid(grid)
    return all_flashed(grid) if step2 else flashes


def part1():
    grid = [l.copy() for l in data]
    
    flashes = 0
    for _ in range(100):
        flashes += step(grid)

    return flashes


def part2():
    grid = [l.copy() for l in data]
    
    steps = 1
    while not step(grid, step2=True):
        steps += 1

    return steps


print(part1())
print(part2())