a = int(input("Enter your age:"))

# if, elif, else ladder 

if(a>18):
    print("You are eligible to vote")
    print("Congrats!!")

elif(a<0):
    print("Invalid age") # the space is called indentation 


elif(a==0):
    print("Age cant be zero")

else:
    print("You are not eligible to vote")
    print("Sorry!!")

print("End of program")
    
