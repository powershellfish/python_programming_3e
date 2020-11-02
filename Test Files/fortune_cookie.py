# Fortune Cookie
# Demonstrated the elif clause, and random module (with randint)

import random

print("Welcome to Yen Cheng!")
print("Hope your dinner was great. Here's your fortune!")

fortune = random.randint(1,5)

if fortune == 1:
    # lucky
    print("You will be fortunate this year.")

elif fortune == 2:
    # wise
    print("You will advise your friends on important matters.")

elif fortune == 3:
    # challenge
    print("You will be tested. Hold fast.")

elif fortune == 4:
    # happy
    print("You will be very happy this week!")

elif fortune == 5:
    # confused
    print("This week looks very murky...")

else:
    print("Illegal fortune value! No cookie for you!")

input("\n\nPress the enter key to exit.")
