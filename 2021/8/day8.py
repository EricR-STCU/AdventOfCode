with open('./day8.txt') as f:
    data = [l.strip() for l in f.readlines()]


def identify(nums):
    digits = {}
    def get(f):
        r = [n for n in nums if f(n)][0]
        nums.remove(r)
        return r

    digits[1] = get(lambda n: len(n)==2)
    digits[7] = get(lambda n: len(n)==3)
    digits[4] = get(lambda n: len(n)==4)
    digits[8] = get(lambda n: len(n)==7)

    digits[9] = get(lambda n: len(n ^ (digits[7] | digits[4])) == 1)
    digits[6] = get(lambda n: len(n & (digits[8] - digits[1])) == 5)
    digits[5] = get(lambda n: n < digits[6])
    digits[0] = get(lambda n: len(digits[6] & n) == 5)
    digits[2] = get(lambda n: len(digits[1] & n) == 1)
    digits[3] = nums[0]

    return digits


def get_display_val(digits, display):
    display_val = 0
    for p, num in enumerate(display[::-1]):
        for x, d in digits.items():
            if num==d:
                display_val += x * 10**(p)

    return display_val


def parse(string):
    return [set(s) for s in string.split(' ')]


def part1():
    d = [*data]

    total = 0
    for line in d:
        _, display = line.split(' | ')
        display = parse(display)
        total += sum(len(digit) in [2, 3, 4, 7] for digit in display)
    return total


def part2():
    d = [*data]

    total = 0
    for line in d:
        coded_digits, display = line.split(' | ')
        digits = identify(parse(coded_digits))
        total += get_display_val(digits, parse(display))
    return total


print(part1())
print(part2())