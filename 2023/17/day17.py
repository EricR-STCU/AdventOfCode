from collections import defaultdict, deque


test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.readlines()
data = [d.strip() for d in data]

R = len(data)
C = len(data[0])
G = {}
for r in range(R):
    for c in range(C):
        G[c+r*1j] = int(data[r][c])
        
def part1():
    COST = defaultdict(lambda: 1e9)
    # location, direction, remaining straight steps
    cur = (0, 1, 2)
    q = deque()
    q.append(cur)
    COST[cur] = 0
    i = 0
    while len(q) > 0:
        i = (i+1)%10_000_000
        if i%10_000== 0:
            print(i//10_000)
        cur = q.pop()
        next = get_next(cur)
        for n in next:
            potential = COST[cur]+G[n[0]]
            cur_cost = COST[n]
            if cur_cost>potential:# and (R+C)*7>potential and G[n[0]] not in [8, 9]:
                COST[n] = potential
                q.append(n)

    ans = []
    for k, v in COST.items():
        if k[0] == (C-1)+(R-1)*1j:
            ans.append(v)
    print(min(ans))
    return

def get_next(cur):
    candidates = []
    (l, d, r) = cur
    candidates.append((l+(d*1j), d*1j, 2))
    candidates.append((l+(d*-1j), d*-1j, 2))
    if r > 0:
        candidates.append((l+d, d, r-1))
    candidates = [c for c in candidates if 0<=c[0].real<C and 0 <=c[0].imag<R]
    return candidates

def get_next2(cur):
    (l, d) = cur
    candidates = [(l+d*1j*i, d*1j) for i in range(4, 11)]
    candidates += [(l+d*-1j*i, d*-1j) for i in range(4, 11)]
    candidates = [c for c in candidates if 0<=c[0].real<C and 0 <=c[0].imag<R]
    return candidates

def part2():
    COST = defaultdict(lambda: 1e9)
    # location, direction
    q = deque()
    COST[(0, 1)] = 0
    first_moves = [(i, 1) for i in range(4, 11)]
    for fm in first_moves:
        COST[fm] = sum(int(c) for c in data[0][1:fm[0]+1])
    q.extend(first_moves)
    i = 0
    while len(q) > 0:
        i = (i+1)%10_000_000
        if i%10_000== 0:
            print(i//10_000)
        cur = q.pop()
        next = get_next2(cur)
        for n in next:
            potential = COST[cur]+sum(G[cur[0]+x*n[1]] for x in \
                  range(int(abs(cur[0].real-n[0].real)+abs(cur[0].imag-n[0].imag))))
            cur_cost = COST[n]
            if cur_cost>potential:
                COST[n] = potential
                q.append(n)

    print(len(COST))
    ans = []
    for k, v in COST.items():
        if k[0] == (C-1)+(R-1)*1j:
            ans.append(v)
    print(min(ans))
    return

#part1()
part2()