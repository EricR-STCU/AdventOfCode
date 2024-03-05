test = False
input_file = "in.txt"
test_file = "test.txt"
with open(input_file if not test else test_file) as f:
    data = f.read()

letters = data.split('\n\n')
letters = [l.split() for l in letters]
folds = []
    
def part1():
    total_row = 0
    total_col = 0
    for l in letters:
        found = False
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                found = True
                top = l[:i+1]
                bottom = l[i+1:]
                for (lf, rt) in zip(top[::-1], bottom):
                    if lf != rt:
                        found = False
                        break
                if found:
                    folds.append('row ' + str(i))
                    total_row += i+1
        if not found:
            get_col = lambda i: [col[i] for col in l]
            for i in range(len(l[0])-1):
                if  get_col(i) == get_col(i+1):
                    found = True
                    left = [get_col(c) for c in range(0, i+1)]
                    right = [get_col(c) for c in range(i+1, len(l[0]))]
                    for (lf, rt) in zip(left[::-1], right):
                        if lf != rt:
                            found = False
                            break
                    if found:
                        total_col += i+1
                        folds.append('col ' + str(i))
                        break
    print(total_row*100+total_col)
    
    return



def part2():
    total_row = 0
    total_col = 0
    for num, ll in enumerate(letters):
        found = False
        for row in range(len(ll)):
            if found:
                break
            for col in range(len(ll[0])):
                if found:
                    break
                l = [x for x in ll]
                l[row] = ll[row][:col]+('#' if ll[row][col] == '.' else '#')+ll[row][col+1:]
                assert len(l[row]) == len(ll[0])
                for i in range(len(l)-1):
                    if l[i] == l[i+1]:
                        found = True
                        top = l[:i+1]
                        bottom = l[i+1:]
                        for (lf, rt) in zip(top[::-1], bottom):
                            if lf != rt:
                                found = False
                                break
                        if found and folds[num] != ('row '+str(i)):
                            total_row += i+1
                        else:
                            found = False
                if not found:
                    get_col = lambda i: [col[i] for col in l]
                    for i in range(len(l[0])-1):
                        if  get_col(i) == get_col(i+1):
                            found = True
                            left = [get_col(c) for c in range(0, i+1)]
                            right = [get_col(c) for c in range(i+1, len(l[0]))]
                            for (lf, rt) in zip(left[::-1], right):
                                if lf != rt:
                                    found = False
                                    break
                            if found and folds[num] != ('col ' + str(i)):
                                total_col += i+1
                                break
                            else:
                                found = False
    print(total_row*100+total_col)
    return

part1()
part2()