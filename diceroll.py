import random

# Define a function to simulate rolling a single die with a given number of sides
def roll_die(num_sides):
    return random.randint(1, num_sides)

# Define a function to roll multiple dice and add up the results
def roll_dice(num_dice, num_sides):
    total = 0
    for i in range(num_dice):
        total += roll_die(num_sides)
    return total

# Example usage: roll 2 six-sided dice and display the result
result = roll_dice(2, 6)
print("You rolled a total of", result)
