import random

count = 0
heads = 0
tails = 0

while count < 100:
    coin = random.randint(1,2)
    if coin == 1:
        print("Heads!\n")
        count += 1
        heads += 1
    elif coin == 2:
        print("Tails!\n")
        count += 1
        tails += 1

print("Heads:", heads)
print("Tails:", tails)
        
