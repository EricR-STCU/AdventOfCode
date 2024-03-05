test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.readlines()
data = [l.strip() for l in data]

def part1():
    global data
    lines, cols = [], []
    for r in range(len(data)):
        if not any(c == '#' for c in data[r]):
            lines.append(r)
    for c in range(len(data[0])):
        if not any(ch == '#' for ch in [l[c] for l in data]):
            cols.append(c)
    for i, l in enumerate(lines):
        data.insert(l+i, data[l+i])
    for i, c in enumerate(cols):
        new_data = []
        for line in data:
            new_data.append(line[:c+i]+'.'+line[c+i:])
        data = new_data
    G = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '#':
                G.append(r+c*1j)
    total = 0
    for a in range(len(G)):
        for b in range(a, len(G)):
            A = G[a]
            B = G[b]
            t = abs(A.real-B.real)+abs(A.imag-B.imag)
            #print(A, B, t)
            total += t
    print(total)
    return


def part2():
    lines, cols = [], []
    for r in range(len(data)):
        if not any(c == '#' for c in data[r]):
            lines.append(r)
    for c in range(len(data[0])):
        if not any(ch == '#' for ch in [l[c] for l in data]):
            cols.append(c)
    G = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '#':
                R = r + (1_000_000-1) * sum(1 for l in lines if l<r)
                C = c + (1_000_000-1) * sum(1 for col in cols if col<c)
                G.append((R, C))

    total = 0
    for a in range(len(G)):
        for b in range(a, len(G)):
            A = G[a]
            B = G[b]
            t = abs(A[0]-B[0])+abs(A[1]-B[1])
            #print(A, B, t)
            total += t
    print(total)
    return
part1()
part2()