from collections import defaultdict
from functools import cmp_to_key
from itertools import combinations_with_replacement


with open("in.txt") as f:
    data = f.readlines()
    
data = [d.split() for d in data]
order = 'AKQJT98765432'
order2 = 'AKQT98765432J'
o = 'AKQT98765432'

    
def part1():
    data.sort(key=cmp_to_key(compare))
    total = 0
    for i, [h, b] in enumerate(data):
        total += (i+1) * int(b)
    print(total)
    return


def part2():
    data.sort(key=cmp_to_key(compare2))
    total = 0
    for i, [h, b] in enumerate(data):
        total += (i+1) * int(b)
    print(total)
    return


def compare(AA, BB):
    A = AA[0]
    B = BB[0]
    r1, r2 = rank(A), rank(B)
    if r1<r2:
        return -1
    if r1>r2:
        return 1
    for a, b in zip(A, B):
        if order.index(a) > order.index(b):
            return -1
        if order.index(a) < order.index(b):
            return 1
    return 0


def rank(hand):
    d = defaultdict(int)
    for c in hand:
        d[c] += 1
    if len(set(hand)) == 1:
        return -1
    if max(d.values()) == 4:
        return -2
    if 3 in d.values() and 2 in d.values():
        return -3
    if 3 in d.values():
        return -4
    if sum(1 if v == 2 else 0 for v in d.values()) == 2:
        return -5
    if 2 in d.values():
        return -6
    return -7


def compare2(AA, BB):
    A = AA[0]
    B = BB[0]
    r1, r2 = rank2(A), rank2(B)
    if r1<r2:
        return -1
    if r1>r2:
        return 1
    for a, b in zip(A, B):
        if order2.index(a) > order2.index(b):
            return -1
        if order2.index(a) < order2.index(b):
            return 1
    return 0


def rank2(hand):
    if 'J' in hand:
        hand = convert(hand)    
    d = defaultdict(int)
    for c in hand:
        d[c] += 1

    if len(set(hand)) == 1:
        return -1
    if max(d.values()) == 4:
        return -2
    if 3 in d.values() and 2 in d.values():
        return -3
    if 3 in d.values():
        return -4
    if sum(1 if v == 2 else 0 for v in d.values()) == 2:
        return -5
    if 2 in d.values():
        return -6
    return -7

def convert(hand: str):
    hand = hand.replace('J', '')
    best = '23457'
    for x in combinations_with_replacement(o, 5-len(hand)):
        test = hand+str.join('', x)
        if compare([best, 0], [test, 0]) == -1:
            best = test
    return best



part1()
part2()