import random

total_heads = 0
total_tails = 0
count = 0


while count < 100:

    coin = random.randint(1, 2)

    if coin == 1:
        print("Heads!\n")
        total_heads += 1
        count += 1

    elif coin == 2:
        print("Tails!\n")
        total_tails += 1
        count += 1

print("\nOkay, you flipped heads", total_heads, "times ")
print("\nand you flipped tails", total_tails, "times ")
