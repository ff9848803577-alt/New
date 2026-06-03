# WAP which finds out whether a given name is present in a list 

list = ["Bikki", "Santosh", " Rohit"]

name = input("Enter your name:")

if(name in list): # here in a keyword which is use to check whether the name is present in the list or not
    print("Name is present in the list")
else:
    print("Name is not present in the list")