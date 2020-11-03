import random

heads = 0
tails = 0
count = 0

# Initializes heads, tails and count at zero.

while count < 100:
    coin = random.randint(1, 2)
    if coin == 1:
        print("Heads!\n")
        heads += 1
        count +=1
        
# While the program hasn't reached 100, assign a random integer to COIN
# If coin is equal to 1, then print "heads". Increment and count by 1 each time.
# Otherwise (elif) the coin is equal to 2, then print "tails". Increment and count by 1 each time.

    elif coin == 2:
        print("Tails!\n")
        tails += 1
        count += 1

print("Heads:", heads)
print("Tails:", tails)
