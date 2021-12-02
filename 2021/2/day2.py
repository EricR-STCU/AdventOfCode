with open('./day2.txt') as f:
    data = [l.strip().split(' ') for l in f.readlines()]

def part1():
  h = sum(int(x[1]) for x in data if x[0] == 'forward')
  d = sum(int(x[1]) for x in data if x[0] == 'down')
  u = sum(int(x[1]) for x in data if x[0] == 'up')
  return h*(d-u)

def part2():
  aim = 0
  p = 0
  y = 0
  for x in data:
    if x[0] == 'forward':
      p += int(x[1])
      y += aim*int(x[1])
    if x[0] == 'down':
      aim += int(x[1])
    if x[0] == 'up':
      aim -= int(x[1])
  return p*y

print(part1())
print(part2())