# Generates a random restaurant from the list

import random

restaurant = 0
count = 0

while count <= 1:
    restaurant = random.randint(1,10)
    if restaurant == 1:
        print("Jake and Telly's\n")
    elif restaurant == 2:
        print("Noodles\n")
    elif restaurant == 3:
        print("Phantom Canyon\n")
    elif restaurant == 4:
        print("McDonalds\n")
        
print("Here's where you'll eat tonight:", restauraunt)
