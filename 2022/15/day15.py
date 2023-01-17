from collections import defaultdict, Counter, deque
from string import ascii_lowercase

with open('./in.txt') as f:
    data = [l.strip() for l in f.readlines()]
    SB = []
    for line in data:
        sensor, beacon = line.split('closest')
        sensor = sensor[sensor.index('=')+1:sensor.index(':')].split(', y=')
        sensor = (int(sensor[0]), int(sensor[1]))
        beacon = beacon[beacon.index('=')+1:].split(', y=')
        beacon = (int(beacon[0]), int(beacon[1]))
        SB.append((sensor, beacon))
    
                    
def d(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def p1(y = 2000000):
    G = 0
    minx, maxx = 1e9, -1e9
    for s, b in SB:
        distance = d(s, b)
        minx = min(minx, s[0]-distance)
        maxx = max(maxx, s[0]+distance)
        

        
    print(minx, maxx)
    for x in range(minx-10000, maxx+10000):
        for s, b in SB:
            distance = d(s, b)
            if d(s, (x, y)) <= distance:
                G += 1
                break
    B = set()
    for _, b in SB:
        B.add(b)
    for b in B:
        if b[1] == y:
            G -= 1
    return G


def get_shell(s, b):
    print(s, b)
    distance = d(s, b)+1
    for i in range(distance+1):
        j = distance-i
        if s[0]+i in range(4000000) and s[1]+1 in range(4000000):
            yield (s[0]+i, s[1]+j)
        if s[0]-i in range(4000000) and s[1]+1 in range(4000000):
            yield (s[0]-i, s[1]+j)
        if s[0]+i in range(4000000) and s[1]-1 in range(4000000):
            yield (s[0]+i, s[1]-j)
        if s[0]-i in range(4000000) and s[1]-1 in range(4000000):
            yield (s[0]-i, s[1]-j)


def p2(M=4000000):
    shells = [set(get_shell(s, b)) for s, b in SB]
    candidates = set()
    for i in range(len(shells)-2):
        for j in range(i+1, len(shells)-1):
            cur = shells[i] & shells[j]
            for k in range(j+1, len(shells)):
                print(i, j, k)
                candidate = cur & shells[k]
                if len(candidate) == 1:
                    candidates.add(candidate.pop())
                    
    print(candidates)
    for candidate in candidates:
        if all(d(s, candidate) > d(s, b) for s, b in SB) and 0 < candidate[0] <= M and 0 < candidate[1] <= M:
            return candidate[0]*4000000 + candidate[1]


#print(p1())
print(p2())