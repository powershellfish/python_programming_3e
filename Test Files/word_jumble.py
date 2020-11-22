# Working on Word Jumble Concept

import random
WORDS = ("sunset", "sunrise", "mountain", "river", "desert")

word = random.choice(WORDS)

correct = word

jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
"""
        Welcome to Word Jumble!

    Unscramble the letters to make a word.
    Press the enter key at the prompt to quit.
"""
)

print("\nHere's the jumble:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's incorrect.")
    guess = input("Your guess: ")

if guess == correct:
    print("Great job! You guessed correctly!\n")

print("Thanks for playing!")

input("\n\nPress Enter to exit.")
