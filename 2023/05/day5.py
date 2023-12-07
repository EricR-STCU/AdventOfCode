test = False
with open("in.txt" if not test else "test.txt") as f:
    data = f.readlines()

seeds = data[0][data[0].index(' ')+1:]
seeds = [int(s) for s in seeds.split()]

ssm = data[3:38] if not test else data[3:5]
ssm = [[int(n) for n in s.split()] for s in ssm]

sfm = data[40:73] if not test else data[7:10]
sfm = [[int(n) for n in s.split()] for s in sfm]

fwm = data[75:103] if not test else data[12:16]
fwm = [[int(n) for n in s.split()] for s in fwm]

wlm = data[105:120] if not test else data[18:20]
wlm = [[int(n) for n in s.split()] for s in wlm]

ltm = data[122:154] if not test else data[22:25]
ltm = [[int(n) for n in s.split()] for s in ltm]

thm = data[156:188] if not test else data[27:29]
thm = [[int(n) for n in s.split()] for s in thm]

hlm = data[190:] if not test else data[31:]
hlm = [[int(n) for n in s.split()] for s in hlm]

maps = [ssm, sfm, fwm, wlm, ltm, thm, hlm]
    
def part1():
    minn = seeds[0]
    for seed in seeds:
        for mp in maps:
            for m in mp:
                if seed in range(m[1], m[1]+m[2]): #of by one?
                    seed = m[0] + (seed-m[1])            
                    break
        minn = min(minn, seed)
    print(minn)
    return


def part2():
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append([seeds[i], seeds[i]+seeds[i+1]-1])
    for mp in maps:
        print("m")
        next_ranges = []
        for m in mp:
            search_again = []
            for rng in ranges:
                remainder, next = overlap(rng, [m[1], m[1]+m[2]-1])
                if next:
                    next_ranges.append([m[0]+next[0]-m[1], m[0]+next[1]-m[1]])
                if remainder:
                    search_again += remainder
            ranges = search_again
        ranges = next_ranges + ranges
    print(min(r[0] for r in ranges))
    return

def overlap(r, rr):
    if rr[0]<=r[0]<=r[1]<=rr[1]:
        return None, r
    elif r[0]<rr[0]<=rr[1]<r[1]:
        return [[r[0], rr[0]-1], [rr[1]+1, r[1]]], rr
    elif r[0]<=rr[0]<=r[1]<=rr[1]:
        return [[r[0], rr[0]-1]], [rr[0], r[1]]
    elif rr[0]<=r[0]<rr[1]<=r[1]:
        return [[rr[1]+1, r[1]]], [r[0], rr[1]]
    elif r[1] < rr[0] or r[0] > rr[1]:
        return [r], None
    else:
        print('wtf', r, rr)
        return None, None



#part1()
part2()