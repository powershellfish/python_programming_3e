# Coin Flip Attempt 14

# Imports the random module to generate a random integer.

import random

# Sets all variables to start at 0.

count = 0
heads = 0
tails = 0

# While the count is under 100 attempts, the coin "flips".
# The integer for the coin is generated with randint. 
# If the value is 1, then print "Heads!", count heads once, and increase the count by 1.
# If the value is 2, then print "Tails!", count tails once, and increase the count by 1.


while count < 100:
    coin = random.randint(1,2)
    if coin == 1:
        print("Heads!\n")
        heads += 1
        count += 1
    elif coin == 2:
        print("Tails!\n")
        heads += 2
        count += 2

# Print the total number of heads.
# Print the total number of tails.

print("Heads:", heads)
print("Tails:", tails)
