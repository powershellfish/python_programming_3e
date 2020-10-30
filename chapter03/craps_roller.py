# Craps Roller
# Demonstrates random number generation

import random

# random is a MODULE
# randint is a FUNCTION and produces a random integer 
# randrange is a FUNCTION and 

# generate random numbers 1 - 6
die1 = random.randint(1, 6)

die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress the enter key to exit.")
