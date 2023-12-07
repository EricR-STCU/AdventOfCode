with open("in.txt") as f:
    data = f.readlines()
    
def part1():
    times = [42, 89, 91, 89]
    tobeat = [308, 1170, 1291, 1467]
    total = 1
    for t, d in zip(times, tobeat):
        ways = 0
        for i in range(t):
            if i*(t-i)>d:
                ways += 1
        total *= ways
    print(total)
    return


def part2():
    time = 42_899_189
    tobeat = 308_1170_1291_1467
    #time = 71530
    #tobeat = 940200
    before = 1
    while before*(time-before) < tobeat:
        before += 1
    after = time
    while after*(time-after) < tobeat:
        after -= 1
    print(after-before+1)
    return
part1()
part2()