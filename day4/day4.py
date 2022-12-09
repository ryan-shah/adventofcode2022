def completeOverlap(a1, a2, b1, b2):
    return (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2)

def betweenNums(target, start, end):
    return target >= start and target <= end

def partialOverlap(a1, a2, b1, b2):
    return betweenNums(a1, b1, b2) \
        or betweenNums(a2, b1, b2) \
        or betweenNums(b1, a1, a2) \
        or betweenNums(b2, a2, a1)

def part1():
    count = 0
    with open("day4/input.txt") as f:
        lines = f.readlines()
        for line in lines:
            a,b = line.split(",")
            a1, a2 = [int(x) for x in a.split("-")]
            b1, b2 = [int(x) for x in b.split("-")]
            if completeOverlap(a1, a2, b1, b2):
                count += 1
    print(count)

def part2():
    count = 0
    with open("day4/input.txt") as f:
        lines = f.readlines()
        for line in lines:
            a,b = line.split(",")
            a1, a2 = [int(x) for x in a.split("-")]
            b1, b2 = [int(x) for x in b.split("-")]
            if partialOverlap(a1, a2, b1, b2):
                count += 1
    print(count)

#part1()
part2()
