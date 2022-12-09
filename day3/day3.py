import string

letters = string.ascii_lowercase + string.ascii_uppercase

def part1():
    count = 0
    with open("day3/input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            split = int(len(line)/2)
            first = line[:split]
            second = line[split:]
            for c in first:
                if c in second:
                    count += (letters.index(c) + 1)
                    break
    print(count)

def part2():
    count = 0
    with open("day3/input.txt") as f:
        lines = f.readlines()
        for i in range(int(len(lines)/3)):
            line1 = lines[i*3]
            line2 = lines[(i*3)+1]
            line3 = lines[(i*3)+2]
            for c in line1:
                if c in line2 and c in line3:
                    count += (letters.index(c) + 1)
                    break
    print(count)

#part1()
part2()