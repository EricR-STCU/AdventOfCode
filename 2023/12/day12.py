import itertools as it


test = True
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.readlines()
data = [d.strip() for d in data]
springs = [d.split()[0] for d in data]
matches = [d.split()[1] for d in data]
matches = [[int(x) for x in n.split(',')] for n in matches]
counts = []
    
def part1():
    total = 0
    for s, m in zip(springs, matches):
        cnt = 0
        x = sum(1 for ss in s if ss=='?')
        for combo in it.product('.#', repeat=x):
            test = get(s, combo)
            if match(test, m):
                cnt += 1
        total += cnt
        counts.append(cnt)
    print(total)
    print(counts)
    return


def get(s, map):
    x = 0
    new = ''
    for c in s:
        if c == '?':
            new += map[x]
            x += 1
        else:
            new += c
    return new


def match(s:str, m):
    ss = s.split('.')
    ss = [sss for sss in ss if sss != '']
    if len(ss) != len(m):
        return False
    for [sss, l] in zip(ss, m):
        if len(sss) != l:
            return False
    return True

def part2():
    total = 0
    for i, [s, m] in enumerate(zip(springs, matches)):
        s = s+'?'+s+'?'+s+'?'+s+'?'+s
        m = m*5
        cnt = 0
        
        possibilities = []
        base = '.'.join('#'*n for n in m)
        print(s)
        print(base)
        print(counts[i])

        total += cnt
    print(total)
    return

part1()
part2()