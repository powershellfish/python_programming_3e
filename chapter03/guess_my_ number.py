# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random

# Import allows you to import or load modules. In this case, the module is "random".
# The program asks the player for their name, takes that input and prints it.
# Then it explains what it will do and tells the player what to do.

name = input("Hi.  What's your name? ")
print("\nHi,",name,".")
print("Welcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
# This uses the random module by generating a random integer and assigning it to the_number
# then asking the player to guess what the number is and gives them one try to do it.
# tries = x is the number of guesses the program will list + however many tries they perform
# so we start with 1.

the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# This is the guessing loop.
# as long as the player gueses a number that is not equal to the number, and if
# that number is greater than the random integer, print "lower..."
# and if the number is less than the number, print "higher..."
# and each time, print "Take a guess:"

while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

# Let the player know that they guessed the number correctly, and print the number of times
# it took them to guess correctly.
# Because the condition "while guess != the number: is false, the loop ends and prints the text
# below.

print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
