# Playing around with message analyzer
# Demonstrates the len() function and the in operator

message = input("Text me: ")

print("\nYour message is ", len(message), "characters long.")

print("\nThe letter e")
if "e" in message:
    print("is in your text.")
else:
    print("Hrm, looks like you don't have any e's in your message to me.")

input("\nPress the enter key to exit.")
