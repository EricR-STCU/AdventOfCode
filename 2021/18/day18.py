with open('./day18.txt') as f:
    data = f.readlines()
nums = []
for line in data:
    exec(f'nums.append({line.strip()})')


class P():
    def __init__(self, tree=[0,0], parent=None):
        self.L = P(tree[0], self)
        self.R = P(tree[1], self)
        self.UP = parent

    def get_l_node():
        n = self
        while n == n.UP.L:
            n = n.UP
            if n is None:
                return P()
        n = n.L
        while n.R is not int:
            n = n.R
        return n

    def get_r_node():
        n = self
        while n == n.UP.R:
            n = n.UP
            if n is None:
                return P()
        n = n.R
        while n.L is not int:
            n = n.L
        return n


def reduce(num):
    cont = True
    while cont:
        cont = False
        #explode
        i = 0
        for n in num:
            while True:

        #split
    return num


def add(a, b):
    return [a, b]

def part1():
    x = nums[0]
    for n in nums[1:]:
        x = add(x, n)
        x = reduce(x)
    return x

def part2():
    return 0

print(part1())
print(part2())