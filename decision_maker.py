# Decision Maker Project
# Takes user inputs and randomly returns one input

import random

# List of options
option_list = []

while True:
    try:
        # Number of options
        option_number = int(input("Enter number of options: "))
        print()
        break
    except ValueError: # Error management ensuring program doesn't crash
        print("Error. Enter option number: ")

# Iterates through range
for i in range(option_number):
    option = str(input(f"Enter choice {i + 1}: "))
    option_list.append(option) # Adds submitted options to list

decision = random.choice(option_list) # Randomly returns one option

print()
print(f"Decision: {decision}")
