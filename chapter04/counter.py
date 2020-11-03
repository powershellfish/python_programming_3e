# Counter
# Demonstrates the range() function

# Prints "Counting:" and numbers 0-10

print("Counting:")
for i in range(10):
    print(i, end=" ")

# Prints "Counting by fives:" and then numbers 0-50 in increments of 5

print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end=" ")

# Prints "Counting backwards:" and then numbers 10-0, subtracting each time

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")

# Ends the program

input("\n\nPress the enter key to exit.\n")
