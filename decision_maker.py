# Decision Maker Project
# Takes user inputs and randomly returns one input

import random

option_1 = str(input("Enter option 1: "))
option_2 = str(input("Enter option 2: "))

options = [option_1, option_2]
decision = random.choice(options)

print(decision)