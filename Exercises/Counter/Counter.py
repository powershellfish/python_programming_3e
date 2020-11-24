# Finicky Counter 2
# Playing around with the counter code

count = 0
# Count starts at zero, but does not print 0
while True:
    count += 1
    # Count increases by 1 each time
    if count > 10:
       break
    if count == 5:
        continue
    print(count)
    
input("\n\nPress the enter key to exit.")
