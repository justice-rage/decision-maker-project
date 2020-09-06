# Decision Maker Project
# Takes user inputs and randomly returns one input

import random

# List of options
option_list = []

# Number of options
option_number = int(input("Enter number of options: "))
print()

# Iterates through range
for i in range(0, option_number):
    option = str(input(f"Enter choice {i + 1}: "))

    option_list.append(option) # Adds submitted options to list

decision = random.choice(option_list) # Randomly returns one option

print()
print(f"Decision: {decision}")
