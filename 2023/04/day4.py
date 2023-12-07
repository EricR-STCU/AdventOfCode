from collections import defaultdict


with open("in.txt") as f:
    data = f.readlines()

cards = [d[d.index(':')+1:].strip() for d in data]
cards = [c.split(' | ') for c in cards]
cards = [[a.split(), b.split()] for a, b in cards]

def part1():
    total = 0
    for card in cards:
        cnt = len(set(card[0]) & set(card[1]))
        total += 0 if cnt == 0 else 2**(cnt-1)
    print(total)
    return


def part2():
    card_copy_count = defaultdict(int)

    for i, card in enumerate(cards):
        card_num = i+1
        card_copy_count[card_num] += 1
        cnt = len(set(card[0]) & set(card[1]))
        for x in range(card_num+1, card_num+cnt+1):
            card_copy_count[x] += card_copy_count[card_num]
        
    print(sum(card_copy_count.values()))
    return

part1()
part2()