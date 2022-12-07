from collections import defaultdict, Counter, deque

with open('./in.txt') as f:
    data = [l.strip() for l in f]

    
def parse():
    i = 0
    root = Dir()
    cur = root
    while i < len(data):
        if data[i].startswith("$ cd"):
            a, b, c = data[i].split(' ')
            i += 1
            match c:
                case "..":
                    cur = cur.Parent
                    continue
                case "/":
                    cur = root
                    continue
                case new_dir:
                    cur = cur.Files[new_dir]
                    continue
        elif data[i].startswith("$ ls"):
            i += 1
            while i<len(data) and not data[i].startswith("$"):
                x, name = data[i].split(' ')
                if x == "dir":
                    if name not in cur.Files:
                        cur.Files[name] = Dir(cur)
                else:
                    cur.Files[name] = int(x)
                i += 1
    return root


class Dir():
    def __init__(self, parent=None) -> None:
        self.Files = {}
        self.Parent = parent
        
    def size(self):
        total = 0
        for f in self.Files.values():
            if type(f) is Dir:
                total += f.size()
            else:
                total += f
        return total


    def find_p1(self):
        size = self.size()
        subdir_totals = 0
        for v in self.Files.values():
            if type(v) is Dir:
                subdir_totals += v.find_p1()
        if size <= 100000:
            return  size+subdir_totals
        return subdir_totals
    

    def find_p2(self, small, needed):
        for d in self.Files.values():
            if type(d) is Dir:
                sd = d.size()
                if small > sd > needed:
                    small = d.find_p2(sd, needed)
        return small


def p1():
    root = parse()
    return root.find_p1()


def p2():
    root = parse()
    needed = 30000000 - (70000000 - root.size())
    smallest = root.size()
    
    return root.find_p2(smallest, needed)


print(p1())
print(p2())