with open('./day3.txt') as f:
    data = [l.strip() for l in f.readlines()]

def part1():
    g = []
    e = []

    for i in range(len(data[0])):
        zeros = sum(l[i]=='0' for l in data)
        ones = sum(l[i]=='1' for l in data)

        g.append('1' if zeros < ones else '0')
        e.append('0' if zeros < ones else '1')

    gamma = int(''.join(g), base=2)
    epsilon = int(''.join(e), base=2)

    return gamma*epsilon

def part2():
    oxygen = data.copy()
    co2 = data.copy()

    for i in range(len(data[0])):
        zeros = sum(l[i]=='0' for l in oxygen)
        ones = sum(l[i]=='1' for l in oxygen)

        oxygen = [x for x in oxygen if int(x[i]) == (1 if zeros<=ones else 0)]
        
        if len(oxygen) == 1:
            break

    for i in range(len(data[0])):
        zeroes = sum(l[i]=='0' for l in co2)
        ones = sum(l[i]=='1' for l in co2)

        co2 = [x for x in co2 if int(x[i]) == (0 if zeroes<=ones else 1)]

        if len(co2) == 1:
            break

    oxygen_rating = int(oxygen[0], base=2)
    co2_rating = int(co2[0], base=2)

    return oxygen_rating*co2_rating


print(part1())
print(part2())