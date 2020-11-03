import random

count = 0
heads = 0
tails = 0

while count < 100:
    coin = random.randint(1,2)
    if coin == 1:
        print("Heads!\n")
        heads += 1
        count += 1

    elif coin == 2:
        print("Tails!\n")
        tails += 2
        count += 2

print("Heads:", heads)
print("Tails:", tails)
