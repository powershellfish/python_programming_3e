# Random Access
# Demonstrates string indexing

# Imports the random module

import random

# Prints the text: The word is: latte

word = "latte"
print("The word is: ", word, "\n")

# Create two endpoints so random.randrange() can choose a random integer to
# represent the letter.
# len(word) means "the highest positive int corresponding to any letter in this string"
# -len(word means "the lowest int corresponding to any letter in this string"

high = len(word)
low = -len(word)

# This for loop

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\n\nPress the enter key to exit.")
