# Playing around with string concatenation and loops

message = input("Enter a message: ")
new_message = ""

print()
for letter in message:
    new_message += letter
    print("New string:", new_message)

