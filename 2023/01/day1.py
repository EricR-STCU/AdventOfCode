with open("in.txt") as f:
    data = f.readlines()
    
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
match = {
         "one": "1",
         "two": "2",
         "three": "3",
         "four": "4",
         "five": "5",
         "six": "6",
         "seven": "7",
         "eight": "8",
         "nine": "9",
         "0": "0",
         "1": "1",
         "2": "2",
         "3": "3",
         "4": "4",
         "5": "5",
         "6": "6",
         "7": "7",
         "8": "8",
         "9": "9"}
    
def part1():
    total = 0
    for l in data:
        v = ""
        for c in l:
            if c in "0123945867":
                v += c
                break
        for c in l[::-1]:
            if c in "0123945867":
                v += c
                break
        if len(v) == 0:
            v = 0
        total += int(v) 
    print(total)
    return


def part2():
    total = 0

    for l in data:
        print("============")
        print(l)
        ll = l[:]


        for i in range(len(l)):
            for d in digits:
                if d in l[i:i+len(d)]:
                    l = l.replace(d, match[d])
                    break
        for i in range(2, len(ll)):
            print(ll[-i:-i+len(d)])
            for d in digits:
                if d in ll[-i:-i+len(d)]:
                    ll = ll[::-1].replace(d[::-1], match[d])[::-1]
                    #ll = ll.replace(d, match[d])
                    break
        print(l)
        print(ll)
            


        v = ""
        for c in l:
            if c in "0123945867":
                v += c
                break
        for c in ll[::-1]:
            if c in "0123945867":
                v += c
                break
        if len(v) == 0:
            v = "0"
        total += int(v) 
    print(total)
    return

part1()
part2()