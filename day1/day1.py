# day1
def part1():
    with open("day1/input.txt") as f:
        lines = f.readlines()
        max_count = 0
        count = 0
        for line in lines:
            if line == "\n":
                max_count = max(count, max_count)
                count = 0
            else:
                count += int(line)

        print(max_count)

def part2():
    with open("day1/input.txt") as f:
        lines = f.readlines()
        max_counts = [0]*3
        count = 0
        for line in lines:
            if line == "\n":
                max_counts += [count]
                max_counts.sort(reverse=True)
                max_counts = max_counts[:3]
                count = 0
            else:
                count += int(line)

        print(sum(max_counts))

print("PART_1")
part1()
print("PART_2")
part2()