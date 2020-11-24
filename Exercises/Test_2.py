# Python3 program for above implementation 
  
# Function to print the string 
def printString(str, ch, count): 
    occ, i = 0, 0
  
    # If given count is 0 
    # print the given string and return 
    if (count == 0): 
        print(str) 
  
    # Start traversing the string 
    for i in range(len(str)): 
  
        # Increment occ if current char  
        # is equal to given character 
        if (str[i] == ch): 
            occ += 1
  
        # Break the loop if given character has 
        # been occurred given no. of times 
        if (occ == count): 
            break
  
    # Print the string after the occurrence 
    # of given character given no. of times 
    if (i < len(str)- 1): 
        print(str[i + 1: len(str) - i + 2]) 
  
    # Otherwise string is empty 
    else: 
        print("Empty string") 
  
# Driver code 
if __name__ == '__main__': 
    str = "geeks for geeks"
    printString(str, 'e', 2) 
