from math import floor, ceil
with open('./day18.txt') as f:
    data = f.readlines()
nums = []
for line in data:
    exec(f'nums.append({line.strip()})')


class Tree():
    def __init__(self, tree=[0,0], parent=None):
        self.L = Tree(tree[0], self) if type(tree[0]) is list else tree[0]
        self.R = Tree(tree[1], self) if type(tree[1]) is list else tree[1]
        self.UP = parent

    ### return the node to the left whos right node is a leaf
    def get_l_node(self):
        n = self
        while n.UP and n == n.UP.L:
            n = n.UP

        if not n.UP: return (None, None)
        if type(n.UP.L) is int: return (n.UP, "L")

        n = n.UP.L

        while type(n.R) is not int:
            n = n.R

        return (n, "R")

    def get_r_node(self):
        n = self
        while n.UP and n == n.UP.R:
            n = n.UP

        if not n.UP: return (None, None)
        if type(n.UP.R) is int: return (n.UP, "R")

        n = n.UP.R

        while type(n.L) is not int:
            n = n.L

        return (n, "L")
    

    def explode(self):
        n, lr = self.get_l_node()
        if n:
            match lr:
                case "L":
                    n.L += self.L
                case "R":
                    n.R += self.L

        n, lr = self.get_r_node()
        if n:
            match lr:
                case "L":
                    n.L += self.R
                case "R":
                    n.R += self.R

        if self.UP.L == self:
            self.UP.L = 0
        else:
            self.UP.R = 0
            
        return
            

    def split(self, lr):
        if lr == "L":
            n = self.L
            self.L = Tree([floor(n/2), ceil(n/2)], self)

        if lr == "R":
            n = self.R
            self.R = Tree([floor(n/2), ceil(n/2)], self)

        return
    

    def add(self, tree):
        new = Tree()
        new.L = self
        new.R = tree
        self.UP = new
        tree.UP = new
        return new
    

    def magnitude(self):
        lm = self.L if type(self.L) is int else self.L.magnitude()
        rm = self.R if type(self.R) is int else self.R.magnitude()
        return 3*lm + 2*rm
    

    def try_explode(self, depth=0):
        if type(self.L) is int and type(self.R) is int and depth >= 4:
            self.explode()
            return True
        if type(self.L) is Tree and self.L.try_explode(depth + 1): return True
        if type(self.R) is Tree and self.R.try_explode(depth + 1): return True
        return False


    def try_split(self):
        if type(self.L) is int and self.L >= 10:
            self.split("L")
            return True
        elif type(self.R) is int and self.R >= 10:
            self.split("R")
            return True
        if type(self.L) is Tree and self.L.try_split(): return True
        if type(self.R) is Tree and self.R.try_split(): return True
        return False
    

    def reduce(self):
        while self.try_explode() or self.try_split():
            continue


    def __str__(self):
        return "["+self.L.__str__() + ", " + self.R.__str__() + "]"



def p1():
    t = Tree(nums.pop(0))
    while nums:
        t = t.add(Tree(nums.pop(0)))
        t.reduce()
        
    print(t)
    return t.magnitude()
    


print(p1())