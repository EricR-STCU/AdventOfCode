with open('./in.txt') as f:
    data = []
    cur = []
    for line in f.readlines():
        if line.strip() != '':
            cur.append(int(line.strip()))
        else:
            data.append(cur)
            cur = []

def p1():
    return max(sum(elf) for elf in data)


def p2():
    elfs = [sum(elf) for elf in data]
    elfs.sort()
    return sum(elfs[-3:])

print(p1())
print(p2())