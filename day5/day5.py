stacks = []
def readCrates(lines):
    for i in range(int(len(lines[0])/4)):
        stacks.append([])
    for line in lines:
        if line[1] == "1":
            break
        for i in range(len(stacks)):
            index = i * 4 + 1
            if line[index] != " ":
                stacks[i].insert(0, line[index]) 

def part1():
    with open("day5/input.txt") as f:
        lines = []
        line = ""
        while line != "\n":
            line = f.readline()
            lines.append(line)
        readCrates(lines)
        lines = f.readlines()
        for line in lines:
            _, num, _, start, _, end = line.split(" ")
            for i in range(int(num)):
                stacks[int(end) - 1].append(stacks[int(start) - 1].pop())
    output = ""
    for i in range(len(stacks)):
        output += stacks[i][len(stacks[i]) - 1]
    print(output)

def part2():
    with open("day5/input.txt") as f:
        lines = []
        line = ""
        while line != "\n":
            line = f.readline()
            lines.append(line)
        readCrates(lines)
        lines = f.readlines()
        for line in lines:
            _, num, _, start, _, end = line.split(" ")
            crates = stacks[int(start) - 1][-int(num):]
            stacks[int(start) - 1] = stacks[int(start) - 1][:-int(num)]
            stacks[int(end) - 1] = stacks[int(end) - 1] + crates
    output = ""
    for i in range(len(stacks)):
        output += stacks[i][len(stacks[i]) - 1]
    print(output)

# part1()
part2()