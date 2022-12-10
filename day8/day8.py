grid = []

def print_grid():
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            print(grid[j][i], end=' ')
        print()

def visible(x, y):
    point = grid[y][x]
    # check edge
    if (x == 0) or (y == 0) or (x == len(grid) - 1) or (y == len(grid) - 1):
        return True  

    left = right = top = bottom = True
    # check left
    for i in range(x):
        gp = grid[y][i]
        if grid[y][i] >= point:
            left = False
    # check right
    for i in range(x + 1, len(grid)):
        gp = grid[y][i]
        if grid[y][i] >= point:
            right = False
    # check top
    for j in range(y):
        gp = grid[j][x]
        if grid[j][x] >= point:
            top = False
    # check bottom
    for j in range(y + 1, len(grid)):
        gp = grid[j][x]
        if grid[j][x] >= point:
            bottom = False
    return any([left, right, top, bottom])
    

with open("day8/input.txt") as f:
    lines = f.read().split("\n")
    grid = [[int(tree) for tree in line] for line in lines]


def part1():
    count = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if visible(i, j):
                count += 1
    print(count)

def senic_score(x, y):
    point = grid[y][x]
    # check edge
    if (x == 0) or (y == 0) or (x == len(grid) - 1) or (y == len(grid) - 1):
        return 0
    left = right = top = bottom = 0
    # check left
    for i in range(x-1,-1,-1):
        gp = grid[y][i]
        left += 1
        if grid[y][i] >= point:
            break 
    # check right
    for i in range(x + 1, len(grid)):
        gp = grid[y][i]
        right += 1
        if grid[y][i] >= point:
            break
    # check top
    for j in range(y-1,-1,-1):
        gp = grid[j][x]
        top += 1
        if grid[j][x] >= point:
            break
    # check bottom
    for j in range(y + 1, len(grid)):
        gp = grid[j][x]
        bottom += 1
        if grid[j][x] >= point:
            break
    score =  left * right * top * bottom
    return score

def part2():
    max_score = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if visible(i, j):
                max_score = max(max_score, senic_score(i, j))
    print(max_score)

#print_grid()        
#part1()
part2()