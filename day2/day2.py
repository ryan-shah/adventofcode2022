rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]
points = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def winner(a, b):
    if points[a] == points[b]:
        return 3
    if a in rock and b in scissors:
        return 0
    if a in paper and b in rock:
        return 0
    if a in scissors and b in paper:
        return 0
    return 6
        

def part1():
    with open("day2/input.txt") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            a, b = line.strip().split(" ")
            count += (points[b] + winner(a, b))
        print(count)

def pickWinningMove(a):
    if a in rock:
        return "Y"
    if a in paper:
        return "Z"
    if a in scissors:
        return "X"

def pickSameMove(a):
    if a in rock:
        return "X"
    if a in paper:
        return "Y"
    if a in scissors:
        return "Z"

def pickLosingMove(a):
    if a in rock:
        return "Z"
    if a in paper:
        return "X"
    if a in scissors:
        return "Y"

def part2():
    with open("day2/input.txt") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            a, b = line.strip().split(" ")
            if b == "X":
                b = pickLosingMove(a)
            elif b == "Y":
                b = pickSameMove(a)
            else:
                b = pickWinningMove(a)
            count += (points[b] + winner(a, b))
        print(count)

#part1()
part2()