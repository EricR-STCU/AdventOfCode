def get_board(b):
    return [[[int(x), False] for x in row.split(' ') if x] for row in b.split('\n')]

def not_hit_sum(board):
    return sum(sum(x[0] for x in row if not x[1]) for row in board)

def mark(b, x):
    for line in b:
        for i in line:
            i[hit] = i[hit] or i[sq_val] == x

def check(board):
    return any([all(x[hit] for x in row) for row in board]) or \
    any(all(row[i][hit] for row in board) for i in range(len(board)))

with open('./day4.txt') as f:
    data = [l.strip() for l in f.readlines()]

moves = [int(x) for x in data[0].split(',')]
_boards = [get_board(b) for b in '\n'.join(data[2:]).split('\n\n')]
sq_val, hit = 0, 1

def part1():
    boards = [*_boards]
    for m in moves:
        for b in boards:
            mark(b, m)
            if check(b):
                return m*not_hit_sum(b)
    return 0

def part2():
    boards = [*_boards]
    for m in moves:
        for b in range(len(boards)):
            mark(boards[b], m)
            if check(boards[b]):
                if sum(1 for b in boards if b) == 1:
                    return m*not_hit_sum(boards[b])
                boards[b] = []
        
    return 0

print(part1())
print(part2())
