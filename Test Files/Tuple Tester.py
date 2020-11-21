# Among Us Tuple Tester


# Creates a tuple with all of the crewmates in Among Us
crewmates = ("cyan",
           "red",
           "green",
           "blue",
           "yellow",
           "orange",
           "black",
           "purple")


# Creates a tuple with the imposters in Among Us
imposters = ("pink",
             "white")

# Prints the list of crewmates/imposters in the tuple by using a FOR loop

print("\nHere is the list of crewmates and imposters:\n")
for item in crewmates:
    print(item)

# Uses the LEN function to print the total number of elements in the tuple amongus

print("\nThere are", len(crewmates), "of us.")

print("\nLet's see who's an imposter...")
input("\nPress Enter to find out...")

# Uses IF statements to test for membership in crewmates or imposters. 

if "pink" in crewmates:
    print("\nglitterbot is a crewmate.")

if "cyan" in crewmates:
    print("\ncyan is clearly a crewmate.")

if "white" in imposters:
    print("\nBut Devon is sus!")

# Demonstrates slicing

start = int(input("\nEnter a number to start a slice: "))
finish = int(input("\nNow enter a number to finish the slice: "))
print("crewmates[", start, ":", finish, "] is", end=" ")
print(crewmates[start:finish])

start = int(input("\nEnter a number to start a slice: "))
finish = int(input("\nNow enter a number to finish the slice: "))
print("imposters[", start, ":", finish, "] is", end=" ")
print(imposters[start:finish])

input("\nPress Enter to see what tuple concatenation looks like:")

# Concatenation

crewmates = ("cyan", "red", "green", "blue", "yellow", "orange", "black", "purple")
print("You find all the crewmates clutered together. They are:")
print(crewmates)
print("You find the imposters who haven't killed anyone yet:")
crewmates += imposters
print("The group now consists of:")
print(crewmates)

input("\nPress Enter to exit this hellscape.")
