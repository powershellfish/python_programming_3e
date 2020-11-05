# Message Analyzer
# Demonstrates the len() function and the in operator

# Defines message as a variabe, and gets the information from the user as
# text input.

message = input("Enter a message: ")

# This line counts the number of characters in the text string and prints them.

print("\nThe length of your message is:", len(message))

# This loop looks to see if the letter e is present. 

print("\nThe most common letter in the English language, 'e',")
if "e" in message:
    print("is in your message.")
else:
    print("is not in your message.")

input("\n\nPress the enter key to exit.")

