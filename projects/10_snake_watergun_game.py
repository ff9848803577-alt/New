'''
1 for snake
-1 for water 
0 for gun 

'''

import random 
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice(s,w,g):")
youDict = {"s": 1, "w": -1, "g": 0 }
reverseDict = {1: "Snake", -1: "Water", 0:"Gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}" )

if (computer == you):
    print("Its a draw!")

''' else:
    if(computer == -1 and you == 1):
        print("YOU WIN!")
    elif(computer == 1 and you == -1):
        print("YOU LOSE!")
    elif(computer == 0 and you == 1):
        print("YOU WIN!")
    elif(computer == 1 and you == 0):
        print("YOU LOSE!")
    elif(computer == 0 and you == -1):
        print("YOU LOSE!")
    elif(computer == -1 and you == 0):
        print("YOU WIN!")
    
    else:
        print("Something went wrong!!") '''

# we can replace the above code with this given single line of code:

if((computer - you ) == -1 or (computer - you ) == 2):
    print("YOU LOSE!")

        
    