def part1():
    with open("day6/input.txt") as f:
        line = f.readline()
        for i in range(len(line)):
            prev3 = [*set(line[i-3:i])]
            if len(prev3) == 3 and line[i] not in prev3:
                print(i+1)
                break

def part2():
    with open("day6/input.txt") as f:
        line = f.readline()
        for i in range(len(line)):
            prev3 = [*set(line[i-13:i])]
            if len(prev3) == 13 and line[i] not in prev3:
                print(i+1)
                break

#part1()
part2()