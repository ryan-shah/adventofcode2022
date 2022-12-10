# Initial Grid
grid = [['.'] * 6 for i in range(5)]
head = 0
tail = 1
rope = []
moves = []
tail_pos = [(0,4)]
x_moves = ['L', 'R']
y_moves = ['U', 'D']

def print_grid():
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            for k in range(len(rope)):
                if rope[k][0] == i and rope[k][1] == j:
                    print(k, end = ' ')
                    break
            else:
                print(grid[j][i], end=' ')
        print()

def readInput():
    global moves
    with open("day9/input.txt") as f:
        moves = [line for line in f.read().split("\n")]

def updateGrid(move):
    global rope, head, tail
    x_dist = rope[head][0] - rope[tail][0]
    y_dist = rope[head][1] - rope[tail][1]
    did_move = False
    # check move right
    if x_dist == 2 and y_dist == 0:
        rope[tail][0] += 1
        did_move = True
    # check move left
    elif x_dist == -2 and y_dist == 0:
        rope[tail][0] -= 1
        did_move = True
    # check move up
    elif y_dist == -2 and x_dist == 0:
        rope[tail][1] -= 1
        did_move = True
    # check move down
    elif y_dist == 2 and x_dist == 0:
        rope[tail][1] += 1
        did_move = True

    if abs(x_dist) + abs(y_dist) > 2:
        rope[tail][0] += int(x_dist / abs(x_dist))
        rope[tail][1] += int(y_dist / abs(y_dist))
    


def do_move(move):
    global rope, head, tail
    d, n = move.split(' ')
    for i in range(int(n)):
        head = 0
        tail = 1
        if d == 'R':
            rope[head][0] += 1
        elif d == 'L':
            rope[head][0] -= 1
        elif d == 'U':
            rope[head][1] -= 1
        else:
            rope[head][1] += 1
        for j in range(len(rope)-1):
            if j == 1:
                x =1
                pass
            head = j
            tail = j + 1
            updateGrid(d)
        #print_grid()
        #input()
        tail_pos.append((rope[len(rope)-1][0], rope[len(rope)-1][1]))

def part1():
    global rope
    rope = [[0, 4] for i in range(2)]
    readInput()
    for move in moves:
        do_move(move)
    print(len(set(tail_pos)))

def part2():
    global rope
    rope = [[0, 4] for i in range(10)]
    readInput()
    for move in moves:
        do_move(move)
    print(len(set(tail_pos)))

#part1()
part2()


