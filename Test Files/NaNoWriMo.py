#NaNoWriMo Word Count Program

greeting = str("Welcome to NaNoWriMo Bot!")
print(greeting.upper())
print("""\n\n\nooooo      ooo           ooooo      ooo                            
`888b.     `8'           `888b.     `8'                            
 8 `88b.    8   .oooo.    8 `88b.    8   .ooooo.                   
 8   `88b.  8  `P  )88b   8   `88b.  8  d88' `88b                  
 8     `88b.8   .oP"888   8     `88b.8  888   888                  
 8       `888  d8(  888   8       `888  888   888                  
o8o        `8  `Y888""8o o8o        `8  `Y8bod8P'                  
                                                                   
                                                                   
                                                                   
oooooo   oooooo     oooo           o8o  ooo        ooooo           
 `888.    `888.     .8'            `"'  `88.       .888'           
  `888.   .8888.   .8'   oooo d8b oooo   888b     d'888   .ooooo.  
   `888  .8'`888. .8'    `888""8P `888   8 Y88. .P  888  d88' `88b 
    `888.8'  `888.8'      888      888   8  `888'   888  888   888 
     `888'    `888'       888      888   8    Y     888  888   888 
      `8'      `8'       d888b    o888o o8o        o888o `Y8bod8P' 
                                                                   
                                                                   
                                                                   
oooooooooo.    .oooooo.   ooooooooooooo                            
`888'   `Y8b  d8P'  `Y8b  8'   888   `8                            
 888     888 888      888      888                                 
 888oooo888' 888      888      888                                 
 888    `88b 888      888      888                                 
 888    .88P `88b    d88'      888                                 
o888bood8P'   `Y8bood8P'      o888o                                
                                   """)
print("\nThis bot will help you find out if you're on track for your daily word count for NaNoWriMo.")

totalword = 50000
dailycount = 1667
curwordcount = ""
date = ""
finalcount = ""

date = int(input("\nWhat is today's date? Enter a number between 1-30. "))
curwordcount = int(input("\nHow many words have you currently written? "))

finalcount = (date*dailycount)

print("You should have written a minimum of", finalcount, "words so far.")

if curwordcount < finalcount:
    print("You are", (finalcount-curwordcount),"words behind. Keep going!")

if curwordcount > finalcount:
    print("You're ahead! Awesome!")



