# Simple Calc

totalword = 50000
dailycount = 1667
curwordcount = ""
date = ""
finalcount = ""

date = int(input("What is today's date?"))
curwordcount = int(input("\nHow many words have you currently written?"))

finalcount = (date*dailycount)

print("You should have written", finalcount, "words so far.")

if curwordcount < finalcount:
    print("You are", (finalcount-curwordcount),"words behind.")

if curwordcount > finalcount:
    print("You're ahead!")


