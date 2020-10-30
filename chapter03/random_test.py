# Playing around with randomization

import random

# random is a module
# randint and randrange are functions that belong to the random module
# randint generates random numbers within the range specified, including those two numbers
# randrange also generates random numbers in a different way
# randrange looks at the defined range but only between 0 and one short of the last number

randonum = random.randint(1,10)
randorange = random.randrange(2) +3

print("Your random number is", randonum,".", "\nand I hope you like it because that's what you get!")

print("\nWe will print the random range function:", randorange,)

input("\n\nPress the Enter key to exit.")
