with open('./day1.txt') as f:
    data = [int(l.strip()) for l in f.readlines()]

part1 = lambda data: sum(data[i] < data[i+1] for i in range(len(data)-1))
part2 = lambda data: sum(data[i] < data[i+3] for i in range(len(data)-3))

print(part1(data))
print(part2(data))