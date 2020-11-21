# Among Us Tuple Tester

amongus = ("cyan",
           "pink",
           "red",
           "green",
           "blue",
           "yellow",
           "orange",
           "black",
           "white",
           "purple")

print("\nHere is the list of crewmates and imposters:\n")

for item in amongus:
    print(item)

print("\nThere are", len(amongus), "of us.")

input("\nPress the enter key to learn more.")

if "pink" in amongus:
    print("\nglitterbot is sus.")

if "cyan" in amongus:
    print("\ncyan is clearly a crewmate.")
