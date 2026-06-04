# WAP to print multiplication table of a given number 

n = int(input("Enter a number:"))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

# here we use f sting to insert multiple variables in a string 

# Solving same qun using  while loop 

i = 1 
while(i<11):
    print(f"{n} * {i} = {n*i}")
    i +=1