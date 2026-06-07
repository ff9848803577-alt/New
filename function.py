# function is a block of code which only runs when it is called 
# it helps avoid code repetition and returns data as a result 
# we use def keyword  to define function 


def avg(): # function define
    a = int(input("Enter your number:"))
    b = int(input("Enter your number:"))
    c = int(input("Enter your number:"))

    average = (a+b+c)/3
    print(average)

avg() # functon call
avg()
avg()
avg()