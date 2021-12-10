from collections import deque

with open('./day10.txt') as f:
    data = [line.strip() for line in f.readlines()]


M = {
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
    '<': '>',
    '>': '<',
    '(': ')',
    ')': '(',
}
score_corrupt = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}
score_incomplete = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}
open_ = '[{(<'
close = ']})>'
wrong = []


def part1():
    d = [*data]

    bad = []
    for line in d:
        Q = deque()
        for symbol in line:
            if symbol in close and symbol != M[Q[-1]]:
                bad.append(symbol)
                wrong.append(line)
                break
            if symbol in close:
                Q.pop()
            else:
                Q.append(symbol)
    
    return sum(score_corrupt[c] for c in bad)


def part2():
    d = [*data]
    d = [line for line in d if line not in wrong]

    line_completion = []
    for line in d:
        Q = deque()
        for i, symbol in enumerate(line):
            if symbol in close:
                Q.popleft()
            else:
                Q.appendleft(symbol)
        line_completion.append([M[c] for c in Q])

    scores = []
    for line in line_completion:
        score = 0
        for c in line:
            score = score * 5 + score_incomplete[c]
        scores.append(score)
    scores.sort()
    return scores[len(scores)//2]


print(part1())
print(part2())