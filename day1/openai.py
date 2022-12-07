import sys
def part1():
    max_calories = 0
    max_elf = -1
    current_elf = 0
    current_calories = 0

    # Read input from stdin
    for line in sys.stdin:
    # Calculate calories for the current Elf
        calories = int(line.strip())
        current_calories += calories

        # If this is a new Elf, compare calories with max_calories and update max_calories and max_elf if necessary
        if calories == 0:
            if current_calories > max_calories:
                max_calories = current_calories
                max_elf = current_elf

            current_elf += 1
            current_calories = 0

    # Print the Elf with the most calories and the number of calories they're carrying
    print("Elf %d is carrying the most calories with %d calories." % (max_elf, max_calories))

def part2():
    max_calories = 0
    max_elf = -1
    current_elf = 0
    current_calories = 0
    top_three_calories = 0

    # Read input from stdin
    for line in sys.stdin:
        # Calculate calories for the current Elf
        calories = int(line.strip())
        current_calories += calories

        # If this is a new Elf, compare calories with max_calories and update max_calories and max_elf if necessary
        if calories == 0:
            if current_calories > max_calories:
                top_three_calories += max_calories
                max_calories = current_calories
                max_elf = current_elf

            current_elf += 1
            current_calories = 0

    # Add the maximum number of calories to the total
    top_three_calories += max_calories

    # Print the total number of calories carried by the top three Elves
    print("The top three Elves are carrying %d calories in total." % top_three_calories)