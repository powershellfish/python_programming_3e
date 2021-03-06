# Exclusive Network
# Demonstrates logical operators and compound conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username:
    username = input("Username: ")

# This while loop ensures that the program won't continue until a username
# is entered.

password = ""
while not password:
    password = input("Password: ")

# This while loop ensures that the program won't continue until a password
# is also entered.

if username == "glitterbot" and password == "Gizmo":
    print("Hey there, glitterbot.")
    security = 6

# This loop says "if user is glitterbot and password is Gizmo, then true,
# and print "Hey there, glitterbot." and assign a security level of 6.
# None of the ELIF statements below are executed because the code stops
# running as soon as one of them is TRUE.
# The last ELSE statement only runs if the user doesn't match a username
# or password to what is in the code below. One or the other must be a match.

elif username == "M.Dawson" and password == "secret":
    print("Hi, Mike.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Hey, Sid.")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("What's up, Shigeru?")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How goes it, Will?")
    security = 3
elif username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1
else:
    print("Login failed.  You're not so exclusive.\n")

input("\n\nPress the enter key to exit.")
