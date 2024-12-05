import itertools as it
import re
from collections import defaultdict, Counter

test = False
input_file = "in.txt"
test_file = "test.txt"

def load():
    with open(input_file if not test else test_file) as f:
        data = f.read()
    top, bottom = data.split("\n\n")

    top = top.split("\n")
    top = [[int(x) for x in l.strip().split("|")] for l in top]

    bottom = bottom.strip().split("\n")
    bottom = [[int(x) for x in l.strip().split(",")] for l in bottom]

    return (top, bottom)
    

def part1():
    rules, instr = load()
    
    R = defaultdict(lambda:[])
    for r in rules:
        R[r[0]].append(r[1])
        
    correct = []
    for line in instr:
        good = True
        for i in range(len(line)):
            cur = line[i]
            before = line[:i]
            after = line[i+1:]
            
            for n in before:
                if n in R[cur]:
                    good = False
                    break
            for n in after:
                if cur in R[n]:
                    good = False
                    break
        if good:
            correct.append(line[len(line)//2])
    
    print(sum(correct))
    return


def part2():
    rules, instr = load()
    
    R = defaultdict(lambda:[])
    for r in rules:
        R[r[0]].append(r[1])
        
    incorrect = []
    for line in instr:
        good = True
        for i in range(len(line)):
            cur = line[i]
            before = line[:i]
            after = line[i+1:]
            
            for n in before:
                if n in R[cur]:
                    good = False
                    break
            for n in after:
                if cur in R[n]:
                    good = False
                    break

        if not good:
            incorrect.append(line)
            
    new_centers = []
    for badline in incorrect:
        newline = [badline.pop()]
        for n in badline:
            for i in range(len(newline)):
                if newline[i] in R[n]:
                    newline.insert(i, n)
                    break
            if not n in newline:
                newline.append(n)

        new_centers.append(newline[len(newline)//2])

    print(sum(new_centers))
    return

part1()
part2()