cycles = [20, 60, 100, 140, 180, 220]
result = []
register = 1
current_cycle = 0
queue = []
image = ['.' for i in range(40*6)]

def print_image():
    for i in range(len(image)):
        print(image[i], end=' ')        
        if((i+1) % 40 == 0):
            print()

def readInput():
    global queue
    with open("day10/input.txt") as f:
        lines = f.read().split("\n")
        lines.reverse()
        for line in lines:
            if line.startswith("addx"):
                val = int(line.split(" ")[1])
                queue += [val, 0]
            else:
                queue += [0]

def run():
    global current_cycle, register
    while len(queue) > 0:
        current_cycle += 1
        register_range = [register - 1, register, register + 1]
        if (current_cycle-1) % 40 in register_range:
            image[current_cycle-1] = '#'
        if current_cycle in cycles:
            result.append(register * current_cycle)
        register += queue.pop()
        #   print(current_cycle, register)

def part1():
    readInput()
    run()
    print(result)
    print(sum(result))

def part2():
    readInput()
    run()
    print_image()

# part1()
part2()
