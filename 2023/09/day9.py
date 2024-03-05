test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.readlines()
data = [[int(x) for x in l.split()] for l in data]


def r(l:list):
    n = []
    for i in range(len(l)-1):
        n.append(l[i+1]-l[i])
    return n


def part1():
    total = 0
    for l in data.copy():
        cur = l
        tree = [cur]
        while not all(x==0 for x in cur):
            cur = r(cur)
            tree.append(cur)
        for i in range(len(tree)-1, 0, -1):
            tree[i-1].append(tree[i-1][-1]+tree[i][-1])
        total += tree[0][-1]
    print(total)
    return

def part2():
    total = 0
    for l in data.copy():
        cur = l
        tree = [cur]
        while not all(x==0 for x in cur):
            cur = r(cur)
            tree.append(cur)
        for i in range(len(tree)-1, 0, -1):
            tree[i-1].insert(0, tree[i-1][0]-tree[i][0])
        total += tree[0][0]
    print(total)
    return


part1()
part2()